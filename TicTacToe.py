#1.Print out the board
from IPython.display import clear_output
def display_board(board):
    clear_output()
    
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])

#2.Assign markers X and O to players 1 and 2
def player_input():
    marker= ''
    
    while not (marker == 'X' and marker == "O"):
        marker = input('Player 1: Choose X or O: ').upper()
    
    if marker == 'X':
        return('X', 'O')
    else:
        return('O', 'X')


#3.Position the marker in the board
def place_marker(board, marker, position):
    board[position]=marker


#4.Check if the game has been won
def win_check(board, mark):
    return((board[7]==board[8]==board[9]==mark) or
    (board[4]==board[5]==board[6]==mark) or
    (board[1]==board[2]==board[3]==mark) or
    (board[7]==board[4]==board[1]==mark) or
    (board[8]==board[5]==board[2]==mark) or
    (board[9]==board[6]==board[3]==mark) or
    (board[1]==board[5]==board[9]==mark) or
    (board[7]==board[5]==board[3]==mark))


#5.Assign which player goes first
import random
def choose_first():
    if random.randint(0,1)==0:
        return 'Player 1'
    else:
        return 'Player 2'


#6.Check if there is still free space in the board
def space_check(board, position):
    return board[position]== ' '


#7.Check if the board is full
def full_board(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


#8.Ask the player's next position, check if it is free and place it
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position=int(input('Choose your next position(1-9)'))
    return position


#9.Check for game to continue
def replay():
    return input('Keep playing? Y or N').lower().startswith ('y')


#10.Run the game

print ('Welcome to Tic Tac Toe!')
#keep running the game
while True:
    ##set the game(board, players, markers)
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first!')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
        
    ##play game
    while game_on:
        if turn == 'Player1':
            ###show the board
            display_board(the_board)
            ###choose a position
            position = player_choice(the_board)
            ###place the marker in position
            place_marker(the_board, player1_marker, position)
            ###check if win
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 has won!')
                game_on = False
            ###check if tie
            else:
                if full_board(the_board):
                    display_board(the_board)
                    print ('Game tied!')
                    game_on = False
                    break
                else:
                    turn= "Player2"
        ##no win or tie, go to player 2
        else:
            ###show the board
                display_board(the_board)
            ###choose a position
                position = player_choice(the_board)
            ###place the marker in position
                place_marker(the_board, player2_marker, position)
            ###check if win
                if win_check(the_board, player2_marker):
                    display_board(the_board)
                    print('Player 2 has won!')
                    game_on = False
            ###check if tie
                else:
                    if full_board(the_board):
                        display_board(the_board)
                        print ('Game tied!')
                        break
                    else:
                        turn= "Player1"
#end the game
    if not replay():
        break