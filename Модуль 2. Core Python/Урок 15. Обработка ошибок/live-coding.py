# Тема: Обработка исключений (try/except/else/finally)
# Продемонстрируйте использование блоков try, except, else и finally.
# Покажите обработку исключений при чтении и записи файла.
# print(1 / 0)  # ZeroDivisionError: division by zero

# try:
    # действие, которое мы хотим проверить
# except:
    # действие, которое произошло, при совершении ошибки


# шаблон try/except
# try:
#     x = 1 / 0
# except ZeroDivisionError as e:
#     print(f'Произошла ошибка {e}')
# print('Продолжение выполнение работы программы')

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
# try:
#     result = 10 / 2
# except ZeroDivisionError:
#     print("Деление на ноль невозможно")
# else:  # выполняется только если ошибка не была перехвачена
#     print("Результат:", result)

# Обработка ошибок при записи в файл
# try:
#     with open("example.txt", "w") as file:
#         file.write("Hello, World!")
# except IOError:
#     print("Ошибка ввода-вывода")
# else:
#     print("Запись успешна")
# finally:
#     print("Операция завершена")


# try:
#     with open("example.txt", "r") as file:
#         content = file.read()
# except FileNotFoundError:
#     print("Ошибка: файл не найден")
# except PermissionError:
#     print("Ошибка: нет доступа к файлу")
# except IOError as e:
#     print(f"Ошибка ввода-вывода: {e}")













# Тема: Расространение исключения. Возбуждение исключения.
# Покажите в режиме live-coding и объясните:
# - Иерархию исключений
# - Распространение исключения

# Распространение исключения
def function1():  # Запуск цепочки вызовов
    function1()

def function1():
    try:
        function2()  # Вызов function2
    except ZeroDivisionError:
        print("Ошибка обработана в function1")  # Обработка исключения

def function2():
    function3()  # Вызов function3

def function3():
    result = 1 / 0  # Исключение возникает здесь (деление на ноль)
    # Исключение передается из function3 в function2, затем в function1,
    # где оно и обрабатывается.
function1()

# - Возбуждение исключение через raise
def check_positive_number(digit):
    if digit < 0:
        raise ValueError('Число должно быть положительным.')
    return True

try:
    check_positive_number(-10)
except ValueError:
    print('Ошибка перехвачена')