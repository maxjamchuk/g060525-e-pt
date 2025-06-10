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
from itertools import product, count

inventory = [
    {'product': "Laptop", 'price': 10, 'count': 13},
    {'product': "Mouse", 'price': 50, 'count': 1},
    {'product': "Keyboard", 'price': 30, 'count': 33},
    {'product': "Monitor", 'price': 20, 'count': 10}
]

action_list= [
        [1, "Показать список товаров."],
        [2, "Добавить товар."],
        [3, "Удалить товар."],
        [4, "Обновить название товара, стоимость или количество."],
        [5, "Найти товар по названию."],
        [6, "Вывести список товаров меньше определнной стоимости."],
        [7, "Вывести список товаров меньше определенного количества."],
        [0, "Выйти."]
]

def show_actions():
    for action in action_list[0:]:
        print(f"{action[0]}. {action[1]}")
    #print( action_list)
def exit_program():
    print("Вы выбрали выход из программы!\n пока пока лузеры!")
    exit(0)
def show_inventory():
    if len(inventory) == 0:
        print("Инвентарь пуст!")
    else:
        for i in range(len(inventory)):
            item=inventory[i]
            print(f"{i}: {item['product']}, {item['count']}, {item['price']} \n")

def add_product():
    name= input("Введите название товара: ")
    price= float(input("Введите цену товара: "))
    count= int(input("Введите количество товара: "))
    inventory.append({'product': name, 'price': price, 'count': count})
    print("Товар добавлен!\n")

def del_product():
    show_inventory()
    index = int(input("Введите номер товара для удаления"))
    if 0 <= index < len(inventory):
        del inventory[index]
        print("Товар не найден.\n")
    else:
        print("Товар не найден")

def update_product():
    show_inventory()
    index=int(input("Введите номер товара для обновления"))
    if 0 <= index < len(inventory):
        name = input("Введите новое имя товара: ")
        price = float(input("Новая цена: "))
        count = int(input("Новое количетсво: "))
        inventory[index]['product'] = name
        inventory[index]['price'] = price
        inventory[index]['count'] = count
        print("Товар обновлён!")
    else:
        print("Неверный номер товара!")
def find_product():
    name = input("Введите название товара для поиска: ")
    found = False
    for item in inventory:
        if item["product"].lower == name.lower():
            print(f"{item['product']} | Цена: {item['price']} | Кол-во: {item['count']}")

def filter_by_count():
    max_count = int(input("Введите максимальное количество: "))
    for item in inventory:
        if item['count'] < max_count:
            print(f"{item['product']} | Цена: {item['price']} | Кол-во {item['count']}")

def filter_more_count():
    max_count = int(input("Введите максимальное количество: "))
    for item in inventory:
        if item['count'] > max_count:
            print(f"{item['product']} | Цена: {item['price']} | Кол-во {item['count']}")

while True:
    show_actions()
    user_input = int(input("ВВедите номер вашего действия: "))
    if user_input == 1:
        show_inventory()
    elif user_input == 0:
        exit_program()
    elif user_input == 2:
        add_product()
    elif user_input == 3:
        del_product()
    elif user_input==4:
        update_product()
    elif user_input == 5:
        find_product()
    elif user_input == 6:
        filter_by_count()
    elif user_input == 7:
        filter_more_count()
    else:
        print("Вы ввели номер неправильной команды")