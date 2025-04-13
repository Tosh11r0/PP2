import pygame
import datetime

pygame.init()

WIDTH, HEIGHT = 900, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.image.load(r"lab7\first_game\clock.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
pygame.display.set_caption("First game")

ar_min = pygame.image.load(r"lab7\first_game\min_hand.png")
ar_min = pygame.transform.scale(ar_min, (100, 400))
ar_sec = pygame.image.load(r"lab7\first_game\sec_hand.png")
ar_sec = pygame.transform.scale(ar_sec, (100, 400))

Center = (WIDTH // 2, HEIGHT // 2)

def rotate_and_blit(image, angle, center):
    rotated_image = pygame.transform.rotate(image, angle)
    rect = rotated_image.get_rect(center=center)
    screen.blit(rotated_image, rect.topleft)

clock = pygame.time.Clock()
RUN = True

while RUN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

    screen.blit(background, (0, 0))

    now = datetime.datetime.now()
    minutes, seconds = now.minute, now.second
    sec_angle = -seconds * 6
    min_angle = -(minutes * 6 + seconds * 0.1)

    rotate_and_blit(ar_min, min_angle, Center)
    rotate_and_blit(ar_sec, sec_angle, Center)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
