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
from itertools import count

inventory = [
    {'product': "Laptop", 'price': 10, 'count': 13},
    {'product': "Mouse", 'price': 50, 'count': 1},
    {'product': "Keyboard", 'price': 30, 'count': 33},
    {'product': "Monitor", 'price': 20, 'count': 10}
]
def show_inventory(inventory):
    if not inventory:
        print("Инвентарь пуст.")
    else:
        print("Ваш инвентарь:")
        for item in inventory:
            print(f"Товар: {item['product']}, Цена: {item['price']}, Количество: {item['count']}")
def add_inventory(inventory):
    name=input("Введите название товара: ")
    price_item=input("Введите цену товара: ")
    count_item=input("Введите количество товара: ")
    inventory.append({'product': name, 'price': price_item, 'count': count_item})
    print(f"Товар {name} добавлен в инвентарь.")
    print(inventory)
def delet_item(inventory):
    name=input("Введите название товара, который хотите удалить: ").lower()
    for i, item in enumerate(inventory):
        if item['product'].lower() == name:
            del inventory[i]
            print(f"Товар '{item['product']}' удалён из инвентаря.")
            return
    print("Товар с таким названием не найден.")
def update_item(inventory):
        name=input("Введите название товара, который хотите изменить: ").lower()
        for item in inventory:
            if  item['product'].lower() == name:
                new_name=input("Введите новое название товара: ")
                new_price= int(input("Введите новую цену товара: "))
                new_count= int(input("Введите новое количество товара: "))
                item['product'] =new_name
                item['price'] = new_price
                item['count'] = new_count
                print(f"Товар {name} был изменен на {item['product'], item['price'], item['count'] }")
                return
def found_item(inventory):
    name=input("Введите название товара, который хотите найти: ").lower()
    for item in inventory:
        if item['product'].lower() == name:
            print(item)
            break
    else:
        print("Введенного товара не существует.")
def low_coast_item(inventory):
    user_price=int(input("Введите максимальную цену товара: "))
    found = False
    for item in inventory:
        if item['price'] < user_price:
            print(item)
            found=True
    if not found:
        print("Товара ценой ниже введенной не существует")
def low_count_item(inventory):
    user_count = int(input("Введите максимальное количество товара: "))
    found = False
    for item in inventory:
        if item['count'] < user_count:
            print(item)
            found=True
    if not found:
        print("Товара количеством ниже введенного не существует.")






while True:
    user_input = input(
        "1. Показать список товаров.\n"
        "2. Добавить товар.\n"
        "3. Удалить товар.\n"
        "4. Обновить название товара, стоимость или количество.\n"
        "5. Найти товар по названию.\n"
        "6. Вывести список товаров меньше определнной стоимости.\n"
        "7. Вывести список товаров меньше определенного количества.\n"
        "8. Выйти.\n"
    )
    if user_input == "1":
        show_inventory(inventory)
    elif user_input == "2":
        add_inventory(inventory)
    elif user_input == "3":
        delet_item(inventory)
    elif user_input == "4":
        update_item(inventory)
    elif user_input == "5":
        found_item(inventory)
    elif user_input =="6":
        low_coast_item(inventory)
    elif user_input == "7":
        low_count_item(inventory)
    elif user_input == "8":
        print("Выход из программы.")
        break

