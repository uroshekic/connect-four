class ConnectFour:
    def __init__(self, columns = 7, rows = 6, player1 = 'X', player2 = 'O'):
        self.size = {'c' : columns, 'r': rows} # 7 columns x 6 rows
        self.grid = []
        self.first_player = True # True - player 1 on the move, False - player 2 on the move
        self.players = {True : player1, False : player2} # Anything except ? (question mark) AND 1 character only!
        self.game_over = False
        self.grid = [[] for i in range(self.size['c'])]

    # Returns True if disc was successfully dropped, False otherwise
    def drop(self, column): # Drop a disc into a column
        if self.game_over: return False # Cannot proceed because game has already ended.
        
        if column < 0 or column >= self.size['c']:
            return False
        if len(self.grid[column]) >= self.size['r']:
            return False

        self.grid[column].append(self.players[self.first_player])

        c = self.check()
        if c == False:
            self.first_player = not self.first_player
            return True
        else:
            self.game_over = c
            return True

        
    # Returns False - meaning game is on OR 'win'/'draw' meaning game is over.
    def check(self): # Check whether player has won or forced draw.
        d = 0 # Number of discs
        for i, column in enumerate(self.grid):
            d += len(self.grid[i])
            for j, row in enumerate(column):
                h = i + 4 <= self.size['c'] # Nismo v eni izmed zadnjih štirih stolpcev
                v = j + 4 <= len(self.grid[i]) # V tem stolpcu obstajajo vsaj štiri vrstice
                
                if v: # Check vertically (four fields to the right)
                    if 1 == len(set(self.grid[i][j:j+4])):
                        return 'win'
                    
                if h: # Check horizontally (four fields up)
                    if len(self.grid[i]) > j and len(self.grid[i+1]) > j and len(self.grid[i+2]) > j and len(self.grid[i+3]) > j: 
                        s_r = set()
                        for k in range(4):
                            s_r.add(self.grid[i+k][j])
                        if 1 == len(s_r):
                            return 'win'
                            
                if h: # Check diagonally (up-right)
                    s = set()
                    for k in range(4):
                        if len(self.grid[i+k]) > j + k:
                            s.add(self.grid[i+k][j+k])
                        else:
                            s.add('??')
                    if 1 == len(s):
                        return 'win'
                    
                if h and j - 4 + 1 >= 0: # Check diagonally (down-right)
                # j - 4 + 1 > 0 : Začne se naj komaj v 4. stolpcu (ki ima indeks 3)
                    s = set()
                    for k in range(4):
                        if len(self.grid[i+k]) > j - k:
                            s.add(self.grid[i+k][j-k])
                        else:
                            s.add('??')
                    if 1 == len(s):
                        return 'win'

        if d == self.size['c']*self.size['r']:
            return 'draw'
        
        return False
    

class ConnectFour_Text(ConnectFour):        
    def current(self):
        print(self.players[self.first_player])
        
    def drop(self, column):
        parent_drop = super(ConnectFour_Text, self).drop(column)
        print(self)
        if self.game_over != False:
            print('Game has ended.')
        return
        
    def __print__(self):
        s = ' ' + ''.join([str(i + 1) + ' ' for i in range(self.size['c'])]) + '\n'
        for r1 in range(self.size['r']):
            r = self.size['r'] - r1 - 1
            s += '|'
            for c in range(self.size['c']):
                if len(self.grid[c]) > r:
                    s += self.grid[c][r]
                else:
                    s += ' '
                s += '|'
            s += '\n'
        s += '+' + (2*self.size['c'] - 1)*'-' + '+\n'
        if self.game_over == 'win':
            s += 'Player ' + self.players[self.first_player] + ' WON!'
        elif self.game_over == 'draw':
            s += 'DRAW!'
        else:
            s += 'Turn: ' + self.players[self.first_player]
        return s

    def __repr__(self): return self.__print__();

    def play(self):
        print('HOW TO PLAY:\nSelect a number of column (1-'  + str(self.size['c']) + ') and pass the keyboard to your opponent.\n')
        print(self)
        valid_columns = list(map(str, range(1, self.size['c'] + 1)))
        while self.game_over == False:
            c = input('Select a column: ')
            print()
            if c in valid_columns:
                self.drop(int(c) - 1)
        print('I hope you enjoyed it!')


ConnectFour = ConnectFour_Text()
ConnectFour.play()

# Test cases
##g = ConnectFour_Text()
''' Draw
for i in range(6): g.drop(0)
for i in range(6): g.drop(1)
for i in range(6): g.drop(6)
for i in range(5): g.drop(5)
for i in range(6): g.drop(2)
for i in range(6): g.drop(3)
for i in range(6): g.drop(4)
g.drop(5)
#'''

''' Player 1 wins vertically
for i in range(3): g.drop(1); g.drop(2);
g.drop(1)
#'''

''' Player 2 wins horizontally
for i in range(3): g.drop(1+i); g.drop(1+i);
g.drop(5)
g.drop(4)
g.drop(5)
g.drop(4)
#'''

''' Player 1 wins diagonally (up-right)
g.drop(0)
g.drop(1); g.drop(1)
g.drop(2); g.drop(3); g.drop(2); g.drop(2)
g.drop(3); g.drop(4); g.drop(3); g.drop(3)
#'''

''' Player 1 wins diagonally (up-right) #2
g.drop(0); g.drop(1); g.drop(2); g.drop(3); g.drop(4); g.drop(5);
g.drop(0); g.drop(1); g.drop(2); g.drop(3); g.drop(4); g.drop(5);
g.drop(2+0)
g.drop(2+1); g.drop(2+1)
g.drop(2+2); g.drop(2+3); g.drop(2+2); g.drop(2+2)
g.drop(2+3); g.drop(2+4); g.drop(2+3); g.drop(2+3)
#'''

''' Player 1 wins diagonally (down-right)
g.drop(0); g.drop(0); g.drop(3); g.drop(0); g.drop(0);
g.drop(6);
g.drop(1); g.drop(1); g.drop(1); g.drop(2); g.drop(2)
#'''
