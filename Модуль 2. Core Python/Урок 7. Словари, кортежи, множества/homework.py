# Тема: словари

# Задача 1: Анализ данных о сотрудниках
# У вас есть словарь, содержащий информацию о сотрудниках компании.
# Необходимо провести различные операции с этими данными.
#
# Задание:
# 1. Выведите имена всех сотрудников.
# 2. Найдите и выведите общую сумму зарплат всех сотрудников.
# 3. Добавьте нового сотрудника "David" с возрастом 28, отделом "IT" и зарплатой 6500.
# 4. Обновите зарплату "Alice" до 5500.
# 5. Удалите сотрудника "Charlie".
# 6. Выведите данные о каждом сотруднике в формате:
# "Имя: {name}, Возраст: {age}, Отдел: {department}, Зарплата: {salary}"
#
employees = {
"Alice": {"age": 30, "department": "HR", "salary": 5000},
"Bob": {"age": 25, "department": "IT", "salary": 6000},
"Charlie": {"age": 35, "department": "Finance", "salary": 7000}
 }

employees["Alex"] = {"age": 40, "department": "Marketing", "salary": 8000}
for name in employees:
    print(name)
    total_salary = sum(emp["salary"] for emp in employees.values())
    print("Total salary:", total_salary)
    employees["David"] = {"age": 28, "department": "IT", "salary": 6500}
    employees["Alice"]["salary"] = 5500
    del employees["Charlie"]
    for name, info in employees.items():
        print(f"Name: {name}, Age: {info['age']}, Department: {info['department']}, Salary: {info['salary']}")


# Задача 2: Управление запасами товаров
# У вас есть словарь, содержащий информацию о запасах товаров в магазине.
# Необходимо провести различные операции с этими данными.
#
# Задание:
# 1. Выведите названия всех товаров.
# 2. Увеличьте количество "Apples" на 10.
# 3. Измените цену "Bananas" на 1.5.
# 4. Удалите товар "Cherries".
# 5. Добавьте новый товар "Dates" с количеством 15 и ценой 4.
# 6. Выведите общую стоимость всех товаров (количество * цена для каждого товара и сумма этих значений).
#
# inventory = {
#     "Apples": {"quantity": 50, "price": 2},
#     "Bananas": {"quantity": 30, "price": 1},
#     "Cherries": {"quantity": 20, "price": 3},
# }
inventory = {
    "Apples": {"quantity": 50, "price": 2},
    "Bananas": {"quantity": 30, "price": 1},
    "Cherries": {"quantity": 20, "price": 3},
}

inventory["Apples"]["quantity"] += 10
inventory["Bananas"]["price"] = 1
del inventory["Cherries"]
inventory["Dates"] = {"quantity": 15, "price": 4}
total_value = 0
for product, data in inventory.items():
    total_value += data["quantity"] * data["price"]
    print("Tot al inventory value:", total_value)

print("Available products:", list(inventory.keys()))

# Тема: кортежи и множества.

# Задача 1: Обработка данных о координатах
# У вас есть список координат, каждая из которых представлена кортежем (x, y).
# Необходимо провести различные операции с этими данными.
#
# Задание:
# 1. Выведите все координаты.
# 2. Найдите сумму всех координат по оси x и по оси y.
# 3. Добавьте новую координату (70, 80).
# 4. Замените первую координату на (15, 25).
# 5. Выведите все координаты, отсортированные по оси x.
#
# coordinates = [(10, 20), (30, 40), (50, 60)]

coordinates = [(10, 20), (30, 40), (50, 60)]
for point in coordinates:
    print(point)

sum_x = sum(x for x, y in coordinates)
sum_y = sum(y for x, y in coordinates)
print("Summa x:", sum_x)
print("Summa y:", sum_y)

coordinates.append((70, 80))

coordinates[0] = (15, 25)

coordinates_sorted = sorted(coordinates, key=lambda coord: coord[0])
print("Sorted coordinates X:")
for point in coordinates_sorted:
    print(point)

