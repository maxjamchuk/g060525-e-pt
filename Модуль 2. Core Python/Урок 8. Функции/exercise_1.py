# Задача 1: Анализ чисел
# Напишите функцию `analyze_numbers(numbers)`, которая принимает список чисел
# и возвращает кортеж из трех значений: сумма всех чисел, среднее значение и количество четных чисел.
#
# Вывод функции: (21, 3.5, 3)
def analyze_numbers(numbers54675465):
    c=len(numbers54675465)

    sum_1=sum(numbers54675465)

    average=sum_1 / c

    eval_c=sum (1 for n in numbers54675465 if n % 2 ==0)

    return (sum_1, average, eval_c)


numbers = [1, 2, 3, 4, 5, 6]
result = analyze_numbers(numbers)
print(result)


# Задача 2: Работа со строками
# Напишите функцию `analyze_strings(strings)`, которая принимает список строк
# и возвращает кортеж из трех значений: самая длинная строка, самая короткая строка и количество строк, содержащих букву "a"..
#
# Вывод функции: ('banana', 'date', 3)
strings = ["apple", "banana", "cherry", "date"]
def analyze_strings(strings):
    longest=max(strings, key=len)
    shortest=min(strings, key=len)
    count_a = sum(1 for s in strings if "a" in s)
    return (longest, shortest, count_a)

print(analyze_strings(strings))


# Задача 3: Обработка словаря сотрудников
# Напишите функцию `analyze_salaries(employees)`, которая принимает словарь сотрудников и
# возвращает кортеж из трех значений: средняя зарплата, максимальная зарплата и имя сотрудника с максимальной зарплатой.
#
employees = {"Alice": 5000, "Bob": 7000, "Charlie": 6000}
# Вывод функции: (6000.0, 7000, 'Bob')
def analyze_employees(employees):
    salaries = employees.values()
    average = sum(salaries) / len(salaries)
    max_salary = max(salaries)
    max_name=max(employees, key=employees.get)
    return (average, max_salary, max_name)

print(analyze_employees(employees))



# Задача 4: Фильтрация списка
# Напишите функцию `filter_numbers(numbers)`, которая принимает список чисел и
# возвращает кортеж из двух списков: четные числа и нечетные числа.
#
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Вывод функции: ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9])

def filter_numbers(numbers):
    even=[n for n in numbers if n % 2 == 0]
    odd = [n for n in numbers if n % 2 != 0]
    return (even, odd)

print(filter_numbers(numbers))