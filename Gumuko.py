N, M = 15, 15
a_row = 5
n_players = 2
marks = ['X', 'O']
grid = [['-']*M for _ in range(N)]

#This function prints the grid of Gomoku as the game progresses
def print_grid():
    for i in range(n_players):
        print('Player %d: %c  ' % (i+1, marks[i]), end='')
        if i < n_players-1:
            print('vs  ', end='')
    print()
    print('--' + '---' * M + '--')
    for i in range(N):
        print(end='|  ')
        for j in range(M):
            print(grid[i][j], end='  ')
        print(end='|')
        print()
        print('--' + '---' * M + '--')

#This function checks if the game has a win state or not
def check_win(mark):
    for i in range(M-4):     #check_rows
      for j in range(N):
        if grid[j][i] == grid[j][i+1] == grid[j][i+2] == grid[j][i+3] == grid[j][i+4] == mark:
          return True
    
    for i in range(M):         
      for j in range(N-4):
        if grid[j][i] == grid[j+1][i] == grid[j+2][i] == grid[j+3][i] == grid[j+4][i] == mark:
          return True
    
    for i in range(M-4):      #check_dagonals
      for j in range(N-4):
        if grid[j][i] == grid[j+1][i+1] == grid[j+2][i+2] == grid[j+3][i+3] == grid[j+4][i+4]== mark:
          return True
    
    for i in range (4,M):
      for j in range(N-4):
        if grid[j][i] == grid[j+1][i-1] == grid[j+2][i-2]==grid[j+3][i-3] == grid[j+4][i-4] == mark:
          return True
    return False

#This function checks if the game has a tie state or not for the given mark
def check_tie_player(mark):
    flag1,flag2,flag3,flag4 = True,True,True,True
    for i in range(M-4):     #check_rows
      for j in range(N):
        if (grid[j][i] == mark or grid[j][i] == '-') and (grid[j][i+1] == mark or grid[j][i+1] == '-') and (grid[j][i+2] == mark or grid[j][i+2] == '-') and( grid[j][i+3] == mark or grid[j][i+3]== '-')and (grid[j][i+4] == mark or grid[j][i+4] == '-'):
          flag1 = False
    
    for i in range(M):         #check_columns
      for j in range(N-4):
        if (grid[j][i] == mark or grid[j][i] == '-') and(grid[j+1][i] == mark or grid[j+1][i] == '-')and (grid[j+2][i] == mark or grid[j+2][i] == '-') and (grid[j+3][i] == mark or grid[j+3][i] =='-') and(grid[j+4][i] == mark or grid[j+4][i] == '-'):
          flag2 = False
    
    for i in range(M-4):      #check_dagonals
      for j in range(N-4):
        if (grid[j][i] == mark or grid[j][i] == '-') and (grid[j+1][i+1] == mark or grid[j+1][i+1] == '-') and (grid[j+2][i+2] == mark or grid[j+2][i+2] == '-')and (grid[j+3][i+3] == mark or grid[j+3][i+3] == '-') and (grid[j+4][i+4]== mark or grid[j+4][i+4] == '-'):
          flag3 = False
    
    for i in range (4,M):
      for j in range(N-4):
        if (grid[j][i] == mark or grid[j][i] == '-') and (grid[j+1][i-1] == mark or grid[j+1][i-1] == '-') and (grid[j+2][i-2]== mark or grid[j+2][i-2] == '-') and (grid[j+3][i-3] == mark or grid[j+3][i-3] == '-') and (grid[j+4][i-4] == mark or grid[j+4][i-4] == '-'):
          flag4 = False
    
    if(flag1 and flag2 and flag3 and flag4):
      return True
    return False  

#This function checks if the game has a tie state or not
def check_tie():
    all_tie = True
    for mark in marks:
        if not check_tie_player(mark):
            all_tie = False
    return all_tie
	
#This function checks if given cell is empty or not 
def check_empty(i, j):
    if grid[i][j] == '-':
      return True
    return False  

#This function checks if given position is valid or not 
def check_valid_position(i, j):
    if i <= 14 and i >= 0 and j <=14 and j >=0:
      return True
    return False  

#This function sets the given mark to the given cell
def set_cell(i, j, mark):
    grid[i][j] = mark

#This function clears the game structures
def grid_clear():
    for i in range(N):
      for j in range(N):
        grid[i][j] = '-'

#This function reads a valid position input
def read_input():
    i, j = map(int, input('Enter the row index and column index: ').split())
    while not check_valid_position(i, j) or not check_empty(i, j):
        i, j = map(int, input('Enter a valid row index and a valid column index: ').split())
    return i, j


#MAIN FUNCTION
def play_game():
    print("Gomoku Game!")
    print("Welcome...")
    print("============================")
    player = 0
    while True:
        #Prints the grid
        print_grid()
        #Read an input position from the player
        print('Player %s is playing now' % marks[player])
        i, j = read_input()
        #Set the player mark in the input position
        set_cell(i, j, marks[player])
        #Check if the grid has a win state
        if check_win(marks[player]):
            #Prints the grid
            print_grid()
            #Announcement of the final statement
            print('Congrats, Player %s is won!' % marks[player])
            break
        #Check if the grid has a tie state
        if check_tie():
            #Prints the grid
            print_grid()
            #Announcement of the final statement
            print("Woah! That's a tie!")
            break		
        #Player number changes after each turn
        player = (player + 1) % n_players


while True:
	grid_clear()
	play_game()
	c = input('Play Again [Y/N] ')
	if c not in 'yY':
		break
