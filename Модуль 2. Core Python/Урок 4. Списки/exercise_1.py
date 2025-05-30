# Упражнение 1: Управление списком покупок
# Создайте список покупок, содержащий элементы "bread", "milk", "eggs".
# Измените элемент "milk" на "almond milk".
# Создайте срез, содержащий первые два элемента списка.
# Создайте вложенный список, где каждый элемент списка покупок будет содержать его цену.

shopping=["bread", "milk", "eggs"]
shopping[1]="almond milk"
list=shopping[1:2]
print(list)
price=[shopping[0], 25], [shopping[1], 500], [shopping[2], 500000000]


# Выведите список покупок, срез и вложенный список.
# print(shopping_list)  # Ожидаемый результат: ["bread", "almond milk", "eggs"]
# print(slice_shopping_list)  # Ожидаемый результат: ["bread", "almond milk"]
# print(detailed_shopping_list)  # Ожидаемый результат: [["bread", 1.5], ["almond milk", 3.0], ["eggs", 2.0]]
print(shopping)
print(price)


# Упражнение 2: Управление списком студентов и их оценок
# Создайте список студентов, содержащий элементы "Alice", "Bob", "Charlie", "David".
# Измените имя второго студента на "Eve".
# Создайте срез, содержащий студентов: "Bob", "Charlie".
# Создайте вложенный список, где каждый студент имеет список своих оценок.
students=["Alice", "Bob", "Charlie", "David", "VALENTINA KIS"]
students[1]="Eve&Adam"
cut=students[1:3]
print(cut)
ocenka=[[students[0],1],[students[1],12],[students[2],8],[students[3],2],[students[4],100500]]
print(ocenka)
# Выведите список студентов, срез и вложенный список.
# print(students)  # Ожидаемый результат: ["Alice", "Eve", "Charlie", "David"]
# print(top_students)  # Ожидаемый результат: ["Bob", "Charlie"]
# print(student_grades)  # Ожидаемый результат: [["Alice", [90, 85, 88]], ["Eve", [75, 80, 82]], ["Charlie", [95, 92, 93]], ["David", [78, 85, 84]]]



# Упражнение 3: Управление списком задач
# Создайте список задач, содержащий элементы "task1", "task2", "task3", "task4.
# Измените третью задачу на "task3 updated".
# Создайте срез, содержащий последние две задачи.
# Создайте вложенный список, где каждая задача имеет свой статус (True - выполнено, False - не выполнено).
tasks=[ ["task1", True],
        ["task2", False],
        ["task3", False],
        ["task4", False],
         ]
tasks[2][0]="task3 updated"


# Выведите список задач, срез и вложенный список.
# print(tasks)  # Ожидаемый результат: ["task1", "task2", "task3 updated", "task4"]
# print(last_tasks)  # Ожидаемый результат: ["task3", "task4"]
# print(detailed_tasks)  # Ожидаемый результат: [["task1", True], ["task2 updated", False], ["task3", True], ["task4", False]]
print(tasks[2:3])
print(tasks)