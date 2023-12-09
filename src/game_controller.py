import pygame
class GameController:
  
  def __init__(self, game_board, game_board_view):
    self.game_board = game_board
    self.game_board_view = game_board_view
    self.in_menu = True 

  def mainloop(self):
    self.menuloop()  
    self.gameloop()  
      
  def menuloop(self):
    menu_font = pygame.font.Font(None, 36)
    start_text = menu_font.render('Press S to start ', True, ('white'))
    quit_text = menu_font.render('Press Q to quit', True, ('white'))
    
    while self.in_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:  # 'S' key starts the game 
                    self.in_menu = False
                elif event.key == pygame.K_q:  # 'Q' key quits the game 
                    pygame.quit()
                    exit()

        self.game_board_view.screen.fill((0, 0, 0))  #background color is black 
        self.game_board_view.screen.blit(start_text, (100, 100))  #draws the begining text
        self.game_board_view.screen.blit(quit_text, (100, 150))  #draws the ending text 
        
        pygame.display.flip()
        pygame.time.wait(100)

  def gameloop(self):
    while True:
        moved = False 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.game_board.right()
                    moved = True 
                elif event.key == pygame.K_LEFT:
                    self.game_board.left()
                    moved = True 
                elif event.key == pygame.K_UP:
                    self.game_board.up()
                    moved = True 
                elif event.key == pygame.K_DOWN:
                    self.game_board.down()
                    moved = True 
                elif event.key == pygame.K_q: #ends the game
                    self.gameoverloop() 
                    return  
                
        if moved:
            self.game_board.add_tile()

        self.game_board_view.draw()  #draws the board 
        if self.game_board.check_game_over():
            self.gameoverloop()
            break
        pygame.time.wait(100)  

  def gameoverloop(self):
    self.game_board.check_and_update_high_score()
    self.game_board_view.draw_game_over() 
    self.game_board_view.draw_high_score()  
    pygame.time.wait(3000)
    