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
