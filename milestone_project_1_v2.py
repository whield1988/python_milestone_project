"""
1. Display a board
2. User can input 1-9
3. Check if the user input is taken, else, ask for another number
4. Add the mark to the board
5. Check if the user wins or tie, else, next player's turn
6. Play again?
"""

board = [" "]*10
current_player = "player_1"
player_1_mark, player_2_mark = ("O","X")

def display_board(board):
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-----")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-----")
    print(board[7] + "|" + board[8] + "|" + board[9])

def ask_player_1_input():
    position = int(input("Please choose a number from 1-9: "))
    board[position] = "X"

def ask_player_2_input():
    position = int(input("Please choose a number from 1-9: "))
    board[position] = "O"

def check_win():
    if board[1] == board[2] == board[3] == player_1_mark or board[1] == board[2] == board[3] == player_2_mark:
        return True
    if board[4] == board[5] == board[6] == player_1_mark or board[4] == board[5] == board[6] == player_2_mark:
        return True
    if board[7] == board[8] == board[9] == player_1_mark or board[7] == board[8] == board[9] == player_2_mark:
        return True
    if board[1] == board[4] == board[7] == player_1_mark or board[1] == board[4] == board[7] == player_2_mark:
        return True
    if board[2] == board[5] == board[8] == player_1_mark or board[2] == board[5] == board[8] == player_2_mark:
        return True
    if board[3] == board[6] == board[9] == player_1_mark or board[3] == board[6] == board[9] == player_2_mark:
        return True
    if board[1] == board[5] == board[9] == player_1_mark or board[1] == board[5] == board[9] == player_2_mark:
        return True
    if board[3] == board[5] == board[7] == player_1_mark or board[3] == board[5] == board[7] == player_2_mark:
        return True
    else:
        return False

def replay():
    if input("Type 'YES' to play again or 'NO' to quit: ") == 'YES':
        game_on = True
    else:
        game_on = False

def play_game():

    current_player = 'player_1'

    play_game = input('Enter "YES" to play or "NO" to quit: ')
    if play_game.upper() == 'YES':
        game_on = True

        while game_on:

            display_board(board)

            if current_player == 'player_1':
                ask_player_1_input()
                if check_win() == True:
                    print(current_player+" wins!")
                    break
                else:
                    current_player = 'player_2'

            elif current_player == 'player_2':
                ask_player_2_input()
                if check_win() == True:
                    print(current_player + " wins!")
                    break
                else:
                    current_player = 'player_1'

    elif play_game.lower() == 'no':
        print("Thanks for stopping by!")

play_game()