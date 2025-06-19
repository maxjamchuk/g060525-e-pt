from linecache import cache
from functools import wraps
from pprint import pprint


# Тема: Декораторы

# 1. Создайте декоратор validate, который проверяет, что все переданные функции аргументы являются положительными числами.
# Если нет, выводит сообщение об ошибке.
#
# Вывод: Ошибка: все аргументы должны быть положительными числами

def validate(func):
    def wrapper(*args, **kwargs):
        all_args=list(args)+ list(kwargs.values())
        if any(not isinstance(x, (int, float)) or x <=0 for x in all_args):
            print("Ошибка: Все аргументы должны быть положительными числами.")
            return
        result=func(*args, **kwargs)
        print(f"Аргументы: {', '. join(str(x) for x in args)} приводят к результату → {result}")
        return result
    return wrapper


# 2. Создайте декоратор cache, который запоминает результаты выполнения функции для заданных аргументов и возвращает
# этот результат при повторном вызове декорируемой функции с теми же аргументами.


# # Вывод: 55
#
# Вывод: 55 (использует кеш)
saved_results = {}

def cache(func):
    global saved_results
    def wrapper(*args, **kwargs):
        key = (func.__name__, args, tuple(sorted(kwargs.items())))
        if key in saved_results:
            print("Результат взят из Кеши: ")
            return saved_results[key]
        result = func(*args, **kwargs)
        saved_results[key] = result
        return result
    return wrapper

@validate
@cache
def summa_blya(a,b):
    return a+b

@validate
@cache
def minus(a,b):
    return b-a

print(summa_blya(1,2))
print(summa_blya(-1,2))
print(summa_blya(21,2))
print(summa_blya(1,-2))
print(summa_blya(1501,2))
print(summa_blya(-11,-2))
print(summa_blya(1,2))

print(minus(-1,2))
print(minus(1,2))
print(minus(1,2))
pprint(saved_results)