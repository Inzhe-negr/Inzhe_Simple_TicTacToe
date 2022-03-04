field = [[" ", " ", " "] for _ in range(3)]


def print_field():
    border = "---------"
    print(border)
    for row in field:
        print("|", " ".join(row), "|")
    print(border)


def get_next_coordinates():
    is_input_failed = True
    x_y = []
    while is_input_failed:
        x_y = input("Enter the coordinates: ").split(" ")
        if all((a.isnumeric() for a in x_y)):
            x_y = [int(a) - 1 for a in x_y]
        else:
            print("You should enter numbers!")
            continue
        if any((a < 0 or a > 2 for a in x_y)):
            print("Coordinates should be from 1 to 3!")
            continue
        if field[x_y[0]][x_y[1]] != " ":
            print("This cell is occupied! Choose another one!")
            continue
        else:
            is_input_failed = False
    return x_y


def make_move(char):
    x, y = get_next_coordinates()
    field[x][y] = char
    print_field()


def win_list():
    wins = [row[0] for row in field if row[0] == row[1] == row[2]]
    for i in range(3):
        if field[0][i] == field[1][i] == field[2][i]:
            wins.append(field[0][i])
    if field[0][0] == field[1][1] == field[2][2]:
        wins.append(field[0][0])
    if field[2][0] == field[1][1] == field[0][2]:
        wins.append(field[2][0])
    return [winner for winner in wins if winner in ["X", "O"]]


def is_full_field():
    filled_count = len([item for row in field for item in row if item != " "])
    return filled_count == 9


def is_game_over():
    is_over = False
    winners = win_list()
    if len(winners) == 1:
        print(winners[0], "wins")
        is_over = True
    elif is_full_field():
        print("Draw")
        is_over = True
    return is_over


def play_game():
    player = "X"
    while not is_game_over():
        make_move(player)
        if player == "X":
            player = "O"
        else:
            player = "X"


print_field()
play_game()
