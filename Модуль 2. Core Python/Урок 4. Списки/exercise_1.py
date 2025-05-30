# Упражнение 1: Управление списком покупок
# Создайте список покупок, содержащий элементы "bread", "milk", "eggs".
s_l=["bread", "milk", "eggs"]
# Измените элемент "milk" на "almond milk".
s_l[1]="almond milk"
# Создайте срез, содержащий первые два элемента списка.
ss_l=s_l[0:2]
# Создайте вложенный список, где каждый элемент списка покупок будет содержать его цену.
s_l1=[["bread", 0.50], ["milk", 1], ["eggs", 1.2]]
# Выведите список покупок, срез и вложенный список.
print(s_l)
print(ss_l)
print(s_l1)
# print(shopping_list)  # Ожидаемый результат: ["bread", "almond milk", "eggs"]
# print(slice_shopping_list)  # Ожидаемый результат: ["bread", "almond milk"]
# print(detailed_shopping_list)  # Ожидаемый результат: [["bread", 1.5], ["almond milk", 3.0], ["eggs", 2.0]]


# Упражнение 2: Управление списком студентов и их оценок
# Создайте список студентов, содержащий элементы "Alice", "Bob", "Charlie", "David".
students=["Alice", "Bob", "Charlie", "David"]
# Измените имя второго студента на "Eve".
students[1]="Eve"
# Создайте срез, содержащий студентов: "Bob", "Charlie".
top_students=students[1:3]
# Создайте вложенный список, где каждый студент имеет список своих оценок.
students_grades=["Alice", [7,6,8], "Eve", [6, 7, 10], "Charlie", [10, 10, 10], "David", [3, 4, 6] ]
# Выведите список студентов, срез и вложенный список.
print(students)
print(students_grades)
print(top_students)
# print(students)  # Ожидаемый результат: ["Alice", "Eve", "Charlie", "David"]
# print(top_students)  # Ожидаемый результат: ["Bob", "Charlie"]
# print(student_grades)  # Ожидаемый результат: [["Alice", [90, 85, 88]], ["Eve", [75, 80, 82]], ["Charlie", [95, 92, 93]], ["David", [78, 85, 84]]]



# Упражнение 3: Управление списком задач
# Создайте список задач, содержащий элементы "task1", "task2", "task3", "task4.
tasks=["task1", "task2", "task3", "task4"]
# Измените третью задачу на "task3 updated".
tasks[2]="task3 updated"
# Создайте срез, содержащий последние две задачи.
last_tasks=tasks[2:]
# Создайте вложенный список, где каждая задача имеет свой статус (True - выполнено, False - не выполнено).
detailed_tasks=[["task1", True], ["task2", False], ["task3", False], ["task4", True]]
# Выведите список задач, срез и вложенный список.
print(tasks)
print(last_tasks)
print(detailed_tasks)
# print(tasks)  # Ожидаемый результат: ["task1", "task2", "task3 updated", "task4"]
# print(last_tasks)  # Ожидаемый результат: ["task3", "task4"]
# print(detailed_tasks)  # Ожидаемый результат: [["task1", True], ["task2 updated", False], ["task3", True], ["task4", False]]
