# # Тема: функции
# #
# # Покажите в формате live-coding и объясните:
# # - Процесс создания и вызова функции.
# # - Использование оператора return для возврата значения из функции.
# # - Использования именованных аргументов, что делает вызов функции более гибким.
#
# def greet(name, greeting="Hello", *, punctuation="!"):
#     """
#     Функция для приветствия пользователя.
#
#     :param name: Имя пользователя.
#     :param greeting: Приветствие, по умолчанию "Hello".
#     :param punctuation: Знак препинания в конце приветствия, по умолчанию "!".
#     :return: Строка с приветствием.
#     """
#     return f"{greeting}, {name}{punctuation}"
#
# # Пример вызова функции
# print(greet("Alice"))  # Вывод: Hello, Alice!
# print(greet("Alice", greeting="Hi"))  # Вывод: Hi, Alice!
# print(greet("Alice", "Hi", punctuation='!!!'))  # Вывод: Hi, Alice!!!
# name_ = "Bob"
# greeting_ = "Welcome"
# punctuation_ = '!!?'
# print(greet(name_, greeting_, punctuation=punctuation_))  # Вывод: Welcome, Bob!!?
#
# # Тема: args, kwargs
# #

def foo(name, age, *args, **kwargs):
    """
    Функция для демонстрации работы с произвольным числом параметров.

    :param name: Имя пользователя.
    :param age: Возраст пользователя.
    :param args: Произвольное число позиционных аргументов.
    :param kwargs: Произвольное число именованных аргументов.
    :return: Строка с информацией о пользователе и дополнительных параметрах.
    """
    info = f"Name: {name}, Age: {age}"

    if args:
        info += f", Additional Positional Args: {args}"

    if kwargs and 'k' in kwargs:
        info += f", Additional Named Args: {kwargs}"

    return info

# print(foo("Alice", 30))  # Вывод: Name: Alice, Age: 30
print(foo("Alice", 30, 'qwe', 'qweqwe', 'qweqweqweqwe', k=1, j=2, kk=3))

# Покажите в формате live-coding и объясните:
# - Как работать с произвольным числом параметров с помощью args и *kwargs.
