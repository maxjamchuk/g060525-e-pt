# Темы: Спецсимволы и экранирование символов, Форматирование строк и F-строки
# Результат по каждому заданию необходимо выводить в консоль через print().

# 1. Вставьте символ новой строки в строку "Hello World".
# Ожидаемый результат:
# Hello
# World
print("Hello\nWorld")


# 2. Вставьте символ обратного слэша в строку "This is a backslash: ".
# Ожидаемый результат: "This is a backslash: \"
str2 = "This is a backslash: \\"
print(str2)


# 3. Экранируйте кавычки в строке "He said, "Hello!"".
# Ожидаемый результат: He said, "Hello!"
str3 = "He said, \"Hello!\""
print(str3)


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
course="Python"
level="beginner"
print("This is a {} course for {} learners.".format(course,level))



# 9. Используйте F-строку для строки "This is a ... course for ... learners." с переменными
# course="Python" и level="beginner". Ожидаемый результат: "This is a Python course for beginner learners."
course="Python"
level="beginner"
print(f"This is a {course} course for {level} learners.")

# 10. Используйте метод `format()` для строки "Welcome to the ... workshop." с переменной topic="Machine Learning".
# Ожидаемый результат: "Welcome to the Machine Learning workshop."
workshop="Machine Learning"
print("Welcome to the {} workshop.".format(workshop))

# 11. Используйте F-строку для строки "Welcome to the ... workshop." с переменной topic="Machine Learning".
# Ожидаемый результат: "Welcome to the Machine Learning workshop."
topic="Machine Learning"
print(f"Welcome to the{topic}workshop.")


# 12. Придумайте название переменной и поместите в нее строку "machine learning",
# затем преобразуйте первые буквы слов в заглавный регистр, чтобы получилось "Machine Learning".
# Затем создайте переменную со строкой "Course: ". Используйте метод `format()`, чтобы показать в консоле
# "Course: Machine Learning"
str12 = "machine learning"
str12_1 = str12.title()
course1 = "Course: "
print(" {} {}".format(course1, str12_1))

# 13. Объедините строки "Data" и "Science" с пробелом между ними, дублируйте результат три раза, и используйте F-строку
# для строки "Field: ...". Ожидаемый результат: "Field: Data ScienceData ScienceData Science"
str13 = "Data" +" "+ "Science"
str13_1 = str13*3
print(f"Field:{str13_1}")


# 14. Выведите третий символ строки "Information", затем используйте метод `format()` для строки "Third character: ...".
# Ожидаемый результат: "Third character: f"
str14 = "Information"
str14_1 = str14[2]
print("Third character:{}".format(str14_1))

# 15. Определите длину строки "Neural Networks", умножьте её на 2, и используйте F-строку для строки "Length: ".
# Ожидаемый результат: "Length: 28"
str15 = "Neural Networks"*2
str15_1 = len(str15)
print(f"Length: {str15_1}")



# 16. Преобразуйте строку "Deep Learning" в заглавный регистр, найдите индекс подстроки "LEARNING", и выведите символ
# на этом индексе. Ожидаемый результат: "L"
str16 = "Deep Learning".upper()
index16 =str16.find("LEARNING")
result = str16[index16]
print(result)

# 20. Определите длину строки "Starta", затем преобразуйте её в строку и добавьте к строке " has length of ",
# используя метод `format()`. Ожидаемый результат: "Starta has length of 6"
str20 = "Starta"
str20_1 = len(str20)
print("{} has length of {}".format(str20,str20_1))

