# Тема: Чтение и запись данных в файл.

# Задание 1: Чтение данных из файла
# 1. Откройте файл `data.txt` для чтения.
# 2. Прочитайте весь контент файла и выведите его на экран.
# 3. Прочитайте первые 10 символов файла и выведите их на экран.
# 4. Прочитайте одну строку из файла и выведите ее на экран.
# 5. Прочитайте все строки файла и выведите их на экран.

with open("data.txt", "r") as file:

    content = file.read()
    print("Весь контент файла:")
    print(content)

file = open("data.txt", "r")

content = file.read()
print("Весь файл:")
print(content)

file.close()


# Задание 2: Запись данных в файл
# 1. Откройте (создайте) файл `output.txt` для записи.
# 2. Запишите в файл строку "Hello, World!".
# 3. Запишите в файл список строк: ["This is line 1\n", "This is line 2\n"].
# 4. Закройте файл.
# 5. Откройте файл `output.txt` для чтения и выведите его содержимое на экран.



file = open("output.txt", "w")
file.write("Привіт, це новий файл!\n")
file.close()

file = open("output.txt", "r")
content = file.read()
print("Вміст файлу output.txt:")
print(content)
file.close()




# Задание 3: Добавление данных в файл
# 1. Откройте (создайте) файл `log.txt` для добавления данных.
# 2. Добавьте строку "New log entry\n" в конец файла.
# 3. Добавьте список строк ["Log entry 1\n", "Log entry 2\n"] в конец файла.
# 4. Закройте файл.
# 5. Откройте файл `log.txt` для чтения и выведите его содержимое на экран.
file = open("log.txt" , "w+")
content = file.read()
file.write("New log entry\n")
lines = ["Log entry 1\n", "Log entry 2\n"]
file.writelines(lines)
file.close()


file = open("log.txt", "r")
content = file.read()
print("Вміст log.txt:")
print(content)
file.close()

# Задание 4: Работа с указателем
# 1. Откройте (создайте) файл `pointer_example.txt` для чтения и записи.
# 2. Запишите в файл строку "Python File Handling\n".
# 3. Переместите указатель в начало файла и прочитайте первую строку.
# 4. Переместите указатель на позицию 7 и прочитайте следующие 5 символов.
# 5. Переместите указатель в конец файла и добавьте строку "End of file\n".
# 6. Переместите указатель в начало файла и прочитайте весь файл.

file = open("pointer_example.txt","w+")
file.write("Python File Handling\n")

file.seek(0)
line = file.readline()
print("Первая строка:", line.strip())

file.seek(7)
segment = file.read(5)
print("Перший рядок: " , line.strip())

file = open("pointer_example.txt","a+")
file.write("End of file\n")

file.seek(0)
segment = file.read()
print("Весь файл: " , line.strip())

file.close()