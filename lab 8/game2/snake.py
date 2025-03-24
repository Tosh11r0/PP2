import pygame
import random

# Размер клетки
size = 30
half_size = size // 2

# Разрешение игрового поля, округляем к ближайшему кратному size*2
res = 750
res = res // size // 2 * 2 * size

# Начальная позиция змейки
snake_start_pos = res // 2


# Длина начальной змейки
length = 4

# Начальное тело змейки (список координат)
snake = [(snake_start_pos, snake_start_pos)]

# Начальное направление движения
dx, dy = size, 0  # идёт вправо

# Создание экрана
pygame.init()
screen = pygame.display.set_mode((res, res))
clock = pygame.time.Clock()

# Случайная позиция яблока (кратная size)
apple = (random.randrange(0, res, size), random.randrange(0, res, size))

# Игровой цикл
is_running = True
while is_running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    # Обработка нажатий клавиш
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and dy == 0:
        dx, dy = 0, -size
    elif keys[pygame.K_DOWN] and dy == 0:
        dx, dy = 0, size
    elif keys[pygame.K_LEFT] and dx == 0:
        dx, dy = -size, 0
    elif keys[pygame.K_RIGHT] and dx == 0:
        dx, dy = size, 0

    # Получаем текущую голову и создаём новую
    head_x, head_y = snake[-1]
    new_head = (head_x + dx, head_y + dy)
    snake.append(new_head)

    # Удаляем хвост, если длина змейки не увеличивается
    if len(snake) > length:
        del snake[0]

    # Проверка на поедание яблока
    if new_head == apple:
        length += 1
        while True:
            apple = (random.randrange(0, res, size), random.randrange(0, res, size))
            if apple not in snake:
                break

    # Проверка на столкновение со стенами
    if not (0 <= new_head[0] < res and 0 <= new_head[1] < res):
        is_running = False

    # Проверка на столкновение с собой
    if len(snake) != len(set(snake)):
        is_running = False

    # Отрисовка
    screen.fill((0, 0, 0))  # чёрный фон

    # Отрисовка тела змейки
    [pygame.draw.rect(screen, (0, 255, 0), (x, y, size, size)) for x, y in snake]

    # ✅ Яблоко теперь рисуется как квадрат — точно по сетке!
    pygame.draw.rect(screen, (255, 0, 0), (apple[0], apple[1], size, size))

    # Обновление экрана
    pygame.display.flip()
    clock.tick(10)  # скорость: 10 кадров в секунду

pygame.quit()
