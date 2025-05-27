# Тема: Основные методы строк
# Результат по каждому заданию необходимо выводить в консоль через print().

# 1. Преобразуйте строку "hOw aRe yOu?" в верхний регистр.
# Ожидаемый результат: "HOW ARE YOU?"
str = "hOw aRe yOu?"
print(str.upper())
# 2. Посчитайте количество символов "a" в строке "Bananas are amazing!".
str = "Bananas are amazing!"
print(str.count("a"))
# 3. Преобразуйте строку "PYTHON PROGRAMMING" в нижний регистр.
# Ожидаемый результат: "python programming"
str = "PYTHON PROGRAMMING"
print(str.lower())

# 4. Удалите начальные пробелы из строки "   Discover new worlds   ".
# Ожидаемый результат: "Discover new worlds   "
str = "   Discover new worlds   "
print(str.strip())

# 5. Замените "rainy" на "sunny" в строке "It was a rainy day.".
# Ожидаемый результат: "It was a sunny day."
str = "It was a rainy day."
print(str.replace("rainy" ,"sunny"))

# 6. Найдите индекс подстроки "innovation" в строке "Innovation drives progress.".
str = "Innovation drives progress."
print(str.find("Innovation"))

# 7. Удалите конечные пробелы из строки "   Explore the universe   ".
# Ожидаемый результат: "   Explore the universe"
str = "   Explore the universe   "
print(str.rstrip())


# 8. Найдите индекс подстроки "galaxy" в строке "The Milky Way galaxy is vast.".
str = "The Milky Way galaxy is vast."
print(str.find("galaxy"))

# 9. Разделите строку "Apple;Banana;Cherry;Date" по точке с запятой.
# Ожидаемый результат: ["Apple", "Banana", "Cherry", "Date"]
str = "Apple;Banana;Cherry;Date"
print(str.split(";"))

# 10. Замените "robots" на "humans" в строке "In the future, robots will rule the world.".
# Ожидаемый результат: "In the future, humans will rule the world."
str = "In the future, robots will rule the world."
print(str.replace("robots", "humans"))

# 11. Преобразуйте строку "artificial intelligence" в заглавный регистр.
# Ожидаемый результат: "Artificial Intelligence"
str = "artificial intelligence"
print(str.title())


# 12. Разделите строку "Python is a versatile language" по пробелам.
# Ожидаемый результат: ["Python", "is", "a", "versatile", "language"]
str = "Python is a versatile language"
print(str.split(" "))


# 13. Удалите начальные и конечные пробелы из строки "   Learn Python   ".
# Ожидаемый результат: "Learn Python"
str = "   Learn Python   "
print(str.strip(" "))
