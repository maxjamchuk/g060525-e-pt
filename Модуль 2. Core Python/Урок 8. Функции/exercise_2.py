# Задача 1: Генерация словаря
# Напишите функцию `create_dict(keys, values)`, которая принимает два списка: ключи и значения,
# и возвращает словарь, где ключи из первого списка, а значения из второго.
#
# keys = ["name", "age", "city"]
# values = ["Alice", 30, "New York"]
# Вывод функции: {'name': 'Alice', 'age': 30, 'city': 'New York'}

def create_dict(keys, values):
    """
    Функция для создания словаря из двух списков: ключей и значений.

    :param keys: Список
    :param values: Список значений
    :return: Словарь, где ключи из первого списка, а значения из второго.
    """
    answer = {}
    for el in range(len(keys)):
        answer[keys[el]] = values[el]

    return answer
    # return dict(zip(keys, values))


# Задача 2: Подсчет символов в строке
# Напишите функцию `count_characters(string)`, которая принимает строку и
# возвращает словарь, где ключи - это символы строки, а значения - количество их вхождений.
#
# string = "hello world"
# Вывод функции: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

def count_characters(string):
    """
    Функция для подсчета символов в строке.

    :param string: Строка, в которой нужно посчитать символы.
    :return: Словарь, где ключи - символы строки, а значения - количество их вхождений.
    """
    character_count = {}
    for char in string:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

    # d = defaultdict(int)
    # for char in string:
    #     d[char] += 1
    # return dict(d)

# Задача 3: Обработка произвольного числа аргументов
# Напишите функцию `sum_positive_negative(*args)`, которая принимает произвольное число числовых аргументов
# и возвращает кортеж из двух значений: сумма положительных чисел и сумма отрицательных чисел.
#
# sum_positive_negative(1, -2, 3, -4, 5)
# Вывод функции: (9, -6)

def sum_positive_negative(*args):
    sym_positive = 0
    sym_negative = 0
    for num in args:
        if num >= 0:
            sym_positive += num
        elif num < 0:
            sym_negative += num

    return sym_positive, sym_negative
print(sum_positive_negative(1, -2, 3, -4, 5))  # Вывод: (9, -6)
# Задача 4: Генерация строки из именованных аргументов
# Напишите функцию `generate_string(**kwargs)`, которая принимает произвольное число именованных аргументов и возвращает строку, состоящую из ключей и значений в формате "key=value".
#
# generate_string(name="Alice", age=30, city="New York")
# Вывод функции: name=Alice, age=30, city=New York

def generate_string(**kwargs):
    """
    Функция для генерации строки из именованных аргументов.

    :param kwargs: Именованные аргументы, которые нужно преобразовать в строку.
    :return: Строка, состоящая из ключей и значений в формате "key=value".
    """
    return ', '.join(f"{key}={value}" for key, value in kwargs.items())


