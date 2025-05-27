# Темы: Операции над строками, Индексы и срезы строк
# Результат по каждому заданию необходимо выводить в консоль через print().

# 1. Объедините строки "Hello" и "London" без пробела. Ожидаемый результат: "HelloLondon"
str1 = "Hello"
str2 = "London"
result = str1 + str2
print(result)
# 2. Выведите последний символ строки "Programming". Ожидаемый результат: "g"
str1 = "Programming"
last_char = str1[-1]
print(last_char)
# 3. Дублируйте строку "Hi" три раза. Ожидаемый результат: "HiHiHi"
str1 = "Hi"
print(str1*3)
# 4. Определите длину строки "Artificial Intelligence".
str1 = "Artificial Intelligence"
print(len(str1))
# 5. Объедините строки "Good" и "Morning" с запятой между ними. Ожидаемый результат: "Good,Morning"
str1 = "Good"
str2 = "Morning"
print(str1 + "," + str2)
# 6. Создайте срез строки "Natural Language Processing" со значением "nguag".
str1 = "Natural Language Processing"
#str1.find("nguag") поиск начала среза
substring = str1[10:15]
print(substring)
# 7. Объедините строки "Data" и "Science" с дефисом между ними. Ожидаемый результат: "Data-Science"
str1 = "Data"
str2 = "Science"
print(str1 + "-" + str2)
# 8. Объедините строки "AI" и "ML" с двоеточием между ними. Ожидаемый результат: "AI:ML"
str1 = "AI"
str2 = "ML"
print(str1 + ":" + str2)
# 9. Дублируйте строку "Test" шесть раз. Ожидаемый результат: "TestTestTestTestTestTest"
str1 = "Test"
print(str1*6)
# 10. Выведите первый символ строки "Python". Ожидаемый результат: "P"
str1 = "Python"
print(str1[0])
# 11. Создайте срез строки "Hello, Anna!" от 0 до 5. Ожидаемый результат: "Hello"
str1 = "Hello, Anna"
print(str1[:5])
# 12. Определите длину строки "Natural Language Processing".
str1 = "Natural Language Processing"
print(len(str1))
# 13. Выведите второй символ строки "Лето". Ожидаемый результат: "е"
str1 = "Лето"
print(str1[1])
# 14. Выведите предпоследний символ строки "Machine Learning". Ожидаемый результат: "n"
str1 = "Machine Learning"
print(str1[-2])
# 15. Дублируйте строку "Yes" четыре раза. Ожидаемый результат: "YesYesYesYes"
str1 = "Yes"
print(str1*4)
# 16. Создайте срез строки "Deep Learning" со значением "ep Le".
str1 = "Deep Learning"
print(str1[2:7])
# 17. Выведите третий символ строки "Computer Vision". Ожидаемый результат: "m"
str1 = "Computer Vision"
print(str1[2])
# 18. Определите длину строки "Deep Learning". Ожидаемый результат: 13
str1 = "Deep Learning"
print(len(str1))
# 19. Объедините строки "Python" и "Rocks" с пробелом между ними. Ожидаемый результат: "Python Rocks"
str1 = "Python"
str2 = "Rocks"
print(str1 + " " + str2)
# 20. Создайте срез строки "Data Science" со значением "cien".
str1 = "Data Science"
print(str1[6:10])

# Тема: Основные методы строк
# Результат по каждому заданию необходимо выводить в консоль через print().

# 1. Преобразуйте строку "hOw aRe yOu?" в верхний регистр.
# Ожидаемый результат: "HOW ARE YOU?"
str1 = "hOw aRe yOu?"
print(str1.upper())
# 2. Посчитайте количество символов "a" в строке "Bananas are amazing!".
str1 = "Bananas are amazing!"
print(str1.count("a"))
# 3. Преобразуйте строку "PYTHON PROGRAMMING" в нижний регистр.
# Ожидаемый результат: "python programming"
str1 = "PYTHON PROGRAMMING"
print(str1.lower())
# 4. Удалите начальные пробелы из строки "   Discover new worlds   ".
# Ожидаемый результат: "Discover new worlds   "
str1 = "   Discover new worlds   "
print(str1.lstrip())
# 5. Замените "rainy" на "sunny" в строке "It was a rainy day.".
# Ожидаемый результат: "It was a sunny day."
str1 = "It was a rainy day."
print(str1.replace("rainy", "sunny"))
# 6. Найдите индекс подстроки "innovation" в строке "Innovation drives progress.".
str1 = "Innovation drives progress."
print(str1.find("Innovation"))
# 7. Удалите конечные пробелы из строки "   Explore the universe   ".
# Ожидаемый результат: "   Explore the universe"
str1 = "   Explore the universe   "
print(str1.rstrip())
# 8. Найдите индекс подстроки "galaxy" в строке "The Milky Way galaxy is vast.".
str1 = "The Milky Way galaxy is vast."
print(str1.find("galaxy"))
# 9. Разделите строку "Apple;Banana;Cherry;Date" по точке с запятой.
# Ожидаемый результат: ["Apple", "Banana", "Cherry", "Date"]
str1 = "Apple;Banana;Cherry;Date"
print(str1.split(";"))
# 10. Замените "robots" на "humans" в строке "In the future, robots will rule the world.".
# Ожидаемый результат: "In the future, humans will rule the world."
str1 = "In the future, robots will rule the world."
print(str1.replace("robots" , "humans"))
# 11. Преобразуйте строку "artificial intelligence" в заглавный регистр.
# Ожидаемый результат: "Artificial Intelligence"
str1 = "artificial intelligence"
print(str1.title())
# 12. Разделите строку "Python is a versatile language" по пробелам.
# Ожидаемый результат: ["Python", "is", "a", "versatile", "language"]
str1 = "Python is a versatile language"
print(str1.split(" "))
# 13. Удалите начальные и конечные пробелы из строки "   Learn Python   ".
# Ожидаемый результат: "Learn Python"
str1 = "   Learn Python   "
print(str1.strip())
# Темы: Спецсимволы и экранирование символов, Форматирование строк и F-строки
# Результат по каждому заданию необходимо выводить в консоль через print().

