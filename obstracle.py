import random
# class Obstacle:
#     def __init__(self, left, top, board):
#         self.left = left
#         self.top = top
class Coins:
    def __init__(self, left, top, board):
        self.__left = left
        self.__top = top
        # super().__init__(left, top, board)
        
    
    def create_coins(self, left, top, board):
        number = random.randrange(1,10)
        for i in range(number):
            # board.grid[top][left+i] = '$'
            # board.grid[top+1][left+i] = '$'
            board.set_grid(left+i, top, '$')
            board.set_grid(left+i, top+1, '$')
    
    def put_coins(self, board):
        for i in range(0, 820, 200):
            
            x = random.randint(13, 30) ##height
            y = random.randint(5, 150)  ##width
            self.create_coins(y+i, x, board)
    
    def remove_coin(self, left, top, board):
        board.set_grid(left, top, ' ')
    
    
class Fire_Beams:
    def __init__(self, left, top, board):
        self.__left = left
        self.__top = top
    def create_horizontal_beams(self, left, top, board):
        for i in range(6):
            board.set_grid(left + i, top, '*')
    def create_vertical_beams(self, left,top, board):                              
        for i in range(6):                                    
            board.set_grid(left, top+i,'*')                             
    def create_slanting_beams(self, left, top, board):                                                
        for i in range(6):                                        
            # board.grid[top+5-i] [left + i] = '*'
            board.set_grid(left+i, top+5-i, '*')

    def put_beams(self,board):
        # for i in range(0, 1200, 75):
        #     self.create_horizontal_beams(0 + i, 12, board)
        #     self.create_vertical_beams(89 + i, 24, board)
        #     self.create_slanting_beams(47+ i, 34, board)
       
        self.create_horizontal_beams(60, 8, board)
        self.create_vertical_beams(120, 24, board)
        self.create_slanting_beams(182, 12, board)
        self.create_horizontal_beams(240, 8, board)
        self.create_vertical_beams(300, 22, board)
        self.create_slanting_beams(360, 11, board)
        self.create_horizontal_beams(420, 8, board)
        self.create_vertical_beams(480, 24, board)
        self.create_slanting_beams(540, 12, board)
        self.create_horizontal_beams(600, 8, board)
        self.create_vertical_beams(660, 24, board)
        self.create_slanting_beams(720, 12, board)
        self.create_horizontal_beams(780, 8, board)
        self.create_vertical_beams(840, 24, board)
        # self.create_slanting_beams(900, 12, board)
        # self.create_horizontal_beams(960, 8, board)
        # self.create_vertical_beams(1120, 24, board)
        # self.create_slanting_beams(1180, 12, board)
        # self.create_horizontal_beams(1240, 8, board)
        # self.create_vertical_beams(1300, 24, board)
       
        # self.create_horizontal_beams(780, 8, board)
        # self.create_vertical_beams(810, 24, board)
        # self.create_slanting_beams(840, 12, board)
        # self.create_horizontal_beams(870, 8, board)
        # self.create_vertical_beams(900, 24, board)
        # self.create_slanting_beams(930, 12, board)
        # self.create_horizontal_beams(810, 8, board)
        # self.create_vertical_beams(840, 24, board)
        # self.create_slanting_beams(870, 12, board)
        # self.create_horizontal_beams(900, 8, board)
        # self.create_vertical_beams(930, 24, board)
        # self.create_slanting_beams(960, 12, board)
        # self.create_horizontal_beams(990, 8, board)
        # self.create_vertical_beams(1020, 24, board)
        # self.create_slanting_beams(1080, 12, board)
        # self.create_horizontal_beams(1120, 8, board)
        # self.create_vertical_beams(1160, 24, board)
        # self.create_slanting_beams(1200, 12, board)
        # self.create_horizontal_beams(1250, 8, board)
        # self.create_vertical_beams(1280, 24, board)
        # self.create_slanting_beams(1310, 12, board)
                    

    def remove_beam(self, left, board):
        for  i in range(50):
            for j in range(left - 20, left + 20):
                # if board.grid[i][j] == '*':
                #     board.grid[i][j] = ' '
                grid = board.get_grid()
                if grid[i][j] == '*':
                    board.set_grid(j, i, ' ')
                    
    def remove_beam_only_right(self, left, board):
        for i in range(50):
            for j in range(left - 30, left + 30):
                # if board.grid[i][j] == '*':
                #     board.grid[i][j] =' '
                grid = board.get_grid()
                if grid[i][j] == '*':
                    board.set_grid(j, i, ' ')
            
class Power_booster:
    def __init__(self,x,y,board):
        self.__x = x
        self.__y = y
    
    def create_power_booster(self, board):
        
        # board.grid[20][12] = '@'
        # board.grid[23][100]='@'
        # board.grid[26][162]='@'
        # board.grid[12][202]='@'
        # board.grid[4][302]='@'
        # board.grid[30][402]='@'
        # board.grid[25][503]='@'    
        # board.grid[26][543]='@'
        # board.grid[27][637]='@'
        # board.grid[13][739]='@'
        # board.grid[10][803]='@'
        # board.grid[31][920]='@'
        # board.grid[29][1001]='@'
        # board.grid[38][1207]='@'
        # board.grid[29][1302]='@'
        board.set_grid(12, 20, '@')
        board.set_grid(100, 23, '@')
        board.set_grid(162, 26, '@')
        board.set_grid(202, 12, '@')
        board.set_grid(302, 4, '@')
        board.set_grid(402, 30, '@')
        board.set_grid(503, 25, '@')
        board.set_grid(543, 26, '@')
        board.set_grid(637, 27, '@')
        board.set_grid(739, 13, '@')
        board.set_grid(803, 10, '@')
        # board.set_grid(920, 31, '@')
        # board.set_grid(1001, 29, '@')
        # board.set_grid(1207, 38, '@')
        # board.set_grid(1302, 29, '@')
      
        
        
        

class Magnet:                                 ### The object will start attracting in range +-40

    def __init__(self, left, top, board):
        self.__left = left
        self.__top = top
    
    def create_magnet(self, left, top, board):
        for i in range(1, 5):
            #board.grid[self.__top+i][self.__left] = '|'
            board.set_grid(self.__left, self.__top + i, '|')
            #board.grid[self.__top+i][self.__left+1] = '|'
            board.set_grid(self.__left+1, self.__top + i, '|')
            board.set_grid(self.__left+8, self.__top+i,'|')
            board.set_grid(self.__left+9, self.__top+i, '|')
            #board.grid[self.__top+i][self.__left+8] = '|'
            #board.grid[self.__top+i][self.__left+9] = '|'
        for j in range(10):
            #board.grid[self.__top][self.__left + j] = '|'
            board.set_grid(self.__left + j, self.__top, '|')
    def put_magnet(self, board):
        self.create_magnet(330, 2, board)
        
        
        
        
