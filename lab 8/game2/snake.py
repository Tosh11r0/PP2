import pygame  # Импортируем библиотеку pygame для создания игры
import random  # Импортируем random для генерации случайных координат яблока

# Размер одной клетки (один шаг змейки)
size = 30
half_size = size // 2  # Половина размера клетки (можно использовать для центрирования)

# Размер окна (игрового поля), округляется до ближайшего кратного двойному size
res = 750
res = res // size // 2 * 2 * size  # Гарантируем, что размер поля делится на size*2

# Начальная позиция змейки (по центру экрана)
snake_start_pos = res // 2

# Начальная длина змейки
length = 4

# Список координат змейки, начинается с одной клетки в центре
snake = [(snake_start_pos, snake_start_pos)]

# Начальное направление движения: вправо
dx, dy = size, 0

# Создание игрового окна
pygame.init()
screen = pygame.display.set_mode((res, res))  # Устанавливаем размеры окна
clock = pygame.time.Clock()  # Таймер для регулировки FPS

# Генерируем случайную позицию яблока (координаты кратны size, чтобы совпадали с сеткой)
apple = (random.randrange(0, res, size), random.randrange(0, res, size))

# Основной игровой цикл
is_running = True
while is_running:
    # Обработка событий (например, закрытие окна)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False  # Завершаем игру

    # Обработка клавиш для управления направлением змейки
    keys = pygame.key.get_pressed()  # Получаем список нажатых клавиш
    if keys[pygame.K_UP] and dy == 0:  # Вверх, если не идём уже вверх/вниз
        dx, dy = 0, -size
    elif keys[pygame.K_DOWN] and dy == 0:  # Вниз
        dx, dy = 0, size
    elif keys[pygame.K_LEFT] and dx == 0:  # Влево
        dx, dy = -size, 0
    elif keys[pygame.K_RIGHT] and dx == 0:  # Вправо
        dx, dy = size, 0

    # Получаем координаты головы змейки
    head_x, head_y = snake[-1]
    # Вычисляем новые координаты головы
    new_head = (head_x + dx, head_y + dy)
    # Добавляем новую голову в список змейки
    snake.append(new_head)

    # Если змейка не съела яблоко — удаляем хвост
    if len(snake) > length:
        del snake[0]

    # Проверка: съела ли змейка яблоко?
    if new_head == apple:
        length += 1  # Увеличиваем длину змейки
        while True:
            # Генерируем новую позицию яблока
            apple = (random.randrange(0, res, size), random.randrange(0, res, size))
            if apple not in snake:  # Убедимся, что яблоко не появляется внутри змейки
                break

    # Проверка: врезалась ли змейка в стену?
    if not (0 <= new_head[0] < res and 0 <= new_head[1] < res):
        is_running = False  # Игра закончена

    # Проверка: столкнулась ли змейка с самой собой?
    if len(snake) != len(set(snake)):  # Если в списке змейки есть дубликаты
        is_running = False  # Игра закончена

    # Отрисовка
    screen.fill((0, 0, 0))  # Заливаем фон чёрным

    # Рисуем каждую часть тела змейки
    [pygame.draw.rect(screen, (0, 255, 0), (x, y, size, size)) for x, y in snake]

    # Рисуем яблоко — красный квадрат на позиции яблока
    pygame.draw.rect(screen, (255, 0, 0), (apple[0], apple[1], size, size))

    # Обновляем экран
    pygame.display.flip()
    clock.tick(10)  # Частота кадров: 10 FPS

# Выход из pygame
pygame.quit()
