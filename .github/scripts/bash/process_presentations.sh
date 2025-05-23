#!/bin/bash

source "$(dirname "$0")/common.sh"

# Функция для получения относительного пути
get_relative_path() {
    local target=$1
    local base=$2
    
    # Используем python для получения относительного пути
    python3 -c "import os; print(os.path.relpath('$target', '$base'))"
}

# Функция для создания ссылки на презентацию
create_link() {
    local presentation=$1
    local relative_path=$2
    local metadata=$3
    local type=$4
    
    if [[ ! -f "$presentation" ]]; then
        handle_error 1 "Presentation file does not exist: $presentation" "create_link"
    fi
    
    # Определяем тип презентации
    local emoji="📊"
    local type_name="Презентация"
    
    for type_info in "${PRESENTATION_TYPES[@]}"; do
        IFS=':' read -r type_key type_emoji type_label <<< "$type_info"
        if [[ "$type" == "$type_key" ]]; then
            emoji="$type_emoji"
            type_name="$type_label"
            break
        fi
    done
    
    # Получаем метаданные
    if [[ -z "$metadata" ]]; then
        log "WARNING" "No metadata provided for $presentation"
        metadata="0|Unknown"
    fi
    
    local slides=$(echo "$metadata" | cut -d'|' -f1)
    local date=$(echo "$metadata" | cut -d'|' -f2)
    
    log "DEBUG" "Creating link for $presentation (Type: $type_name, Slides: $slides, Date: $date)"
    
    # Создаем ссылку с метаданными
    echo "- $emoji [$(basename "$presentation" .pptx)]($relative_path) (Слайдов: $slides, Обновлено: $date)"
}

# Функция для создания выпадающего списка
create_collapsible() {
    local title=$1
    local content=$2
    
    echo "<details>"
    echo "<summary>$title</summary>"
    echo ""
    echo "$content"
    echo "</details>"
    echo ""
}

# Функция для сканирования директории
scan_directory() {
    local dir=$1
    
    if [[ ! -d "$dir" ]]; then
        handle_error 1 "Directory does not exist: $dir" "scan_directory"
    fi
    
    log "INFO" "Scanning directory: $dir"
    
    local toc=""
    local presentations_content=""
    local module_number="999"
    local is_module_dir=false
    local module_content=""
    
    # Проверяем, является ли директория модулем
    if is_module "$dir"; then
        is_module_dir=true
        module_number=$(get_module_number "$dir")
        module_name=$(basename "$dir")
        log "INFO" "Found module: $module_name (Number: $module_number)"
    fi
    
    # Создаем presentations.md в директории с презентациями
    if [ -n "$(find "$dir" -maxdepth 1 -name "*.pptx")" ]; then
        local lesson_content=""
        lesson_content+="### $(basename "$dir")\n\n"
        
        # Обрабатываем презентации
        for presentation in "$dir"/*.pptx; do
            if [ -f "$presentation" ]; then
                relative_path=$(get_relative_path "$presentation" ".")
                
                # Получаем метаданные презентации
                metadata=$(python3 "$(dirname "$0")/../get_presentation_metadata.py" "$presentation")
                if [[ $? -ne 0 ]]; then
                    log "WARNING" "Failed to get metadata for $presentation"
                    metadata="0|Unknown"
                fi
                
                # Определяем тип презентации
                type="lecture"
                if [[ "$presentation" == *"practice"* ]]; then
                    type="practice"
                elif [[ "$presentation" == *"additional"* ]]; then
                    type="additional"
                fi
                
                # Добавляем ссылку в TOC
                lesson_content+="$(create_link "$presentation" "$relative_path" "$metadata" "$type")\n"
            fi
        done
        
        if $is_module_dir; then
            module_content+="$lesson_content"
        else
            presentations_content+="$lesson_content"
        fi
    fi
    
    # Рекурсивно обрабатываем поддиректории
    for subdir in "$dir"/*/; do
        if [ -d "$subdir" ]; then
            if $is_module_dir; then
                # В модуле ищем только презентации
                if [ -n "$(find "$subdir" -maxdepth 1 -name "*.pptx")" ]; then
                    module_content+="$(scan_directory "$subdir")\n"
                fi
            else
                # В корневой директории ищем только модули
                if is_module "$subdir"; then
                    local subdir_content=$(scan_directory "$subdir")
                    if [[ -n "$subdir_content" ]]; then
                        presentations_content+="$(create_collapsible "$(basename "$subdir")" "$subdir_content")"
                    fi
                fi
            fi
        fi
    done
    
    if $is_module_dir && [[ -n "$module_content" ]]; then
        echo -e "$module_content"
    else
        echo -e "$presentations_content"
    fi
}

# Основная функция
main() {
    local root_dir=$1
    local output_file=$2
    
    log "INFO" "Starting presentation processing"
    log "INFO" "Root directory: $root_dir"
    log "INFO" "Output file: $output_file"
    
    # Проверяем зависимости
    check_dependencies
    
    # Проверяем входные параметры
    if [[ ! -d "$root_dir" ]]; then
        handle_error 1 "Root directory does not exist: $root_dir" "main"
    fi
    
    if [[ -z "$output_file" ]]; then
        handle_error 1 "Output file is not specified" "main"
    fi
    
    # Создаем заголовок с вводной частью
    echo -e "$OUTPUT_HEADER" > "$output_file"
    echo "" >> "$output_file"
    
    # Сканируем директорию и добавляем содержимое в файл
    scan_directory "$root_dir" >> "$output_file"
    
    # Добавляем разделитель и информацию об обновлении
    echo "" >> "$output_file"
    echo "$OUTPUT_SEPARATOR" >> "$output_file"
    echo "" >> "$output_file"
    echo "Последнее обновление: $(date '+%Y-%m-%d %H:%M:%S')" >> "$output_file"
    
    log "INFO" "Presentation processing completed"
}

# Проверяем аргументы
if [ $# -ne 2 ]; then
    handle_error 1 "Usage: $0 <directory> <output_file>" "main"
fi

main "$1" "$2" 