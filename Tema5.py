def printing():
    print(' ')
    print('---------')
    print(f"| {values[0]} {values[1]} {values[2]} |")
    print(f"| {values[3]} {values[4]} {values[5]} |")
    print(f"| {values[6]} {values[7]} {values[8]} |")
    print('---------')


def user_input():
    global moves
    global values
    while True:
        input_ = input("Enter case: ")
        if not input_.isdigit():
            print("Enter digit")
            continue
        elif not 1 <= int(input_) <= 9:
            print("Not valid case")
            continue
        elif values[int(input_) - 1] != '_':
            print("Case already occupied")
        else:
            values[int(input_) - 1] = 'X'
            moves += 1
            break


def robot_input():
    global values
    global moves
    if values[4] == '_':
        values[4] = 'O'
    elif values[0] == "_":
        values[0] = "O"
    elif values[2] == "_":
        values[2] = "O"
    elif values[6] == "_":
        values[6] = "O"
    elif values[8] == "_":
        values[8] = "O"
    elif values[1] == "_":
        values[1] = "O"
    elif values[3] == "_":
        values[3] = "O"
    elif values[5] == "_":
        values[5] = "O"
    else:
        values[7] = "O"
    moves += 1


def winner():
    global values
    posibilities = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for posibility in posibilities:
        if values[posibility[0]] == values[posibility[1]] == values[posibility[2]] and values[posibility[0]] != '_':
            return True
        else:
            continue

values = ['_' for i in range(9)]
moves = 0
printing()
while True:
    user_input()
    printing()
    if winner():
        print(f'X wins')
        break
    if moves == 9:
        print('Draw')
        break
    robot_input()
    printing()
    if winner():
        print(f'O wins')
        break
    if moves == 9:
        print("Draw")
        break


