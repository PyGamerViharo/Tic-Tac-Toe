board = [' ' for x in range(10)]
Player1 = input("Player 1. Please enter your name: ")
Player2 = input("Player 2. Please enter your name: ")

def insertLetter(letter, pos):
    board[pos] = letter


def isSpaceFree(pos):
    return board[pos] == ' '

def showBoard(board):
    print("Here's a diagram of the board numbers: ")
    print("  1 | 2 | 3")
    print("-------------")
    print("  4 | 5 | 6")
    print("-------------")
    print("  7 | 8 | 9")
    print(" ")
    print(" ")

def printBoard(board):
    print('  ' + board[1] + ' |  ' + board[2] + ' |  ' + board[3])
    print("--------------")
    print('  ' + board[4] + ' |  ' + board[5] + ' |  ' + board[6])
    print("--------------")
    print('  ' + board[7] + ' |  ' + board[8] + ' |  ' + board[9])


def isWinner(board, le):
    return(board[7] == le and board[8] == le and board[9] == le) or (board[4] == le and board[5] == le and board[6] == le) or (board[1] == le and board[2] == le and board[3] == le) or (board[7] == le and board[4] == le and board[1] == le) or (board[8] == le and board[5] == le and board[2] == le) or (board[9] == le and board[6] == le and board[3] == le) or (board[1] == le and board[5] == le and board[9] == le) or (board[3] == le and board[5] == le and board[7] == le)

def playerMove():
    run = True
    while run:
        move = input(Player1 + "'s turn! Make your move(1 - 9): ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if isSpaceFree(move):
                    run = False
                    insertLetter('X', move)

                else:
                    print("This space is full! Please try again.")

            else:
                print("Please type a number within the range!")

        except:
            print("Please type a number!")

def player2Move():
    run = True
    while run:
        move = input(Player2 + "'s turn! Make your move(1 - 9): ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if isSpaceFree(move):
                    run = False
                    insertLetter('O', move)

                else:
                    print("This space is full! Please try again.")

            else:
                print("Please type a number within the range!")

        except:
            print("Please type a number!")

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    print("Welcome to Tic Tac Toe!")
    print("While making your move, please enter only integers.")

    while not isBoardFull(board):
        showBoard(board)
        printBoard(board)
        if not isWinner(board, 'O'):
            playerMove()
            printBoard(board)

        elif isWinner(board, 'O'):
            print("Congratulations! " + Player2 + " won!")
            break

        if not isWinner(board, 'X'):
            player2Move()
            printBoard(board)

        elif isWinner(board, 'X'):
            print("Congratulations! " + Player1 + " won!")
            break

    if isBoardFull(board):
            print("Tie!")

main()
