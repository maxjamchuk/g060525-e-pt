# Тема: Чтение и запись данных в файл.

# Задание 1: Чтение данных из файла
# 1. Откройте файл `data.txt` для чтения.
# 2. Прочитайте весь контент файла и выведите его на экран.
# 3. Прочитайте первые 10 символов файла и выведите их на экран.
# 4. Прочитайте одну строку из файла и выведите ее на экран.
# 5. Прочитайте все строки файла и выведите их на экран.
file = open("text_files/data.txt", "r")
print(file.read())
file.seek(0)
first_ten = file.read(10)
print(first_ten)
file.seek(0)
one_str = file.readline()
print(one_str)
all_str = file.readlines()
print(all_str)
file.close()
# Задание 2: Запись данных в файл
# 1. Откройте (создайте) файл `output.txt` для записи.
# 2. Запишите в файл строку "Hello, World!".
# 3. Запишите в файл список строк: ["This is line 1\n", "This is line 2\n"].
# 4. Закройте файл.
# 5. Откройте файл `output.txt` для чтения и выведите его содержимое на экран.
file_w = open("text_files/output.txt", "w")
file_w.write("Hello, World!\n")
file_w.writelines(["This is line 1\n", "This is line 2\n"])
file_w.close()
file_w = open("text_files/output.txt", "r")
print(file_w.read())
file_w.close()
# Задание 3: Добавление данных в файл
# 1. Откройте (создайте) файл `log.txt` для добавления данных.
# 2. Добавьте строку "New log entry\n" в конец файла.
# 3. Добавьте список строк ["Log entry 1\n", "Log entry 2\n"] в конец файла.
# 4. Закройте файл.
# 5. Откройте файл `log.txt` для чтения и выведите его содержимое на экран.
file_w1 = open("text_files/log.txt", "a")
file_w1.write("New log entry\n")
file_w1.writelines(["Log entry 1\n", "Log entry 2\n"])
file_w1.close()
file_w1 = open("text_files/log.txt", "r")
print(file_w1.read())
file_w1.close()

# Задание 4: Работа с указателем
# 1. Откройте (создайте) файл `pointer_example.txt` для чтения и записи.
# 2. Запишите в файл строку "Python File Handling\n".
# 3. Переместите указатель в начало файла и прочитайте первую строку.
# 4. Переместите указатель на позицию 7 и прочитайте следующие 5 символов.
# 5. Переместите указатель в конец файла и добавьте строку "End of file\n".
# 6. Переместите указатель в начало файла и прочитайте весь файл.
file2 = open("text_files/pointer_example.txt", "w+")
file2.write("Python File Handling\n")
file2.seek(0)
first_line =file2.readline()
file2.seek(7)
next_five = file2.read(5)
file2.seek(0, 2)
last_str = file2.write("End of file\n")
file2.seek(0)
print(file2.read())
file2.close()

