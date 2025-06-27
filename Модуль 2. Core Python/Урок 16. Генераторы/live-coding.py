# Тема: Итераторы и генераторы. Функции-генераторы. Выражения-генераторы
# Покажите в режиме live-coding и объясните:
# - Создание и использование итератора
# Пример 1
# numbers = [1, 2, 3, 4, 5]  # Готовая коллекция элементов
# iter_numbers = iter(numbers)  # Создается итератор
#
# print(next(iter_numbers))  # Вывод по одному элементу
# print(next(iter_numbers))  # Вывод по одному элементу
# print(next(iter_numbers))  # Вывод по одному элементу
# print(next(iter_numbers))  # Вывод по одному элементу
# print(next(iter_numbers))  # Вывод по одному элементу
# print(next(iter_numbers))  # StopIteration

# цикл for реализует внутри себя iter() и next()
# iter_numbers = iter(numbers)  # Создается итератор
# while True:
#     try:
#         print(next(iter_numbers))
#     except StopIteration:
#         break


# Пример 2
# def number_generator():  # Генератор (функция-генератор)
#     for num in range(1, 6):  # Создание элементов
#         yield num  # yield останавливает цикл, запоминает его состояние
#                    # и отдает один элемент при каждом вызове
#
# gen_numbers = number_generator()
# print(next(gen_numbers))  # Вывод по одному элементу
# print(next(gen_numbers))  # Вывод по одному элементу
# print(next(gen_numbers))  # Вывод по одному элементу

# Пример 4
# def num_ret():  # Обычная функция
#     for num in range(1, 6):
#         return num
#
# ret = num_ret()
# print(ret)
# print(ret)
# print(ret)
# print(ret)
# print(ret)

# Пример 6
# squares_gen = (x * x for x in range(10))  # Выражение-генератор
# print(next(squares_gen))
# print(next(squares_gen))

# Пример 7
# squares_gen = (x * x for x in range(10))  # Выражение-генератор
# print(list(squares_gen))

# Пример 8
# numbers = [10, 20, 30, 40, 50]
# iter_numbers = iter(numbers)
#
# print(next(iter_numbers))  # 10
# print(next(iter_numbers))  # 20
# print(next(iter_numbers))  # 30
# print(next(iter_numbers))  # 40
# print(next(iter_numbers))  # 50
# print(next(iter_numbers))  # StopIteration

# Пример 9
# def countdown(n):
#     while n > 0:
#         yield n
#         n -= 1
#
# gen = countdown(3)
# print(next(gen))
# print(next(gen))
# print(next(gen))

# Пример 10
# def even_numbers(n):
#     for i in range(n):
#         if i % 2 == 0:
#             yield i
#
# gen = even_numbers(5)
# print(next(gen))
# print(next(gen))
# print(next(gen))

# - Создание и использование функции-генератора
# - Создание и использование выражения-генератора












# Тема: Генераторы и встроенные функции
# Покажите в режиме live-coding и объясните:
# - Использование генератора вместе с встроенными функциями list, set, min, max, sum.
# - Использование генератора вместе с циклом for.











# Тема: Генераторы и файлы
# Покажите в режиме live-coding и объясните:
# - Чтение файлов построчно через генераторы
# - Чтение файлов по частям через генераторы
# - Фильтрацию с файлами через генераторы





