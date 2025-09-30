import pygame
import time
import random

WIDTH = 600
HEIGHT = 600

# initialise the positions
positions = {(x,y):0 for x in range(10) for y in range(10)}
positions[(0,0)] = "SH"

# initalise pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)


# class to store the snake body
class Snake(pygame.sprite.Sprite):
    def __init__(self, x, y, width=10, height=10, img=None):
        super().__init__()
        self.image = pygame.image.load(img) if img else pygame.rect((width, height))
        self.rect = self.image.get_rect(topleft=(x - (width/2), y - (height/2)))
    def update(self, speed):
        ...
        


# key press
def detect_key_press():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_w:  
                    ...
                elif event.key == pygame.K_a:  
                    ...
                elif event.key == pygame.K_s:
                    ...
                elif event.key == pygame.K_d:
                    ...    

# generate apple at random position
def generate_apple():
    x = random.randint(0, 10)
    y = random.randint(0, 10)

    while positions[(x, y)] != 0:
        x = random.randint(0, 10)
        y = random.randint(0, 10)
    
    positions[(x, y)] = "A"

# main game loop
def main():
    snake = pygame.sprite.Group()
    for position in positions:
        ...
     
if __name__ == "__main__":
    main()

time.sleep(3)
pygame.quit()