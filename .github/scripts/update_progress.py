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

def get_user_stats(prs: List) -> Dict:
    """Собирает статистику по пользователям."""
    users = {}
    
    for pr in prs:
        user = pr.user.login
        if user not in users:
            users[user] = {
                'status': 'Не начал',
                'progress': 0,
                'last_activity': None,
                'current_module': None,
                'completed_lessons': [],
                'in_progress': []
            }
        
        result = parse_pr_title(pr.title)
        if result:
            module_num, lesson_num, lesson_name = result
            lesson_info = f"[Модуль {module_num}] Урок {lesson_num}: {lesson_name}"
            
            if pr.state == 'closed' and get_pr_status(pr) == 'completed':
                users[user]['completed_lessons'].append(lesson_info)
                users[user]['progress'] += 1
            elif pr.state == 'open':
                users[user]['in_progress'].append(lesson_info)
            
            users[user]['last_activity'] = pr.updated_at.strftime('%Y-%m-%d')
            users[user]['current_module'] = module_num
            users[user]['status'] = 'Активный' if pr.state == 'open' else 'Неактивный'
    
    return users

def update_contributors_file(lessons: Dict[str, List[Dict]], users: Dict):
    """Обновляет файл CONTRIBUTORS.md."""
    with open(CONTRIBUTORS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Обновляем статус уроков
    for module_num, module_lessons in lessons.items():
        for lesson in module_lessons:
            pattern = f"- \\[ \\] Урок {lesson['number']}: {lesson['name']}"
            replacement = f"- [{'x' if lesson['status'] == 'completed' else ' '}] Урок {lesson['number']}: {lesson['name']}"
            content = content.replace(pattern, replacement)
    
    # Обновляем статистику пользователей
    users_section = "## Участники и их прогресс\n\n"
    for username, stats in users.items():
        users_section += f"### @{username}\n"
        users_section += f"- **Статус**: {stats['status']}\n"
        users_section += f"- **Прогресс**: {stats['progress']}/4 уроков\n"
        users_section += f"- **Последняя активность**: {stats['last_activity'] or 'Нет'}\n"
        users_section += f"- **Текущий модуль**: {stats['current_module'] or 'Нет'}\n\n"
        
        users_section += "#### Пройденные уроки\n"
        if stats['completed_lessons']:
            for lesson in stats['completed_lessons']:
                users_section += f"- {lesson}\n"
        else:
            users_section += "- Нет пройденных уроков\n"
        
        users_section += "\n#### В процессе\n"
        if stats['in_progress']:
            for lesson in stats['in_progress']:
                users_section += f"- {lesson}\n"
        else:
            users_section += "- Нет уроков в процессе\n"
        
        users_section += "\n"
    
    # Заменяем секцию пользователей
    content = re.sub(
        r"## Участники и их прогресс\n\n.*?(?=## Прогресс по модулям)",
        users_section,
        content,
        flags=re.DOTALL
    )
    
    # Обновляем общую статистику
    total_users = len(users)
    active_users = sum(1 for stats in users.values() if stats['status'] == 'Активный')
    total_lessons = sum(len(lessons) for lessons in lessons.values())
    completed = sum(1 for module in lessons.values() for lesson in module if lesson['status'] == 'completed')
    in_progress = sum(1 for module in lessons.values() for lesson in module if lesson['status'] == 'in_progress')
    remaining = total_lessons - completed - in_progress
    
    stats_pattern = r"## Общая статистика\n- Всего участников: \d+\n- Активных участников: \d+\n- Всего уроков: \d+\n- Пройдено: \d+\n- В процессе: \d+\n- Осталось: \d+"
    stats_replacement = f"## Общая статистика\n- Всего участников: {total_users}\n- Активных участников: {active_users}\n- Всего уроков: {total_lessons}\n- Пройдено: {completed}\n- В процессе: {in_progress}\n- Осталось: {remaining}"
    content = re.sub(stats_pattern, stats_replacement, content)
    
    # Обновляем рейтинг участников
    sorted_users = sorted(users.items(), key=lambda x: x[1]['progress'], reverse=True)
    rating_section = "## Рейтинг участников\n"
    for i, (username, stats) in enumerate(sorted_users, 1):
        rating_section += f"{i}. @{username} - {stats['progress']} уроков\n"
    
    content = re.sub(
        r"## Рейтинг участников\n.*?(?=---)",
        rating_section,
        content,
        flags=re.DOTALL
    )
    
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
    
    # Собираем статистику по пользователям
    users = get_user_stats(prs)
    
    # Обновляем файл
    update_contributors_file(lessons, users)
    print("Progress updated successfully")

if __name__ == "__main__":
    main() 