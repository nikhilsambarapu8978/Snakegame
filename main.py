import pygame
import random
import time

pygame.init()
width, height = 600, 600
game_screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

snake_x, snake_y = width // 2, height // 2
change_x, change_y = 0, 0
snake_body = [(snake_x, snake_y)]
clock = pygame.time.Clock()
score = 0
font = pygame.font.SysFont(None, 35)

def spawn_food():
    while True:
        food_x = random.randrange(0, width, 10)
        food_y = random.randrange(0, height, 10)
        if (food_x, food_y) not in snake_body:
            return food_x, food_y

food_x, food_y = spawn_food()

def display_snake():
    global snake_x, snake_y, change_x, change_y, food_x, food_y, score
    snake_x = (snake_x + change_x) % width
    snake_y = (snake_y + change_y) % height
    if (snake_x, snake_y) in snake_body[1:]:
        game_over()
    snake_body.append((snake_x, snake_y))
    if food_x == snake_x and food_y == snake_y:
        score += 10
        food_x, food_y = spawn_food()
    else:
        del snake_body[0]
    game_screen.fill((0, 0, 0))
    pygame.draw.rect(game_screen, (0, 255, 0), [food_x, food_y, 10, 10])
    for (x, y) in snake_body:
        pygame.draw.rect(game_screen, (255, 255, 255), [x, y, 10, 10])
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    game_screen.blit(score_text, [10, 10])
    pygame.display.update()

def game_over():
    game_screen.fill((0, 0, 0))
    game_over_text = font.render("GAME OVER", True, (255, 0, 0))
    final_score_text = font.render("Final Score: " + str(score), True, (255, 255, 255))
    game_screen.blit(game_over_text, [width // 3, height // 3])
    game_screen.blit(final_score_text, [width // 3, height // 2])
    pygame.display.update()
    time.sleep(3)
    pygame.quit()
    quit()

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and change_x == 0:
                change_x = -10
                change_y = 0
            elif event.key == pygame.K_RIGHT and change_x == 0:
                change_x = 10
                change_y = 0
            elif event.key == pygame.K_UP and change_y == 0:
                change_x = 0
                change_y = -10
            elif event.key == pygame.K_DOWN and change_y == 0:
                change_x = 0
                change_y = 10

    display_snake()
    clock.tick(10)

pygame.quit()
quit()
