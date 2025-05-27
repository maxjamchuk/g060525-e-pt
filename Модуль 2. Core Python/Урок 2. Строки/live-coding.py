# from icecream import ic as print
# # Конкатенации строк
str1 = "Hello"
# resul1 = str1 + " " + "World"
# print(resul1)
# # Дублирования строк
# str2 = "Hello1"
# resul2 = str2 * 3
# print(resul2[:-1])
# # Работу с индексами
# str3 = "Hello World"
# print(str3[0])  # Первый символ
# print(str3[-1])  # Последний символ
# print(str3[0:5])  # Срез от 0 до 5 (не включая 5)
# # Использование срезов
# print(str3[6:])  # Срез от 6 до конца
# print(str3[:5])  # Срез от начала до 5 (не включая 5)
#
#
# str4 = " hello, anna!"
# print(str4.upper())
# print(str4.lower())
# print(str4.title())  # Приводит к заглавной букве каждое слово
# print(str4.capitalize())  # Приводит к заглавной букве только первую букву строки
# print(str4.strip())  # Удаляет пробелы в начале и конце строки
# print(str4.replace("anna", "World"))  # Заменяет "Anna" на "World"
# print(str4.split(", "))  # Разделяет строку по запятой и пробелу
# print(str4.find("Anna"))  # Находит индекс подстроки "Anna"
# # print(str4.index("Anna"))  # Находит индекс подстроки "Anna", выбросит ошибку, если не найдено
# print(str4.count("a"))  # Считает количество вхождений "a" в строке
# print(str4.startswith("Hello"))  # Проверяет, начинается ли строка с "Hello"
# print(str4.endswith("!"))  # Проверяет, заканчивается ли строка на "!"

str_with_backslash = "Hello\\World"
print(str_with_backslash)  # Выводит строку с обратным слэшем
str_with_quotes = 'Hello "World"'
print(str_with_quotes)  # Выводит строку с кавычками
str_with_single_quotes = 'Hello \'World\''
print(str_with_single_quotes)  # Выводит строку с одинарными кавычками
str_with_new_str = "Hello\nWorld"
print(str_with_new_str)  # Выводит строку с переносом строки
str_with_tab = "Hello\tWorld"
print(str_with_tab)  # Выводит строку с табуляцией
str_with_unicode = "Hello \u2602"  # Юникод символа зонтика
print(str_with_unicode)  # Выводит строку с юникод символом
str_with_f_string = f"Hello {str1}!"  # Форматированная строка
print(str_with_f_string)  # Выводит строку с использованием f-строки
print("Hello {} World".format('test'))  # Выводит строку с разделителем