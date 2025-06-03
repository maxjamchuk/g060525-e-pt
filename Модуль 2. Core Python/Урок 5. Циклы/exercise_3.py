# Проект: Управление библиотекой
#
# Описание:
# Разработайте программу для управления библиотекой. Программа должна позволять добавлять книги в библиотеку,
# удалять книги, искать книги по автору и выводить список всех книг с их авторами и статусами (в наличии или выдана).
#
# Требования: Реализуйте работу всех пунктов меню.

library = [
    ["Война и мир", "Толстой", "В наличии"],
    ["Преступление и наказание", "Достоевский", "Выдана"],
    ["Мастер и Маргарита", "Булгаков", "В наличии"],
    ["Python для чайников", "Какой то крутой челик", "В наличии"],
    ["Как пояснить Валентине Python", "Александр", "Выдана"]
        ]

actions=[
    [1, "Показать список всех книг"],
    [2, "Добавить книгу"],
    [3, "Удалить книгу"],
    [4, "Поменять статус книги"],
    [5, "Показаить книги определенного автора"],
    [6, "Показать книги с определенным статусом"],
]


while True:
    print("\nМеню")
    for action in actions[0:]:
        print(f"{action[0]}. {action[1]}")
    print("0. Выход!")

    choice = input("Выберите действие, введя его номер: ")

    # Продолжите программу ниже.
    if choice == "0":
        print("Выход из программы.")
        break

    elif choice == "1":
        print("список ВСЕХ книг: ")
        for book in library:
            print(f"Название:{book[0]}, Автор: {book[1]}, Статус: {book[2]}")

    elif choice == "2":
        title = input("введите название книги: ").strip()
        title.lower()
        title.title()
        author= input("ВВедите автора Книги: ").strip()
        author.lower()
        author.title()
        status = "В наличии"
        library.append([title, author, status])
        print(f"Добавлена книга: {title}, {author}")
    elif choice == "3":
        print("список ВСЕХ книг: ")
        for idx, book in enumerate(library):
            print(f"{idx}. Название:{book[0]}, Автор: {book[1]}, Статус: {book[2]}")
        delete=int(input("Введите индекс книги для удаления"))
        if 0 <= delete <= len(library):
            removed = library.pop(delete)
            #library.remove(delete)
            print(f"Книга: {removed[0]}, Была удалена.")
    elif choice == "4":
        print("список ВСЕХ книг: ")
        for idx, book in enumerate(library):
            print(f"{idx}. Название:{book[0]}, Автор: {book[1]}, Статус: {book[2]}")
        change=int(input("Введите индекс книги для изменения статуса: "))
        if 0 <= change <= len(library):
            if library[change][2]=='В наличии':
                library[change][2]="Выдана"
            else:
                library[change][2] = 'В наличии'
    elif choice == "5":
        author = input("Введите имя автора: ").strip().lower()
        author.title()
        found= False
        print(f"\nКниги за авторством {author.title()}")
        for book in library:
            if book[1] == author.title:
                print(f"{book[0]}, {book[2]}")
                found = True
        if not found:
            print("Книг этого автора не найдено.")
    elif choice == "6":
        status = input("Введите статус книги 0 - Выдана, 1 - В наличии.")
        if status == 1:
            status = "В наличии"
        else:
            status = "Выдана"
        found = False
        print(f"\nКниги со статусом ' {status} ' ")
        for book in library:
            if book[2] == status:
                print(f"{book[0]}, {book[1]}")
                found = True
        if not found:
            print("Книг с таким статусом нет.")
    else:
        print(f"вы ввели {choice} но такого действия нет поэтому ДИнахуй!")