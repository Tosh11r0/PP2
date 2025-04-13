import pygame
import random

size = 30
half_size = size // 2

res = 750
res = res // size // 2 * 2 * size

snake_start_pos = res // 2
length = 4
snake = [(snake_start_pos, snake_start_pos)]
dx, dy = size, 0

pygame.init()
screen = pygame.display.set_mode((res, res))
clock = pygame.time.Clock()

apple = (random.randrange(0, res, size), random.randrange(0, res, size))

score = 0
font = pygame.font.Font(None, 36)

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and dy == 0:
        dx, dy = 0, -size
    elif keys[pygame.K_DOWN] and dy == 0:
        dx, dy = 0, size
    elif keys[pygame.K_LEFT] and dx == 0:
        dx, dy = -size, 0
    elif keys[pygame.K_RIGHT] and dx == 0:
        dx, dy = size, 0

    head_x, head_y = snake[-1]
    new_head = (head_x + dx, head_y + dy)
    new_head = (new_head[0] % res, new_head[1] % res)
    snake.append(new_head)

    if len(snake) > length:
        del snake[0]

    if new_head == apple:
        length += 1
        score += 1
        while True:
            apple = (random.randrange(0, res, size), random.randrange(0, res, size))
            if apple not in snake:
                break

    if len(snake) != len(set(snake)):
        is_running = False

    screen.fill((0, 0, 0))
    [pygame.draw.rect(screen, (0, 255, 0), (x, y, size, size)) for x, y in snake]
    pygame.draw.rect(screen, (255, 0, 0), (apple[0], apple[1], size, size))
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
