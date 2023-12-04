import random

class GameBoard:
    def __init__(self):
        self.grid = [[0] * 4 for _ in range(4)]
        self.add_tile()
        self.add_tile()

    def add_tile(self):
        empty = False
        for row in self.grid:
            if 0 in row:
                empty = True
                break

        if not empty:
            return  #if there is no empty spaces do nothing 

        added = False
        while not added:
            row = random.randint(0, 3)
            col = random.randint(0, 3)
            if self.grid[row][col] == 0:
                self.grid[row][col] = 4 if random.randint(0,100) < 40 else 2
                added = True

    def print_board(self):
        for row in self.grid:
            print(row)
        print("Let's start!!!")

    def hor_reflect(self):
        r = 0
        for row in self.grid:
            self.grid[r] = row[::-1] 
            r += 1

    def ver_reflect(self):
        r = 0
        for row in self.grid[::-1]:
            self.grid[r] = row
            r += 1

    def left(self):
        for k in range(3):  
            for i in range(4):  
                for j in range(3): 
                    if self.grid[i][j] == 0:  
                        self.grid[i][j] = self.grid[i][j+1]  
                        self.grid[i][j+1] = 0 

        for i in range(4):  
            for j in range(3):
                if self.grid[i][j] == self.grid[i][j + 1]:
                    self.grid[i][j] *= 2  
                    self.grid[i][j + 1] = 0  

        for k in range(3):  
            for i in range(4):
                for j in range(3):
                    if self.grid[i][j] == 0:
                        self.grid[i][j] = self.grid[i][j + 1]
                        self.grid[i][j + 1] = 0

    def right(self):
        self.hor_reflect()  
        self.left()        
        self.hor_reflect() 

    def up(self):
        for k in range(3):
            for i in range(1, 4):
                for j in range(4):
                    if self.grid[i - 1][j] == 0:
                        self.grid[i - 1][j] = self.grid[i][j]
                        self.grid[i][j] = 0

        for i in range(1, 4):
            for j in range(4):
                if self.grid[i][j] == self.grid[i - 1][j]:
                    self.grid[i - 1][j] *= 2
                    self.grid[i][j] = 0

        for k in range(3):
            for i in range(1, 4):
                for j in range(4):
                    if self.grid[i - 1][j] == 0:
                        self.grid[i - 1][j], self.grid[i][j] = self.grid[i][j], self.grid[i - 1][j]

    def down(self):
        self.ver_reflect()
        self.up()
        self.ver_reflect()

    def check_game_over(self):
        
        zero = 0  
        for i in range(4):
            for j in range(4):
                if self.grid[i][j] == 0:
                    zero = 1

        same_neighbor = 0 
        for i in range(3):
            for j in range(3):
                if self.grid[i][j] == self.grid[i][j + 1] or self.grid[i][j] == self.grid[i + 1][j]:
                    same_neighbor = 1

        if zero == 0 and same_neighbor == 0:  
            return True

        return False 