# Задача 2: Обработка данных о продуктах
# У вас есть список продуктов, каждый из которых представлен кортежем (название, цена).
# Необходимо провести различные операции с этими данными.
#
# Задание:
# 1. Выведите все продукты.
# 2. Найдите суммарную стоимость всех продуктов.
# 3. Добавьте новый продукт "Date" с ценой 4.
# 4. Замените цену "Apple" на 2.5.
# 5. Выведите все продукты, отсортированные по цене.
#
# products = [("Apple", 2), ("Banana", 1), ("Cherry", 3)]
products = [("Apple", 2), ("Banana", 1), ("Cherry", 3)]
for product in products:
    print(product)

total_price = sum(price for name, price in products)
print("Total price:",total_price)

products.append(("Date", 4))

products = [(name, 2.5) if name == "Apple" else (name, price) for name, price in products]

products_sorted = sorted(products, key=lambda item: item[1])
print("Product sorted by price:")
for product in products_sorted:
    print(product)

# Задача 3: Управление группами пользователей
# У вас есть множество пользователей, и вам необходимо выполнить различные операции с этими данными.
#
# Задание:
# 1. Выведите всех пользователей.
# 2. Добавьте нового пользователя "David".
# 3. Удалите пользователя "Bob".
# 4. Проверьте, есть ли пользователь "Alice" в множестве.
# 5. Выведите количество пользователей.
#
# users = {"Alice", "Bob", "Charl
groups = {
    "admins":{"alice", "bob"},
    "editors":{"carol", "david"},
    "viewers":{"eve"}
}
groups["admins"].add("david")

groups["editors"].discard("bob")

user = "david"
print("Is alice an editor", user in groups["editors"])

all_users = set()
for users in groups.values():
    all_users.update(users)
print("All users:",len( all_users))




# Задача 4: Управление наборами данных
# У вас есть два множества, представляющих различные наборы данных.
# Необходимо провести различные операции с этими множествами.
#
# Задание:
# 1. Выведите элементы обоих множеств.
# 2. Найдите объединение двух множеств.
# 3. Найдите пересечение двух множеств.
# 4. Найдите разность множеств `set1` и `set2`.
# 5. Проверьте, является ли `set2` подмножеством `set1`.
#
#set1 = {1, 2, 3, 4, 5}
#set2 = {4, 5, 6, 7, 8}

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1:", set1)
print("Set 2:", set2)

union_set = set1 | set2
print("Union:", union_set)

common = set1 ^ set2
print("Intersection:",common)

difference = set1 - set2
print("Difference (set1 - set2):",difference)

sub = set2.issubset(set1)
print("Is set2 a sub of set1?", sub)


# Проект: Управление инвентарем в интернет-магазине
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

inventory = [
     {'product': "Laptop", 'price': 10, 'count': 13},
     {'product': "Mouse", 'price': 50, 'count': 1},
    {'product': "Keyboard", 'price': 30, 'count': 33},
    {'product': "Monitor", 'price': 20, 'count': 10}
]
for item in inventory:
    print(item['name'], "-", item['price']), "Quantity", item['count']

name = input("Enter product name")
price = float(input("Enter product price:"))
count = int(input("Enter product quantity:"))
new_product = {'name': name, 'proce': price, 'quantity': count}
inventory.append(new_product)
print("New product added:", new_product)

delete_name = input(("Enter the name of  the product to delete:"))
for item in inventory:
    if item['name'].lower() == delete_name.lower():
        inventory.remove(item)
        print("Product removed:", delete_name)
        break
else:
    print("Product not found.")

update_name = input("Enter the name of the product to update:")

for item in inventory:
    if item['name'].lower() == update_name.lower():
        new_name = input("New name (or press Enter to keep the same):")
        new_price = input("New price (or press Enter to kee the same):")
        new_count = input("New quantity (or press Enter to keep the same):")

        if new_name:
            item['name'] = new_name
            if new_price:
                item['price'] = float(new_price)
                if new_count:
                    item['count'] = int(new_count)
                    print("Product not found.")

search = input("Enter name to search:")
for item in inventory:
    if item['name'].lower() == search.lower():
        print("Found:", item)
        break
else:
    print("Product not found.")

    max_price = float(input("Enter maximum price:"))
    for item in inventory:
        if item['price'] < max_price:
            print(item['name'], "-", item['price'])

min_count = int(input("Show products with quantity less than:"))
for item in inventory:
    if item['count'] < min_count:
        print(item['name'], "- In stock:", item['count'])

