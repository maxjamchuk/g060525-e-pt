### Тема: Рекурсия

# 1. Напишите функцию `sum_list(lst)`, которая возвращает сумму всех элементов списка `lst` с помощью рекурсии.
# Пример использования:
# print(sum_list([1, 2, 3, 4, 5]))  # Вывод: 15
def sum_list(lst):
    if not lst:
        return 0
    return lst[0 + sum_list(lst[1:])]
print(sum_list([1, 2, 3, 4, 5]))

# 2. Напишите функцию `is_palindrome(s)`, которая проверяет, является ли строка `s` палиндромом
# (порядок букв одинаковый при чтении слева направо и справа налево) с помощью рекурсии.
# Пример использования:
# print(is_palindrome("radar"))  # Вывод: True
# print(is_palindrome("hello"))  # Вывод: False
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print(is_palindrome("radar"))  # Вывод: True
print(is_palindrome("hello"))  # Вывод: False




# 3. Напишите функцию `find_max`, которая возвращает минимальный элемент в списке `lst` с помощью рекурсии.
# Пример использования:
# print(find_min([4, 2, 8, 1, 9]))  # Вывод: 1

def find_max(lst):
    if len(lst) == 1:
        return lst[0]
    return max(lst[0], find_min(lst[1:]))
print(find_max([4, 2, 8, 1, 9]))  # Вывод: 9


# Тема: Дополнительная практика на рекурсию

# 1. Напишите функцию `sum_of_digits(n)`, которая возвращает сумму цифр числа `n` с помощью рекурсии.
# Пример использования:
# print(sum_of_digits(12345))  # Вывод: 15
def sum_of_digits(n):
    n = str(n)
    if not n:
        return 0
    return int(n[0]) + sum_of_digits(int(n[1:])) if len(n) > 1 else int(n[0])
print(sum_of_digits(12345))

# 2. Напишите функцию `reverse_string(s)`, которая возвращает строку `s` в обратном порядке с помощью рекурсии.
# Пример использования:
# print(reverse_string("hello"))  # Вывод: "olleh"
def reverse_string(s):
    if not s:
        return s
    return reverse_string(s[1:]) + s[0]
print(reverse_string("hello"))

# 3. Напишите функцию `list_length(lst)`, которая возвращает длину списка `lst` с помощью рекурсии.
# Пример использования:
# print(list_length([1, 2, 3, 4, 5]))  # Вывод: 5

def list_length(lst):
    if not lst:
        return 0
    return 1 + list_length(lst[1:])
print(list_length([1, 2, 3, 4, 5]))



# Тема: Дополнительная практика на функции

# 1. Напишите функцию `multiply_all`, которая принимает произвольное количество числовых аргументов с помощью `*args`
# и возвращает их произведение.
# Пример использования:
def multiply_all(*args):
    if not args:
        return 1
    if len(args) == 1:
        return args[0]
    return args[0] * multiply_all(*args[1:])


print(multiply_all(1, 2, 3, 4))  # Вывод: 24


# 2. Напишите функцию `merge_dicts`, которая принимает произвольное количество словарей с помощью `**kwargs`
# и возвращает один объединённый словарь.
# Пример использования:
# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
# print(merge_dicts(**dict1, **dict2))  # Вывод: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
def merge_dicts(**kwargs):
    if not kwargs:
        return {}
    keys = list(kwargs.keys())
    if len(keys) == 1:
        return {keys[0]: kwargs[keys[0]]}

    first_key = keys[0]
    first_value = kwargs.pop(first_key)
    rest_merged = merge_dicts(**kwargs)
    rest_merged[first_key] = first_value
    return rest_merged

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
print(merge_dicts(**dict1, **dict2))  # Вывод: {'a': 1, 'b': 2, 'c': 3, 'd': 4}




# 3. Напишите функцию `make_flatten`, которая создаёт функцию `flatten`, превращающую вложенный список в одноуровневый.
# Пример использования:
# flatten = make_flatten()
# print(flatten([1, [2, [3, 4], 5], 6]))  # Вывод: [1, 2, 3, 4, 5, 6]

def make_flatten():
    def flatten(lst):
        result = []
        for el in lst:
            if isinstance(el, list):
                result.extend(flatten(el))
            else:
                result.append(el)
        return result
    return flatten
flatten = make_flatten()
print(flatten([1, [2, [3, 4], 5], 6]))  # Вывод: [1, 2, 3, 4, 5, 6]

# 4. Напишите рекурсивную функцию `find_min`, которая возвращает минимальный элемент в списке `lst`.
# Пример использования:
# print(find_min([4, 2, 8, 1, 5]))  # Вывод: 1


def find_min(lst):
    if len(lst) == 1:
        return lst[0]
    return min(lst[0], find_min(lst[1:]))
print(find_min([4, 2, 8, 1, 5]))

# 5. Напишите функцию `show_info`, которая принимает произвольное количество именованных и неименованных аргументов
# с помощью `*args` и `**kwargs` и выводит их.
# Пример использования:
#args = (1, 2, 3)
#kwargs = {"name": "Alice", "age": 30}
#show_info(*args, **kwargs)
# Вывод:
# Args: (1, 2, 3)
# Kwargs: {'name': 'Alice', 'age': 30}
def show_info(*args, **kwargs):
    print(args)
    print(kwargs)
show_info(1, 2, 3, name = "Alice", age = 30)
