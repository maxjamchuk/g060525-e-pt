# Дополнительная практика
authenticated = False


# 1. Создайте декоратор requires_auth, который проверяет наличие определенного флага authenticated и выполняет
# функцию только если этот флаг установлен в True.
#



# Вывод: Доступ запрещен: пользователь не аутентифицирован

# Вывод: Секретная информация


# 2. Создайте декоратор call_counter, который отслеживает количество вызовов декорируемой функции и
# выводит это количество при каждом вызове.
#
#
# # Вывод:
# # Функция greet вызвана 1 раз(а)
# # Привет, Алиса!
#
# # Вывод:
# # Функция greet вызвана 2 раз(а)
# # Привет, Боб!

def requires_auth(func):
    def wrapper(*args, **kwargs):
        if not authenticated:
            print("Доступ запрещен")
            return
        return func(*args, **kwargs)
    return wrapper

def call_counter(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Функция {func.__name__} вызвана {count} раз(ф)")
        return func(*args, **kwargs)
    return wrapper




@requires_auth
@call_counter
def greet(name):
    print('Hello {}'.format(name))
    print('ВНИМАНИЕ СЕКРЕТНАЯ ИНФОРМАЦИЯ!\n\n')
    print("Берём урановой руды кусок,\nПодкладываем в реактор впрок,\nТуда нейтронов горсть бросай —\nЧтоб критичность шла через край.\n\nПотом магнитов пару штук,\nИ сверхпроводник — не забудь, друг.\nОбмотай всё в оболочку,\nДобавь таймер — и готова бомболочка!")
    print('КОНЕЦ СЕКРЕТНОЙ ИНФОРМАЦИИ!\n\n\n\n\n\n\n\n\n')

greet('John')
greet('Bob')
greet('Алиса')
authenticated = True
greet('Валентина')
greet('Владимир')
greet('Кирилл')
authenticated = False
greet('Преподаватель Александр')
authenticated = True
greet('Зоряна')
greet('Марина')
greet('и другие...')
