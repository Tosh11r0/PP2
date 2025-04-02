import pygame
import datetime

pygame.init()

WIDTH, HEIGHT = 900, 800 #ширина и высота экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #создаем сам экран

background = pygame.image.load(r"lab7\first_game\clock.png") #загружаем изображение часов
background = pygame.transform.scale(background, (WIDTH, HEIGHT)) #масштабирование
pygame.display.set_caption("First game") #команда для заголовка сверху экрана



ar_min = pygame.image.load(r"lab7\first_game\min_hand.png")#минутная стрелка
ar_min = pygame.transform.scale(ar_min, (100, 400))
ar_sec = pygame.image.load(r"lab7\first_game\sec_hand.png")#секундная стрелка
ar_sec = pygame.transform.scale(ar_sec, (100, 400))

Center = (WIDTH // 2, HEIGHT // 2) #устанавливаем точку центра экрана

def rotate_and_blit(image, angle, center): #функция для поворота стрелки
    rotated_image = pygame.transform.rotate(image, angle) #оворачивает картинку на нужный угол (в градусах, по часовой — отрицательно).
    rect = rotated_image.get_rect(center=center)# получаем прямоугольник, который оборачивает повернутое изображение, и выставляем его центр.
    screen.blit(rotated_image, rect.topleft) #отрисовываем изображение на экране по координатам.

clock = pygame.time.Clock()
RUN = True

while RUN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False #для закрытия окна игры

    screen.blit(background, (0, 0)) #Рисуем фон (часы без стрелок) в левом верхнем углу экрана.

    now = datetime.datetime.now()
    minutes, seconds = now.minute, now.second
    sec_angle = -seconds * 6  #Умножаем на -1, потому что rotate() поворачивает против часовой
    min_angle = -(minutes * 6 + seconds * 0.1)

    rotate_and_blit(ar_min, min_angle, Center)
    rotate_and_blit(ar_sec, sec_angle, Center)

    pygame.display.flip() # обновляет экран (то, что нарисовали, становится видимым).
    clock.tick(60)

pygame.quit()
