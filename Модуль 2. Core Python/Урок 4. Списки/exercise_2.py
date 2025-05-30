# Упражнение 1: Управление списком фильмов и их рейтингов

# 1.1 Создайте список фильмов, содержащий элементы "Movie1", "Movie2", "Movie3".
movies=[ "Movie1", "Movie2", "Movie3" ]
# 1.2 Пропишите условие: добавить в список фильм "Movie4", если его еще нет в списке.

if ("Movie4" not in movies):
    movies.append("Movie4")
print(movies)


newlist=["Movie5", "Movie6", "Movie7"]
# 1.3 Пропишите условия: если количество фильмов больше 2, то название второго фильма меняется на "Updated Movie2".
# Если количество фильмов меньше 5, то объедините имеющийся список с новым списком ["Movie5", "Movie6", "Movie7"]
if (len(movies) > 2):
    movies[1]="Updated Movie2"
if (len(movies) < 5):
    movies.extend(newlist)



# 1.4 Создайте вложенный список, где каждый фильм имеет свой год выпуска и рейтинг:
# ["Movie1", 2010, 8.1], ["Updated Movie2", 2015, 7.5], ["Movie3", 2020, 8.6], ["Movie4", 2021, 7.9],
# ["Movie5", 2013, 8.5], ["Movie6", 2018, 8.6], ["Movie7", 2023, 7.0]

movies2=[
["Movie1", 2010, 8.1],
["Updated Movie2", 2015, 7.5],
["Movie3", 2020, 8.6],
["Movie4", 2021, 7.9],
["Movie5", 2013, 8.5],
["Movie6", 2018, 8.6],
["Movie7", 2023, 7.0]
]

# 1.5 Добавьте фильм ["Movie", 2002, 7.7] в начало вложенного списка.
movies2.insert(0, ["Movie", 2002, 7.7])

# 1.6 Выведите список фильмов и вложенный список.
# print(movie_list)  #  "Movie1", "Movie2", "Movie3", "Movie4", "Movie5", "Movie6", "Movie7"
# print(movie_details)  # Ожидаемый результат: [["Movie", 2002, 7.7], ["Movie1", 2010, 8.1], ["Updated Movie2", 2015, 7.5],
# ["Movie3", 2020, 8.6], ["Movie4", 2021, 7.9], ["Movie5", 2013, 8.5], ["Movie6", 2018, 8.6], ["Movie7", 2023, 7.0]]
print(movies)
print(movies2)







# Упражнение 2: Анализ списка курсов и их продолжительности

# 2.1 Создайте список курсов, содержащий элементы "Python", "Java", "JavaScript".
course_list=["Python", "Java", "JavaScript"]

# 2.2 Добавьте в список курс "C++".

course_list.append("C++")
# 2.3 Измените название второго курса на "Kotlin".
course_list[1]="Kotlin"
# 2.4 Если первые три курса "Python", "Kotlin", "JavaScript", то создайте срез, содержащий первые три курса.
if (course_list.index("Python") <=2) and (course_list.index("Kotlin") <=2) and (course_list.index("JavaScript") <=2):
    cut_list=course_list[0:3]

# print(cut_list)

# 2.5 Отсортируйте курсы по названиям.

course_list.sort()
print(course_list)
# 2.6 Cоздайте вложенный список, где каждый курс имеет свою продолжительность в часах.
# ["Python", 40], ["Kotlin", 30], ["JavaScript", 35], ["C++", 50]

course_hours = ["Python", 40], ["Kotlin", 30], ["JavaScript", 35], ["C++", 50]

# 2.7 Выполните сложение часов всех курсов во вложенном списке и выведите общую продолжительность всех курсов.
hours_sum=0
c=len(course_hours)-1
for i in range(c + 1):
    hours_sum += course_hours[i][1]



print(hours_sum)

# 2.8 Выведите в консоль:
# - отсортированный список курсо, # Ожидаемый результат:['C++', 'JavaScript', 'Kotlin', 'Python']
# - срез, # Ожидаемый результат: ['Python', 'Kotlin', 'JavaScript']
# - вложенный список, # Ожидаемый результат: [['Python', 40], ['Kotlin', 30], ['JavaScript', 35], ['C++', 50]]
# - общую продолжительность всех курсов. # Ожидаемый результат: 155

