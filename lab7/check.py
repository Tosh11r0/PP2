import pygame
pygame.init()

running = True
clock = pygame.time.Clock()
screen = pygame.display.set_mode((780, 680))

# Цвета
Black = (0, 0, 0)
White = (255, 255, 255)

# Шрифт
font = pygame.font.Font(None, 40)

# Переменная для текста
text1 = None

while running:
    screen.fill(White)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                text1 = font.render("Hello", True, Black)  # создаём текст при нажатии W

    if text1:
        screen.blit(text1, (200, 200))  # отображаем текст на экране
    pygame.draw.circle(screen, (0, 255, 0), (100, 100), 50)

    pygame.display.flip()
    clock.tick(60)
