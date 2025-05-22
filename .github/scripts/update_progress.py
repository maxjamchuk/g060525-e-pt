#!/usr/bin/env python3
import os
import sys
import json
import re
from datetime import datetime
from typing import Dict, List, Tuple
import requests
from github import Github

# Конфигурация
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_NAME = os.getenv('GITHUB_REPOSITORY')
CONTRIBUTORS_FILE = 'CONTRIBUTORS.md'

def parse_pr_title(title: str) -> Tuple[int, int, str]:
    """Парсит название PR и извлекает номер модуля, урока и название."""
    pattern = r'\[Модуль (\d+)\] Урок (\d+): (.+)'
    match = re.match(pattern, title)
    if match:
        module_num = int(match.group(1))
        lesson_num = int(match.group(2))
        lesson_name = match.group(3)
        return module_num, lesson_num, lesson_name
    return None

def get_pr_status(pr) -> str:
    """Определяет статус PR."""
    if pr.state == 'closed':
        # Проверяем, есть ли комментарии от владельца
        comments = pr.get_issue_comments()
        for comment in comments:
            if comment.user.login == pr.base.repo.owner.login:
                return 'review'
        return 'completed'
    return 'in_progress'

def update_contributors_file(lessons: Dict[str, List[Dict]]):
    """Обновляет файл CONTRIBUTORS.md."""
    with open(CONTRIBUTORS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Обновляем статус уроков
    for module_num, module_lessons in lessons.items():
        for lesson in module_lessons:
            pattern = f"- \\[ \\] Урок {lesson['number']}: {lesson['name']}"
            replacement = f"- [{'x' if lesson['status'] == 'completed' else ' '}] Урок {lesson['number']}: {lesson['name']}"
            content = content.replace(pattern, replacement)
    
    # Обновляем статистику
    total = sum(len(lessons) for lessons in lessons.values())
    completed = sum(1 for module in lessons.values() for lesson in module if lesson['status'] == 'completed')
    in_progress = sum(1 for module in lessons.values() for lesson in module if lesson['status'] == 'in_progress')
    remaining = total - completed - in_progress
    
    stats_pattern = r"## Статистика\n- Всего уроков: \d+\n- Пройдено: \d+\n- В процессе: \d+\n- Осталось: \d+"
    stats_replacement = f"## Статистика\n- Всего уроков: {total}\n- Пройдено: {completed}\n- В процессе: {in_progress}\n- Осталось: {remaining}"
    content = re.sub(stats_pattern, stats_replacement, content)
    
    # Обновляем дату
    content = re.sub(
        r"Последнее обновление: .+",
        f"Последнее обновление: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        content
    )
    
    with open(CONTRIBUTORS_FILE, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    if not GITHUB_TOKEN:
        print("Error: GITHUB_TOKEN not set")
        sys.exit(1)
    
    if not REPO_NAME:
        print("Error: GITHUB_REPOSITORY not set")
        sys.exit(1)
    
    # Инициализируем GitHub API
    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(REPO_NAME)
    
    # Получаем все PR
    prs = repo.get_pulls(state='all')
    
    # Собираем информацию об уроках
    lessons = {}
    for pr in prs:
        result = parse_pr_title(pr.title)
        if result:
            module_num, lesson_num, lesson_name = result
            module_key = f"Модуль {module_num}"
            
            if module_key not in lessons:
                lessons[module_key] = []
            
            lessons[module_key].append({
                'number': lesson_num,
                'name': lesson_name,
                'status': get_pr_status(pr)
            })
    
    # Сортируем уроки по номеру
    for module_lessons in lessons.values():
        module_lessons.sort(key=lambda x: x['number'])
    
    # Обновляем файл
    update_contributors_file(lessons)
    print("Progress updated successfully")

if __name__ == "__main__":
    main() 