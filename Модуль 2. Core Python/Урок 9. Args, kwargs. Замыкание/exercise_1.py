# Тема: Упаковка аргументов с помощью *args, **kwargs и распаковка через * и **

# 1. Напишите функцию sum_all, которая принимает произвольное количество числовых аргументов
# с помощью *args и возвращает их сумму.
def sum_all(*args):
    return sum(args)
print(sum_all(45,56,76,10))

# 2. Напишите функцию combine_lists, которая принимает несколько списков в качестве аргументов с помощью *args
# и возвращает один объединённый список.
def combine_lists(*args):
    lst1=[]
    for lst in args:
        lst1.extend(lst)
    return lst1
print(combine_lists([1,4,6], [3,7,6], [8,4,6]))

# 3. Напишите функцию print_details, которая принимает два аргумента name и age.
# Затем создайте словарь с ключами name и age, распакуйте его и передайте в функцию print_details.
def print_details(name,age):
    print(f"name: {name} ,age: {age} ")
person = {"name": "David",
            "age": 40 }
print_details(**person)

# 4. Напишите функцию filter_numbers, которая принимает произвольное количество числовых аргументов с помощью *args
# и возвращает список только тех чисел, которые больше 10.
def filter_numbers(*args):
    numbers=[]
    for num in args:
        if num > 10:
            numbers.append(num)
    return numbers
print(filter_numbers(5, 12, 15, 7, 8, 13))