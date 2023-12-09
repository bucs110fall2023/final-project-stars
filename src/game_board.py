import random
import requests

class GameBoard:
    def __init__(self):
        self.grid = [[0] * 4 for _ in range(4)]
        self.add_tile()
        self.add_tile()
        self.score = 0

    def get_high_score_from_server(self):
        """"
        Gets the high score from a server using a get request.
        Returns the high score as an integer, or 0 if the request fails.
        """
        response = requests.get("https://example.com/api/highscore")
        if response.status_code == 200:
            return int(response.json()['high_score'])
        else:
            return 0
     
    def update_high_score_to_server(self):
        """
        Updates the high score on a server using a post request.
        Prints a message if the update fails.
        """
        response = requests.post("https://example.com/api/highscore", json={"high_score": self.high_score})
        if response.status_code != 200:
            print("Failed to update high score on server.")
    
    def check_and_update_high_score(self):
        """
        Checks the current score with the highest score obtained from the server.
        """
        high_score = self.get_high_score_from_server()
        if high_score is None:
            high_score = 0
        if self.score > high_score:
            self.high_score = self.score
            self.update_high_score_to_server()

    def add_tile(self):
        """
        Adds a new tile to a random empty space on the board, with a 40% chance of 4 and a 60% chance of 2. 
        If no empty spaces are available, no action is taken.
        """
        empty = False
        for row in self.grid:
            if 0 in row:
                empty = True
                break

        if not empty:
            return  

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
        """
        This function reflects the game board horizontally, reversing each row.
        """
        r = 0
        for row in self.grid:
            self.grid[r] = row[::-1] 
            r += 1

    def ver_reflect(self):
        """
        This function reflects the game board vertically, reversing each row.
        """
        r = 0
        for row in self.grid[::-1]:
            self.grid[r] = row
            r += 1

    def left(self):
        """
        This function shifts all tiles on the game board to left.
        First block used to shift all cells to the left. 
        Second for block used to merge cells of the same value. 
        Third block is used to shift the cells left again to fill any gaps may have been created after the merge. 
        """
        for k in range(3):  
            for i in range(4):  
                for j in range(3): 
                    if self.grid[i][j] == 0:  
                        self.grid[i][j] = self.grid[i][j+1]  
                        self.grid[i][j+1] = 0 

        for i in range(4):  
            for j in range(3):
                if self.grid[i][j] == self.grid[i][j + 1]:
                    self.score += self.grid[i][j] * 2
                    self.grid[i][j] *= 2  
                    self.grid[i][j + 1] = 0  

        for k in range(3):  
            for i in range(4):
                for j in range(3):
                    if self.grid[i][j] == 0:
                        self.grid[i][j] = self.grid[i][j + 1]
                        self.grid[i][j + 1] = 0

    def right(self):
        """
        This function shifts all cells on the game board right by using hor_reflect and left function.
        """
        self.hor_reflect()  
        self.left()        
        self.hor_reflect() 

    def up(self):
        """
        This function shifts all cells on the game board up.
        The first block shifts all cells upwards, moving cells into any empty spaces.
        The second block merges any tiles of the same value that are neighbour on top of each other.
        The third block shifts the cells upwards again to fill any gaps created after the merge.
        """
        for k in range(3):
            for i in range(1, 4):
                for j in range(4):
                    if self.grid[i - 1][j] == 0:
                        self.grid[i - 1][j] = self.grid[i][j]
                        self.grid[i][j] = 0

        for i in range(1, 4):
            for j in range(4):
                if self.grid[i][j] == self.grid[i - 1][j]:
                    self.score += self.grid[i][j] * 2 
                    self.grid[i - 1][j] *= 2 
                    self.grid[i][j] = 0

        for k in range(3):
            for i in range(1, 4):
                for j in range(4):
                    if self.grid[i - 1][j] == 0:
                        self.grid[i - 1][j], self.grid[i][j] = self.grid[i][j], self.grid[i - 1][j]

    def down(self):
        """
        This function shifts all cells on the game board down by using ver_reflect and up function.
        """
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