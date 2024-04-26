import pygame
import random
from pygame.math import Vector2

#Screen Attributes

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BLOCK_SIZE = 20
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)


def draw_snake(screen, snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, BLOCK_SIZE, BLOCK_SIZE))

def draw_fruit(screen, fruit):
    pygame.draw.rect(screen, RED, (*fruit, BLOCK_SIZE, BLOCK_SIZE))

def game_loop(screen, snake, snake_direction, fruit):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return 
        
        #Snake Movement

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)

            elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction = (0, 1)

            elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction = (-1, 0)

            elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction = (1, 0)

    #Position of snake's head

    new_head = (snake[0][0] + snake_direction[0] * BLOCK_SIZE,
                snake[0][1] + snake_direction[1] * BLOCK_SIZE)
    
    snake.insert(0, new_head)

    '''base case'''

    #Checking for death collision

    if (new_head[0] < 0 or new_head[0] >= SCREEN_WIDTH or
            new_head[1] < 0 or new_head[1] >= SCREEN_HEIGHT or
            new_head in snake[1:]):
        pygame.quit()
        return  
    
    #Checking for fruit collision

    if new_head == fruit:
        fruit = (random.randint(0, SCREEN_WIDTH // BLOCK_SIZE - 1) * BLOCK_SIZE,
                    random.randint(0, SCREEN_HEIGHT // BLOCK_SIZE - 1) * BLOCK_SIZE)
        
    else:
        snake.pop()
    
    #Clearing the screen and drawing updated objects

    screen.fill(BLACK)

    draw_snake(screen, snake)

    draw_fruit(screen, fruit)

    pygame.display.flip()
    
    pygame.time.delay(100)

    game_loop(screen, snake, snake_direction, fruit)

def run_game():
    
    #Setting up the screen

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill(BLACK)
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()
    pygame.display.flip()
    clock.tick(FPS)

    snake = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
    snake_direction = (1, 0)  
    
    #Random generation of fruit position

    fruit = (random.randint(0, SCREEN_WIDTH // BLOCK_SIZE - 1) * BLOCK_SIZE,
             random.randint(0, SCREEN_HEIGHT // BLOCK_SIZE - 1) * BLOCK_SIZE)

    #Constructing the objects

    draw_snake(screen, snake)
    draw_fruit(screen, fruit)

    game_loop(screen, snake, snake_direction, fruit)

    pygame.quit()

run_game()