# Тема: Декораторы
#
# Продемонстрируйте создание и использование декораторов на примерах.
# Объясните механизм работы декоратора, передачу аргументов.
#
# Например, напишите декоратор timeit, который замеряет и выводит время выполнения декорируемой функции.
# В качестве декорируемых функций используйте две функции, одна из которых генерит четные числа от 0 до 10 000
# через цикл for и метод append. А другая генерит эти же цифры через генератор списков.
import time


def time_off(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Function {func.__name__} executed in {end - start:.4f} seconds')
        return result
    return wrapper

def logit(func):
    def wrapper(*args, **kwargs):
        print(f'Calling function {func.__name__} with arguments {args} and keyword arguments {kwargs}')
        result = func(*args, **kwargs)
        print(f'Function {func.__name__} returned {result}')
        return result
    return wrapper

@time_off
def even_numbers():
    even_numbers = []
    for i in range(10_000_000):
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers

@time_off
def ogg_numbers():
    return [i for i in range(10_000_000) if i % 2 != 0]



def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@logit
@time_off
@repeat(30)
def say_hello(name):
    print(f'Hello, {name}')

say_hello('Alex')
