import pygame
import os

pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Second game") #создаем экран для проигрвыателя

WHITE = (255, 255, 255)
font = pygame.font.Font(None, 36) #дефолт дизайн для кнопок

music_folder = r"lab7\second game" #путь к папке с музыкой
playlist = [os.path.join(music_folder, f) for f in os.listdir(music_folder) if f.endswith('.mp3')] # список всех .mp3 файлов в папке.
current_track = 0

pygame.mixer.init()

def play_track(index):  #загружает и начинает воспроизводить трек с заданным индексом.
    pygame.mixer.music.load(playlist[index])
    pygame.mixer.music.play()

def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    play_track(current_track)

def previous_track():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    play_track(current_track)

# Круглые кнопки
button_radius = 40
play_center = (WIDTH // 2, HEIGHT // 2 + 20)
stop_center = (WIDTH // 2, HEIGHT // 2 + 110)
previous_center = (WIDTH // 2 - 150, HEIGHT // 2 + 65)
next_center = (WIDTH // 2 + 150, HEIGHT // 2 + 65)

RUNNING = True
play_track(current_track)

while RUNNING:
    screen.fill(WHITE)

    pygame.draw.rect(screen, (133, 153, 133), pygame.Rect(100, 100, 600, 400))
    pygame.draw.rect(screen, (89, 89, 89), pygame.Rect(110, 110, 580, 380))

    buttons = [(play_center, 'Play'), (stop_center, 'Stop'),
               (previous_center, 'Previous'), (next_center, 'Next')]

    for center, label in buttons:
        pygame.draw.circle(screen, (0, 0, 0), center, button_radius + 3)
        pygame.draw.circle(screen, (171, 171, 171), center, button_radius)
        text = font.render(label, True, WHITE)
        text_rect = text.get_rect(center=center)
        screen.blit(text, text_rect)

    current_song = os.path.basename(playlist[current_track]).replace('.mp3', '')
    song_text = font.render(current_song, True, WHITE)
    song_rect = song_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(song_text, song_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if (pygame.math.Vector2(event.pos) - play_center).length() <= button_radius:
                pygame.mixer.music.unpause()
            if (pygame.math.Vector2(event.pos) - stop_center).length() <= button_radius:
                pygame.mixer.music.pause()
            if (pygame.math.Vector2(event.pos) - previous_center).length() <= button_radius:
                previous_track()
            if (pygame.math.Vector2(event.pos) - next_center).length() <= button_radius:
                next_track()

    pygame.display.flip()

pygame.quit()
