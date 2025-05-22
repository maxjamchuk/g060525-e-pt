#!/usr/bin/env python3

import os
import sys
import subprocess
import tempfile
from pathlib import Path
from typing import List, Dict, Tuple
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from github import Github
from github.PullRequest import PullRequest

def get_changed_files(pr: PullRequest) -> List[str]:
    """Получает список измененных файлов в PR."""
    return [file.filename for file in pr.get_files()]

def run_ruff_check(file_path: str) -> Tuple[str, bool]:
    """Запускает ruff для проверки файла."""
    try:
        result = subprocess.run(
            ["ruff", "check", file_path],
            capture_output=True,
            text=True
        )
        has_issues = bool(result.stdout.strip())
        return result.stdout, has_issues
    except subprocess.CalledProcessError as e:
        return f"Ошибка при запуске ruff: {e}", True

def run_pylint_check(file_path: str) -> Tuple[str, bool]:
    """Запускает pylint для проверки файла."""
    try:
        result = subprocess.run(
            ["pylint", file_path],
            capture_output=True,
            text=True
        )
        has_issues = bool(result.stdout.strip())
        return result.stdout, has_issues
    except subprocess.CalledProcessError as e:
        return f"Ошибка при запуске pylint: {e}", True

def check_syntax(file_path: str) -> Tuple[str, bool]:
    """Проверяет синтаксис Python файла."""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "py_compile", file_path],
            capture_output=True,
            text=True
        )
        has_issues = bool(result.stderr.strip())
        return result.stderr, has_issues
    except subprocess.CalledProcessError as e:
        return f"Ошибка при проверке синтаксиса: {e}", True

def try_run_code(file_path: str) -> Tuple[str, bool]:
    """Пытается запустить код в изолированной среде."""
    try:
        # Создаем временный файл для запуска
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as temp_file:
            temp_file.write(f"""
import sys
import traceback

try:
    with open('{file_path}', 'r') as f:
        code = f.read()
    exec(code)
    print("Код выполнен успешно")
except Exception as e:
    print(f"Ошибка при выполнении: {{e}}")
    traceback.print_exc()
""")
            temp_path = temp_file.name

        # Запускаем код в изолированной среде
        result = subprocess.run(
            [sys.executable, temp_path],
            capture_output=True,
            text=True,
            timeout=5  # Ограничиваем время выполнения
        )
        
        # Удаляем временный файл
        os.unlink(temp_path)
        
        has_issues = bool(result.stderr.strip())
        return result.stderr or result.stdout, has_issues
    except subprocess.TimeoutExpired:
        return "Ошибка: Превышено время выполнения (5 секунд)", True
    except Exception as e:
        return f"Ошибка при запуске кода: {e}", True

def get_ai_recommendations(file_path: str, content: str, model, tokenizer) -> Tuple[str, bool]:
    """Получает рекомендации от модели для улучшения кода."""
    try:
        prompt = f"""Ты - опытный Python разработчик. Проанализируй код и дай рекомендации по улучшению. 
Фокусируйся на: читаемости, производительности, безопасности и лучших практиках.

Код для анализа:
```python
{content}
```

Дай подробные рекомендации по улучшению кода."""

        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
        outputs = model.generate(
            **inputs,
            max_new_tokens=500,
            temperature=0.7,
            top_p=0.9,
            do_sample=True
        )
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Извлекаем только рекомендации (после промпта)
        recommendations = response.split("Дай подробные рекомендации по улучшению кода.")[-1].strip()
        has_recommendations = bool(recommendations.strip())
        return recommendations, has_recommendations
    except Exception as e:
        return f"Ошибка при получении AI рекомендаций: {e}", True

def create_review_comment(pr: PullRequest, file_path: str, ruff_output: str, pylint_output: str, syntax_output: str, run_output: str, ai_recommendations: str):
    """Создает комментарий к PR с результатами проверки."""
    comment = f"""## Анализ файла: {file_path}

### Результаты проверки синтаксиса:
```
{syntax_output}
```

### Результаты проверки ruff:
```
{ruff_output}
```

### Результаты проверки pylint:
```
{pylint_output}
```

### Результаты запуска кода:
```
{run_output}
```

### Рекомендации по улучшению:
{ai_recommendations}
"""
    pr.create_issue_comment(comment)

def notify_author(pr: PullRequest, files_with_issues: List[str]):
    """Отправляет уведомление автору PR о найденных проблемах."""
    if not files_with_issues:
        return

    author = pr.user.login
    files_list = "\n".join(f"- {file}" for file in files_with_issues)
    
    notification = f"""Привет, @{author}! 👋

Я проанализировал ваш PR и нашел несколько моментов, которые стоит улучшить:

{files_list}

Пожалуйста, ознакомьтесь с комментариями к каждому файлу для получения подробных рекомендаций.

Если у вас есть вопросы или нужна помощь с исправлениями, дайте знать! 🤝
"""
    
    pr.create_issue_comment(notification)

def main():
    # Получаем токен из переменных окружения
    github_token = os.getenv("GITHUB_TOKEN")
    
    if not github_token:
        print("Ошибка: Не найден GitHub токен")
        sys.exit(1)
    
    # Инициализируем GitHub клиент
    g = Github(github_token)
    
    # Получаем информацию о PR
    repo_name = os.getenv("GITHUB_REPOSITORY")
    event_path = os.getenv("GITHUB_EVENT_PATH")
    
    if not event_path:
        print("Ошибка: Не найден путь к файлу события")
        sys.exit(1)
        
    # Читаем информацию о PR из файла события
    import json
    with open(event_path, 'r') as f:
        event_data = json.load(f)
        pr_number = event_data['pull_request']['number']
    
    print(f"Анализ PR #{pr_number}")
    
    repo = g.get_repo(repo_name)
    pr = repo.get_pull(pr_number)
    
    # Загружаем модель
    print("Загрузка модели...")
    model_name = "microsoft/phi-2"  # Используем phi-2, которая не требует токена
    
    tokenizer = AutoTokenizer.from_pretrained(
        model_name,
        trust_remote_code=True
    )
    
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="auto",
        trust_remote_code=True,
        torch_dtype=torch.float16,
        low_cpu_mem_usage=True
    ).eval()
    
    # Получаем измененные файлы
    changed_files = get_changed_files(pr)
    files_with_issues = []
    
    # Анализируем каждый файл
    for file_path in changed_files:
        if not file_path.endswith('.py'):
            continue
            
        print(f"Анализ файла: {file_path}")
        
        # Получаем содержимое файла
        file_content = repo.get_contents(file_path, ref=pr.head.sha).decoded_content.decode()
        
        # Запускаем проверки
        ruff_output, has_ruff_issues = run_ruff_check(file_path)
        pylint_output, has_pylint_issues = run_pylint_check(file_path)
        syntax_output, has_syntax_issues = check_syntax(file_path)
        run_output, has_run_issues = try_run_code(file_path)
        ai_recommendations, has_ai_recommendations = get_ai_recommendations(file_path, file_content, model, tokenizer)
        
        # Если есть проблемы, добавляем файл в список
        if any([has_ruff_issues, has_pylint_issues, has_syntax_issues, has_run_issues, has_ai_recommendations]):
            files_with_issues.append(file_path)
        
        # Создаем комментарий
        create_review_comment(pr, file_path, ruff_output, pylint_output, syntax_output, run_output, ai_recommendations)
    
    # Отправляем уведомление автору, если есть проблемы
    if files_with_issues:
        notify_author(pr, files_with_issues)

if __name__ == "__main__":
    main() 