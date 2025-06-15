# Задача 1: Анализ чисел
# Напишите функцию `analyze_numbers(numbers)`, которая принимает список чисел
# и возвращает кортеж из трех значений: сумма всех чисел, среднее значение и количество четных чисел.
#
# numbers = [1, 2, 3, 4, 5, 6]
# Вывод функции: (21, 3.5, 3)
from statistics import quantiles

def analyze_numbers(numbers):
    total = sum(numbers)
    e_nan = total / len (numbers) if numbers else  0
    c_tan = sum( n for n in numbers if n % 2 == 0)
    return (total, e_nan, c_tan)

print(analyze_numbers ([1, 2, 3, 4, 5, 6]))

# Задача 2: Работа со строками
# Напишите функцию `analyze_strings(strings)`, которая принимает список строк
# и возвращает кортеж из трех значений: самая длинная строка, самая короткая строка и количество строк, содержащих букву "a"..
#
# strings = ["apple", "banana", "cherry", "date"]
# Вывод функции: ('banana', 'date', 3)
def analyze_strings(strings):
    if not strings:
        return (None, None, 0)

    first = max(strings, key= len)
    last = min(strings, key = len)
    count = len(strings)
    long_count = sum( 1 for s in strings if 'a' in s.lower())

    return(first, last,long_count, count)
print(analyze_strings (["apple","banana", "data", "cherry"]))

# Задача 3: Обработка словаря сотрудников
# Напишите функцию `analyze_salaries(employees)`, которая принимает словарь сотрудников и
# возвращает кортеж из трех значений: средняя зарплата, максимальная зарплата и имя сотрудника с максимальной зарплатой.
#
# employees = {"Alice": 5000, "Bob": 7000, "Charlie": 6000}
# Вывод функции: (6000.0, 7000, 'Bob')
def analyze_salaries(employees):
    if not employees:
        return (0, 0, None)

    ses = sum(employees.values())
    total = ses / len(employees)
    max_salary = max(employees.values())
    max_employee = max(employees, key = employees.get)

    return (ses,total, max_salary, max_employee)

print(analyze_salaries({"Alice": 5000, "Bob": 7000, "Charlie": 6000}))


# Задача 4: Фильтрация списка
# Напишите функцию `filter_numbers(numbers)`, которая принимает список чисел и
# возвращает кортеж из двух списков: четные числа и нечетные числа.
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Вывод функции: ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9])
def fiter_numbers(numbers):
    even_numbers = [n for n in numbers if n % 2 == 0]
    odd_numbers = [n for n in numbers if n % 2 != 0]

    return (even_numbers, odd_numbers)

print(fiter_numbers([1,2,3,4,5,6,7,8,9,10]))

# Задача 5: Генерация словаря
# Напишите функцию `create_dict(keys, values)`, которая принимает два списка: ключи и значения,
# и возвращает словарь, где ключи из первого списка, а значения из второго.
#
# keys = ["name", "age", "city"]
# values = ["Alice", 30, "New York"]
# Вывод функции: {'name': 'Alice', 'age': 30, 'city': 'New York'}

def create_dict(keys, values):
    result = {}
    for i in range(len(keys)):
        result = [keys[i]] = values[i]
    return result
#

# Задача 6: Подсчет символов в строке
# Напишите функцию `count_characters(string)`, которая принимает строку и
# возвращает словарь, где ключи - это символы строки, а значения - количество их вхождений.
#
# string = "hello world"
# Вывод функции: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
def count_characters(string):
    result = {}
    for char in string:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result
string = "hello world"
print(count_characters(string))


# Задача 7: Обработка произвольного числа аргументов
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

# Задача 8: Генерация строки из именованных аргументов
# Напишите функцию `generate_string(**kwargs)`, которая принимает произвольное число именованных аргументов и возвращает строку, состоящую из ключей и значений в формате "key=value".
#
# generate_string(name="Alice", age=30, city="New York")
# Вывод функции: name=Alice, age=30, city=New York

def generate_string(**kwargs):
    parts = []
    for key, value in kwargs.items():
        parts.append(f"{key} = {value}")
        return ", ".join(parts)
    print(generate_string(name= "Alice", age= 30, city= "New York"))


# Проект: Перепишите проект из урока 7 в функциональном стиле.
# Управление инвентарем в интернет-магазине
# Разработайте программу для управления инвентарем интернет-магазина.
# Программа должна позволять добавлять новые товары и удалять имеющиеся,
# обновлять наименование, цену и количество существующих товаров,
# искать товары по названию, выводить список всех товаров и их количество,
# а также выводить товары с количеством ниже заданного значения стоимости и количества.
#
# Меню:
# 1. Показать список товаров.
# 2. Добавить товар.
# 3. Удалить товар.
# 4. Обновить название товара, стоимость или количество.
# 5. Найти товар по названию.
# 6. Вывести список товаров меньше определнной стоимости.
# 7. Вывести список товаров меньше определенного количества.

# inventory = [
#     {'product': "Laptop", 'price': 10, 'count': 13},
#     {'product': "Mouse", 'price': 50, 'count': 1},
#     {'product': "Keyboard", 'price': 30, 'count': 33},
#     {'product': "Monitor", 'price': 20, 'count': 10}
# ]

inventory = [
    {'product': "Laptop", 'price': 10, 'count': 13},
    {'product': "Mouse", 'price': 50, 'count': 1},
    {'product': "Keyboard", 'price': 30, 'count': 33},
    {'product': "Monitor", 'price': 20, 'count': 10}
]

def show_inventory(inventory):
    if not inventory:
        print("Инвентарь пуст.")
        return
    print("Список товаров:")
    for item in inventory:
        print(f"Product: {item['product']}, Price: {item['price']},Quantity : {item['quantity']}")
def add_product():
    name = input("Productname:")
    price = float(input("Price:"))
    men = int(input("Quantity:"))
    inventory.append({'product': name, 'price': price, 'quantity':quantity})
    print("Product added.")

def show_low_stock():
    limit = int(input("Show products with quantity below:"))
    for item in inventory:
        if item['quantity'] < limit:
            print(f"{item['product']}:{item['quantity']} inits")


while True:

        "1. Показать список товаров.\n"
        "2. Добавить товар.\n"
        "3. Удалить товар.\n"
        "4. Обновить название товара, стоимость или количество.\n"
        "5. Найти товар по названию.\n"
        "6. Вывести список товаров меньше определнной стоимости.\n"
        "7. Вывести список товаров меньше определенного количества.\n"
        "8. Выйти.\n"

        choice = input("Choose an option  (1-4):")
        if choice == "1":
            show_inventory()
        elif choice == "2":
                add_product()
        elif choice == "3":
                show_low_stock()
        elif choice == "4":
            print("Goodbye!")
        else:
            print("Invalid input.")



