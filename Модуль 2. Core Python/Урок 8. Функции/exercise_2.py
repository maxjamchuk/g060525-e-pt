# Задача 1: Генерация словаря
# Напишите функцию `create_dict(keys, values)`, которая принимает два списка: ключи и значения,
# и возвращает словарь, где ключи из первого списка, а значения из второго.
#
# Вывод функции: {'name': 'Alice', 'age': 30, 'city': 'New York'}

def create_dict(keys, values):
    return dict(zip(keys, values))

keys = ["name", "age", "city"]
values = ["Alice", 30, "New York"]
result=create_dict(keys, values)
print(result)


# Задача 2: Подсчет символов в строке
# Напишите функцию `count_characters(string)`, которая принимает строку и
# возвращает словарь, где ключи - это символы строки, а значения - количество их вхождений.
#
string = "hello world"
# Вывод функции: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

def count_characters(string):
    result = {}
    for char in string:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

result= count_characters(string)
print(result)


# Задача 3: Обработка произвольного числа аргументов
# Напишите функцию `sum_positive_negative(*args)`, которая принимает произвольное число числовых аргументов
# и возвращает кортеж из двух значений: сумма положительных чисел и сумма отрицательных чисел.
#
# sum_positive_negative(1, -2, 3, -4, 5)
# Вывод функции: (9, -6)

def sum_positive_negative(*args):
    positive=0
    negative=0
    for number in args:
        if number >=0:
            positive += number
        else:
            negative += number
    return (positive, negative)

result= sum_positive_negative(1, -2, 3, -4, 5)
print(result)

# Задача 4: Генерация строки из именованных аргументов
# Напишите функцию `generate_string(**kwargs)`, которая принимает произвольное число именованных аргументов и возвращает строку, состоящую из ключей и значений в формате "key=value".
#
# generate_string(name="Alice", age=30, city="New York")
# Вывод функции: name=Alice, age=30, city=New York

def generate_string(**kwargs):
    parts = []
    for key, value in kwargs.items():
        parts.append(f"{key}={value}")
    return ", ".join(parts)

result = generate_string(name="Alice", age=30, city="New York", razmer_sisek=5, dlinna_chlena=3)
print(result)