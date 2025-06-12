# Тема: Глобальные и локальные переменные. Вложенные функции и замыкания.

# 1. Напишите функцию increment_global, которая увеличивает значение глобальной переменной counter на 1 каждый раз,
# когда она вызывается.
# increment_global()
# print(counter)  # Вывод: 1
# increment_global()
# print(counter)  # Вывод: 2
counter=0
def increment_global():
    global counter
    counter+=1
    return counter
print(increment_global())
print(increment_global())
# 2. Напишите функцию outer, которая содержит внутреннюю функцию inner. Внутренняя функция должна увеличивать
# значение переменной count, объявленной во внешней функции, на 1 каждый раз при её вызове.
# counter = outer()
# print(counter())  # Вывод: 1
# print(counter())  # Вывод: 2

def outer_funct():
    count = 0
    def inner_funct():
        nonlocal count
        count+=1
        return count
    return inner_funct
counter1=outer_funct()






# 3. Напишите функцию make_multiplier, которая принимает аргумент factor. Внутри этой функции создайте и
# верните функцию multiplier, которая умножает свой аргумент на factor.
# mult_by_2 = make_multiplier(2)
# print(mult_by_2(5))  # Вывод: 10
# mult_by_3 = make_multiplier(3)
# print(mult_by_3(5))  # Вывод: 15
def make_multiplier(factor):
    def multiplier(factoring):
        return factor * factoring
    return multiplier
mult_by_2 = make_multiplier(2)
print(mult_by_2(5))  # Вывод: 10
mult_by_3 = make_multiplier(30)
print(mult_by_3(50))  # Вывод: 15


# 4. Напишите функцию make_prefixer, которая принимает строку prefix и возвращает внутреннюю функцию prefixer.
# Внутренняя функция должна добавлять prefix к любому переданному ей аргументу.
# add_hello = make_prefixer("Hello, ")
# print(add_hello("Alice"))  # Вывод: Hello, Alice
# print(add_hello("Bob"))    # Вывод: Hello, Bob
def make_prefixer(prefix):
    def add_hello(name):
        return f"{prefix} {name} "
    return add_hello
add_hello = make_prefixer("Hello, ")
print(add_hello("Alice"))  # Вывод: Hello, Alice
print(add_hello("Bob"))    # Вывод: Hello, Bob



