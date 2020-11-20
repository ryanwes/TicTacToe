# Format of board and Function to print Tic Tac Toe
def print_tic_tac_toe(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")
 
 
# Function to print the score-board
def print_scoreboard(score_board):

    print("\t    | SCOREBOARD | ")
 
    players = list(score_board.keys())
    print("\t   ", players[0], "\t    ", score_board[players[0]])
    print("\t   ", players[1], "\t    ", score_board[players[1]])
 
# Function to check if any player has won
def check_win(position, user):
 
    # Checking for win (3 in a row vertical, horizonal, diagonal)
    list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
 
    # Loop check for winner
    for x in list:
        if all(y in position[user] for y in x):
 
            # Return True if win
            return True
    # Return False if winner isn't established       
    return False       
 
# Function to check if the game is tie
def check_tie(position):
    #Counting markers
    if len(position['X']) + len(position['O']) == 9:
        return True
    return False       
 
# Function for a single game of Tic Tac Toe
def single_game(user):
 
    
    values = [' ' for x in range(9)]
     
    # Stores the positions occupied by X and O
    position = {'X':[], 'O':[]}
     
    # Loop for a single game of Tic Tac Toe
    while True:
        print_tic_tac_toe(values)
         
        # Verifies moves
        try:
            print("Choose position between 1-9")
            print("Player ", user, " turn. Which box? : ", end="")
            move = int(input()) 
        except ValueError:
            print("Wrong Input!!! Try Again")
            continue
 
        #Validate move is 1-9
        if move < 1 or move > 9:
            print("Wrong Input!!! Try Again")
            continue
 
        # Validate spot isn't taken
        if values[move-1] != ' ':
            print("Place already filled. Try again!!")
            continue
 
        # Updating grid status 
        values[move-1] = user
 
        # Updating player positions
        position[user].append(move)
 
        # Function call for checking win
        if check_win(position, user):
            print_tic_tac_toe(values)
            print("Player ", user, " has won the game!!")     
            print("\n")
            return user
 
        # Function call for checking tie game
        if check_tie(position):
            print_tic_tac_toe(values)
            print("Tie Game")
            print("\n")
            return 'T'
            
 
        # Flipping player 
        if user == 'X':
            user = 'O'
        else:
            user = 'X'
 
if __name__ == "__main__":
    
    print("Play TicTacToe!!")
    print("Player 1")
    player1 = input("What is your name? : ")
    print("\n")
 
    print("Player 2")
    player2 = input("What is your name? : ")
    print("\n")
     
    # Stores the player who chooses X and O
    user = player1
 
    # Saves which marker each player has
    player_marker = {'X' : "", 'O' : ""}
 
    
    options = ['X', 'O']
 
    # Stores the scoreboard
    score_board = {player1: 0, player2: 0}
    print_scoreboard(score_board)
 
    # Game Loop for a series of Tic Tac Toe
    # The loop runs until the players quit 
    while True:
 
        # Player Menu - Listed here and below to draw user attention
        print("""
            ****Layout for Game****
            1 | 2 | 3
            4 | 5 | 6
            7 | 8 | 9
         """)
        print("Turn to choose for", user)
        print("Enter 1 to be X")
        print("Enter 2 to be O")
        print("Enter 3 to Exit Game")
        print("""
            ****Layout for Game****
            1 | 2 | 3
            4 | 5 | 6
            7 | 8 | 9
         """)
 
        # Function for marker
        try:
            marker = int(input())   
        except ValueError:
            print("Unacceptable Input")
            continue
 
        # statements for player marker  
        if marker == 1:
            player_marker['X'] = user
            if user == player1:
                player_marker['O'] = player2
            else:
                player_marker['O'] = player1
 
        elif marker == 2:
            player_marker['O'] = user
            if user == player1:
                player_marker['X'] = player2
            else:
                player_marker['X'] = player1
         
        elif marker == 3:
            print("Final Scores")
            print_scoreboard(score_board)
            break  
 
        else:
            print("Wrong Choice!!!! Try Again\n")
 
        # Saves winner of game
        winner = single_game(options[marker-1])
         
        # Upadates after Each win - Won't record ties
        if winner != 'T' :
            player_won = player_marker[winner]
            score_board[player_won] = score_board[player_won] + 1
 
        print_scoreboard(score_board)
        # Switch player who chooses X or O
        if user == player1:
            user = player2
        else:
            user = player1