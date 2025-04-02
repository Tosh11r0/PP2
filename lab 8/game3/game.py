import pygame as pygame  # Импортируем библиотеку pygame

pygame.init()  # Инициализируем все модули pygame
FPS = 120  # Частота кадров (максимум 120 кадров в секунду)
FramePerSec = pygame.time.Clock()  # Объект для управления временем

#Keys:
# "1" - draw  # Клавиша 1 — рисование
# "2" - delete  # Клавиша 2 — удаление (стиратель)

#font
font = pygame.font.Font(None,26)  # Шрифт по умолчанию, размер 26

#COLORS
RED = (255,0,0)  # Красный
GREEN = (0,255,0)  # Зелёный
BLUE = (0,0,255)  # Синий
WHITE = (255,255,255)  # Белый
BLACK = (0,0,0)  # Чёрный

#Screen
WIDTH, HEIGHT = 700,700  # Размер окна (ширина, высота)
screen = pygame.display.set_mode((WIDTH,HEIGHT))  # Создаём окно с заданными размерами
pygame.display.set_caption("Paint")  # Устанавливаем заголовок окна

#Pencil
radius = 5  # Радиус кисти
mouse_x = WIDTH/2  # Начальная позиция мыши по X (центр экрана)
mouse_y = HEIGHT/2  # Начальная позиция мыши по Y (центр экрана)
color = RED  # Цвет кисти по умолчанию — красный

#position
positions_draw = []  # Список для хранения позиций и цветов нарисованных точек

trace = False  # Отслеживает, зажата ли кнопка мыши
draw = False  # Режим рисования (True) или стирания (False)
RUN = True  # Основной флаг для цикла игры
while RUN:
    screen.fill(WHITE)  # Очищаем экран (заливка белым)

    for event in pygame.event.get():  # Обработка событий
        if event.type == pygame.QUIT:  # Если нажали на крестик окна
            RUN = False  # Завершаем цикл

        if event.type == pygame.MOUSEMOTION:  # Если двигаем мышь
            mouse_x, mouse_y = pygame.mouse.get_pos()  # Получаем текущую позицию мыши

        #CHECK on press mouse's keys:
        if event.type == pygame.MOUSEBUTTONDOWN:  # Если нажата кнопка мыши
            trace = True  # Включаем отслеживание
            mouse_x, mouse_y = pygame.mouse.get_pos()  # Обновляем координаты мыши
        if event.type == pygame.MOUSEBUTTONUP:  # Если отпущена кнопка мыши
            trace = False  # Отключаем отслеживание

        #Check on click keyboard's keys:
        if event.type == pygame.KEYDOWN:  # Если нажата клавиша на клавиатуре
            if event.key == pygame.K_w and radius < 50:  # Если нажата W и радиус меньше 50
                radius += 5  # Увеличиваем радиус
            if event.key == pygame.K_s and radius > 5:  # Если нажата S и радиус больше 5
                radius -= 5  # Уменьшаем радиус

            #change color:
            if event.key == pygame.K_r:  # Если нажата R
                color = RED  # Меняем цвет на красный
            if event.key == pygame.K_g:  # Если нажата G
                color = GREEN  # Меняем цвет на зелёный
            if event.key == pygame.K_b:  # Если нажата B
                color = BLUE  # Меняем цвет на синий

            if event.key == pygame.K_1:  # Если нажата клавиша 1
                draw = True  # Включаем режим рисования
            if event.key == pygame.K_2:  # Если нажата клавиша 2
                draw = False  # Включаем режим стирания (удаления)

    if draw:  # Если режим рисования включён
        if trace:  # И если мышь нажата
            positions_draw.append((mouse_x,mouse_y,color))  # Добавляем точку с цветом в список
    else:  # Если режим удаления
        if trace:  # И если мышь нажата
            positions_draw.append((mouse_x,mouse_y,WHITE))  # Добавляем точку с белым цветом (стиратель)

    for x,y,c in positions_draw:  # Проходимся по всем точкам
        pygame.draw.circle(screen,c,(x,y), radius)  # Рисуем окружность в нужной позиции и цвете

    # Отображение текста с подсказками
    text1 = font.render("1-draw", True,BLACK)  # Текст про рисование
    text2 = font.render("2-remove", True,BLACK)  # Текст про удаление
    textr = font.render("r-red", True,BLACK)  # Текст про красный цвет
    textg = font.render("g-green", True,BLACK)  # Текст про зелёный цвет
    textb = font.render("b-blue", True,BLACK)  # Текст про синий цвет
    text_rb = font.render("w-radius+", True,BLACK)  # Текст про увеличение радиуса
    text_rl = font.render("s-radius-", True,BLACK)  # Текст про уменьшение радиуса

    screen.blit(text1, (10,10))  # Вывод текста на экран
    screen.blit(text2, (10,30))
    screen.blit(textr, (10,50))
    screen.blit(textg, (10,70))
    screen.blit(textb, (10,90))
    screen.blit(text_rb, (600,10))
    screen.blit(text_rl, (600,30))

    pygame.display.flip()  # Обновление экрана
    pygame.display.update()  # Альтернативное обновление экрана (необязательно обе)
    FramePerSec.tick(FPS)  # Ограничение частоты кадров

pygame.quit()  # Завершение работы pygame
