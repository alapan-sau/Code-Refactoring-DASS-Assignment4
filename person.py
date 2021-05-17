import time

class Person:
    def __init__(self, left, top, lives, board):
      self._left = left
      self._top = top
      self._coins = 0
      self._lives = 3
    def get_lives(self):
        return self._lives  
    def get_coins(self):
        return self._coins
    def set_left(self, x):
        self._left = x
    def set_top(self, x):
        self._top = x 
    def get_left(self):
        return self._left
    def get_top(self):
        return self._top 
    def set_lives(self, x):
        self._lives = x 
        
    def jump(self):                         
        self._top = self._top - 1
    
    
class  Din(Person):
    def __init__(self, left, top, lives, time, board):
        super().__init__(left, top, lives, board)
       
        self.__remaining_time = time
        self.__speed = 1
        self.__boost_time = 0
        self.__shield_on = 0 ### when sheild_on is 1 then shield is on 
        self.__enemy_killed = 0
       
    def create_din(self, board):
        if self.__shield_on == 0: 
            # board.grid[self._top][self._left+4] = '.'
            # board.grid[self._top+1][self._left+3] = '.'
            # board.grid[self._top+1][self._left+5] = '.'
            board.set_grid(self._left+4, self._top, '.')
            board.set_grid(self._left+3, self._top + 1, '.')
            board.set_grid(self._left+5, self._top + 1, '.')
            
            for i in range(2,6):
                for j in range(2, 7):
                    # board.grid[self._top+i][self._left+j] = '.'
                    board.set_grid(self._left+j, self._top + i, '.')
            for i in range(6, 9):
                # board.grid[self._top+i][self._left+3] = '.'
                # board.grid[self._top+i][self._left+5] = '.'
                board.set_grid(self._left+3, self._top+i, '.')
                board.set_grid(self._left+5, self._top +i, '.')
            # board.grid[self._top+3][self._left+1] = '.'
            # board.grid[self._top+4][self._left] = '.'
            # board.grid[self._top+3][self._left+7] = '.'
            # board.grid[self._top+4][self._left+8] = '.'
            board.set_grid(self._left+1, self._top+3, '.')
            board.set_grid(self._left, self._top+4, '.')
            board.set_grid(self._left+7, self._top+3, '.')
            board.set_grid(self._left+8, self._top+4, '.')

        elif self.__shield_on == 1:
            for j in range(4):
                # board.grid[self._top + j][self._left + 8] = '.'
                board.set_grid(self._left+8, self._top + j, '.')
            # board.grid[self._top][self._left+4] = '.'
            # board.grid[self._top+1][self._left+3] = '.'
            # board.grid[self._top+1][self._left+5] = '.'
            board.set_grid(self._left+4, self._top, '.') 
            board.set_grid(self._left+3, self._top+1, '.') 
            board.set_grid(self._left+5, self._top+1, '.') 
            # board.set_grid(self._left+4, self.top, '.')      
            for i in range(2,6):
                for j in range(2, 7):
                    # board.grid[self._top+i][self._left+j] = '.'
                    board.set_grid(self._left+j, self._top + i, '.') 
            for i in range(6, 9):
                # board.grid[self._top+i][self._left+3] = '.'
                # board.grid[self._top+i][self._left+5] = '.'
                board.set_grid(self._left+3, self._top +i, '.')
                board.set_grid(self._left+5, self._top +i, '.')
                  
            # board.grid[self._top+3][self._left+1] = '.'
            # board.grid[self._top+4][self._left] = '.'
            # board.grid[self._top+3][self._left+7] = '.'
            # board.grid[self._top+4][self._left+8] = '.'
            board.set_grid(self._left+1, self._top+3, '.') 
            board.set_grid(self._left, self._top+4, '.') 
            board.set_grid(self._left+7, self._top+3, '.') 
            board.set_grid(self._left+8, self._top+4, '.') 
    
    

    
                        
        # for i in range(2):
        #     for j in range (2):
        #         board.grid[self.top+i][self.left+j] = 'm'
                
    # def remove_din(self, board):
    #     # print("Hey I am in remove din function")
    #     if board.grid[self.top][self.left+4] == '.':
    #         board.grid[self.top][self.left+4] = ' '
    #     if board.grid[self.top+1][self.left+3] == '.':
    #         board.grid[self.top+1][self.left+3] = ' '
    #     if board.grid[self.top+1][self.left+5] == '.':
    #         board.grid[self.top+1][self.left+5] = '.'
        
    #     # board.grid[self.top+2][self.left+2] = '.'
    #     # board.grid[self.top+2][self.left+3] = '.'
    #     # board.grid[self.top+2][self.left+4] = '.'
    #     # board.grid[self.top+2][self.left+5] = '.'
    #     # board.grid[self.top+2][self.left+6] = '.'
    #     for i in range(2,6):
    #         for j in range(2, 7):
    #             if board.grid[self.top+i][self.left+j] == '.':
    #                 board.grid[self.top+i][self.left+j] = ' '
    #     for i in range(6, 9):
    #         if board.grid[self.top+i][self.left+3] == '.':
    #             board.grid[self.top+i][self.left+3] = ' '
    #         if board.grid[self.top+i][self.left+5] == '.':
    #             board.grid[self.top+i][self.left+5] = ' '
    #     if board.grid[self.top+3][self.left+1] == '.':
    #         board.grid[self.top+3][self.left+1] = ' '
    #     if board.grid[self.top+4][self.left] == '.':
    #         board.grid[self.top+4][self.left] = ' '
    #     if board.grid[self.top+3][self.left+7] == '.':
    #         board.grid[self.top+3][self.left+7] = ' '
    #     if board.grid[self.top+4][self.left+8] == '.':
    #         board.grid[self.top+4][self.left+8] = ' '
    

    
                    
    def remove_din(self, board):
        if(self.__shield_on):
            for j in range(4):
                # board.grid[self._top + j][self._left + 8] = ' '
                board.set_grid(self._left+8, self._top + j, ' ') 
        # board.grid[self._top][self._left+4] = ' '
        # board.grid[self._top+1][self._left+3] = ' '
        # board.grid[self._top+1][self._left+5] = ' '

        # for i in range(2,6):
        #     for j in range(2, 7):
        #         board.grid[self._top+i][self._left+j] = ' '
        # for i in range(6, 9):
        #     board.grid[self._top+i][self._left+3] = ' '
        #     board.grid[self._top+i][self._left+5] = ' '
        # board.grid[self._top+3][self._left+1] = ' '
        # board.grid[self._top+4][self._left] = ' '
        # board.grid[self._top+3][self._left+7] = ' '
        # board.grid[self._top+4][self._left+8] = ' '
        board.set_grid(self._left+4, self._top, ' ')
        board.set_grid(self._left+3, self._top + 1, ' ')
        board.set_grid(self._left+5, self._top + 1, ' ')
            
        for i in range(2,6):
            for j in range(2, 7):
                    # board.grid[self._top+i][self._left+j] = '.'
                board.set_grid(self._left+j, self._top + i, ' ')
        for i in range(6, 9):
                # board.grid[self._top+i][self._left+3] = '.'
                # board.grid[self._top+i][self._left+5] = '.'
            board.set_grid(self._left+3, self._top+i, ' ')
            board.set_grid(self._left+5, self._top +i, ' ')
            # board.grid[self._top+3][self._left+1] = '.'
            # board.grid[self._top+4][self._left] = '.'
            # board.grid[self._top+3][self._left+7] = '.'
            # board.grid[self._top+4][self._left+8] = '.'
        board.set_grid(self._left+1, self._top+3, ' ')
        board.set_grid(self._left, self._top+4, ' ')
        board.set_grid(self._left+7, self._top+3, ' ')
        board.set_grid(self._left+8, self._top+4, ' ')
        
    def remove_din_on_collision(self, board):
        grid = board.get_grid()    
        if grid[self._top][self._left+4] == '.':
            # board.grid[self._top][self._left+4] = ' '
            board.set_grid(self._left+4, self._top, ' ')
            
        grid = board.get_grid()    
        
        if grid[self._top+1][self._left+3] == '.':
            # board.grid[self._top+1][self._left+3] = ' '
            board.set_grid(self._left+3, self._top + 1, ' ')
            
        grid = board.get_grid()
            
        if grid[self._top+1][self._left+5] == '.':
            # board.grid[self._top+1][self._left+5] = '.'
            board.set_grid(self._left+5, self._top + 1, ' ')
        grid = board.get_grid()          
      
        for i in range(2,6):
            for j in range(2, 7):
                grid = board.get_grid()    
                if grid[self._top+i][self._left+j] == '.':
                    board.set_grid(self._left+j, self._top + i, ' ')
                    # board.grid[self._top+i][self._left+j] = ' '
        for i in range(6, 9):
            grid = board.get_grid()    
            if grid[self._top+i][self._left+3] == '.':
                # board.grid[self._top+i][self._left+3] = ' '
                board.set_grid(self._left+3, self._top+i, ' ')
            
            grid = board.get_grid()    
            if grid[self._top+i][self._left+5] == '.':
                # board.grid[self._top+i][self._left+5] = ' '
                board.set_grid(self._left+5, self._top +i, ' ')
        grid = board.get_grid()    
        if grid[self._top+3][self._left+1] == '.':
            # board.grid[self._top+3][self._left+1] = ' '
            board.set_grid(self._left+1, self._top+3, ' ')
        
        grid = board.get_grid()    
        if grid[self._top+4][self._left] == '.':
            #board.grid[self._top+4][self._left] = ' '
            board.set_grid(self._left, self._top+4, ' ')
       
        grid = board.get_grid()    
        if grid[self._top+3][self._left+7] == '.':
            #board.grid[self._top+3][self._left+7] = ' '
            board.set_grid(self._left+7, self._top+3, ' ')
       
        grid = board.get_grid()    
        if grid[self._top+4][self._left+8] == '.':
            #board.grid[self._top+4][self._left+8] = ' '
            board.set_grid(self._left+8, self._top+4, ' ')
    
      
    def decrease_live(self, board):
        self._lives -= 1
