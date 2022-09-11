#Copy your code from Complete the Game or Tic Tac Toe with Random NPC
#Then copy your completed minimax from Getting the Row Col Values

#2.5.4
# Global Variables
board = [["-","-","-"],["-","-","-"],["-","-","-"]]
player = 'X'

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

def print_board():
    print("\n")
    print("\t0\t\t1\t\t2")
    count = 0
    for item in board:
        row = ""
        for space in item:
            row += "\t" + space + "\t"
        print(count,row + "\n")
        count+= 1

def minimax(player):
    # copy your basecase here:
    optimalRow = -1
    optimalCol = -1
    if check_win("O"):
        #print("Will result in O win")
        return (10, None, None)
    elif check_win("X"):
        #print("Will result in O loss")
        return (-10, None, None)
    elif check_tie():
        #print("Will result in tie")
        return (0, None, None)

    # implement recursive case
    if player == "O":
        best = -1000
        for row in range(3):
            for col in range(3):
                if board[row][col] == "-":
                    # print("Place 0 at " + str(row) + "," + str(col))
                    place_player("O", row, col)
                    # print_board()
                    temp = best
                    best = max(best, minimax("X")[0])
                    if temp != best:
                        optimalRow = row
                        optimalCol = col
                    place_player("-", row, col)
                    # print("O: Return to original board.")
                    # print_board()
        return (best, optimalRow, optimalCol)
    if player == "X":
        worst = 1000
        for row in range(3):
            for col in range(3):
                if board[row][col] == "-":
                    # print("Place X at " + str(row) + "," + str(col))
                    place_player("X", row, col)
                    # print_board()
                    temp = worst
                    worst = min(worst, minimax("O")[0])
                    if temp != worst:
                        optimalRow = row
                        optimalCol = col
                    place_player("-", row, col)
                    # print("X: Return to original board.")
                    # print_board()
        return (worst, optimalRow, optimalCol)


##Don't edit this code
# It checks to see if your minimax function is working correctly
def print_board():
    print("\n")
    print("\t0\t\t1\t\t2")
    count = 0
    for item in board:
        row = ""
        for space in item:
            row += "\t" + space + "\t"
        print(count,row + "\n")
        count+= 1



#updated version
def take_turn(player):
        if player == 'X':
            while True:
                print(player + "'s Turn")
                row = int(input('Enter a row: '))
                col = int(input('Enter a column: '))

                if not is_valid_move(row, col):
                    print("Please enter a valid move")
                    continue

                else:
                    place_player(player, row, col)
                    print_board()
                    #print("break from this")
                    print()
                    break

        elif player == 'O':
            print("NPC Doing Its Thing...")
            mini = minimax('O')
            score, row, col = mini[0], mini[1], mini[2]
            place_player(player, row, col)
            print("NPC playing player at Row: "+ str(row)+ " and Col: "+str(col))
            print_board()
            print()

'''----------------------------'''
'''-------Game Start-----------'''
print("Start Tic Tac Toe Game")
print()
while True:
    if not check_tie():
        take_turn(player)
        if check_win(player) == True:
            print(player + " wins!")
            break
        else:
            player = swap_turn(player)
    else:
        print("It's a Tie")
        break
