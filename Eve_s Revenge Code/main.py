import pygame, sys, random
from pygame.math import Vector2
import pygame.mixer
import fruit
import snake

my_fruit = fruit.FRUIT()
my_snake = snake.SNAKE()

#diff library
class MAIN: #eating the snack
    def __init__(self):
        self.snake = my_snake
        self.fruit = my_fruit
        self.show_controls = True # added variable for pop-up
        
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        
    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.snake.color_update()
        self.draw_score()
        self.other_instructions()

        if self.show_controls:
    # create a pop-up rectangle and display the instructions
            pop_up_rect = pygame.Rect(80, 150, 450, 150)
            pygame.draw.rect(screen, (255, 255, 255), pop_up_rect)
            pygame.draw.rect(screen, (0, 0, 0), pop_up_rect, 2)
            control_font = pygame.font.Font('assets/retro_computer.ttf', 16)
            control_text1 = control_font.render("Welcome to Eve's Revenge!", True, (0, 0, 0))
            control_text2 = control_font.render("Eat as many apples as you can!", True, (0, 0, 0))
            control_text3 = control_font.render("But only the same color as you!", True, (0, 0, 0))
            control_text4 = control_font.render("Use arrow keys to play!", True, (0, 0, 0))
            screen.blit(control_text1, (pop_up_rect.x + 10, pop_up_rect.y + 10))
            screen.blit(control_text2, (pop_up_rect.x + 10, pop_up_rect.y + 50))
            screen.blit(control_text3, (pop_up_rect.x + 10, pop_up_rect.y + 80))
            screen.blit(control_text4, (pop_up_rect.x + 10, pop_up_rect.y + 110))

        if self.show_controls and any(pygame.key.get_pressed()[key] for key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]):
            # if the instructions are being displayed and any arrow key is pressed, set display_instructions to False
            self.show_controls = False
        
    def check_collision(self):
        for fruit in self.fruit.fruits:
            if fruit['position'] == self.snake.body[0]:
                if fruit['color'] == self.snake.color:  # if the fruit color matches the snake color, increase length
                    self.snake.add_block()
                    self.snake.play_eat_correct()
                else:  # if the fruit color does not match the snake color, decrease length
                    self.snake.remove_block()
                    self.snake.play_eat_wrong()
                
                self.snake.color_changer()
                
                if fruit['image'] != self.fruit.blue:  # if the blue apple was not eaten, respawn it at a random position
                    self.fruit.randomize(self.fruit.fruits.index(fruit))
               
            for block in self.snake.body[1:]:  # prevent the fruit spawning on the snake's body
                if block == fruit['position']:
                    self.fruit.randomize(self.fruit.fruits.index(fruit))
                    break

    def check_fail(self):
    # check if the snake is outside the screen
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
            
    # check if the snkae is only 2 length
        if len(self.snake.body) == 1:
            self.game_over()
            
    # check if the snake hits its own body
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

            
    def game_over(self):
        self.snake.reset()
        
    def draw_score(self): #scoring
        score_text = str(len(self.snake.body) - 3)
        game_font = pygame.font.Font('assets/retro_computer.ttf', 25)
        score_display = game_font.render(score_text, True, (0, 0, 0))
        score_x = int (cell_size * cell_number - 60)
        score_y = int (cell_size * cell_number + 50)
        score_rect = score_display.get_rect(center = (score_x, score_y))

        # fill background with the same color as screen
        bg_rect = pygame.Rect(0, 600, 600, 100)
        pygame.draw.rect(screen, (125, 215, 70), bg_rect)

        # center the score display inside the bg_rect
        screen.blit(score_display, score_rect)

    def other_instructions(self): #the green bar below
        ins_font = pygame.font.Font('assets/retro_computer.ttf', 15)
        instructions1 = ins_font.render("Use arrow keys to play", True, (0, 0, 0))
        instructions2 = ins_font.render("Eat the correct apple", True, (0, 0, 0))
        instructions3= ins_font.render("Press ESCAPE to exit the game", True, (0, 0, 0))
        ins_x = 10
        ins1 = instructions1.get_rect(left=ins_x, centery=625)
        ins2 = instructions2.get_rect(left=ins_x, centery=650)
        ins3 = instructions3.get_rect(left=ins_x, centery=675)
        screen.blit(instructions1, ins1)
        screen.blit(instructions2, ins2)
        screen.blit(instructions3, ins3)

pygame.mixer.pre_init(44100, -16, 2, 512)     
pygame.init()

pygame.mixer.music.load('sounds/sitting on soft grass.wav')
pygame.mixer.music.set_volume(0.5)

pygame.mixer.music.play(-1)

cell_size = 40
cell_number = 15
screen = pygame.display.set_mode((600, 700))
clock = pygame.time.Clock() #influence time hm the game loop fast

SCREEN_UPDATE = pygame.USEREVENT #we trigger this
pygame.time.set_timer(SCREEN_UPDATE, 150) #triggers 150 milliseconds

main_game = MAIN()

while True: #event loop
    for event in pygame.event.get(): #do this when
        if event.type == pygame.QUIT: #someone wanted to quit the window
            pygame.quit() #quits the window
            sys.exit() #quits the window
       
        if event.type == SCREEN_UPDATE:
            main_game.update()
            
        #controlling the snake
        if event.type == pygame.KEYDOWN: #like keyVal == win.checkKey()
            if event.key == pygame.K_UP: #specific key, up arrow
                if main_game.snake.direction.y != 1: #prevents reversing
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_RIGHT: #specific key, right arrow
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_DOWN: #specific key, down arrow
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT: #specific key, left arrow
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit
        
    #screen.fill((125, 215, 70))
    bg_grass = pygame.image.load("assets/grassland.png")
    screen.blit(bg_grass, (0, 0))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
