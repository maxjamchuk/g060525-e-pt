# Тема: Дополнительная практика

# 1. Напишите функцию create_user, которая принимает параметры username, email
# и произвольное количество дополнительных данных с помощью **kwargs.
# Функция должна возвращать словарь с информацией о пользователе.
users = []
def create_user(username, email, **kwargs):
    user_data = {"username": username, "email": email, **kwargs}
    users.append(user_data)
create_user(username="david120", email="dvd12001@gmail.com", name="David", age=40, country="USA")
print(users)
# 2. Напишите функцию make_replacer, которая принимает два аргумента old и new. Внутри этой функции создайте
# и верните функцию replacer, которая заменяет все вхождения old на new в переданной ей строке.
# replace_a_with_o = make_replacer("a", "o")
# print(replace_a_with_o("banana"))  # Вывод: bonono
# print(replace_a_with_o("apple"))   # Вывод: opple
def make_replacer(old, new):
    def replacer(text):
        return text.replace(old, new)
    return replacer
replace_a_with_o = make_replacer("a", "o")
print(replace_a_with_o("banana"))
print(replace_a_with_o("apple"))

# 3. Напишите функцию make_suffixer, которая принимает строку suffix и возвращает внутреннюю функцию suffixer.
# Внутренняя функция должна добавлять suffix к любому переданному ей аргументу.
# add_exclamation = make_suffixer("!")
# print(add_exclamation("Hello"))  # Вывод: Hello!
# print(add_exclamation("Wow"))    # Вывод: Wow!
def make_suffixer(suffixer):
    def add_str(str):
        return f"{str}{suffixer}"
    return add_str
add_exclamation = make_suffixer("!")
print(add_exclamation("Hello"))  # Вывод: Hello!
print(add_exclamation("Wow"))    # Вывод: Wow!

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
            if case=="lower":
                return text.lower()
            elif case=="upper":
                return text.upper()
            elif case=="swap":
                return text.swapcase()
            else:
                return text
    return case_changer
to_upper = make_case_changer("upper")
print(to_upper("hello"))
to_lower = make_case_changer("lower")
print(to_lower("WORLD"))



# 5. Напишите функцию make_trimmer, которая принимает аргумент length. Внутри этой функции создайте и
# верните функцию trimmer, которая обрезает строку до заданной длины.
# trim_to_3 = make_trimmer(3)
# print(trim_to_3("Hello"))  # Вывод: Hel
# print(trim_to_3("World"))  # Вывод: Wor
def make_trimmer(length):
    def trimmer(text):
        new_text=text[:length]
        return new_text
    return trimmer
trim_to_3 = make_trimmer(3)
print(trim_to_3("Hello"))  # Вывод: Hel
print(trim_to_3("World"))  # Вывод: Wor