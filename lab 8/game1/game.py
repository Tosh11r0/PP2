from random import *
import pygame, sys
from pygame.locals import *
import random

pygame.init()
FPS = 60
FramePerSec = pygame.time.Clock()

WIDTH, HIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HIGHT))
background = pygame.image.load(r"D:\PP2\lab 8\game1\road.jpg")
background = pygame.transform.scale(background, (WIDTH, HIGHT))
pygame.display.set_caption("Race")

font = pygame.font.Font(None, 36)

face_w, face_h = 150, 200
face = pygame.image.load(r"D:\PP2\lab 8\game1\face.png")
face = pygame.transform.scale(face, (face_w, face_h))
step_face = 10
face_x = 350
face_y = 600

gem_w, gem_h = 100, 100
gem = pygame.image.load(r"D:\PP2\lab 8\game1\gem.png")
gem = pygame.transform.scale(gem, (gem_w, gem_h))
step_gem = 10
gem_exist = False
score = 0

object_w, object_h = 150, 150
object = pygame.image.load(r"D:\PP2\lab 8\game1\rock.png")
object = pygame.transform.scale(object, (object_w, object_h))
step_object = 10
object_exist = False

def reset_game():
    global object_spawn_x, object_spawn_y
    object_spawn_x, object_spawn_y = randint(20, WIDTH - 20), -10
    object_exist = True

RUN = True
while RUN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

    keys = pygame.key.get_pressed()
    if keys[K_LEFT] and face_x > step_face:
        face_x -= step_face
    if keys[K_RIGHT] and face_x < WIDTH - (step_face + face_w):
        face_x += step_face

    if not object_exist:
        object_spawn_x, object_spawn_y = randint(20, WIDTH - object_w), -10
        object_exist = True

    if not gem_exist:
        gem_xy = [randint(20, WIDTH - object_w), -10]
        gem_exist = True

    if gem_exist:
        gem_xy[1] += step_gem
        if gem_xy[1] >= HIGHT:
            gem_exist = False

    if object_exist:
        object_spawn_y += step_object
        if object_spawn_y >= HIGHT:
            object_exist = False

    screen.blit(background, (0, 0))
    screen.blit(face, (face_x, face_y))
    screen.blit(gem, (gem_xy))
    screen.blit(object, (object_spawn_x, object_spawn_y))

    if (object_spawn_y >= face_y - (face_h // 2) + (face_h // 4)) and (face_x - face_h // 2 < object_spawn_x < face_x + face_h // 2):
        print("СТОЛКНОВЕНИЕ")
        screen.fill((255, 0, 0))
        text_game_over = font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(text_game_over, (350, 400))
        score = 0
        pygame.display.flip()
        pygame.time.wait(3000)
        object_exist = False
        gem_exist = False
        continue

    if (gem_xy[1] >= face_y + (face_h // 4)) and (face_x - face_h // 2 < gem_xy[0] < face_x + face_h // 2):
        gem_exist = False
        score += 5

    text_score = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text_score, (50, 50))

    pygame.display.flip()
    pygame.display.update()
    FramePerSec.tick(FPS)

pygame.quit()
