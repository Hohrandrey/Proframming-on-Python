import csv
import datetime
from collections import defaultdict, Counter
import matplotlib.pyplot as plt
from enum import IntEnum
import pandas as pd


class Status(IntEnum):
    Submitted = 0
    Checked = 2
    Failed = 3
    NotSubmitted = 4
    CheckedSubmitted = 5
    CheckedFailed = 6


def parse_time(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')


def load_csv(filename):
    with open(filename, encoding='utf8') as f:
        return list(csv.reader(f, delimiter=','))


# Загрузка данных
messages = load_csv('messages.csv')
checks = load_csv('checks.csv')
statuses = load_csv('statuses.csv')
groups = load_csv('groups.csv')
games = load_csv('GAMES.csv')

group_names = {row[0]: row[1] for row in groups[1:]}


def create_plot(title):
    """Создает график с заголовком"""
    plt.figure(figsize=(12, 6))
    plt.title(title, fontsize=14, y=1.02, fontweight='bold')
    plt.tight_layout()


def task_3_2():
    """3.2: Распределение активности студентов по времени суток"""
    create_plot("3.2: Распределение активности по времени суток")
    hours = [parse_time(row[4]).hour for row in messages[1:] if len(row) > 4]
    plt.hist(hours, bins=24, color='#4285F4', edgecolor='white')
    plt.xlabel('Час дня', fontsize=12)
    plt.ylabel('Количество сообщений', fontsize=12)
    plt.xticks(range(0, 24))
    plt.grid(axis='y', alpha=0.3)
    plt.show()


def task_3_3():
    """3.3: Общее количество сообщений по задачам"""
    create_plot("3.3: Сообщения по задачам")
    task_counts = Counter(row[1] for row in messages[1:] if len(row) > 1)
    tasks = sorted(task_counts.items(), key=lambda x: int(x[0]))
    plt.bar([f'Задача {t[0]}' for t in tasks], [t[1] for t in tasks], color='#34A853')
    plt.xlabel('Номер задачи', fontsize=12)
    plt.ylabel('Количество сообщений', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', alpha=0.3)
    plt.show()


def task_3_4():
    """3.4: Динамика активности по задачам"""
    create_plot("3.4: Динамика активности по задачам")
    first_date = min(parse_time(row[4]) for row in messages[1:] if len(row) > 4).date()
    task_days = defaultdict(list)

    for row in messages[1:]:
        if len(row) > 4:
            days = (parse_time(row[4]).date() - first_date).days
            task_days[row[1]].append(days)

    for task in sorted(task_days.keys(), key=int):
        days = sorted(Counter(task_days[task]).items())
        plt.plot([d[0] for d in days], [d[1] for d in days],
                 label=f'Задача {task}', marker='o', linewidth=2)

    plt.xlabel('Дни с начала семестра', fontsize=12)
    plt.ylabel('Количество сообщений', fontsize=12)
    plt.legend()
    plt.grid(alpha=0.3)
    plt.show()


def task_3_5():
    """3.5: Группы с наибольшим количеством сообщений"""
    create_plot("3.5: Топ групп по сообщениям")
    group_counts = Counter(row[3] for row in messages[1:] if len(row) > 3)
    top_groups = group_counts.most_common(5)
    names = [group_names.get(g[0], g[0]) for g in top_groups]
    plt.barh(names, [g[1] for g in top_groups], color='#FBBC05')
    plt.xlabel('Количество сообщений', fontsize=12)
    plt.grid(axis='x', alpha=0.3)
    plt.show()


def task_3_6():
    """3.6: Группы с наибольшим количеством правильных решений"""
    create_plot("3.6: Топ групп по правильным решениям")
    correct = {row[1] for row in checks[1:] if len(row) > 3 and Status(int(row[3])) == Status.Checked}
    group_correct = Counter(row[3] for row in messages[1:] if len(row) > 0 and row[0] in correct)
    top_groups = group_correct.most_common(5)
    names = [group_names.get(g[0], g[0]) for g in top_groups]
    plt.barh(names, [g[1] for g in top_groups], color='#0F9D58')
    plt.xlabel('Правильных решений', fontsize=12)
    plt.grid(axis='x', alpha=0.3)
    plt.show()


def task_3_7():
    """3.7: Самые легкие и сложные задачи"""
    create_plot("3.7: Сложность задач")
    message_to_task = {msg[0]: msg[1] for msg in messages[1:] if len(msg) > 1}
    task_stats = defaultdict(lambda: {'total': 0, 'correct': 0})

    for row in checks[1:]:
        if len(row) > 3 and row[1] in message_to_task:
            task = message_to_task[row[1]]
            task_stats[task]['total'] += 1
            if Status(int(row[3])) == Status.Checked:
                task_stats[task]['correct'] += 1

    tasks = sorted(task_stats.items(), key=lambda x: x[1]['correct'] / x[1]['total'] if x[1]['total'] else 0)
    easiest = tasks[-5:]
    hardest = tasks[:5]

    plt.barh([f'Задача {t[0]}' for t in hardest],
             [t[1]['correct'] / t[1]['total'] for t in hardest],
             color='#DB4437', label='Сложные')
    plt.barh([f'Задача {t[0]}' for t in easiest],
             [t[1]['correct'] / t[1]['total'] for t in easiest],
             color='#4285F4', label='Легкие')

    plt.xlabel('Доля правильных решений', fontsize=12)
    plt.legend()
    plt.grid(axis='x', alpha=0.3)
    plt.xlim(0, 1)
    plt.show()


def task_3_8():
    """3.8: Группы с наибольшим количеством достижений"""
    create_plot("3.8: Топ групп по достижениям")
    group_ach = defaultdict(int)
    for row in statuses[1:]:
        if len(row) > 5 and row[5]:
            group_ach[row[2]] += len(row[5].split(';'))

    top_groups = sorted(group_ach.items(), key=lambda x: x[1], reverse=True)[:5]
    names = [group_names.get(g[0], g[0]) for g in top_groups]
    plt.barh(names, [g[1] for g in top_groups], color='#673AB7')
    plt.xlabel('Количество достижений', fontsize=12)
    plt.grid(axis='x', alpha=0.3)
    plt.show()


def task_3_9():
    """3.9: Топ-10 студентов по рейтингу"""
    create_plot("3.9: Рейтинг студентов")
    student_scores = defaultdict(int)
    for row in statuses[1:]:
        if len(row) > 5 and row[5]:
            student = f"{group_names.get(row[2], row[2])} (вар. {row[1]})"
            student_scores[student] += len(row[5].split(';'))

    top_students = sorted(student_scores.items(), key=lambda x: x[1], reverse=True)[:10]
    plt.barh([s[0] for s in top_students], [s[1] for s in top_students], color='#FF5722')
    plt.xlabel('Количество достижений', fontsize=12)
    plt.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    plt.show()


def task_3_10():
    """3.10: Группы с разнообразными решениями"""
    create_plot("3.10: Разнообразие решений")
    group_methods = defaultdict(set)
    for row in checks[1:]:
        if len(row) > 2 and Status(int(row[3])) == Status.Checked:
            group = next((msg[3] for msg in messages[1:] if len(msg) > 0 and msg[0] == row[1]), None)
            if group:
                group_methods[group].add(row[2])

    top_groups = sorted(group_methods.items(), key=lambda x: len(x[1]), reverse=True)[:5]
    names = [group_names.get(g[0], g[0]) for g in top_groups]
    plt.barh(names, [len(g[1]) for g in top_groups], color='#009688')
    plt.xlabel('Уникальных методов решения', fontsize=12)
    plt.grid(axis='x', alpha=0.3)
    plt.show()


def task_3_11():
    """3.11: Популярные годы выпуска игр"""
    create_plot("3.11: Годы выпуска игр")
    df = pd.DataFrame(games[1:], columns=['title', 'genre', 'url', 'year'])
    df['year'] = df['year'].str.extract('(\d{4})').dropna().astype(int)
    year_counts = df['year'].value_counts().sort_index().nlargest(10)
    year_counts.plot(kind='bar', color='#3F51B5', width=0.8)
    plt.xlabel('Год выпуска', fontsize=12)
    plt.ylabel('Количество игр', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', alpha=0.3)
    plt.show()


def task_3_12():
    """3.12: Популярность жанров игр"""
    create_plot("3.12: Популярность жанров")
    df = pd.DataFrame(games[1:], columns=['title', 'genre', 'url', 'year'])
    genre_counts = df['genre'].value_counts().nlargest(10)
    genre_counts.plot(kind='bar', color='#9C27B0')
    plt.xlabel('Жанр', fontsize=12)
    plt.ylabel('Количество игр', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', alpha=0.3)
    plt.show()


if __name__ == "__main__":
    tasks = [
        task_3_2, task_3_3, task_3_4, task_3_5, task_3_6,
        task_3_7, task_3_8, task_3_9, task_3_10, task_3_11, task_3_12
    ]

    for task in tasks:
        task()