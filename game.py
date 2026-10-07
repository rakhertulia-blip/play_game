from types import new_class
def read_choice(prompt, allowed):
    while True:
        choice = input(prompt).strip()
        if choice in allowed:
            return choice
        print("Неверный ввод. Попробуйте ещё раз.")


def can_move(position, step):
    if step not in [1, 2, -1]:
        return False

    new_position = position + step

    if new_position < 1 or new_position > 10:
        return False

    return True


def move_player(position, step):
    if can_move(position, step):
        return position + step

    return position


def show_position(position):
    print("Текущая клетка:", position)
    print("Цель: 8")


def show_rules():
    print("\n--- Правила игры ---")
    print("Вы начинаете с клетки 1.")
    print("Цель — попасть ровно на клетку 8.")
    print("Можно сделать ход: +1, +2 или -1.")
    print("На игру даётся максимум 5 ходов.")
    print("Выйти за пределы клеток 1-10 нельзя.")


def play_game():
    position = 1
    moves = 0

    print("\n--- Поиск сокровища ---")
    print("Вы нашли дорожку к сокровищу!")

    while moves < 5:
        show_position(position)

        if position == 8:
            print("Поздравляем! Вы нашли сокровище!")
            return

        step = read_choice(
            "Введите ход (+1, +2 или -1): ",
            ["1", "2", "-1"]
        )


        step = int(step)

        if not can_move(position, step):
            print("Такой ход невозможен. Ход не расходуется.")
            continue

        position = move_player(position, step)
        moves += 1

        print("Ход выполнен.")

        if position == 8:
            show_position(position)
            print("Поздравляем! Вы нашли сокровище!")
            return

    print("Ходы закончились.")
    print("Вы не нашли сокровище.")


def main():
    while True:
        print("\n=== ПОИСК СОКРОВИЩА ===")
        print("1 - Начать")
        print("2 - Правила")
        print("0 - Выход")

        choice = read_choice("Выберите пункт: ", ["0", "1", "2"])

        if choice == "1":
            play_game()
        elif choice == "2":
            show_rules()
        elif choice == "0":
            print("Игра завершена.")
            break


main()
