# Дополнительная практика


# 1. Создайте декоратор requires_auth, который проверяет наличие определенного флага authenticated и выполняет
# функцию только если этот флаг установлен в True.
#
# authenticated = False

# Вывод: Доступ запрещен: пользователь не аутентифицирован

# Вывод: Секретная информация
authenticated = False
def requires_auth(func):
    def wrapper(*args, **kwargs):
        if authenticated:
            return func(*args, **kwargs)
        else:
            print("Доступ запрещен: пользователь не аутентифицирован")
    return wrapper
@requires_auth
def secret():
    print("Секретная информация")
secret()

authenticated = True
secret()

# 2. Создайте декоратор call_counter, который отслеживает количество вызовов декорируемой функции и
# выводит это количество при каждом вызове.
#
#
# # Вывод:
# # Функция greet вызвана 1 раз(а)
# # Привет, Алиса!
#
# # Вывод:
# # Функция greet вызвана 2 раз(а)
# # Привет, Боб!
from collections import defaultdict

def call_counter(func):
    counts = defaultdict(int)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        counts[key] += 1
        print(f"Функция {func.__name__} с аргументами {args} {kwargs} вызвана {counts[key]} раз(а)")
        return func(*args, **kwargs)
    return wrapper


@call_counter
def greet(name):
    print(f"Hello, {name}")


greet("Alice")
greet("Bob")
greet("Bob")
greet(name="Alice")