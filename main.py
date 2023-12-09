import pygame
#import your controller
from src.game_board import GameBoard
from src.game_board_view import GameBoardView
from src.game_controller import GameController

def main():
    pygame.init()
    #Create an instance on your controller object
    #Call your mainloop
    pygame.init()
    game_board = GameBoard()
    game_board_view = GameBoardView(game_board)
    game_controller = GameController(game_board, game_board_view)
    game_controller.mainloop()
    pygame.quit()
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
