# Тема: Основные методы строк
# Результат по каждому заданию необходимо выводить в консоль через print().

# 1. Преобразуйте строку "hOw aRe yOu?" в верхний регистр.
# Ожидаемый результат: "HOW ARE YOU?"
str1 = "hOw aRe yOu?"
print(str1.upper())

# 2. Посчитайте количество символов "a" в строке "Bananas are amazing!".
str2 = "Bananas are amazing!"
print(str2.count('a'))

# 3. Преобразуйте строку "PYTHON PROGRAMMING" в нижний регистр.
# Ожидаемый результат: "python programming"
str3 = "PYTHON PROGRAMMING"
print(str3.lower())

# 4. Удалите начальные пробелы из строки "   Discover new worlds   ".
# Ожидаемый результат: "Discover new worlds   "
str4 = "   Discover new worlds   "
print(str4.lstrip())

# 5. Замените "rainy" на "sunny" в строке "It was a rainy day.".
# Ожидаемый результат: "It was a sunny day."
str5 = "It was a rainy day."
print(str5.replace('rainy', 'sunny'))

# 6. Найдите индекс подстроки "innovation" в строке "Innovation drives progress.".
str6 = "Innovation drives progress."
print(str6.lower().find('innovation'))

# 7. Удалите конечные пробелы из строки "   Explore the universe   ".
# Ожидаемый результат: "   Explore the universe"
str7 = "   Explore the universe   "
print(str7.rstrip())

# 8. Найдите индекс подстроки "galaxy" в строке "The Milky Way galaxy is vast.".
str8 = "The Milky Way galaxy is vast."
print(str8.lower().find('galaxy'))
print(str8.lower().index('galaxy'))

# 9. Разделите строку "Apple;Banana;Cherry;Date" по точке с запятой.
# Ожидаемый результат: ["Apple", "Banana", "Cherry", "Date"]
str9 = "Apple;Banana;Cherry;Date"
print(str9.split(";"))

# 10. Замените "robots" на "humans" в строке "In the future, robots will rule the world.".
# Ожидаемый результат: "In the future, humans will rule the world."
str10 = "In the future, robots will rule the world."
print(str10.replace('robots', 'humans'))

# 11. Преобразуйте строку "artificial intelligence" в заглавный регистр.
# Ожидаемый результат: "Artificial Intelligence"
str11 = "artificial intelligence"
print(str11.title())

# 12. Разделите строку "Python is a versatile language" по пробелам.
# Ожидаемый результат: ["Python", "is", "a", "versatile", "language"]
str12 = "Python is a versatile language"
print(str12.split(' '))

# 13. Удалите начальные и конечные пробелы из строки "   Learn Python   ".
# Ожидаемый результат: "Learn Python"
str13 = "   Learn Python   "
print(str13.lstrip().rstrip())
