#!/usr/bin/env python3

import os
import sys
import subprocess
from pathlib import Path
from typing import List, Dict
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
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

def get_ai_recommendations(file_path: str, content: str, model, tokenizer) -> str:
    """Получает рекомендации от Qwen для улучшения кода."""
    try:
        prompt = f"""Ты - опытный Python разработчик. Проанализируй код и дай рекомендации по улучшению. 
Фокусируйся на: читаемости, производительности, безопасности и лучших практиках.

Код для анализа:
```python
{content}
```

Дай подробные рекомендации по улучшению кода:"""

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
        recommendations = response.split("Дай подробные рекомендации по улучшению кода:")[-1].strip()
        return recommendations
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
    # Получаем токен из переменных окружения
    github_token = os.getenv("GITHUB_TOKEN")
    
    if not github_token:
        print("Ошибка: Не найден GitHub токен")
        sys.exit(1)
    
    # Инициализируем GitHub клиент
    g = Github(github_token)
    
    # Получаем информацию о PR
    repo_name = os.getenv("GITHUB_REPOSITORY")
    pr_number = int(os.getenv("GITHUB_REF").split("/")[-1])
    
    repo = g.get_repo(repo_name)
    pr = repo.get_pull(pr_number)
    
    # Загружаем модель Qwen
    print("Загрузка модели Qwen...")
    model_name = "Qwen/Qwen2.5-32B-Instruct"
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="auto",
        trust_remote_code=True
    ).eval()
    
    # Получаем измененные файлы
    changed_files = get_changed_files(pr)
    
    # Анализируем каждый файл
    for file_path in changed_files:
        if not file_path.endswith('.py'):
            continue
            
        print(f"Анализ файла: {file_path}")
        
        # Получаем содержимое файла
        file_content = repo.get_contents(file_path, ref=pr.head.sha).decoded_content.decode()
        
        # Запускаем проверки
        ruff_output = run_ruff_check(file_path)
        ai_recommendations = get_ai_recommendations(file_path, file_content, model, tokenizer)
        
        # Создаем комментарий
        create_review_comment(pr, file_path, ruff_output, ai_recommendations)

if __name__ == "__main__":
    main() 