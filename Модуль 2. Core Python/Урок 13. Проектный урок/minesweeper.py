import random
import os

SIZE = 5
MINES = 5

def clear_console():
    #os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" * 50)

def generate_board():
    # Генератор поля игры
    board = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    mine_positions = set()
    while len(mine_positions) < MINES:
        r = random.randint(0, SIZE - 1)
        c = random.randint(0, SIZE - 1)
        mine_positions.add((r, c))
        #Тут мы назначаем случайные координаты минам

    for r, c in mine_positions:
        board[r][c] = '*'
        for i in range(r - 1, r + 2):
            for j in range(c - 1, c + 2):
                if 0 <= i < SIZE and 0 <= j < SIZE and board[i][j] != '*':
                    board[i][j] += 1
                    # тут я делаю инкремент полям для счетчика окружения по умолчанию пустые поля имеют 0
    return board, mine_positions

def print_board(visible):
    # функция отрисовки игового поля с наложением маски открытых полей.
    for row in visible:
        print(" ".join(str(cell) if cell is not None else '-' for cell in row))

def reveal(board, visible, r, c, visited):
    #функция ходов вскрытие пустых клеток которые 0
    if (r, c) in visited or not (0 <= r < SIZE and 0 <= c < SIZE):
        return 0
    visited.add((r, c))
    if visible[r][c] is not None:
        return 0

    visible[r][c] = board[r][c]
    count = 1
    if board[r][c] == 0:
        for i in range(r - 1, r + 2):
            for j in range(c - 1, c + 2):
                count += reveal(board, visible, i, j, visited)
    return count


def play_game():
    #тело игры
    board, mines = generate_board()
    #Создаем игровое поле.
    visible = [[None for _ in range(SIZE)] for _ in range(SIZE)]
    opened = 0
    total_safe = SIZE * SIZE - MINES
    # и базовые игровые параметры.

    print("Добро пожаловать в Сапёра!")
    # Старт
    while True:
        clear_console()
        print_board(visible)
        try:
            # отрисовка поля для начала и трай что бы небыло ошибок
            move = input("Введите координаты клетки (строка столбец): ")
            if move.lower() == 'pressxtowin':
                clear_console()
                final_view = [[board[i][j] for j in range(SIZE)] for i in range(SIZE)]
                print_board(final_view)
                print("(👍≖‿‿≖)👍 Читер победил! Карта открыта полностью. Поздравляем! 👍(≖‿‿≖👍)")
                return
            elif move.lower() in ("q", "quit", "exit"):
                print("Возврат в меню Game Hub...")
                return
            r, c = map(int, move.strip().split())
            r -= 1
            c -= 1
            # разделение строки отброска пробелов Приведение к индексу
            if not (0 <= r < SIZE and 0 <= c < SIZE):
                print("Координаты вне диапазона.")
                continue
            #Проверка диапазона реализована тут
            if visible[r][c] is not None:
                print("Клетка уже открыта.")
                continue
            #Проверка фальшхода
            if board[r][c] == '*':
                clear_console()
                final_view = [[board[i][j] for j in range(SIZE)] for i in range(SIZE)]
                print_board(final_view)
                print("Вы проиграли! Вы попали на мину.")
                break
            # Ход c Открытием пустых клеток

            visited = set()
            newly_opened = reveal(board, visible, r, c, visited)
            opened += newly_opened

            if opened == total_safe:
                print_board([[board[i][j] if board[i][j] != '*' else '-' for j in range(SIZE)] for i in range(SIZE)])
                print("Поздравляем! Вы открыли все безопасные клетки.")
                break
        except ValueError:
            print("Введите два числа через пробел.")

if __name__ == "__main__":
    print("Игра запущена автономно. Разрабочик Pankov Kyrylo http://pankov.it")
    play_game()