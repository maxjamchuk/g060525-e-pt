#!/bin/bash

source "$(dirname "$0")/config.sh"

# Функция для ротации логов
rotate_logs() {
    local log_file=$1
    local max_size=$2
    local max_files=$3
    
    if [[ ! -f "$log_file" ]]; then
        return 0
    fi
    
    local current_size=$(stat -f%z "$log_file" 2>/dev/null || stat -c%s "$log_file")
    
    if [[ $current_size -gt $max_size ]]; then
        # Ротируем существующие файлы
        for ((i=max_files-1; i>=1; i--)); do
            local old_file="${log_file}.${i}"
            local new_file="${log_file}.$((i+1))"
            [[ -f "$old_file" ]] && mv "$old_file" "$new_file"
        done
        
        # Переименовываем текущий файл
        mv "$log_file" "${log_file}.1"
        
        # Создаем новый пустой файл
        touch "$log_file"
    fi
}

# Функция для цветного логирования
log() {
    local level=$1
    local message=$2
    local timestamp=$(date "+$LOG_FORMAT")
    
    # Ротируем логи если нужно
    rotate_logs "$LOG_FILE" "$LOG_MAX_SIZE" "$LOG_MAX_FILES"
    
    # Определяем цвет для уровня логирования
    local color=""
    if [[ "$LOG_COLORS" == "true" ]]; then
        case "$level" in
            "DEBUG") color="$LOG_COLOR_DEBUG" ;;
            "INFO") color="$LOG_COLOR_INFO" ;;
            "WARNING") color="$LOG_COLOR_WARN" ;;
            "ERROR") color="$LOG_COLOR_ERROR" ;;
        esac
    fi
    
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
    
    # Формируем сообщение
    local log_message="[$timestamp] [$level] $message"
    
    # Записываем в лог
    echo -e "${color}${log_message}${LOG_COLOR_RESET}" >> "$LOG_FILE"
    
    # Выводим в консоль если это ошибка или включен режим отладки
    if [[ "$level" == "ERROR" ]] || [[ "$LOG_LEVEL" == "DEBUG" ]]; then
        echo -e "${color}${log_message}${LOG_COLOR_RESET}"
    fi
    
    # Отправляем уведомление если это ошибка
    if [[ "$level" == "ERROR" ]] && [[ "$NOTIFY_ON_ERROR" == "true" ]]; then
        send_notification "$message"
    fi
}

# Функция для отправки уведомлений
send_notification() {
    local message=$1
    
    # Email уведомление
    if [[ -n "$NOTIFY_EMAIL" ]]; then
        echo "Error: $message" | mail -s "Error in GitHub Action" "$NOTIFY_EMAIL"
    fi
    
    # Slack уведомление
    if [[ -n "$NOTIFY_SLACK_WEBHOOK" ]]; then
        curl -X POST -H 'Content-type: application/json' \
            --data "{\"text\":\"Error in GitHub Action: $message\"}" \
            "$NOTIFY_SLACK_WEBHOOK"
    fi
    
    # Telegram уведомление
    if [[ -n "$NOTIFY_TELEGRAM_BOT_TOKEN" ]] && [[ -n "$NOTIFY_TELEGRAM_CHAT_ID" ]]; then
        curl -X POST "https://api.telegram.org/bot$NOTIFY_TELEGRAM_BOT_TOKEN/sendMessage" \
            -d "chat_id=$NOTIFY_TELEGRAM_CHAT_ID" \
            -d "text=Error in GitHub Action: $message"
    fi
}

# Функция для создания резервной копии
create_backup() {
    if [[ "$BACKUP_ENABLED" != "true" ]]; then
        return 0
    fi
    
    local backup_dir="$BACKUP_DIR"
    local timestamp=$(date "+%Y%m%d_%H%M%S")
    local backup_file="${backup_dir}/${BACKUP_PREFIX}${timestamp}${BACKUP_SUFFIX}"
    
    # Создаем директорию для бэкапов если её нет
    mkdir -p "$backup_dir"
    
    # Создаем архив
    tar -czf "$backup_file" .github/scripts .github/workflows
    
    # Удаляем старые бэкапы
    find "$backup_dir" -name "${BACKUP_PREFIX}*${BACKUP_SUFFIX}" -type f | \
        sort -r | tail -n +$((BACKUP_MAX_FILES + 1)) | xargs rm -f
    
    log "INFO" "Created backup: $backup_file"
}

# Функция для записи метрик
record_metric() {
    if [[ "$METRICS_ENABLED" != "true" ]]; then
        return 0
    fi
    
    local metric_name=$1
    local metric_value=$2
    local timestamp=$(date "+%Y-%m-%d %H:%M:%S")
    
    # Создаем директорию для метрик если её нет
    mkdir -p "$(dirname "$METRICS_FILE")"
    
    # Создаем файл если его нет
    if [[ ! -f "$METRICS_FILE" ]]; then
        echo "{}" > "$METRICS_FILE"
    fi
    
    # Добавляем метрику
    local temp_file=$(mktemp)
    jq --arg name "$metric_name" \
       --arg value "$metric_value" \
       --arg time "$timestamp" \
       '. + {($name): {"value": $value, "timestamp": $time}}' \
       "$METRICS_FILE" > "$temp_file"
    mv "$temp_file" "$METRICS_FILE"
    
    # Удаляем старые метрики
    local cutoff_date=$(date -d "$METRICS_RETENTION_DAYS days ago" "+%Y-%m-%d")
    jq 'del(.[] | select(.timestamp < "'"$cutoff_date"'"))' \
       "$METRICS_FILE" > "$temp_file"
    mv "$temp_file" "$METRICS_FILE"
}

# Функция для измерения времени выполнения
measure_time() {
    local start_time=$(date +%s.%N)
    "$@"
    local end_time=$(date +%s.%N)
    local duration=$(echo "$end_time - $start_time" | bc)
    record_metric "execution_time_$1" "$duration"
    echo "$duration"
} 