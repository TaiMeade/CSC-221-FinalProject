"""

Tai Meade
CSC 221
Tic Tac Toe game

"""


def main():
    # Create the board...realized after making this that I could have formatted it in many other ways, but it works.
    board = ['\t','\t|','\t','\t|','\t','\t','\n','\t','\t|','\t','\t|','\t','\t','\n','\t','1','\t|','\t','2','\t|','\t','3','\t','\n','\t','\t|','\t','\t|','\t','\t','\n','\t','\t|','\t','\t|','\t','\t','\n','-------------------------------------------------','\n','\t','\t|','\t','\t|','\t','\t','\n','\t','\t|','\t','\t|','\t','\t','\n','\t','4','\t|','\t','5','\t|','\t','6','\t','\n','\t','\t|','\t','\t|','\t','\t','\n','\t','\t|','\t','\t|','\t','\t','\n','-------------------------------------------------','\n','\t','\t|','\t','\t|','\t','\t','\n','\t','\t|','\t','\t|','\t','\t','\n','\t','7','\t|','\t','8','\t|','\t','9','\t','\n','\t','\t|','\t','\t|','\t','\t','\n','\t','\t|','\t','\t|','\t','\t','\n',]

    # Find indexes of my variable to replace rather than counting them...print(board.index('-',99))
    positionOptions = [15,18,21,55,58,61,95,98,101]
    positionsAlreadyPlayed = []
    playerOne = 'X'
    playerTwo = 'O'
    turnNum = 1
    gameEnd = False

    print(f"{playerOne}'s always go first!")
    while gameEnd != True:
        # Win conditions for X's
        if ((board[positionOptions[0]] == 'X' and board[positionOptions[1]] == 'X' and board[positionOptions[2]]) == 'X') or ((board[positionOptions[0]] == 'X' and board[positionOptions[3]] == 'X' and board[positionOptions[6]]) == 'X') or ((board[positionOptions[0]] == 'X' and board[positionOptions[4]] == 'X' and board[positionOptions[8]]) == 'X') or ((board[positionOptions[1]] == 'X' and board[positionOptions[4]] == 'X' and board[positionOptions[7]]) == 'X') or ((board[positionOptions[2]] == 'X' and board[positionOptions[5]] == 'X' and board[positionOptions[8]]) == 'X') or ((board[positionOptions[2]] == 'X' and board[positionOptions[4]] == 'X' and board[positionOptions[6]]) == 'X') or ((board[positionOptions[3]] == 'X' and board[positionOptions[4]] == 'X' and board[positionOptions[5]]) == 'X') or ((board[positionOptions[0]] == 'X' and board[positionOptions[1]] == 'X' and board[positionOptions[2]]) == 'X'):
            winner = playerOne
            gameEnd = True
            print("".join(board))
            print(f"The winner is {winner}'s!\n")
        
        # Win conditions for O's
        elif ((board[positionOptions[0]] == 'O' and board[positionOptions[1]] == 'O' and board[positionOptions[2]]) == 'O') or ((board[positionOptions[0]] == 'O' and board[positionOptions[3]] == 'O' and board[positionOptions[6]]) == 'O') or ((board[positionOptions[0]] == 'O' and board[positionOptions[4]] == 'O' and board[positionOptions[8]]) == 'O') or ((board[positionOptions[1]] == 'O' and board[positionOptions[4]] == 'O' and board[positionOptions[7]]) == 'O') or ((board[positionOptions[2]] == 'O' and board[positionOptions[5]] == 'O' and board[positionOptions[8]]) == 'O') or ((board[positionOptions[2]] == 'O' and board[positionOptions[4]] == 'O' and board[positionOptions[6]]) == 'O') or ((board[positionOptions[3]] == 'O' and board[positionOptions[4]] == 'O' and board[positionOptions[5]]) == 'O') or ((board[positionOptions[0]] == 'O' and board[positionOptions[1]] == 'O' and board[positionOptions[2]]) == 'O'):
            winner = playerTwo
            gameEnd = True
            print("".join(board))
            print(f"The winner is {winner}'s!\n")

        # Checks if board has been filled by X's/O's
        elif board[positionOptions[0]] == '1' or board[positionOptions[1]] == '2' or board[positionOptions[2]] == '3' or board[positionOptions[3]] == '4' or board[positionOptions[4]] == '5' or board[positionOptions[5]] == '6' or board[positionOptions[6]] == '7' or board[positionOptions[7]] == '8' or board[positionOptions[8]] == '9':
            print("".join(board))
            if (turnNum % 2) == 1:
                whosTurn = playerOne
                decision = int(input(f"{whosTurn}'s select your position (1-9): "))
                while (decision < 1 or decision > 9) or decision in positionsAlreadyPlayed:
                    decision = int(input(f"{whosTurn}'s select your position (1-9): "))
                if decision not in positionsAlreadyPlayed:
                    positionsAlreadyPlayed.append(decision)
                decision -= 1
                board[positionOptions[decision]] = whosTurn
                turnNum += 1

            else:
                whosTurn = playerTwo
                decision = int(input(f"{whosTurn}'s select your position (1-9): "))
                while (decision < 1 and decision > 9) or decision in positionsAlreadyPlayed:
                    decision = int(input(f"{whosTurn}'s select your position (1-9): "))
                if decision not in positionsAlreadyPlayed:
                    positionsAlreadyPlayed.append(decision)
                decision -= 1
                board[positionOptions[decision]] = whosTurn
                turnNum += 1
        else:
            print("".join(board))
            print("It's a draw!\n")
            break

if __name__ == '__main__':
    
    main()