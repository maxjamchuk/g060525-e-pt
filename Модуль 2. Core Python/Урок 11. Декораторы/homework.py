# Тема: Декораторы


# 1. Создайте декоратор validate, который проверяет, что все переданные функции аргументы являются положительными числами.
# Если нет, выводит сообщение об ошибке.
#
# @validate
# def add(a, b):
#     return a + b
#
# print(add(5, 3))
# Вывод: 8
#
# print(add(-1, 3))
# Вывод: Ошибка: все аргументы должны быть положительными числами

# # Вывод: 55
#
# Вывод: 55 (использует кеш)
def validate(func):
    def wrapper(a, b):
        if a > 0 and b > 0:
            result = func(a, b)
        else:
            print("Error: all arquments must be positive numbers")
    return (wrapper

@validate)
def add(a, b):
    return a + b

print(add(5, 3))
print(add(-1, 3))



# 2. Создайте декоратор cache, который запоминает результаты выполнения функции для заданных аргументов и возвращает
# этот результат при повторном вызове декорируемой функции с теми же аргументами.

def cache(func):
    saved = {}
    def wrapper(n):
        if n in saved:
            print("Output:", saved[n],"(uses cache")
            return saved[n]
        else:
            result = func(n)
            saved[n] = result
            print("Output:", result)
            return result
    return wrapper

@cache
def fibonacci(n):
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))
# # Вывод: 55
print(fibonacci(10))
# # Вывод: 55 (использует кеш)




# Дополнительная практика


# 1. Создайте декоратор requires_auth, который проверяет наличие определенного флага authenticated и выполняет
# функцию только если этот флаг установлен в True.
authenticated = False

def reguires_auth(func):
    def wrapper():
        if authenticated:
            return func()
        else:
            print("Доступ запрещен: пользователь не аутентифицирован.")
        return wrapper


@reguires_auth
def secret_function():
    print("Секретная информация")
secret_function()

authenticated = True
secret_function()



# 2. Создайте декоратор call_counter, который отслеживает количество вызовов декорируемой функции и
# выводит это количество при каждом вызове.
def call_counter(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"fФункция {func.__name__}вызвана {count} раз(а) ")
        return func(*args, **kwargs)

    return wrapper

@call_counter
def greet(name):
     print(f"Привет, {name}!")
print("Алиса")
# # Вывод:
# # Функция greet вызвана 1 раз(а)
print("Боб")
# # Вывод:
# # Функция greet вызвана 2 раз(а)
# # Привет, Боб!


# 1. Создайте декоратор to_upper, который преобразует строковый результат функции в верхний регистр.
#
# @to_upper
# def get_greeting(name):
#     return f"Привет, {name}"
#
# print(get_greeting("Алиса"))
# # Вывод: ПРИВЕТ, АЛИСА
def to_upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@to_upper
def greet(name):
    return f"Hello, {name}"

print(greet("Alice"))

# 2. Создайте декоратор limit_calls, который ограничивает количество вызовов функции заданным числом.
# Если функция вызывается больше разрешенного числа раз, выводите сообщение об ошибке.
#
# @limit_calls(3)
# def say_hello(name):
#     print(f"Привет, {name}!")
#
# say_hello("Алиса")
# # Вывод: Привет, Алиса!
# say_hello("Боб")
# # Вывод: Привет, Боб!
# say_hello("Чарли")
# # Вывод: Привет, Чарли!
# say_hello("Дейв")
# # Вывод: Ошибка: функция say_hello может быть вызвана не более 3 раз

def limit_calls(max_calls):
    def decorator(func):
        count = 0
        def wrapper(*args, **kwargs):
            nonlocal count
            if count < max_calls:
                count += 1
                return func(*args, **kwargs)
            else:
                print("You can't call out any more")
        return wrapper
    return decorator

@limit_calls
def say_hello(name):
    print("Hello,", name)

say_hello("Alice")
say_hello("Bob")
say_hello("Чарли!")
say_hello("Дейв")