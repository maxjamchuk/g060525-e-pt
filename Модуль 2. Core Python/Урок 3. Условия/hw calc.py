def calculator():
    while True:
        print("\nВведіть два числа :")
        num1_str = input("Перше число: ")
        num2_str = input("Друге число:")
        a = float(num1_str)
        b = float(num2_str)

        print("операція: + - * / %")
        op = input("Оберіть операцію: ")
        if op == "+":
            print("Результат:", a + b)
        elif op == "-":
            print("Результат:", a - b)
        elif op == "%":
            #:)
            print("Результат:", a * (b / 100))
        elif op == "*":
            print("Результат:", a * b)
        elif op == "/":
            if b != 0:
                print("Результат:", a / b)


            else:
                print("Помилка: ділення на нуль!")
        else:
            print("Нерівна операція")


calculator()





