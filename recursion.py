#2.5.4
# Global Variables
board = []
# player = "X"

# Functions
# copy and paste your print_board function definition here!
def print_board():
    #print("\tWelcome to Tic Tac Toe!")
    print()
    print()
    print("\t" + "0" + "\t" + "1" + "\t" + "2")
    for i in range(len(board)):
        print(i, end='')  # print on same line
        for col in board[i]:
            print("\t" + col, end='')
        print()


# returns true if a row,col on the board is open
def is_valid_move(row, col):
    empty = '-'
    if row > 2 or col > 2:
        return False
    elif board[row][col] == empty:
        return True


# places player on row,col on the board
def place_player(player, row, col):
    board[row][col] = player


def swap_turn(player):
    # return 'Xif player == 'O' else 'O'
    if player == 'O':
        return 'X'
    else:
        return 'O'


def take_turn():
    while True:
        print(player + "'s Turn")
        row = int(input('Enter a row: '))
        col = int(input('Enter a column: '))
        '''if row > 2 or col > 2:
            print("Please enter a valid move")
            continue'''
        if not is_valid_move(row, col):
            print("Please enter a valid move")
            continue
        else:
            place_player(player, row, col)
            print_board()
            print()
            break


# Write your check win functions here:
def checkRows(player):
    for row in board:
        if len(set(row)) == 1:
            if list(row)[0] != '-':
                if list(row)[0] == player:
                    return True
    return False


def checkColumns(player):
    # increment and add into the list
    column_list = []
    for i in range(len(board)):
        column_list *= 0
        # print("column"+str(i))
        for w in range(len(board)):
            column_list.append(board[w][i])
        # print(colum_list)
        if len(set(column_list)) == 1:
            if list(set(column_list))[0] != '-':
                if list(set(column_list))[0] == player:
                    return True
    return False


def checkDiagonals(player):
    diag_list = []
    for i in range(len(board)):
        diag_list.append(board[i][i])
    if len(set(diag_list)) == 1:
        if list(set(diag_list))[0] != '-':
            if list(set(diag_list))[0] == player:
                return True
    diag_list *= 0
    for i in range(len(board)):
        diag_list.append(board[i][len(board) - 1 - i])
    if len(set(diag_list)) == 1:
        if list(set(diag_list))[0] != '-':
            if list(set(diag_list))[0] == player:
                return True
    return False


# check_win
def check_win(player):
    if checkRows(player):
        return True
    elif checkColumns(player):
        return True
    elif checkDiagonals(player):
        return True
    return False


# check tie
def check_tie():
    for i in range(len(board)):
        for w in range(len(board)):
            if board[i][w] == '-':
                return False
    return True


def minimax(player):
    # copy your basecase here:
    if check_win("O"):
        print("Will result in O win")
        return 10
    elif check_win("X"):
        print("Will result in O loss")
        return -10
    elif check_tie():
        print("Will result in tie")
        return 0
    # implement recursive case
    if player == "O":
        best = -1000
        for row in range(3):
            for col in range(3):
                if board[row][col] == "-":
                    print("Place 0 at " + str(row) + "," + str(col))
                    place_player("O", row, col)
                    print_board()
                    best = max(best, minimax("X"))
                    place_player("-", row, col)
                    print("O: Return to original board.")
                    print_board()
        return best
    if player == "X":
        worst = 1000
        for row in range(3):
            for col in range(3):
                if board[row][col] == "-":
                    print("Place X at " + str(row) + "," + str(col))
                    place_player("X", row, col)
                    print_board()
                    worst = min(worst, minimax("O"))
                    place_player("-", row, col)
                    print("X: Return to original board.")
                    print_board()
        return worst


#O wins
print("---------------------------------------")
board.append(["O", "X", "O"])
board.append(["-", "O", "X"])
board.append(["X", "X", "-"])
print("Calling minimax('O') on this board:")
print_board()
print("Minimax should return 10:", minimax("O"))
board.clear()

#tie I think
board.append(["O", "X", "O"])
board.append(["-", "X", "X"])
board.append(["X", "O", "-"])
print("Calling minimax('O') on this board:")
print_board()
print("Minimax should return 0:", minimax("O"))
board.clear()

#X win
board.append(["O", "X", "-"])
board.append(["-", "X", "X"])
board.append(["X", "O", "O"])
print("Calling minimax('O') on this board:")
print_board()
print("Minimax should return -10:", minimax("O"))

