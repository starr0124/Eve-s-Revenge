import pygame, sys, random
from pygame.math import Vector2

cell_size = 40
cell_number = 15
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock() #influence time hm the game loop fast


#diff lib

class FRUIT:
    def __init__(self):
        self.red = pygame.image.load(f'assets/red_apple.png').convert_alpha()
        self.yellow = pygame.image.load(f'assets/yellow_apple.png').convert_alpha()
        self.blue = pygame.image.load(f'assets/blue_apple.png').convert_alpha()

        self.red_color = "red"
        self.yellow_color = "yellow"
        self.blue_color = "blue"

        self.fruits = [{'position': Vector2(2, 2), 'image': self.blue, 'color': self.blue_color}, 
                       {'position': Vector2(5, 5), 'image': self.red, 'color': self.red_color}, 
                       {'position': Vector2(8, 8), 'image': self.yellow, 'color': self.yellow_color}] 

    def draw_fruit(self):
        for fruit in self.fruits:
            fruit_rect = pygame.Rect(int(fruit['position'].x * cell_size), int(fruit['position'].y * cell_size), cell_size, cell_size)
            screen.blit(fruit['image'], fruit_rect)

    def spawn_fruit(self): 
        x = random.randint(0, cell_number - 1)
        y = random.randint(0, cell_number - 1)
        color = random.choice([self.red_color, self.yellow_color, self.blue_color])
        image = self.red if color == self.red_color else self.yellow if color == self.yellow_color else self.blue
        self.fruits.append({'position': Vector2(x, y), 'image': image, 'color': color})

    def randomize(self, index): 
        x = random.randint(0, cell_number - 1)
        y = random.randint(0, cell_number - 1)
        image = self.fruits[index]['image']
        color = self.fruits[index]['color']
        self.fruits[index] = {'position': Vector2(x, y), 'image': image, 'color': color}
