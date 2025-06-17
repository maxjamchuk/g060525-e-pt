# Дополнительная практика
#
#
# 1. Создайте декоратор to_upper, который преобразует строковый результат функции в верхний регистр.
#
# # Вывод: ПРИВЕТ, АЛИСА
def to_upper(func):
    def wrapper(*args, **kwargs):
            text=func(*args, **kwargs)
            return text.upper()
    return wrapper
@to_upper
def lower_str(text):
    return text
print(lower_str("привет, алиса"))
# 2. Создайте декоратор limit_calls, который ограничивает количество вызовов функции заданным числом.
# Если функция вызывается больше разрешенного числа раз, выводите сообщение об ошибке.
#
# Вывод: Привет, Алиса!
# Вывод: Привет, Боб!
# Вывод: Привет, Чарли!
# Вывод: Ошибка: функция say_hello может быть вызвана не более 3 раз
def limit_calls(func):
    count=0
    def wrapper(*args, **kwargs):
        nonlocal count
        count+=1
        if count <=3:
            return func(*args, **kwargs)
        else:
            print(f"Ошибка: функция {func.__name__} может быть вызвана не более 3 раз")
    return wrapper


@limit_calls
def greet(name):
    print(f"Привет, {name}")
greet("Alice")
greet("Bob")
greet("Charlie")
greet("Martin")
