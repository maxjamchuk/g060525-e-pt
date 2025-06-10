# Проект: Управление инвентарем в интернет-магазине
# Разработайте программу для управления инвентарем интернет-магазина.
# Программа должна позволять добавлять новые товары и удалять имеющиеся,
# обновлять наименование, цену и количество существующих товаров,
# искать товары по названию, выводить список всех товаров и их количество,
# а также выводить товары с количеством ниже заданного значения стоимости и количества.
#
from email.policy import default
from itertools import product

# menu =[
# 1., "Показать список товаров.",
# 2.," Добавить товар.",
# 3., "Удалить товар.",
# 4., "Обновить название товара, стоимость или количество.",
# 5., "Найти товар по названию.",
# 6., "Вывести список товаров меньше определнной стоимости.",
# 7., "Вывести список товаров меньше определенного количества." ]

inventory = [
    {'product': "Laptop", 'price': 10, 'count': 13},
    {'product': "Mouse", 'price': 50, 'count': 1},
    {'product': "Keyboard", 'price': 30, 'count': 33},
    {'product': "Monitor", 'price': 20, 'count': 10}
]
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
        print(inventory)
    elif user_input == "2":
        name = input("Введите название товара: ")
        price = input("Введите цену товара: ")
        count = input("Введите количество товара: ")
        inventory.append({'product': name, 'price': price, 'count': count })
        print(inventory)
    elif user_input == "3":
        del_item = input("Введите название товара, который хотите удалить: ")
        for i, item in enumerate(inventory):
            if item['product'].lower() == del_item.lower():
                del inventory[i]
                print(f"Товар {del_item} удален.")
                print(inventory)
                break
        else:
            print(f"Товар {del_item} не найден.")
    elif user_input == "4":
        change_item = input("Введите название товара, который хотите изменить: ")
        for i, item in enumerate(inventory):
            if item['product'].lower() == change_item.lower():
                new_price=input("Введите новую цену: ")
                new_count=input("Введите количество: ")
                inventory[i]['price']= new_price
                inventory[i]['count']= new_count
                print(inventory)
                break
        else:
            print(f"Товар {change_item} не найден.")

    elif user_input == "5":
        show_item = input("Введите название товара который хотите найти: ")
        for i,item in enumerate(inventory):
            if item['product'].lower() == show_item.lower():
                print(inventory[i])
                break
        else:
            print(f"Товар {show_item} не найден. ")
    elif user_input == "6":
        low_coast=int(input("Введите максимальную стоимость: "))
        found = False
        for item in inventory:
            if item['price'] < low_coast:
                print(item)
                found = True
        if not found:
            print("Товаров меньше введенной стоимости не обнаружено. ")

    elif user_input == "7":
        low_count=int(input("Введите максимальнуое количество товара: "))
        found = False
        for item in inventory:
            if int(item['count']) < low_count:
                print(item)
                found = True
        if not found:
            print("Товаров с меньшим количеством не обнаружено")

    elif user_input == "8":
        break

