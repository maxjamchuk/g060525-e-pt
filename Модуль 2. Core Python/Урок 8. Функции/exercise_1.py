# Задача 1: Анализ чисел
# Напишите функцию `analyze_numbers(numbers)`, которая принимает список чисел
# и возвращает кортеж из трех значений: сумма всех чисел, среднее значение и количество четных чисел.
#
numbers = [1, 2, 3, 4, 5, 6]
# # Вывод функции: (21, 3.5, 3)
#
def analyze_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    average=total/ len(numbers)
    total1 = 0
    for number in numbers:
        if number % 2 == 0:
            total1 += 1
    return total, average, total1
print(analyze_numbers(numbers))
# Задача 2: Работа со строками
# Напишите функцию `analyze_strings(strings)`, которая принимает список строк
# и возвращает кортеж из трех значений: самая длинная строка, самая короткая строка и количество строк, содержащих букву "a"..
# Вывод функции: ('banana', 'date', 3)
strings = ["apple", "banana", "cherry", "date"]

def longer_str(strings):
    return max(strings, key=len)
def short_str(strings):
    return min(strings, key=len)
def amount_str_with_a(strings):
    total = 0
    for fruits in strings:
        if "a" in fruits:
            total += 1
    return total
print(longer_str(strings))        # banana
print(short_str(strings))         # date
print(amount_str_with_a(strings)) # 3 (apple, banana, date)
def analyze_strings(strings):
    longest = max(strings, key=len)
    shortest = min(strings, key=len)
    count_with_a = sum(1 for fruits in strings if "a" in fruits)
    return longest, shortest, count_with_a

print(analyze_strings(strings))
# Задача 3: Обработка словаря сотрудников
# Напишите функцию `analyze_salaries(employees)`, которая принимает словарь сотрудников и
# возвращает кортеж из трех значений: средняя зарплата, максимальная зарплата и имя сотрудника с максимальной зарплатой.
employees = {"Alice": 5000, "Bob": 7000, "Charlie": 6000}
def analyze_salaries(employees):
    salaries = employees.values()
    average_salary = sum(salaries) / len(salaries)
    max_salary = max(salaries)
    name_max_salary=max(employees, key=employees.get)
    return average_salary, max_salary, name_max_salary
print(analyze_salaries(employees))
# employees = {"Alice": 5000, "Bob": 7000, "Charlie": 6000}
# Вывод функции: (6000.0, 7000, 'Bob')


# Задача 4: Фильтрация списка
# Напишите функцию `filter_numbers(numbers)`, которая принимает список чисел и
# возвращает кортеж из двух списков: четные числа и нечетные числа.
#

# Вывод функции: ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9])
numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def filter_numbers(numbers1):
    even=[]
    odds=[]
    for num in numbers1:
        if num %2==0:
            even.append(num)
        elif num%2!=0:
            odds.append(num)
    return even, odds
print(filter_numbers(numbers1))