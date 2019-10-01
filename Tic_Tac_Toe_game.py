board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

game_still_going = True
current_player = "X"
winner = None


def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2]  +      "      1|2|3")
    print(board[3] + "|" + board[4] + "|" + board[5]  +      "      4|5|6")
    print(board[6] + "|" + board[7] + "|" + board[8]  +      "      7|8|9")



def play_game():
    display_board()

    while game_still_going:
        # turn handler
        handle_turn(current_player)
        # check the game if ended
        check_if_game_over()
        # flip the other player
        flip_player()
        # the game has ended

        if winner == "X" or winner == "0":
            print(winner + " won")
        elif winner == None:
            print("")
    # display the initial board: first
    handle_turn(current_player)


def handle_turn(current_player):
    print(current_player + " turn")
    position = input("enter the position from 1- 9:  ")
    valid = False
    while not valid:
        while position not in ['1', '2','3', '4', '5', '6', '7', '8', '9' ]:
            position = input("Enter the position from 1 - 9:  ")
        position = int(position) - 1
        # the decrement part is the part of the loop and the if statement is the part of the main while loop which had the valid and the booloan things

        if board[position] == "-":
            valid = True
        else :
            print('You cannot place there')


    board[position] = current_player

    display_board()


def check_if_win():
    global winner
    row_winner = check_rows()

    column_winner = check_columns()

    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
        print("")
    elif column_winner:
        winner = column_winner
        print("")
    elif diagonal_winner:
        winner = diagonal_winner
        print("")
    else:
        winner = None
        print('tie')

    return


# check row columns and check diagonals
def check_rows():
    #check if any of the rows are not empty
    global game_still_going
    # if all three are equal and not equal to a - instead of an X
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going = False
        # RETURN THE WINNER X OR O
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    return


def check_columns():
    global game_still_going
    # if all three are equal and not equal to a - instead of an X
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_still_going = False
        # RETURN THE WINNER X OR O
    if column_1:
        return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2]
    return


def check_diagonals():
    global game_still_going
    # if all three are equal and not equal to a - instead of an X
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[7] != "-"

    if diagonal_1 or diagonal_2:
        game_still_going = False
        # RETURN THE WINNER X OR O
    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[1]

    return


def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False

    return


def check_if_game_over():
    return


def check_if_game_over():
    check_if_win()
    check_if_tie()


def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player =="O":
        current_player = "X"
    return


def game_still_going():
    return


play_game()
