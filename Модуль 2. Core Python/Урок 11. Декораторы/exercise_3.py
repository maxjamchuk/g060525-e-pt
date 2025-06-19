# Дополнительная практика
#
#
# 1. Создайте декоратор to_upper, который преобразует строковый результат функции в верхний регистр.
#
# # Вывод: ПРИВЕТ, АЛИСА


# 2. Создайте декоратор limit_calls, который ограничивает количество вызовов функции заданным числом.
# Если функция вызывается больше разрешенного числа раз, выводите сообщение об ошибке.
#
# Вывод: Привет, Алиса!
# Вывод: Привет, Боб!
# Вывод: Привет, Чарли!
# Вывод: Ошибка: функция say_hello может быть вызвана не более 3 раз


def to_upper(func):
    def warapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            print("Dasfsav,nsabdfsbdafdj.b")
            return result.upper()
        else:
            return result
    return warapper

@to_upper
def greet(name):
    return f'Hello {name}!'


print(greet("вававава"))
greet('ваня')
greet('вася')
greet('лошара')


def limit_calls(max_calls):
    def decorator(func):
        count = 0
        def wrapper(*args, **kwargs):
            nonlocal count
            if count >= max_calls:
                print(f"Ошибка: Функция {func.__name__} Может быть вызвана не более {max_calls} раз(а).")
                return
            count += 1
            return func(*args, **kwargs)
        return wrapper
    return decorator

@limit_calls(5)
def foo():
    print("foo вызвана")

@limit_calls(3)
def bar():
    print("bar вызвана")


foo()
foo()
foo()
foo()
foo()
foo()
foo()
foo()



bar()
bar()
bar()
bar()
bar()
bar()