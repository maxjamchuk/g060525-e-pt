# Проект: Управление библиотекой
#
# Описание:
# Разработайте программу для управления библиотекой. Программа должна позволять добавлять книги в библиотеку,
# удалять книги, искать книги по автору и выводить список всех книг с их авторами и статусами (в наличии или выдана).
#
# Требования: Реализуйте работу всех пунктов меню.

library = [[1, ["Война и мир", "Толстой", "в наличии"]],
           [2, ["Преступление и наказание", "Достоевский", "выдана"]],
           [3, ["Мастер и Маргарита", "Булгаков", "в наличии"]]]
menu=[
    [1, "Показать список всех книг"],
    [2, "Добавить книгу"],
    [3, "Удалить книгу"],
    [4, "Поменять статус книги"],
    [5, "Показать книги определенного автора"],
    [6, "Показать книги с определенным статусом"],[0, "Выход"]
]
while True:
    print(f"\nМеню: {menu} ")
    choice=int(input("\nВведите число для выбора функции: "))
    if choice == 1:
        print(library)
    elif choice == 2:
        title = input("Название: ")
        author = input("Автор: ")
        status = input("Статус книги(выдана/в наличии): ")
        new_index=max(book[0] for book in library) +1 if library else 1
        library.append([new_index, [title, author, status]])
        print(f"Книга {title} добавлена")

    elif choice == 3:
        del_book=input("Введите название книги которую хотите удалить ")
        for book in library:
            if book[1][0].lower() == del_book.lower():
                library.remove(book)
                print(f"Книга {del_book} удалена")
                break
        else:
            print("Книга не найдена")

    elif choice == 4:
        change_title=input("Введите название книги для смены статуса")
        for book in library:
            if book[1][0].lower() == change_title.lower():
                book[1][2] = "выдана" if book[1][2]== "в наличии" else "в наличии"
                print("Статус обновлен")
                break
        else:
            print("Книга не найдена")

    elif choice == 5:
        found_book = input("Введите автора книги ")
        for book in library:
            if book[1][1].lower() == found_book.lower():
                print(f"Книги по автору {found_book}: ", book)
                break

    elif choice == 6:
        find_status = input("Введите статус книги ")
        for book in library:
            if book[1][2].lower()  == find_status.lower():
                print(f"Книги со статусом {book[1][2]}: ", book)

    elif choice == 0:
        print("Выход из программы.")
        break














    # print("1. Показать список всех книг")
    # print("2. Добавить книгу")
    # print("3. Удалить книгу")
    # print("4. Поменять статус книги")
    # print("5. Показать книги определенного автора")
    # print("6. Показать книги с определенным статусом")
    # choice = input("Выберите действие, введя его номер: ")

    # Продолжите программу ниже.