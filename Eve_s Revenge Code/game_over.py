import pygame

class GAMEOVER:
    def game_over(self):
    # try_again or exit the game once hits the wall and body
        pop_up_rect = pygame.Rect(80, 150, 450, 150)
        pygame.draw.rect(screen, (255, 255, 255), pop_up_rect)
        pygame.draw.rect(screen, (0, 0, 0), pop_up_rect, 2)
        gameover_font = pygame.font.Font('assets/retro_computer.ttf', 35)
        game_over_font = pygame.font.Font('assets/retro_computer.ttf', 15)
        game_over_text1 = gameover_font.render("GAME OVER", True, (0, 0, 0))
        game_over_text2 = game_over_font.render("Press ENTER to play again", True, (0, 0, 0))
        game_over_text3 = game_over_font.render("Press ESCAPE to exit", True, (0, 0, 0))
        screen.blit(game_over_text1, (pop_up_rect.x + 100, pop_up_rect.y + 10))
        screen.blit(game_over_text2, (pop_up_rect.x + 10, pop_up_rect.y + 90))
        screen.blit(game_over_text3, (pop_up_rect.x + 10, pop_up_rect.y + 110))

        # set failed to True
        self.failed = True

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        #rest the game
                        self.snake.reset()
                        self.failed = False
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            pygame.display.update()
