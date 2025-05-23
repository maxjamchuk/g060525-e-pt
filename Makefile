.PHONY: setup clean process help

# Переменные
PYTHON := python3
UV := uv
VENV := .venv
SCRIPTS_DIR := .github/scripts

# Цвета для вывода
CYAN := \033[0;36m
GREEN := \033[0;32m
RED := \033[0;31m
NC := \033[0m # No Color

help:
	@echo "$(CYAN)Доступные команды:$(NC)"
	@echo "  $(GREEN)setup$(NC)     - Установка зависимостей и настройка окружения"
	@echo "  $(GREEN)clean$(NC)     - Очистка временных файлов"
	@echo "  $(GREEN)process$(NC)   - Обработка презентаций в директории"

setup:
	@echo "$(CYAN)Установка зависимостей...$(NC)"
	$(PYTHON) -m venv $(VENV)
	. $(VENV)/bin/activate && $(UV) pip install -e .
	@echo "$(GREEN)Зависимости установлены$(NC)"

clean:
	@echo "$(CYAN)Очистка временных файлов...$(NC)"
	find . -name "*.pyc" -type f -delete
	find . -name "__pycache__" -type d -delete
	rm -rf $(VENV)
	@echo "$(GREEN)Очистка завершена$(NC)"

process:
	@echo "$(CYAN)Обработка презентаций...$(NC)"
	. $(VENV)/bin/activate && $(PYTHON) $(SCRIPTS_DIR)/process_presentations.py $(PWD)
	@echo "$(GREEN)Обработка завершена$(NC)" 