#!/bin/bash

# Подключаем конфигурацию
source "$(dirname "$0")/config.sh"

# Создаем директорию для логов если её нет
mkdir -p "$(dirname "$LOG_FILE")"

# Функция для логирования
log() {
    local level=$1
    local message=$2
    local timestamp=$(date "+$LOG_FORMAT")
    
    # Проверяем уровень логирования
    case "$LOG_LEVEL" in
        "DEBUG") ;;
        "INFO")
            [[ "$level" == "DEBUG" ]] && return
            ;;
        "WARNING")
            [[ "$level" == "DEBUG" || "$level" == "INFO" ]] && return
            ;;
        "ERROR")
            [[ "$level" != "ERROR" ]] && return
            ;;
    esac
    
    # Записываем в лог
    echo "[$timestamp] [$level] $message" >> "$LOG_FILE"
    
    # Выводим в консоль если это ошибка
    if [[ "$level" == "ERROR" ]]; then
        echo "Error: $message" >&2
    fi
}

# Функция для обработки ошибок
handle_error() {
    local exit_code=$1
    local error_message=$2
    local error_location=$3
    
    log "ERROR" "$error_message (at $error_location)"
    exit "$exit_code"
}

# Функция для проверки зависимостей
check_dependencies() {
    local deps=("python3" "find" "realpath")
    for dep in "${deps[@]}"; do
        if ! command -v "$dep" &> /dev/null; then
            handle_error 1 "Required dependency '$dep' is not installed" "check_dependencies"
        fi
    done
}

# Функция для проверки, является ли директория модулем
is_module() {
    local dir=$1
    
    if [[ ! -d "$dir" ]]; then
        handle_error 1 "Directory does not exist: $dir" "is_module"
    fi
    
    local name=$(basename "$dir")
    for pattern in "${MODULE_PATTERNS[@]}"; do
        if [[ "$name" =~ $pattern ]]; then
            log "DEBUG" "Directory is a module: $dir"
            return 0
        fi
    done
    
    log "DEBUG" "Directory is not a module: $dir"
    return 1
}

# Функция для получения номера модуля
get_module_number() {
    local dir=$1
    
    if [[ ! -d "$dir" ]]; then
        handle_error 1 "Directory does not exist: $dir" "get_module_number"
    fi
    
    local name=$(basename "$dir")
    for pattern in "${MODULE_PATTERNS[@]}"; do
        if [[ "$name" =~ $pattern ]]; then
            local number=$(echo "$name" | sed -E 's/^([0-9]+).*/\1/')
            log "DEBUG" "Module number for $dir: $number"
            echo "$number"
            return 0
        fi
    done
    
    log "WARNING" "Could not determine module number for $dir, using default 999"
    echo "999"
} 