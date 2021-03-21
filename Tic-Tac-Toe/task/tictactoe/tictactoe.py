symbols = list(' ' * 9)


def is_winner(field, letter):
    return (
            field[0] == field[1] == field[2] == letter or
            field[3] == field[4] == field[5] == letter or
            field[6] == field[7] == field[8] == letter or
            field[0] == field[3] == field[6] == letter or
            field[1] == field[4] == field[7] == letter or
            field[2] == field[5] == field[8] == letter or
            field[0] == field[4] == field[8] == letter or
            field[2] == field[4] == field[6] == letter
    )


def show_grid():
    print('---------')
    i = 0
    for row in range(3):
        print("|", end='')
        for col in range(3):
            print(f" {symbols[i]}", end='')
            i = i + 1
        print(" |")
    print('---------')


show_grid()

turn = 'X'
while True:
    coordinates = input("Enter the coordinates: ").split()
    if len(coordinates) != 2 or not coordinates[0].isdigit() or not coordinates[1].isdigit():
        print("You should enter numbers!")
        continue
    if int(coordinates[0]) not in range(1, 4) or int(coordinates[1]) not in range(0, 4):
        print("Coordinates should be from 1 to 3!")
        continue
    spot = (int(coordinates[0]) - 1) * 3 + int(coordinates[1]) - 1
    if symbols[spot] != ' ':
        print("This cell is occupied! Choose another one!")
        continue

    symbols[spot] = turn
    show_grid()
    if is_winner(symbols, turn):
        print(turn, "wins")
        break
    if not bool(symbols.count(' ')):
        print("Draw")
        break

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'


# wrong_amounts = abs(symbols.count('X') - symbols.count('O')) > 1
# board_full = not bool(symbols.count(' '))
# x_wins = is_winner(symbols, 'X')
# o_wins = is_winner(symbols, 'O')
#
# if x_wins and o_wins or wrong_amounts:
#     print('Impossible')
# elif x_wins:
#     print('X wins')
# elif o_wins:
#     print('O wins')
# elif board_full and (not x_wins and not o_wins):
#     print('Draw')
# else:
#     print('Game not finished')
