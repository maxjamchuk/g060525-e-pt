def viktorina():
    print("Добро пожаловать в Викторину! Ответьте на 5 вопросов.\n")

    score = 0

while True:
    print("1. Столиця Франції?")
    print("1. Лондон\n2. Берлін\n3. Париж")
   #answer = input("Ваш вибір(чи q для виходу): ").lower()
    if answer == "q":
        print("Вихід з вікторини")
        break
    try:
        answer = input(answer)
        if answer == 3:
        print("Правильно!\n")
        score += 1
    else:
        print("Неправильно. Правильна відповідь: 3. Париж\n")


    print("2. Столиця Німеччини?")
    print("1. Лондон\n2. Берлін\n3. Венеція")
    answer = int(input("Ваш вибір: "))
    if answer == 2:
        print("Правильно!\n")
        score += 1
    else:
        print("Неправильно. Правильна відповідь: 2. Берлін\n")


    print("3. Столиця США?")
    print("1. Нью-Йорк\n2. Лос-Анджелес\n3. Вашингтон")
    answer = int(input("Ваш вибір: "))
    if answer == 3:
        print("Правильно!\n")
        score += 1
    else:
        print("Неправильно. Правильна відповідь: 3. Вашингтон\n")


    print("4. Столиця Греції?")
    print("1. Афіни\n2. Стамбул\n3. Київ")
    answer = input("Ваш вибір: ")
    if answer == "1":
        print("Правильно!\n")
        score += 1
    else:
        print("Неправильно. Правильна відповідь: 1. Афіни\n")


    print("5. Столиця Норвегії?")
    print("1. Осло\n2. Порту\n3. Мюнхен")
    answer = input("Ваш вибір: ")
    if answer == "1":
        print("Правильно!\n")
        score += 1
    else:
        print("Неправильно. Правильна відповідь: 1. Осло\n")

    print(f"Гра закінчена! Ви правильно відповіли на {score} з 5 питань.")


viktorina()