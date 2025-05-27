# Темы: Операции над строками, Индексы и срезы строк
# Результат по каждому заданию необходимо выводить в консоль через print().
#from collections.abc import async_generator

# 1. Объедините строки "Hello" и "London" без пробела. Ожидаемый результат: "HelloLondon"
str1= "Hello"
str2= "London"
str3=str1+str2
print(str3)


# 2. Выведите последний символ строки "Programming". Ожидаемый результат: "g"
str="Programming"
print(str[-1])


# 3. Дублируйте строку "Hi" три раза. Ожидаемый результат: "HiHiHi"
str="Hi"
str2=str*3
print(str2)


# 4. Определите длину строки "Artificial Intelligence".
str = "Artificial Intelligence"
count=len(str)
print(count)

# 5. Объедините строки "Good" и "Morning" с запятой между ними. Ожидаемый результат: "Good,Morning"
str1="Good"
str2="Morning"
str3=str1+","+str2
print(str3)

# 6. Создайте срез строки "Natural Language Processing" со значением "nguag".
str="Natural Language Processing"
print(str[10:15])


# 7. Объедините строки "Data" и "Science" с дефисом между ними. Ожидаемый результат: "Data-Science"
str1="Data"
str2="Science"
str3=str1+"-"+str2
print(str3)

# 8. Объедините строки "AI" и "ML" с двоеточием между ними. Ожидаемый результат: "AI:ML"
str1="AI"
str2="ML"
str3=str1+":"+str2
print(str3)

# 9. Дублируйте строку "Test" шесть раз. Ожидаемый результат: "TestTestTestTestTestTest"
str="Test"
str2=str*6
print(str2)

# 10. Выведите первый символ строки "Python". Ожидаемый результат: "P"
str="Python"
print(str[:1])

# 11. Создайте срез строки "Hello, Anna!" от 0 до 5. Ожидаемый результат: "Hello"
str="Hello, Anna"
print(str[0:5])

# 12. Определите длину строки "Natural Language Processing".
str="Natural Language Processing"
count=len(str)
print(count)

# 13. Выведите второй символ строки "Лето". Ожидаемый результат: "е"
str="Лето"
print(str[1])

# 14. Выведите предпоследний символ строки "Machine Learning". Ожидаемый результат: "n"
str="Machine Learning"
print(str[-2])

# 15. Дублируйте строку "Yes" четыре раза. Ожидаемый результат: "YesYesYesYes"
str="Yes"
str2=str*6
print(str2)

# 16. Создайте срез строки "Deep Learning" со значением "ep Le".
str="Deep Learning"
print(str[2:7])

# 17. Выведите третий символ строки "Computer Vision". Ожидаемый результат: "m"
str="Computer Vision"
print(str[2])

# 18. Определите длину строки "Deep Learning". Ожидаемый результат: 13
str="Deep Learning"
count=len(str)
print(count)

# 19. Объедините строки "Python" и "Rocks" с пробелом между ними. Ожидаемый результат: "Python Rocks"
str1="Python"
str2="Rocks"
str3=str1+" "+str2
print(str3)
# 20. Создайте срез строки "Data Science" со значением "cien".
str="Data Science"
print(str[6:10])


