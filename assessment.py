import os

# A little googling yielded this to clear interpereter window:
def cls():
    os.system('cls' if os.name=='nt' else 'clear')





# The game consists of tiles changing values.
class tile:
    def __init__(self):
        self.state = ' '
        
    def set_state(self,player):
        if player == 1:
            self.state = 'X'
        elif player == 2:
            self.state = 'O'




# Those tiles are collected in a 3x3 board, which I want to visualize.
class board:
    def __init__(self):
        self.tiles = [[tile(), tile(), tile()],
                      [tile(), tile(), tile()],
                      [tile(), tile(), tile()]]
        
    def give_board(self):
        output_string=''
        for ii in [0, 1, 2]:
            for jj in [0, 1, 2]:
                output_string+=' '+self.tiles[ii][jj].state+' '
                if jj<2:
                    output_string+='|'
            output_string+='\n'
            if ii<2:
                output_string+='---+---+---\n'
        print(output_string)




 
# Each game has a board, a turn, players, and win conditions.
# Each game needs to report its game-state, check for win conditions,
# and play turns.           
class game:
    def __init__(self):
        self.board = board()
        self.turn = 1
        self.player = 1
        self.draw = False
        self.winner = 0
    
    def give_gamestate(self):
        cls()
        print('Press [Ctrl][C] to exit at any time.\n')
        self.board.give_board()
        if self.draw == False and self.winner == 0:
            print('Turn:\t\t',self.turn)
            print('Player on turn:\t',self.player)
        elif self.winner != 0:
            print('Winner is player ',self.winner)
        elif self.draw == True:
            print('Game is a draw!')
    
    def check_draw(self):
        if self.turn == 9:
            return True
        else:
            return False
            
    def play_turn(self):
        print('\nTo claim a tile, enter a column number, i.e. 1, 2 or 3.')
        column = int(input())
        print('To claim a tile, enter a row number, i.e. 1, 2 or 3.')
        row = int(input())
        if (column > 0 and column < 4 and row > 0 and row < 4):
            ii = row-1
            jj = column-1
            if self.board.tiles[ii][jj].state==' ':
                self.board.tiles[ii][jj].set_state(self.player)
                self.winner = self.check_win()
                self.draw = self.check_draw()
                if self.player == 1:
                    self.player = 2
                elif self.player == 2:
                    self.player = 1
                self.turn+=1
                return True
            else:
                print('That tile is already claimed. Choose another.')
                return False
        else:
            print('That tile does not exist.')
            return False
    
    def check_win(self):
        win = False
        # Check rows
        for row in [0,1,2]:
            if (self.board.tiles[row][0].state != ' ' and
                self.board.tiles[row][0].state == 
                self.board.tiles[row][1].state and
                self.board.tiles[row][0].state == 
                self.board.tiles[row][2].state):
                win = True
        # Check columns
        if win == False:
            for col in [0,1,2]:
                if (self.board.tiles[0][col].state != ' ' and
                    self.board.tiles[0][col].state == 
                    self.board.tiles[1][col].state and
                    self.board.tiles[0][col].state == 
                    self.board.tiles[2][col].state):
                    win = True
        # Check diagonals
        if win == False:
            if (self.board.tiles[1][1].state != ' ' and
                self.board.tiles[0][0].state == 
                self.board.tiles[1][1].state and
                self.board.tiles[2][2].state == 
                self.board.tiles[1][1].state):
                    win = True
            elif (self.board.tiles[1][1].state != ' ' and
                self.board.tiles[0][2].state == 
                self.board.tiles[1][1].state and
                self.board.tiles[2][0].state == 
                self.board.tiles[1][1].state):
                    win = True
        if win == True:
            return self.player
        else:
            return 0






# Now, our user needs to be able to start a game, so dialogue!
print("Hello, welcome to Glenn's tic-tac-toe, v1a!")
print("Would you like to start a game?")
print("Type 'y' and press [Enter] to confirm.")
print("or press [Ctrl][C] to exit.")
reply = input("Start a game? ")

# Start a game:
while reply == 'y':
    current_game=game()
    # So long as the started game has not been won...
    while (current_game.draw == False and
           current_game.winner == 0):
        # ... we want to see the board ...
        current_game.give_gamestate()
        # ... play a turn ...
        turn_done = False
        while turn_done == False:
            turn_done = current_game.play_turn()
    # ... and we want to see the final board when a winning turn occurs.
    current_game.give_gamestate()
    
    # Re-initialize a game?
    print("Do you want to play another game?")
    print("Type 'y' and hit [enter] if you do!")
    reply=input("Start a new game? ")
    
# Goodbye dialogue
print("Goodbye!")
print("Press [Ctrl][C] to exit.")