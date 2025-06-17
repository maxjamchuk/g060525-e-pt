# Тема: Декораторы


# 1. Создайте декоратор validate, который проверяет, что все переданные функции аргументы являются положительными числами.
# Если нет, выводит сообщение об ошибке.
#
# Вывод: Ошибка: все аргументы должны быть положительными числами
def validate(func):
    def chek_nums(*args):
        if all(i >= 1 for i in args):
                print(f"Все чила из {func.__name__} являются положительными.")
                return func(*args)
        else:
                print(f"Ошибка: все аргументы из {func.__name__} должны быть положительными числами")
                return func(*args)
    return chek_nums
@validate
def num(a, b, c):
    return a, b, c
print(num(4, -2, 5))
print(num(1,2,5))

# 2. Создайте декоратор cache, который запоминает результаты выполнения функции для заданных аргументов и возвращает
# этот результат при повторном вызове декорируемой функции с теми же аргументами.


# # Вывод: 55
#
# Вывод: 55 (использует кеш)
def cache(func):
    saved_result= {}

    def wrapper(*args):
        if args in saved_result:
            print(f"{args}(использует кеш)")
            return saved_result[args]
        else:
            result=func(*args)
            saved_result[args]=result
            print(f"Результат {args} сохранен.")
            return result
    return wrapper

@cache
def sum_num(a, b, c):
    return a+b+c
print(sum_num(5, 7, 8 ))
print(sum_num(5, 7, 8 ))
print(sum_num(1, 55, 8 ))
print(sum_num(1, 55, 8 ))


