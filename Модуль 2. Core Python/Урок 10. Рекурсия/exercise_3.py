# Тема: Дополнительная практика на функции

# 1. Напишите функцию `multiply_all`, которая принимает произвольное
# количество числовых аргументов с помощью `*args`
# и возвращает их произведение.
# Пример использования:
# print(multiply_all(1, 2, 3, 4))  # Вывод: 24

def multiply_all(*args):
    if not args:
        return 1
    if len(args) == 1:
        return args[0]
    return args[0] * multiply_all(*args[1:])


# 2. Напишите функцию `merge_dicts`, которая принимает произвольное
# количество словарей с помощью `**kwargs`
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

# 3. Напишите функцию `make_flatten`, которая создаёт
# функцию `flatten`, превращающую вложенный список в одноуровневый.
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
# 4. Напишите функцию `show_info`, которая принимает
# произвольное количество именованных и неименованных аргументов
# с помощью `*args` и `**kwargs` и выводит их.
# Пример использования:
# args = (1, 2, 3)
# kwargs = {"name": "Alice", "age": 30}
# show_info(*args, **kwargs)
# Вывод:
# Args: (1, 2, 3)
# Kwargs: {'name': 'Alice', 'age': 30}
