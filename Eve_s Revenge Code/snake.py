import pygame, sys, random
from pygame.math import Vector2

pygame.init()
cell_size = 40
cell_number = 15

screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()


#diff library
class SNAKE:
    def __init__(self):
        self.body = [Vector2(6, 8), Vector2(5, 8), Vector2(4, 8)]
        self.direction = Vector2(0, 0)
        self.new_block = False
        self.colors = ['red', 'blue', 'yellow']
        self.color = random.choice(self.colors)
        self.color_change = False
        self.update_images()

        #head position
        self.head_up = pygame.image.load('assets/blue_head_u.png').convert_alpha()
        self.head_down = pygame.image.load('assets/blue_head_d.png').convert_alpha()
        self.head_right = pygame.image.load('assets/blue_head_r.png').convert_alpha()
        self.head_left = pygame.image.load('assets/blue_head_l.png').convert_alpha()
        #tail position
        self.tail_up = pygame.image.load('assets/blue_tail_u.png').convert_alpha()
        self.tail_down = pygame.image.load('assets/blue_tail_d.png').convert_alpha()
        self.tail_right = pygame.image.load('assets/blue_tail_r.png').convert_alpha()
        self.tail_left = pygame.image.load('assets/blue_tail_l.png').convert_alpha()
        #body position
        self.body_vertical = pygame.image.load('assets/blue_body_v.png').convert_alpha()
        self.body_horizontal = pygame.image.load('assets/blue_body_h.png').convert_alpha()
        #turn body position
        self.body_tr = pygame.image.load('assets/blue_curve_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('assets/blue_curve_tl.png').convert_alpha()
        self.body_br = pygame.image.load('assets/blue_curve_br.png').convert_alpha()
        self.body_bl = pygame.image.load('assets/blue_curve_bl.png').convert_alpha()
        
        self.eat_correct = pygame.mixer.Sound('sounds/eat_correct.wav')
        self.eat_wrong = pygame.mixer.Sound('sounds/eat_wrong.wav')
        self.eat_correct.set_volume(0.7)
        self.eat_wrong.set_volume(0.7)
        
    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()
        
        for index, block in enumerate(self.body):
            #create a rect (positioning)
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1 :
                        screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1 :
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1 :
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1 :
                        screen.blit(self.body_br, block_rect)
                        

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): self.head = self.head_left
        elif head_relation == Vector2(-1,0): self.head = self.head_right
        elif head_relation == Vector2(0,1): self.head = self.head_up
        elif head_relation == Vector2(0,-1): self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
        elif tail_relation == Vector2(0,1): self.tail = self.tail_up
        elif tail_relation == Vector2(0,-1): self.tail = self.tail_down

    def move_snake(self):
        if self.new_block == True: #extending the snake
            body_copy = self.body[:] #extends the snake infinitely
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:] #duplication
            self.new_block = False #prevents the infinite extension
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self): #
        self.new_block = True

    def remove_block(self):
            self.body.pop()

    def update_images(self):
        self.head_up = pygame.image.load(f'assets/{self.color}_head_u.png').convert_alpha()
        self.head_down = pygame.image.load(f'assets/{self.color}_head_d.png').convert_alpha()
        self.head_right = pygame.image.load(f'assets/{self.color}_head_r.png').convert_alpha()
        self.head_left = pygame.image.load(f'assets/{self.color}_head_l.png').convert_alpha()
        self.tail_up = pygame.image.load(f'assets/{self.color}_tail_u.png').convert_alpha()
        self.tail_down = pygame.image.load(f'assets/{self.color}_tail_d.png').convert_alpha()
        self.tail_right = pygame.image.load(f'assets/{self.color}_tail_r.png').convert_alpha()
        self.tail_left = pygame.image.load(f'assets/{self.color}_tail_l.png').convert_alpha()
        self.body_vertical = pygame.image.load(f'assets/{self.color}_body_v.png').convert_alpha()
        self.body_horizontal = pygame.image.load(f'assets/{self.color}_body_h.png').convert_alpha()
        self.body_tr = pygame.image.load(f'assets/{self.color}_curve_tr.png').convert_alpha()
        self.body_tl = pygame.image.load(f'assets/{self.color}_curve_tl.png').convert_alpha()
        self.body_br = pygame.image.load(f'assets/{self.color}_curve_br.png').convert_alpha()
        self.body_bl = pygame.image.load(f'assets/{self.color}_curve_bl.png').convert_alpha()
        
    def color_update(self):
        if self.color_change:
            self.color = random.choice(self.colors)
            self.update_images()
            self.color_change = False
                         
    def color_changer(self):
        self.color_change = True

    def reset(self):
        self.body = [Vector2(6, 8), Vector2(5, 8), Vector2(4, 8)]
        self.direction = Vector2(0, 0)

    def play_eat_correct(self):
        self.eat_correct.play()

    def play_eat_wrong(self):
        self.eat_wrong.play()
        
pygame.display.update()
