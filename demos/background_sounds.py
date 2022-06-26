import pygame
from pygame.locals import *
from pygame import mixer

pygame.init()

# clock
clock = pygame.time.Clock()

# display window
win_width = 800
win_height = 600
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Sound test")

# colours
GREEN = (111, 115, 100)

# sound mixer
mixer.init()
#mixer.music.load('demos/background_rain_thunder_128kbps_32000hz.ogg')
#mixer.music.load('demos/background_ominous_boom_128kbps_32000hz.ogg')
mixer.music.load('demos/Adrian von Ziegler - Moonsong.ogg')
mixer.music.set_volume(0.3)
mixer.music.play(loops = -1)

pygame.mixer.Channel(0).play(pygame.mixer.Sound('demos/background_rain_thunder_128kbps_32000hz.ogg'), loops = -1)
pygame.mixer.Channel(1).play(pygame.mixer.Sound('demos/background_ominous_boom_128kbps_32000hz.ogg'), loops = -1)

# main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    # update

    
    win.fill(GREEN)
    pygame.display.flip()
    clock.tick(60)