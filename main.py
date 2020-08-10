import pygame
from player import Player, Platform


NAME = "PivoRun"
FPS = 30
group = pygame.sprite.Group()
platforms = []
P_WIDTH = 50
P_HEIGHT = 60

level = [
    '                ',
    '                ',
    '                ',
    '                ',
    '                ',
    '                ',
    '     _          ',
    '        _       ',
    '   __           ',
    ' __             '
]

pygame.init()
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption(NAME)
clock = pygame.time.Clock()

def create_platform(x, y):
    global platforms
    platform = Platform(x, y)
    group.add(platform)
    platforms.append(platform)

def create_lvl(level):
    global platforms
    platforms = []
    global group
    group.empty()
    group.add(player)
    x, y = P_WIDTH * -1, P_HEIGHT * -1
    for _ in range(18):
        create_platform(x, y)
        x += P_WIDTH
    y += P_HEIGHT
    for i in level:
        x = P_WIDTH * -1
        create_platform(x, y)
        x += P_WIDTH
        for j in i:
            if j == '_':
                create_platform(x, y)
            x += P_WIDTH
        create_platform(x, y)
        y += P_HEIGHT
    x = P_WIDTH * -1
    for _ in range(18):
        create_platform(x, y)
        x += P_WIDTH




player = Player(0, win)


while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            print(player.mspeed)
            exit()
    clock.tick(FPS)
    win.fill((255,255,255))
    create_lvl(level)
    player.update()
    player.collide(platforms)
    group.draw(win)

    pygame.display.update()
