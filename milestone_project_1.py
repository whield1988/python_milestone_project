import random


# Display the board
def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("-----")
    print(board[4] + '|' + board[5] + '|' + board[6])
    print("-----")
    print(board[1] + '|' + board[2] + '|' + board[3])


# Let player choose to be X or O
def player_input():
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input("Please choose your marker, X or O: ").upper()

    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')


# Mark the board with the position chose
def place_marker(board, marker, position):
    board[position] = marker


# Check if the player wins
def win_check(board, mark):
    return ((board[1] == board[2] == board[3] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark) or
            (board[1] == board[4] == board[7] == mark) or
            (board[2] == board[5] == board[8] == mark) or
            (board[3] == board[6] == board[9] == mark) or
            (board[1] == board[5] == board[9] == mark) or
            (board[3] == board[5] == board[7] == mark))


# Random pick a player to start
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


# Check if the board has a space
def space_check(board, position):
    return board[position] == ' '


# Check if the board is full
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


# Let player choose a number from 1-9

def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position

# Replay game
def replay():
    return input('Do you want to play again? Y/N: ')


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    newBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(newBoard)
            position = player_choice(newBoard)
            place_marker(newBoard, player1_marker, position)

            if win_check(newBoard, player1_marker):
                display_board(newBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(newBoard):
                    display_board(newBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            display_board(newBoard)
            position = player_choice(newBoard)
            place_marker(newBoard, player2_marker, position)

            if win_check(newBoard, player2_marker):
                display_board(newBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(newBoard):
                    display_board(newBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
