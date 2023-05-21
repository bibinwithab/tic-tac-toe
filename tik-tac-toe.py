#creating the board
board = [" " for i in range(9)]

#the winning combination
winning_combination = [
    (0,1,2), (3,4,5), (6,7,8),  #row
    (0,3,6), (1,4,7), (2,5,8),  #column
    (0,4,8), (6,4,2)            #diagonal
]

#printing the board
def print_board():
    print('-------------')
    for i in range(3):
        row = ' | '.join(board[i*3 : (i+1)*3])   #selects a single row
        print(f'| {row} |')
        print('-------------')

#checking the winner
def check_winner(player):
    for combo in winning_combination:
        if all(board[i] == player for i in combo ):     #checks each element in the board and checks with the winning combinations
            return True
    return False


#the game
def game():
    current_player = 'X'
    game_over = False

    while not game_over:
        print_board()

        print(f"Player {current_player}'s turn.")
        
        #getting a valid input
        valid_move = False
        while not valid_move:
            position = int(input("Enter your move (1-9): "))-1
            if position >= 0 and position < 9 and board[position] == ' ': 
                valid_move = True
                board[position] = current_player
            else:
                print('Invalid move bro!! Give another try')

        #when a player wins
        if check_winner(current_player):
            print_board()
            print(f"Player {current_player} won the game.")
            game_over = True
        
        #when the game is a tie
        elif ' ' not in board:
            print_board()
            print("Tie game.")
            game_over = True

        else:
            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'

#start the game
game()

char = input("Wanna continue? (y/n): ").lower()
if char == 'y':
    game()
else:
    print("Thanks for playing. See ya!")