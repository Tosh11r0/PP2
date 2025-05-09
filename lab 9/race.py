import pygame
import random
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GOLD = (255, 215, 0)
RED = (255, 0, 0)

player_width = 50
player_height = 50
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 5

coin_radius = 1
coin_weight = random.randint(1, 5)
if (coin_weight <=3):
    coin_radius = 5
elif (coin_weight > 3):
    coin_radius = 15

coin_x = random.randint(coin_radius, WIDTH - coin_radius)
coin_y = -coin_radius  # монетка начинается сверху за пределами экрана

coin_speed = 3  # скорость падения монеты

enemy_width = 50
enemy_height = 50
enemy_x = random.randint(0, WIDTH - enemy_width)
enemy_y = 0
enemy_speed = 2

score = 0
coins_collected = 0
N = 5

font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()

def draw_player(x, y):
    pygame.draw.rect(screen, GREEN, (x, y, player_width, player_height))

def draw_coin(x, y, weight):
    pygame.draw.circle(screen, GOLD, (x, y), coin_radius)
    weight_text = font.render(f"W:{weight}", True, BLACK)
    text_rect = weight_text.get_rect(center=(x, y))
    screen.blit(weight_text, text_rect)

def draw_enemy(x, y):
    pygame.draw.rect(screen, RED, (x, y, enemy_width, enemy_height))

def show_score(score):
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (WIDTH - 150, 10))

def show_coins_collected(coins_collected):
    coins_text = font.render(f"Coins: {coins_collected}", True, BLACK)
    screen.blit(coins_text, (10, 10))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()






    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < HEIGHT - player_height:
        player_y += player_speed

    
    coin_y += coin_speed

    
    if (player_x < coin_x + coin_radius and player_x + player_width > coin_x - coin_radius and
        player_y < coin_y + coin_radius and player_y + player_height > coin_y - coin_radius):
        score += coin_weight
        coins_collected += 1
        coin_x = random.randint(coin_radius, WIDTH - coin_radius)
        coin_y = -coin_radius
        coin_weight = random.randint(1, 5)
        if (coin_weight <=3):
            coin_radius = 5
        elif (coin_weight > 3):
            coin_radius = 15


    if coin_y > HEIGHT:
        coin_x = random.randint(coin_radius, WIDTH - coin_radius)
        coin_y = -coin_radius
        coin_weight = random.randint(1, 5)

    if coins_collected >= N:
        enemy_speed = 4

    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = 0
        enemy_x = random.randint(0, WIDTH - enemy_width)

    if (player_x < enemy_x + enemy_width and player_x + player_width > enemy_x and
        player_y < enemy_y + enemy_height and player_y + player_height > enemy_y):
        pygame.quit()
        sys.exit()

    screen.fill(WHITE)
    draw_player(player_x, player_y)
    draw_coin(coin_x, coin_y, coin_weight)
    draw_enemy(enemy_x, enemy_y)
    show_score(score)
    show_coins_collected(coins_collected)
    pygame.display.update()
    clock.tick(60)
