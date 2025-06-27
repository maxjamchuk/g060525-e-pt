# Тема: Генераторы и встроенные функции

# Задача 1: Генератор и функция set()
# Задание: Напишите генератор, который возвращает числа от 1 до 10,
# но если число четное, возвратите его удвоенным.
# Используйте функцию set(),
# чтобы преобразовать результат генератора в множество и выведите его.
# def gen_even_double_numbers():
#     for i in range(1, 11):
#         if i % 2 == 0:
#             yield i * 2
#         else:
#             yield i
#
# result = set(gen_even_double_numbers())
# print(result)

# Задача 2: Генератор и функция sum()
# Задание: Напишите генератор, который возвращает числа от 1 до 20,кратные 3.
# Используйте функцию sum(),
# чтобы найти сумму всех этих чисел и выведите результат.
# def multiple_of_three():
#     for i in range(1, 21):
#         if i % 3 == 0:
#             yield i
#
# result = sum(multiple_of_three())
# print(result)

# Задача 3: Генератор и функции min() и max()
# Задание: Напишите генератор, который возвращает длины
# слов в заданной строке.
# Используйте функции min() и max(),
# чтобы найти минимальную и максимальную длину слов и выведите их.

sentence = "Write a generator that returns word lengths from a given sentence"

def gen_words_from_text(text):
    for word in text.split():
        yield len(word)

max_lengths = max(gen_words_from_text(sentence))
min_lengths = min(gen_words_from_text(sentence))
print(max_lengths)
print(min_lengths)