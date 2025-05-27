# Тема: Основные методы строк
# Результат по каждому заданию необходимо выводить в консоль через print().

# 1. Преобразуйте строку "hOw aRe yOu?" в верхний регистр.
# Ожидаемый результат: "HOW ARE YOU?"
str="hOw aRe yOu?"
str=str.upper()
print(str)

# 2. Посчитайте количество символов "a" в строке "Bananas are amazing!".
str="Bananas are amazing!"
res=str.count("a")
print(res)

# 3. Преобразуйте строку "PYTHON PROGRAMMING" в нижний регистр.
# Ожидаемый результат: "python programming"
str="PYTHON PROGRAMMING"
str=str.lower()
print(str)

# 4. Удалите начальные пробелы из строки "   Discover new worlds   ".
# Ожидаемый результат: "Discover new worlds   "
str="   Discover new worlds   "
str=str.lstrip(str)
print(str)

# 5. Замените "rainy" на "sunny" в строке "It was a rainy day.".
# Ожидаемый результат: "It was a sunny day."
str="It was a rainy day."
str=str.replace("rainy", "sunny")
print(str)

# 6. Найдите индекс подстроки "innovation" в строке "Innovation drives progress.".
str="Innovation drives progress."
res=str.index("innovation")
print(res)

# 7. Удалите конечные пробелы из строки "   Explore the universe   ".
# Ожидаемый результат: "   Explore the universe"
str="   Explore the universe   "
str=str.rstrip(str)
print(str)

# 8. Найдите индекс подстроки "galaxy" в строке "The Milky Way galaxy is vast.".
str="The Milky Way galaxy is vast."
res=str.index("galaxy")
print(res)

# 9. Разделите строку "Apple;Banana;Cherry;Date" по точке с запятой.
# Ожидаемый результат: ["Apple", "Banana", "Cherry", "Date"]
str="Apple;Banana;Cherry;Date"
res=str.split(";")
print(res)

# 10. Замените "robots" на "humans" в строке "In the future, robots will rule the world.".
# Ожидаемый результат: "In the future, humans will rule the world."
str="In the future, robots will rule the world."
res=str.replace("robots", "humans")
print(res)

# 11. Преобразуйте строку "artificial intelligence" в заглавный регистр.
# Ожидаемый результат: "Artificial Intelligence"
str="artificial intelligence"
res=str.title()
print(res)

# 12. Разделите строку "Python is a versatile language" по пробелам.
# Ожидаемый результат: ["Python", "is", "a", "versatile", "language"]
str="Python is a versatile language"
res=str.split(" ")
print(res)

# 13. Удалите начальные и конечные пробелы из строки "   Learn Python   ".
# Ожидаемый результат: "Learn Python"
str="   Learn Python   "
str=str.strip()
print(str)