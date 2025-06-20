def multiply(a, b):
    return a * b
def substract(a, b):
    return a - b
def divide(a, b):
    if b != 0:
        return a // b
    else:
        return "Ошибка: Деление на ноль."

if __name__ == "__main__":
    print("Модуль запущен напрямую")