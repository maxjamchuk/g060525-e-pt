# Тема: Упаковка аргументов с помощью *args, **kwargs и распаковка через * и **

# 1. Напишите функцию sum_all, которая принимает произвольное количество числовых аргументов
# с помощью *args и возвращает их сумму.


# 2. Напишите функцию combine_lists, которая принимает несколько списков в качестве аргументов с помощью *args
# и возвращает один объединённый список.
def combine_lists(*args):
    combined_list = []
    for lst in args:
        combined_list.extend(lst)
    return combined_list

print(combine_lists([1, 2, 3], [4, 5], [6, 7, 8], [6, 7, 8], [6, 7, 8], [6, 7, 8], [6, 7, 8], [6, 7, 8]))  # Вывод: [1, 2, 3, 4, 5, 6, 7, 8]

# 3. Напишите функцию print_details, которая принимает два аргумента name и age.
# Затем создайте словарь с ключами name и age, распакуйте его и передайте в функцию print_details.


# 4. Напишите функцию filter_numbers, которая принимает произвольное количество числовых аргументов с помощью *args
# и возвращает список только тех чисел, которые больше 10.

def filter_numbers(*args):
    numbers = []
    for el in args:
        if el > 10:
            numbers.append(el)
    return numbers
    # return [num for num in args if num > 10]

print(filter_numbers(5, 12, 3, 15, 8, 20))  # Вывод: [12, 15, 20]