import pygame

class GameBoardView:
    def __init__(self, game_board):
        self.game_board = game_board
        self.size = (400, 400)  #window size 
        self.cell_size = 100    #cell size 
        self.cell_margin = 5    #spaces between cells  
        self.colors = {         # colors of the cells  
            0: pygame.Color('lightgrey'),
            2: pygame.Color('yellow'),
            4: pygame.Color('gold'),
        }
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption('2048 Game')

    def draw(self):
        self.screen.fill('black')  #background color: black 

        for i in range(4):
            for j in range(4):
                cell_value = self.game_board.grid[i][j]
                cell_color = self.colors.get(cell_value, ('white'))
                x = j * (self.cell_size + self.cell_margin)
                y = i * (self.cell_size + self.cell_margin)

                pygame.draw.rect(self.screen, cell_color, (x, y, self.cell_size, self.cell_size))

                if cell_value != 0:
                    font = pygame.font.Font(None, 36)
                    text = font.render(str(cell_value), True, ('black'))
                    text_rect = text.get_rect(center=(x + self.cell_size / 2, y + self.cell_size / 2))
                    self.screen.blit(text, text_rect)

        pygame.display.flip()

    def draw_game_over(self):
        font = pygame.font.Font(None, 72)
        text = font.render("Game Over!!!", True, ('red'))
        text_rect = text.get_rect(center=(self.size[0] / 2, self.size[1] / 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()

    def draw_high_score(self):
        high_score_font = pygame.font.Font(None, 36)
        high_score_text = high_score_font.render(f'High Score: {self.game_board.high_score}', True, pygame.Color('white'))
        text_rect = high_score_text.get_rect(center=(self.size[0] / 2, self.size[1] - 50))  
        self.screen.blit(high_score_text, text_rect)
        pygame.display.flip()
