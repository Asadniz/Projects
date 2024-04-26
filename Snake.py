import pygame
import random
from pygame.math import Vector2

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BLOCK_SIZE = 20
FPS = 10
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

def game_loop(snake, snake_direction, fruit):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction = (1, 0)

    new_head = (snake[0][0] + snake_direction[0] * BLOCK_SIZE,
                snake[0][1] + snake_direction[1] * BLOCK_SIZE)
    snake.insert(0, new_head)
    '''base case'''
    if (new_head[0] < 0 or new_head[0] >= SCREEN_WIDTH or
            new_head[1] < 0 or new_head[1] >= SCREEN_HEIGHT or
            new_head in snake[1:]):
        pygame.quit()
        return  

    if new_head == fruit:
        fruit = (random.randint(0, SCREEN_WIDTH // BLOCK_SIZE - 1) * BLOCK_SIZE,
                    random.randint(0, SCREEN_HEIGHT // BLOCK_SIZE - 1) * BLOCK_SIZE)
    else:
        snake.pop()



    game_loop(snake, snake_direction, fruit)
def run_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill(BLACK)
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()
    pygame.display.flip()
    clock.tick(FPS)

    snake = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
    snake_direction = (1, 0)  

    fruit = (random.randint(0, SCREEN_WIDTH // BLOCK_SIZE - 1) * BLOCK_SIZE,
             random.randint(0, SCREEN_HEIGHT // BLOCK_SIZE - 1) * BLOCK_SIZE)

    draw_snake(screen, snake)
    draw_fruit(screen, fruit)

    game_loop(snake, snake_direction, fruit)

    pygame.quit()


run_game()