# Темы: Операции над строками, Индексы и срезы строк
# Результат по каждому заданию необходимо выводить в консоль через print().


# 1. Объедините строки "Hello" и "London" без пробела. Ожидаемый результат: "HelloLondon"
str1 = "Hello"
str2 = "London"
print(str1 + str2)

# 2. Выведите последний символ строки "Programming". Ожидаемый результат: "g"
# Индексация строк
str3 = "Programming"
print(str3[-1])

# 3. Дублируйте строку "Hi" три раза. Ожидаемый результат: "HiHiHi"
str4 = "Hi"
print(str4 * 3)

# 4. Определите длину строки "Artificial Intelligence".
str5 = "Artificial Intelligence"
print(len(str5))

# 5. Объедините строки "Good" и "Morning" с запятой между ними. Ожидаемый результат: "Good,Morning"
str6 = "Good"
str7 = "Morning"
print(str6 + "," + str7)

# 6. Создайте срез строки "Natural Language Processing" со значением "nguag".
str8 = "Natural Language Processing"
print(str8[10:15])
# 7. Объедините строки "Data" и "Science" с дефисом между ними. Ожидаемый результат: "Data-Science"
str9 = "Data"
str10 = "Science"
print(str9 + "-" + str10)

# 8. Объедините строки "AI" и "ML" с двоеточием между ними. Ожидаемый результат: "AI:ML"
str11 = "AI"
str12 = "ML"
print(str11 + ":" + str12)

# 9. Дублируйте строку "Test" шесть раз. Ожидаемый результат: "TestTestTestTestTestTest"
str13 = "Test"
print(str13 * 6)

# 10. Выведите первый символ строки "Python". Ожидаемый результат: "P"
str14 = "Python"
print(str14[0])
print(str14[-6])

# 11. Создайте срез строки "Hello, Anna!" от 0 до 5. Ожидаемый результат: "Hello"
str15 = "Hello, Anna!"
print(str15[0:5])

# 12. Определите длину строки "Natural Language Processing".
str16 = "Natural Language Processing"
print(len(str16))

# 13. Выведите второй символ строки "Лето". Ожидаемый результат: "е"
str17 = "Лето"
print(str17[1])

# 14. Выведите предпоследний символ строки "Machine Learning". Ожидаемый результат: "n"
str18 = "Machine Learning"
print(str18[-2])

# 15. Дублируйте строку "Yes" четыре раза. Ожидаемый результат: "YesYesYesYes"
str19 = "Yes"
print(str19 * 4)

# 16. Создайте срез строки "Deep Learning" со значением "ep Le".
str20 = "Deep Learning"
print(str20[2:7])

# 17. Выведите третий символ строки "Computer Vision". Ожидаемый результат: "m"
str21 = "Computer Vision"
print(str21[2])

# 18. Определите длину строки "Deep Learning". Ожидаемый результат: 13
str22 = "Deep Learning"
print(len(str22))

# 19. Объедините строки "Python" и "Rocks" с пробелом между ними. Ожидаемый результат: "Python Rocks"
str23 = "Python"
str24 = "Rocks"
print(str23 + " " + str24)

# 20. Создайте срез строки "Data Science" со значением "cien".
str25 = "Data Science"
print(str25[-6:-2])


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


# Темы: Спецсимволы и экранирование символов, Форматирование строк и F-строки
# Результат по каждому заданию необходимо выводить в консоль через print().

# 1. Вставьте символ новой строки в строку "Hello World".
# Ожидаемый результат:
# Hello
# World
print("Hello\nWord")

# 2. Вставьте символ обратного слэша в строку "This is a backslash: ".
# Ожидаемый результат: "This is a backslash: \"
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
print("She said, \'Hi!\'")

# 7. Экранируйте обратный слэш в строке "Path to file: C:\\".
# Ожидаемый результат: Path to file: C:\\
print("Path to file: C:\\\\")

# 8. Используйте метод `format()` для строки "This is a ... course for ... learners." с переменными course="Python"
# и level="beginner". Ожидаемый результат: "This is a Python course for beginner learners."
course = "Python"
level = "beginner"
example = "This is a {} course for {} learners.".format(course, level)
print(example)

# 9. Используйте F-строку для строки "This is a ... course for ... learners." с переменными
# course="Python" и level="beginner". Ожидаемый результат: "This is a Python course for beginner learners."
course = "Python"
level = "beginner"
f_example = f"This is a {course} course for {level} learners."
print(f_example)

# 10. Используйте метод `format()` для строки "Welcome to the ... workshop." с переменной topic="Machine Learning".
# Ожидаемый результат: "Welcome to the Machine Learning workshop."
topic = "Machine Learning"
invitation = "Welcome to the {} workshop.".format(topic)
print(invitation)

# 11. Используйте F-строку для строки "Welcome to the ... workshop." с переменной topic="Machine Learning".
# Ожидаемый результат: "Welcome to the Machine Learning workshop."
topic = "Machine Learning"
new_invitation = f"Welcome to the {topic} workshop."
print(new_invitation)

# 12. Придумайте название переменной и поместите в нее строку "machine learning",
str1 = "machine learning"

# затем преобразуйте первые буквы слов в заглавный регистр, чтобы получилось "Machine Learning".
str2 = str1.title()

# Затем создайте переменную со строкой "Course: ". Используйте метод `format()`, чтобы показать в консоле
# "Course: Machine Learning"
str3 = "Cours: "
name = str3 + "{}".format(str2)
print(name)

# 13. Объедините строки "Data" и "Science" с пробелом между ними, дублируйте результат три раза, и используйте F-строку
# для строки "Field: ...". Ожидаемый результат: "Field: Data ScienceData ScienceData Science"
str1 = "Data"
str2 = "Science"
str3 = (str1 + " " + str2) * 3
print(f"Field:{str3}")

# 14. Выведите третий символ строки "Information", затем используйте метод `format()` для строки "Third character: ...".
# Ожидаемый результат: "Third character: f"
str1 = "Information"
str2 = "Third character: {}".format(str1[2])
print(str2)

# 15. Определите длину строки "Neural Networks", умножьте её на 2, и используйте F-строку для строки "Length: ".
# Ожидаемый результат: "Length: 28"
str1 = len("Neural Networks")
print(str1)  # пробел учитывается как символ, итого их количество будет 15
str3 = f"Length: {str1 * 2}"
# str3 =f"Length: {str1*2-2}"  согласно ожидаемого результата задачи -)
print(str3)

# 16. Преобразуйте строку "Deep Learning" в заглавный регистр, найдите индекс подстроки "LEARNING", и выведите символ
# на этом индексе. Ожидаемый результат: "L"
str1 = "Deep Learning".upper()
str2 = str1.index('L')
print(str1[str2])

# 20. Определите длину строки "Starta", затем преобразуйте её в строку и добавьте к строке " has length of ",
# используя метод `format()`. Ожидаемый результат: "Starta has length of 6"
str1 = str(len("Starta"))
print("Starta has length of {} ".format(str1))
