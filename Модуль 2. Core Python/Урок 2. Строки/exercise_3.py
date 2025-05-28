# Темы: Спецсимволы и экранирование символов, Форматирование строк и F-строки
# Результат по каждому заданию необходимо выводить в консоль через print().

# 1. Вставьте символ новой строки в строку "Hello World".
# Ожидаемый результат:
# Hello
# World
str1= "Hello"
str2= "World"
print(str1 +"/n" +str2)


# 2. Вставьте символ обратного слэша в строку "This is a backslash: ".
# Ожидаемый результат: "This is a backslash: \"
str3 = "This is a backslash:\\"
print(str3)


# 3. Экранируйте кавычки в строке "He said, "Hello!"".
# Ожидаемый результат: He said, "Hello!"
str4 = "He said,\"Hello!\""
print(str4)


# 4. Экранируйте одинарные кавычки в строке "It's a sunny day".
# Ожидаемый результат: It's a sunny day

str5 = "It\'s a sunny day"
print(str5)
# 5. Вставьте символ новой строки в строку "Python Programming".
# Ожидаемый результат:
str6 = "Python."
str7 = ("Programming".
print(str6 + "\n" +str7)


# 6. Экранируйте кавычки в строке "She said, 'Hi!'".
# Ожидаемый результат: She said, 'Hi!'
str8 = "She said, 'Hi!'"
print(str8)

# 7. Экранируйте обратный слэш в строке "Path to file: C:\\".
# Ожидаемый результат: Path to file: C:\\
str9 = "Path to file: c:\\"
print(str9)

# 8. Используйте метод `format()` для строки "This is a ... course for ... learners." с переменными course="Python"
# и level="beginner". Ожидаемый результат: "This is a Python course for beginner learners."

course = "Python"
level = "beginner"
str10 = (f"This is a {course} course for {level} learners.")
print(str10)


# 9. Используйте F-строку для строки "This is a ... course for ... learners." с переменными
# course="Python" и level="beginner". Ожидаемый результат: "This is a Python course for beginner learners."

course = "Python"
level = "beginner"
str11 = (f"This is a {course} course for {level} learners")
print(str11)

# 10. Используйте метод `format()` для строки "Welcome to the ... workshop." с переменной topic="Machine Learning".
# Ожидаемый результат: "Welcome to the Machine Learning worksho
topic = "Machine Learning"
str12(f"Welcome to the {topic} workshop")
print(str12)

# 11. Используйте F-строку для строки "Welcome to the ... workshop." с переменной topic="Machine Learning".
# Ожидаемый результат: "Welcome to the Machine Learning workshop."


topic = "Machine Learning workshop"
str13(f"Welcome to the {topic} workshop")
print(str13)
# 12. Придумайте название переменной и поместите в нее строку "machine learning",
# затем преобразуйте первые буквы слов в заглавный регистр, чтобы получилось "Machine Learning".
# Затем создайте переменную со строкой "Course: ". Используйте метод `format()`, чтобы показать в консоле
# "Course: Machine Learning"
str14 = "machine learning"
str15 = "Course:{}"
a = str14.title()
b =(str15.format(a)
print(b)

# 13. Объедините строки "Data" и "Science" с пробелом между ними, дублируйте результат три раза, и используйте F-строку
# для строки "Field: ...". Ожидаемый результат: "Field: Data ScienceData ScienceData Science"

word1 = "Data"
word2 = "Science"
com = word1 + " " + word2
print(f"Field:{com})
# 14. Выведите третий символ строки "Information", затем используйте метод `format()` для строки "Third character: ...".
# Ожидаемый результат: "Third character: f"
str19 = "Information"
str20 = str19[2]
c = (f"Third character: {str20}")

# 15. Определите длину строки "Neural Networks", умножьте её на 2, и используйте F-строку для строки "Length: ".
# Ожидаемый результат: "Length: 28"
str21 = "Neural Networks"
str22 = len(str21 *2)
print(f"Length:{length}")

# 16. Преобразуйте строку "Deep Learning" в заглавный регистр, найдите индекс подстроки "LEARNING", и выведите символ
# на этом индексе. Ожидаемый результат: "L"
str23 = "Deep Learning"
d = str23.upper()
index = d.find("LEANING")
print(d[index])

# 20. Определите длину строки "Starta", затем преобразуйте её в строку и добавьте к строке " has length of ",
# используя метод `format()`. Ожидаемый результат: "Starta has length of 6"

str24 = "Starta"
str25 = len(str24)
p = "{} has langth of{}".format(str24, str25)
print(p)