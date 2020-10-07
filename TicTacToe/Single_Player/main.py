import random
board = [' ' for x in range(10)]

def insertLetter(letter, positions):
    board[positions] = letter


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
        move = input("Your turn! Make your move(1 - 9): ")
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

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let

            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move


def selectRandom(li):
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

def isBoardFull(board):
    if board.count(' ') > 10:
        return True
    else:
        return False

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
            print("Sorry!You lost!")
            break

        if not isWinner(board, 'X'):
            move = compMove()
            if move == 0:
                print("Tie!")

            else:
                insertLetter('O', move)
                print("Computer played in postion ", move)
                printBoard(board)

        elif isWinner(board, 'X'):
            print("Congratulations!You won!")
            break

    if isBoardFull(board):
        print("Tie!")

main()