# # Продемонстрируйте и объясните в режиме live-coding:
# # - Упаковку аргументов с args для списков и кортежей
#
# def func(*args):
#     print(args)
#
# func(1, 2, 3)  # Вывод: (1, 2, 3)
# # - Распаковку аргументов с kwargs для списков и кортежей
#
# def func2(**kwargs):
#     print(kwargs)
#
# func2(a=1, b=2, c=3)  # Вывод: {'a': 1, 'b': 2, 'c': 3}
#
# info = {'name': 'Alice', 'age': 30, 'city': 'New York', 'country': 'USA', 'occupation': 'Engineer'}
# def display_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
# display_info(**info)  # Вывод: name: Alice, age: 30, city: New York
# # - Упаковку аргументов с args и kwargs для списков и кортежей
# def func3(*args, **kwargs):
#     print("Args:", args)
#     print("Kwargs:", kwargs)
# func3(1, 2, 3, a=4, b=5)
#
#
# a= 1
#
# # Продемонстрируйте в режиме live-coding и объясните работу:
# # # - Глобальных и локальных переменных
xx = 10
def outer_function():
    x = 5  # Локальная переменная
    print("Outer x:", x)  # Доступ к локальной переменной

    def inner_function():
        nonlocal x  # Используем nonlocal для доступа к переменной из внешней функции
        x += 1
        print("Inner x:", x)  # Доступ к измененной локальной переменной
        global xx
        xx += 1
        print("Global x:", xx)

    inner_function()
    print("After inner function, outer x:", x)  # Проверяем значение после вызова inner_function
print(outer_function())

#
# # def some_function():
# #     local_var = "I am local"
# #     print(local_var)  # Доступ к локальной переменной
#
# def another_function():
#     def some_function():
#         local_var = "I am local"
#         print(local_var)
#         print(x)
#     some_function()
#     x = "I am global"
#
# def adder(n):
#     def add(x):
#         return x + n
#     return add
#
# add_five = adder(5)
# add_ten = adder(10)
# print(add_five(3))
# print(add_ten(3))
#
# # - Ключевых слов global и nonlocal
# # В- ложенных функций
# # - Замыкания
#