# 1. Вставьте символ новой строки в строку "Hello World".
# Ожидаемый результат:
# Hello
# World
str1 = "Hello world"
print("Hello\nWorld")
# 2. Вставьте символ обратного слэша в строку "This is a backslash: ".
# Ожидаемый результат: "This is a backslash: \"
str1 = "This is a backslash: "
print("This is a backslash: \\")
# 3. Экранируйте кавычки в строке "He said, "Hello!"".
# Ожидаемый результат: He said, "Hello!"
print("He said, \"Hello!\"")
# 4. Экранируйте одинарные кавычки в строке "It's a sunny day".
# Ожидаемый результат: It's a sunny day
print("It\'s a sunny day")
# 5. Вставьте символ новой строки в строку "Python Programming".
# Ожидаемый результат:
# Python
# Programming
print("Python\nProgramming")
# 6. Экранируйте кавычки в строке "She said, 'Hi!'".
# Ожидаемый результат: She said, 'Hi!'
print("She said, \'Hi!'")
# 7. Экранируйте обратный слэш в строке "Path to file: C:\\".
# Ожидаемый результат: Path to file: C:\\
print("Path to file: C:\\\\")
# 8. Используйте метод `format()` для строки "This is a ... course for ... learners." с переменными course="Python"
# и level="beginner". Ожидаемый результат: "This is a Python course for beginner learners."
course="Python"
level="beginner"
formatted_str = "This is a {} course for {} learners.". format(course, level)
print(formatted_str)
# 9. Используйте F-строку для строки "This is a ... course for ... learners." с переменными
# course="Python" и level="beginner". Ожидаемый результат: "This is a Python course for beginner learners."
course="Python"
level="beginner"
formatted_str = f"This is a {course} course for {level} learners."
print(formatted_str)
# 10. Используйте метод `format()` для строки "Welcome to the ... workshop." с переменной topic="Machine Learning".
# Ожидаемый результат: "Welcome to the Machine Learning workshop."
topic="Machine Learning"
formatted_str = "Welcome to the {} workshop.". format(topic)
print(formatted_str)
# 11. Используйте F-строку для строки "Welcome to the ... workshop." с переменной topic="Machine Learning".
# Ожидаемый результат: "Welcome to the Machine Learning workshop."
topic="Machine Learning"
formatted_str = f"Welcome to the {topic} workshop."
print(formatted_str)
# 12. Придумайте название переменной и поместите в нее строку "machine learning",
# затем преобразуйте первые буквы слов в заглавный регистр, чтобы получилось "Machine Learning".
# Затем создайте переменную со строкой "Course: ". Используйте метод `format()`, чтобы показать в консоле
# "Course: Machine Learning"
opala = "machine learning"
opala = opala.title()
_afd_ = "Course: "
formatted_str = f"{_afd_}{opala}"
print(formatted_str)
# 13. Объедините строки "Data" и "Science" с пробелом между ними, дублируйте результат три раза, и используйте F-строку
# для строки "Field: ...". Ожидаемый результат: "Field: Data ScienceData ScienceData Science"
str1 = "Data"
str2 = "Science"
str3 = str1 + " " + str2
str4 = str3*3
formatted_str = f"Field: {str4}"
print(formatted_str)
# 14. Выведите третий символ строки "Information", затем используйте метод `format()` для строки "Third character: ...".
# Ожидаемый результат: "Third character: f"
str1 = "Information"
third_char = str1[2]
formatted_str = f"Third character: {third_char}"
print(formatted_str)
# 15. Определите длину строки "Neural Networks", умножьте её на 2, и используйте F-строку для строки "Length: ".
# Ожидаемый результат: "Length: 28"
str1 = "Neural Networks"
lange = len(str1)
lange = lange * 2
formatted_str = f"Length: {lange}"
print(formatted_str)
# 16. Преобразуйте строку "Deep Learning" в заглавный регистр, найдите индекс подстроки "LEARNING", и выведите символ
# на этом индексе. Ожидаемый результат: "L"
str1 = "Deep Learning"
str1 = str1.upper()
nomer = str1.find("LEARNING")
print(str1[nomer])
# 20. Определите длину строки "Starta", затем преобразуйте её в строку и добавьте к строке " has length of ",
# используя метод `format()`. Ожидаемый результат: "Starta has length of 6"
str1 = "Starta"
lange = len(str1)
formatted_str = f"{str1} has length of {lange}"
print(formatted_str)