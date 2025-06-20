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
