import pygame
import sys


def load_map(path):
    f = open(path + ".txt", "r")
    data = f.read()
    f.close()
    data = data.split("\n")
    mapa_jogo = []
    for row in data:
        mapa_jogo.append(list(row))
    return mapa_jogo


# main

pygame.init()
pygame.display.set_caption("test1")
main_map = load_map("map/main_map")

# main Variaveis

clock = pygame.time.Clock()
window_size = (700, 500)
screen = pygame.display.set_mode(window_size, 0, 32)
scroll = [0, 0]
display = pygame.Surface((350, 250))

# titulo

dirt1 = pygame.image.load("tiles/grass1.png")
water1 = pygame.image.load("tiles/grass.png")

# player

playerx = 350
playery = 350
player_image = pygame.transform.scale(pygame.image.load("player/player.png").convert_alpha(), (150, 150))
player_rect = player_image.get_rect(CENTER=(80, 50))

# button variables
move_right = False
move_left = False
move_up = False
move_down = False

game_map = load_map("map/main_map")

while True:
    screen.blit(player_image, [playerx, playery], player_rect)

    y = 0
    for layer in game_map:
        x = 0
        for tile in game_map:
            if tile == "G":
                display.blit(dirt1, (x * 16, y * 16))
            if tile == "W":
                display.blit(water1, (x * 16, y * 16))
            x += 1
        y += 1

    if move_right:
        playerx += 2
    if move_left:
        playerx -= 2
    if move_up:
        playery -= 2
    if move_down:
        playery += 2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                move_right = True
            if event.key == pygame.K_a:
                move_left = True
            if event.key == pygame.K_w:
                move_up = True
            if event.key == pygame.K_s:
                move_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                move_right = False
            if event.key == pygame.K_a:
                move_left = False
            if event.key == pygame.K_w:
                move_up = False
            if event.key == pygame.K_s:
                move_down = False

    screen.blit(pygame.transform.scale(display, window_size), (0, 0))
    pygame.display.update()
    clock.tick(120)
