# Тема: Обработка исключений (try/except/else/finally)
# Продемонстрируйте использование блоков try, except, else и finally.
# Покажите обработку исключений при чтении и записи файла.
# print(1 / 0)  # ZeroDivisionError: division by zero

# try:
    # действие, которое мы хотим проверить
# except:
    # действие, которое произошло, при совершении ошибки


# шаблон try/except
try:
    x = 1 / 0
except:
    print('Произошла ошибка')
print('Продолжение выполнение работы программы')

# шаблон try/except/finally
# try:
#     file = open('ex.txt', 'r')
#     content = file.read()
# except FileNotFoundError:
#     print('Файл не найден!')
# finally:  # выполняется вне зависимости от того была ли перехвачена ошибка
#     file.close()
#

# else
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Деление на ноль невозможно")
else:  # выполняется только если ошибка не была перехвачена
    print("Результат:", result)















# Тема: Расространение исключения. Возбуждение исключения.
# Покажите в режиме live-coding и объясните:
# - Иерархию исключений
# - Распространение исключения
# - Возбуждение исключение через raise
