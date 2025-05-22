#!/usr/bin/env python3

import os
import sys
import subprocess
from pathlib import Path
from typing import List, Dict
import openai
from github import Github
from github.PullRequest import PullRequest

def get_changed_files(pr: PullRequest) -> List[str]:
    """Получает список измененных файлов в PR."""
    return [file.filename for file in pr.get_files()]

def run_ruff_check(file_path: str) -> str:
    """Запускает ruff для проверки файла."""
    try:
        result = subprocess.run(
            ["ruff", "check", file_path],
            capture_output=True,
            text=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Ошибка при запуске ruff: {e}"

def get_ai_recommendations(file_path: str, content: str) -> str:
    """Получает рекомендации от AI для улучшения кода."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Ты - опытный Python разработчик. Проанализируй код и дай рекомендации по улучшению. Фокусируйся на: читаемости, производительности, безопасности и лучших практиках."},
                {"role": "user", "content": f"Проанализируй этот код и дай рекомендации по улучшению:\n\n{content}"}
            ],
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Ошибка при получении AI рекомендаций: {e}"

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

def main():
    # Получаем токены из переменных окружения
    github_token = os.getenv("GITHUB_TOKEN")
    openai_api_key = os.getenv("OPENAI_API_KEY")
    
    if not github_token or not openai_api_key:
        print("Ошибка: Не найдены необходимые токены")
        sys.exit(1)
    
    # Инициализируем клиенты
    openai.api_key = openai_api_key
    g = Github(github_token)
    
    # Получаем информацию о PR
    repo_name = os.getenv("GITHUB_REPOSITORY")
    pr_number = int(os.getenv("GITHUB_REF").split("/")[-1])
    
    repo = g.get_repo(repo_name)
    pr = repo.get_pull(pr_number)
    
    # Получаем измененные файлы
    changed_files = get_changed_files(pr)
    
    # Анализируем каждый файл
    for file_path in changed_files:
        if not file_path.endswith('.py'):
            continue
            
        # Получаем содержимое файла
        file_content = repo.get_contents(file_path, ref=pr.head.sha).decoded_content.decode()
        
        # Запускаем проверки
        ruff_output = run_ruff_check(file_path)
        ai_recommendations = get_ai_recommendations(file_path, file_content)
        
        # Создаем комментарий
        create_review_comment(pr, file_path, ruff_output, ai_recommendations)

if __name__ == "__main__":
    main() 