## The screen will move continuously therefore when mario reaches the border then we have to push mario to right but this condition won't be put here ## 
    def move_left(self, board):
        if self._left > self.__speed and self._left > board.get_left() + self.__speed:
            self.remove_din(board)
            self._left = self._left - self.__speed
                
    def move_right(self, board):
        if self._left+8 != 920 - self.__speed and self._left+9 <= board.get_left()+200 - self.__speed: 
            self.remove_din(board)     
            self._left = self._left + self.__speed
    def jump(self, board):
        if self._top >= self.__speed + 1:
            self.remove_din(board)
            self._top = self._top - self.__speed
            
    def get_shield_on(self):
        return self.__shield_on
    def get_speed(self):
        return self.__speed

    def get_boost_time(self):
        return self.__boost_time
    def get_enemy_killed(self):
        return self.__enemy_killed
    def set_speed(self, x):
        self.__speed = x
    def set_boost_time(self, x):
        self.__boost_time = x

    def set_shield_on(self, x):
        self.__shield_on = x
          
    def get_remaining_time(self):
        return self.__remaining_time
    
    def set_remaining_time(self, x):
        self.__remaining_time = x
              
        
    # def move_down(self, board):
    #     if self.top + 9 != board.height - 8:
    #         if board.grid[]
    # def move_left(self, board, coins):
    #     if self.left != 0 and self.left != board.left:
    #         t = False
    #         for i in range(9):
    #             for j in range(9):              #########Coins are yet to be considered ######
    #                 # if board.grid[self.top + i][self.left + j] != ' ' and board.grid[self.top + i][self.left + j] != ')' and board.grid[self.top + i][self.left + j] != '(' and board.grid[self.top + i][self.left + j] != '.':
    #                 #     t = True if board.grid[self.top + i][self.left + j] != ' ' and board.grid[self.top + i][self.left + j] != ')' and board.grid[self.top + i][self.left + j] != '(' and board.grid[self.top + i][self.left + j] != '.':
    #                 #     t = True 
    #                 if board.grid[self.top + i][self.left +j] == '$':
    #                     self.collect_coin()
    #                     coins.remove_coin(board)
    #                 elif board.grid[self.top + i][self.left + j] != ' ' and board.grid[self.top + i][self.left + j] != ')' and board.grid[self.top + i][self.left + j] != '(' and board.grid[self.top + i][self.left + j] != '.':
    #                     t = True 
                        
    #         if t != True: ##then you can move
    #             self.remove_din(board)
    #             self.left = self.left - 1
    
    # def move_right(self, board, coins):
    #     if self.left+8 != 1399 and self.left+9 != board.left+200:
    #         t = False
    #         for i in range(9):
    #             for j in range(9):
    #                 if board.grid[self.top + i][self.left + j] != ' ' and board.grid[self.top + i][self.left + j] != ')' and board.grid[self.top + i][self.left + j] != '(' and board.grid[self.top + i][self.left + j] != '.':
    #                     t = True
    #                 if board.grid[self.top + i][self.left +j] == '$':
    #                     self.collect_coin()
    #                     coins.remove_coin(board)
    #         if t != True:
    #             self.remove_din(board)     
    #             self.left = self.left + 1  
    
    # def jump(self, board, coins):
    #     if self.top != 0:
    #         t = False
    #         for i in range(9):
    #             for j in range(9):
    #                 if board.grid[self.top + i][self.left + j] != ' ' and board.grid[self.top + i][self.left + j] != ')' and board.grid[self.top + i][self.left + j] != '(' and board.grid[self.top + i][self.left + j] != '.':
    #                     t = True
    #                 if board.grid[self.top + i][self.left +j] == '$':
    #                     self.collect_coin()
    #                     coins.remove_coin(board)
    #         if t != True:
    #             self.remove_din(board)     
    #             self.top = self.top - 1  
    
    def collect_coin(self):
        self._coins = self._coins + 1
        
    def enemy_killed_increase(self):
        self.__enemy_killed += 1   
        
        
        
        
