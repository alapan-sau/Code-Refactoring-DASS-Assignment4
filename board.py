import time
import os
import random
from colorama import Fore, Back, Style 

class Board:
    def __init__(self):
        self.__width = 1400
        self.__height = 50
        self.__s_width = 200
        self.__left = 0
        self.__grid = [[' ' for i in range(self.__width)] for j in range(self.__height)]
       
    def get_grid(self):
        return self.__grid
    def get_s_width(self):
        return self.__s_width
    def get_height(self):
        return self.__height
    def set_grid(self, x, y, val):
        self.__grid[y][x] = val
    def get_left(self):
        return self.__left
    def set_left(self, x):
        self.__left = x
    
        
    
    
    
    
    
    def move_screen(self, din, t, enemy):
        if t == 0:
            self.__left = self.__left + din.get_speed()
        
        self.__grid[0][self.__left+0] = Fore.WHITE + 'C' + Fore.RESET
        self.__grid[0][self.__left+1] = Fore.WHITE + 'O' + Fore.RESET
        self.__grid[0][self.__left+2] = Fore.WHITE + 'I' + Fore.RESET
        self.__grid[0][self.__left+3] = Fore.WHITE + 'N' + Fore.RESET
        self.__grid[0][self.__left+4] = Fore.WHITE + 'S' + Fore.RESET
        self.__grid[0][self.__left+5] = Fore.WHITE + ':' + Fore.RESET
        self.__grid[0][self.__left+7] =  Fore.WHITE + str(din.get_coins() % 10) + Fore.RESET 
        self.__grid[0][self.__left+6] = Fore.WHITE + str(din.get_coins() // 10) + Fore.RESET 
        self.__grid[0][self.__left+8] = Fore.WHITE + ' ' + Fore.RESET
        self.__grid[0][self.__left+9] = Fore.WHITE + 'L' + Fore.RESET
        self.__grid[0][self.__left+10] = Fore.WHITE + 'I' + Fore.RESET
        self.__grid[0][self.__left+11] = Fore.WHITE + 'V' + Fore.RESET
        self.__grid[0][self.__left+12] = Fore.WHITE + 'E' + Fore.RESET
        self.__grid[0][self.__left+13] = Fore.WHITE + 'S' + Fore.RESET
        self.__grid[0][self.__left+14] = Fore.WHITE + ' ' + Fore.RESET
        self.__grid[0][self.__left+15] = Fore.WHITE + 'P' + Fore.RESET
        self.__grid[0][self.__left+16] = Fore.WHITE + 'L' + Fore.RESET
        self.__grid[0][self.__left+17] = Fore.WHITE + 'A' + Fore.RESET
        self.__grid[0][self.__left+18] = Fore.WHITE + 'Y' + Fore.RESET
        self.__grid[0][self.__left+19] = Fore.WHITE + 'E' + Fore.RESET
        self.__grid[0][self.__left+20] = Fore.WHITE + 'R' + Fore.RESET
        self.__grid[0][self.__left+21] = Fore.WHITE + ':' + Fore.RESET
        self.__grid[0][self.__left+22] = Fore.WHITE + str(din.get_lives()) + Fore.RESET
        self.__grid[0][self.__left+23] = Fore.WHITE + ' ' + Fore.RESET
        self.__grid[0][self.__left+24] = Fore.WHITE + 'L' + Fore.RESET
        self.__grid[0][self.__left+25] = Fore.WHITE + 'I' + Fore.RESET
        self.__grid[0][self.__left+26] = Fore.WHITE + 'V' + Fore.RESET
        self.__grid[0][self.__left+27] = Fore.WHITE + 'E' + Fore.RESET
        self.__grid[0][self.__left+28] = Fore.WHITE + 'S' + Fore.RESET
        self.__grid[0][self.__left+29] = Fore.WHITE + ' ' + Fore.RESET
        self.__grid[0][self.__left+30] = Fore.WHITE + 'E' + Fore.RESET
        self.__grid[0][self.__left+31] = Fore.WHITE + 'N' + Fore.RESET
        self.__grid[0][self.__left+32] = Fore.WHITE + 'E' + Fore.RESET
        self.__grid[0][self.__left+33] = Fore.WHITE + 'M' + Fore.RESET
        self.__grid[0][self.__left+34] = Fore.WHITE + 'Y' + Fore.RESET
        self.__grid[0][self.__left+35] = Fore.WHITE + ':' + Fore.RESET
        self.__grid[0][self.__left+36] = Fore.WHITE + str(enemy.get_lives()) + Fore.RESET 
        
        self.__grid[0][self.__left+37] = Fore.WHITE + 'S' + Fore.RESET
        self.__grid[0][self.__left+38] = Fore.WHITE + 'C' + Fore.RESET
        self.__grid[0][self.__left+39] = Fore.WHITE + 'O' + Fore.RESET
        self.__grid[0][self.__left+40] = Fore.WHITE + 'R' + Fore.RESET
        self.__grid[0][self.__left+41] = Fore.WHITE + 'E' + Fore.RESET
        self.__grid[0][self.__left+42] = Fore.WHITE + 'S' + Fore.RESET
        self.__grid[0][self.__left+43] = Fore.WHITE + ':' + Fore.RESET
        self.__grid[0][self.__left+45] = Fore.WHITE + str((din.get_coins() + din.get_enemy_killed() * 2)%10) + Fore.RESET
        self.__grid[0][self.__left+44] = Fore.WHITE + str((din.get_coins() + din.get_enemy_killed() * 2)//10) + Fore.RESET
        self.__grid[0][self.__left+46] = Fore.WHITE + ' ' + Fore.RESET
        self.__grid[0][self.__left+47] = Fore.WHITE + 'T' + Fore.RESET
        self.__grid[0][self.__left+48] = Fore.WHITE + 'I' + Fore.RESET
        self.__grid[0][self.__left+49] = Fore.WHITE + 'M' + Fore.RESET
        self.__grid[0][self.__left+50] = Fore.WHITE + 'E' + Fore.RESET
        self.__grid[0][self.__left+51] = Fore.WHITE + ' ' + Fore.RESET
        self.__grid[0][self.__left+52] = Fore.WHITE + 'L' + Fore.RESET
        self.__grid[0][self.__left+53] = Fore.WHITE + 'E' + Fore.RESET
        self.__grid[0][self.__left+54] = Fore.WHITE + 'F' + Fore.RESET
        self.__grid[0][self.__left+55] = Fore.WHITE + 'T' + Fore.RESET
        self.__grid[0][self.__left+56] = Fore.WHITE + ' ' + Fore.RESET
        self.__grid[0][self.__left+57] = Fore.WHITE + str((din.get_remaining_time() // 100)) + Fore.RESET
        self.__grid[0][self.__left+58] = Fore.WHITE + str((din.get_remaining_time() % 100)//10) + Fore.RESET
        self.__grid[0][self.__left+59] = Fore.WHITE + str((din.get_remaining_time() % 10))+ Fore.RESET
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    def create_boundary(self):
        
        for i in range(self.__width):
            # self.__grid[self.__height - 1][i] = Fore.WHITE + '^' + Fore.RESET
            self.__grid[self.__height - 1][i] = '^'
        ### making sky above which the mad can't go
        for i in range(self.__width):
            self.__grid[0][i] = Fore.WHITE + '-' + Fore.RESET 
        # self.__grid[0][0] = 'C'
        # self.__grid[0][1] = 'O'
        # self.__grid[0][2] = 'I'
        # self.__grid[0][3] = 'N'
        # self.__grid[0][4] = 'S'
        # self.__grid[0][6] =  str(din.coins % 10)
        # self.__grid[0][5] = str(din.coins // 10)
           
    
    def create_clouds(self, left, top):
        self.__grid[top+3][left] = '('
        self.__grid[top+3][left+1] = '('
        self.__grid[top+3][left+2] = '('
        self.__grid[top+3][left+3] = ')'
        self.__grid[top+3][left+4] = ')'
        self.__grid[top+3][left+5] = ')'
        self.__grid[top+2][left+1] = '('
        self.__grid[top+2][left+2] = '('
        self.__grid[top+2][left+3] = ')'
        self.__grid[top+2][left+4] = ')'
        self.__grid[top+1][left+2] = '('
        self.__grid[top+1][left+3] = ')'

    # def create_coins(self, left, top):
    #     number = random.randrange(1,10)
    #     for i in range(number):
    #         self.__grid[top][left+i] = '$'
    #         self.__grid[top+1][left+i] = '$'
        
    def create_scenery(self):
        self.create_boundary()
        ######## Creating clouds ########
        self.create_clouds(50, 14)
        self.create_clouds(100, 6)
        self.create_clouds(150, 15)
        self.create_clouds(200, 17)
        self.create_clouds(250, 13)
        self.create_clouds(300, 15)
        self.create_clouds(350, 6)
        self.create_clouds(400, 14)    
        self.create_clouds(450, 14)
        self.create_clouds(550, 6)
        self.create_clouds(600, 15)
        self.create_clouds(730, 17)
        self.create_clouds(760, 13)
        self.create_clouds(800, 15)
        self.create_clouds(900, 6)
        self.create_clouds(1000, 14)
        self.create_clouds(1050, 14)
        self.create_clouds(1101, 6)
        self.create_clouds(1140, 15)
        self.create_clouds(1200, 17)
        self.create_clouds(1250, 13)
        self.create_clouds(1300, 15)
        self.create_clouds(1350, 6)
         
        #### Putting coins ######
        # for i in range(0, 1200, 200):
            
        #     x = random.randint(13, 30) ##height
        #     y = random.randint(5, 150)  ##width
        #     self.create_coins(y+i, x)
            
        
            

