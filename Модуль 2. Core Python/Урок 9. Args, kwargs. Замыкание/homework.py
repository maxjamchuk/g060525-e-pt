# Тема: Упаковка аргументов с помощью *args, **kwargs и распаковка через * и **

# 1. Напишите функцию sum_all, которая принимает произвольное количество числовых аргументов
# с помощью *args и возвращает их сумму.
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))
print(sum_all(5, 10, 15, 20))


# 2. Напишите функцию combine_lists, которая принимает несколько списков в качестве аргументов с помощью *args
# и возвращает один объединённый список.
def combine_lists(*args):
    combined_list = []
    for lst in args:
        combined_list.extend(lst)
    return combined_list

print(combine_lists([1, 2, 3], [4, 5], [6, 7, 8], [6, 7, 8], [6, 7, 8], [6, 7, 8], [6, 7, 8], [6, 7, 8]))  # Вывод: [1, 2, 3, 4, 5, 6, 7, 8]


# 3. Напишите функцию print_details, которая принимает два аргумента name и age.
# Затем создайте словарь с ключами name и age, распакуйте его и передайте в функцию print_details.
def print_details(name, age):
    print(f"hello, {name}! You {age}.")

dict = {'name': 'Ana', 'age' : 25}
print_details(**dict)

# 4. Напишите функцию filter_numbers, которая принимает произвольное количество числовых аргументов с помощью *args
# и возвращает список только тех чисел, которые больше 10.
def filter_numbers(*args):
    numbers = []
    for el in args:
        if el > 10:
            numbers.append(el)
    return numbers
    # return [num for num in args if num > 10]

print(filter_numbers(5, 12, 3, 15, 8, 20))  # Вывод: [12, 15, 20]

# Тема: Глобальные и локальные переменные. Вложенные функции и замыкания.

# 1. Напишите функцию increment_global, которая увеличивает значение глобальной переменной counter на 1 каждый раз,
# когда она вызывается.
# increment_global()
# print(counter)  # Вывод: 1
# increment_global()
# print(counter)  # Вывод: 2
def increment_global():
    global counter
    counter += 1
    return

increment_global()
print(counter)


# 2. Напишите функцию outer, которая содержит внутреннюю функцию inner. Внутренняя функция должна увеличивать
# значение переменной count, объявленной во внешней функции, на 1 каждый раз при её вызове.
# counter = outer()
# print(counter())  # Вывод: 1
# print(counter())  # Вывод: 2
def outer():
    count = 0
    def inner():
        nonlocal count
        return count
    return inner
counter = outer()
print(counter)
print(counter)
print(counter)


# 3. Напишите функцию make_multiplier, которая принимает аргумент factor. Внутри этой функции создайте и
# верните функцию multiplier, которая умножает свой аргумент на factor.
# mult_by_2 = make_multiplier(2)
# print(mult_by_2(5))  # Вывод: 10
# mult_by_3 = make_multiplier(3)
# print(mult_by_3(5))  # Вывод: 15
def make_multiplier(factor):
    def multiplier(number):
        return number * factor
    return multiplier
mul = make_multiplier(2)
print(mul(5))

mul = make_multiplier(3)
print(mul(5))


# 4. Напишите функцию make_prefixer, которая принимает строку prefix и возвращает внутреннюю функцию prefixer.
# Внутренняя функция должна добавлять prefix к любому переданному ей аргументу.
# add_hello = make_prefixer("Hello, ")
# print(add_hello("Alice"))  # Вывод: Hello, Alice
# print(add_hello("Bob"))    # Вывод: Hello, Bob
def make_prefixer(prefix):
    def prefixer(word):
        return word + prefix
    return prefixer

add_hello = make_prefixer("Hello, ")
print(add_hello("Alice"))
print(add_hello("Bob"))


# Тема: Дополнительная практика

# 1. Напишите функцию create_user, которая принимает параметры username, email
# и произвольное количество дополнительных данных с помощью **kwargs.
# Функция должна возвращать словарь с информацией о пользователе.
def create_user(username, email, **kwargs):
   user = {"unsername" : username, "email" : email}
   user.update(kwargs)
   return user
user_data = create_user("Valentyna", "valya@example.com")
print(user_data)


# 2. Напишите функцию make_replacer, которая принимает два аргумента old и new. Внутри этой функции создайте
# и верните функцию replacer, которая заменяет все вхождения old на new в переданной ей строке.
# replace_a_with_o = make_replacer("a", "o")
# print(replace_a_with_o("banana"))  # Вывод: bonono
# print(replace_a_with_o("apple"))   # Вывод: opple
def make_replacer(old, new):
   def replacer(text):
       return text.replacer(old, new)
   return replacer
a_with = make_replacer("a", "b")
print(a_with("banana"))
print(a_with("apple"))



# 3. Напишите функцию make_suffixer, которая принимает строку suffix и возвращает внутреннюю функцию suffixer.
# Внутренняя функция должна добавлять suffix к любому переданному ей аргументу.
# add_exclamation = make_suffixer("!")
# print(add_exclamation("Hello"))  # Вывод: Hello!
# print(add_exclamation("Wow"))    # Вывод: Wow!
def make_suffixer(suffix):
   def suffixer(word):
       return word + suffix
   return suffixer

add_exclamation = make_suffixer("!")
print(add_exclamation("Hello"))
print(add_exclamation("Wow"))

# 4. Напишите функцию make_case_changer, которая принимает аргумент case (значения могут быть "upper" или "lower").
# Внутри этой функции создайте и верните функцию case_changer, которая изменяет регистр строки в зависимости от
# переданного аргумента (если передан аргумент с заглавными буквами, то делаете их строчными, если со строчными,
# то делает их заглавными).
# to_upper = make_case_changer("upper")
# print(to_upper("hello"))  # Вывод: HELLO
# to_lower = make_case_changer("lower")
# print(to_lower("WORLD"))  # Вывод: world
def make_case_changer(case):
   def case_changer(text):
       if case == "oben":
           return  text.upper()
       elif case == "unter":
           return text.lower()
       else:
           return text
   return case_changer
to_upper = make_case_changer("oben")
print(to_upper("hello"))
to_lower = make_case_changer(("unter"))
print(to_lower("WORLD"))

# 5. Напишите функцию make_trimmer, которая принимает аргумент length. Внутри этой функции создайте и
# верните функцию trimmer, которая обрезает строку до заданной длины.
# trim_to_3 = make_trimmer(3)
# print(trim_to_3("Hello"))  # Вывод: Hel
# print(trim_to_3("World"))  # Вывод: Wordef count_characters(string):
def make_trimmer(length):
    def trimmer(text):
        return text[: length]
    return trimmer
to_trim = make_trimmer(3)
print(to_trim("Hallo"))
print(to_trim("Welt"))