class Enemy(Person):
    def __init__(self, left, top, lives, board):
        super().__init__(left, top, lives, board)
        self.__s_time = round(time.time())
        self.__speed = 1

    
    def create_enemy(self, board):
        board.set_grid(self._left,self._top+4, '{')
        board.set_grid(self._left+1,self._top+4, 'D')
        board.set_grid(self._left+2,self._top+4, '}')
        board.set_grid(self._left+2,self._top+3, ':')
        board.set_grid(self._left+2,self._top+5, '_')
        board.set_grid(self._left+3,self._top+2, ':')
        board.set_grid(self._left+4,self._top+1, '{')
        board.set_grid(self._left+5,self._top+1, 'O')
        board.set_grid(self._left+6,self._top+1, 'O')
        board.set_grid(self._left+8,self._top+1, '!')
        board.set_grid(self._left+5,self._top, '{') 
        board.set_grid(self._left+6,self._top, ',')
        board.set_grid(self._left+7,self._top, ',')
        board.set_grid(self._left+8,self._top, '}')  
        board.set_grid(self._left+3,self._top+5, '_')
        board.set_grid(self._left+4,self._top+6, '_')
        board.set_grid(self._left+5,self._top+7, '{')
        board.set_grid(self._left+6,self._top+8, '{')
        board.set_grid(self._left+7,self._top+8, '_')
        board.set_grid(self._left+8,self._top+8, '_')
        for i in range(8):
            board.set_grid(self._left+8, self._top + i + 1, '!') 
    
    def remove_enemy(self, board):
        board.set_grid(self._left,self._top+4, ' ')
        board.set_grid(self._left+1,self._top+4, ' ')
        board.set_grid(self._left+2,self._top+4, ' ')
        board.set_grid(self._left+2,self._top+3, ' ')
        board.set_grid(self._left+2,self._top+5, ' ')
        board.set_grid(self._left+3,self._top+2, ' ')
        board.set_grid(self._left+4,self._top+1, ' ')
        board.set_grid(self._left+5,self._top+1, ' ')
        board.set_grid(self._left+6,self._top+1, ' ')
        board.set_grid(self._left+8,self._top+1, ' ')
        board.set_grid(self._left+5,self._top, ' ') 
        board.set_grid(self._left+6,self._top, ' ')
        board.set_grid(self._left+7,self._top, ' ')
        board.set_grid(self._left+8,self._top, ' ')  
        board.set_grid(self._left+3,self._top+5, ' ')
        board.set_grid(self._left+4,self._top+6, ' ')
        board.set_grid(self._left+5,self._top+7, ' ')
        board.set_grid(self._left+6,self._top+8, ' ')
        board.set_grid(self._left+7,self._top+8, ' ')
        board.set_grid(self._left+8,self._top+8, ' ')
        for i in range(8):
            board.set_grid(self._left+8, self._top + i + 1, ' ')
    
    
    def jump(self, board):
        self.remove_enemy(board)
        if self._top > self.__speed:
            self._top = self._top - 1
                                                                                                                                                                                                                                                                                                                                                                                       