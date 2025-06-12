# Задача 1: Генерация словаря
# Напишите функцию `create_dict(keys, values)`, которая принимает два списка: ключи и значения,
# и возвращает словарь, где ключи из первого списка, а значения из второго.
#
# keys = ["name", "age", "city"]
# values = ["Alice", 30, "New York"]
# Вывод функции: {'name': 'Alice', 'age': 30, 'city': 'New York'}
def create_dict(name, age, city):
    return {"Name": name, "Age": age, "City": city}
result = create_dict("Alice", 30, "New York" )
print(result)
# Задача 2: Подсчет символов в строке
# Напишите функцию `count_characters(string)`, которая принимает строку и
# возвращает словарь, где ключи - это символы строки, а значения - количество их вхождений.
#
string = "hello world"
# Вывод функции: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
def count_characters(string):
    result={}
    for char in string:
        if char in result:
            result[char] +=1
        else:
            result[char] = 1
    return result
print(count_characters(string))
# Задача 3: Обработка произвольного числа аргументов
# Напишите функцию `sum_positive_negative(*args)`, которая принимает произвольное число числовых аргументов
# и возвращает кортеж из двух значений: сумма положительных чисел и сумма отрицательных чисел.
#
numbers=(1, -2, 3, -4, 5)
# Вывод функции: (9, -6)
def sum_positive_negative(*args):
    pos_sum=sum(x for x in numbers if x>0)
    neg_sum=sum(x for x in numbers if x<0)
    return pos_sum, neg_sum
print(sum_positive_negative(numbers))
# Задача 4: Генерация строки из именованных аргументов
# Напишите функцию `generate_string(**kwargs)`, которая принимает произвольное число именованных аргументов и возвращает строку, состоящую из ключей и значений в формате "key=value".
#
# generate_string(name="Alice", age=30, city="New York")
# Вывод функции: name=Alice, age=30, city=New York
def generate_string(**kwargs):
    values=[]
    for key, value in kwargs.items():
        values.append(f"{key} = {value}")
    return ", ".join(values)
print(generate_string(name="Alice", age=30, city="New York"))