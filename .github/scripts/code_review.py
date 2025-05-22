#!/usr/bin/env python3

import os
import sys
import subprocess
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

def get_ai_recommendations(file_path: str, content: str, model, tokenizer) -> Tuple[str, bool]:
    """Получает рекомендации от CodeLlama для улучшения кода."""
    try:
        prompt = f"""<s>[INST] Ты - опытный Python разработчик. Проанализируй код и дай рекомендации по улучшению. 
Фокусируйся на: читаемости, производительности, безопасности и лучших практиках.

Код для анализа:
```python
{content}
```

Дай подробные рекомендации по улучшению кода. [/INST]"""

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
        recommendations = response.split("[/INST]")[-1].strip()
        has_recommendations = bool(recommendations.strip())
        return recommendations, has_recommendations
    except Exception as e:
        return f"Ошибка при получении AI рекомендаций: {e}", True

def create_review_comment(pr: PullRequest, file_path: str, ruff_output: str, ai_recommendations: str):
    """Создает комментарий к PR с результатами проверки."""
    comment = f"""## Анализ файла: {file_path}

### Результаты проверки ruff:
```
{ruff_output}
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
    
    # Загружаем модель CodeLlama
    print("Загрузка модели CodeLlama...")
    model_name = "codellama/CodeLlama-7b-Instruct-hf"
    
    # Используем кэшированные пути
    cache_dir = os.getenv("TRANSFORMERS_CACHE", "~/.cache/huggingface/hub")
    torch_cache_dir = os.getenv("TORCH_HOME", "~/.cache/torch")
    
    print(f"Используем кэш моделей: {cache_dir}")
    print(f"Используем кэш PyTorch: {torch_cache_dir}")
    
    tokenizer = AutoTokenizer.from_pretrained(
        model_name,
        trust_remote_code=True,
        cache_dir=cache_dir
    )
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="auto",
        trust_remote_code=True,
        cache_dir=cache_dir,
        torch_dtype=torch.float16  # Используем float16 для экономии памяти
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
        ai_recommendations, has_ai_recommendations = get_ai_recommendations(file_path, file_content, model, tokenizer)
        
        # Если есть проблемы, добавляем файл в список
        if has_ruff_issues or has_ai_recommendations:
            files_with_issues.append(file_path)
        
        # Создаем комментарий
        create_review_comment(pr, file_path, ruff_output, ai_recommendations)
    
    # Отправляем уведомление автору, если есть проблемы
    if files_with_issues:
        notify_author(pr, files_with_issues)

if __name__ == "__main__":
    main() 