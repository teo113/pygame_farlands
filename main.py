import pygame
from pygame.locals import *
from pygame import mixer
import random
import sys

pygame.init()

display = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# player assets
player_walk_images = [
    pygame.image.load("assets/player_stand_left_x1.png"),
    pygame.image.load("assets/player_walk_left_x1.png")
    ]

# player class
class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.moving_left = False
        self.moving_right = False
    def main(self, display):
        #pygame.draw.rect(display, (255, 0, 0), (self.x, self.y, self.width, self.height))
        if self.moving_left:
            display.blit(pygame.transform.scale(player_walk_images[0],(64, 64)), (self.x, self.y))
        elif self.moving_right:
            display.blit(pygame.transform.scale(pygame.transform.flip(player_walk_images[0], True, False), (64, 64)), (self.x, self.y))
        else:
            display.blit(pygame.transform.scale(player_walk_images[0],(64, 64)), (self.x, self.y))

        self.moving_left = False
        self.moving_right = False

# player position
player = Player(400, 300, 32, 32)

display_scroll = [0,0]

while True:
    #display.fill((77, 128, 77))
    display.fill((115, 154, 119))  # grass coloured background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.QUIT
    
    keys = pygame.key.get_pressed()

    # start location objects
    #pygame.draw.rect(display, (255,255,255), (100-display_scroll[0], 100-display_scroll[1], 16, 16))
    display.blit(pygame.transform.scale(pygame.image.load("assets/tree1_x1.png"),(192, 192)), (100-display_scroll[0], 100-display_scroll[1], 16, 16))
    display.blit(pygame.transform.scale(pygame.image.load("assets/ruins_x1.png"),(192, 192)), (500-display_scroll[0], 350-display_scroll[1], 16, 16))
    display.blit(pygame.transform.scale(pygame.image.load("assets/bush1_x1.png"),(128, 128)), (425-display_scroll[0], 475-display_scroll[1], 16, 16))
    display.blit(pygame.transform.scale(pygame.image.load("assets/horse1_saddled_feeding0_x1.png"),(192, 136)), (650-display_scroll[0], 550-display_scroll[1], 24, 17))

    # initialize font
    myfont = pygame.font.SysFont("monospace", 10)

    # render text
    label = myfont.render("You arrive weary after a long journey... Your horse senses danger and refuses to carry on...", 1, (255,255,255))
    display.blit(label, (10, 550))

    # map movement keys to display movement
    if keys[pygame.K_a]:
        display_scroll[0] -= 5
        player.moving_left = True
    if keys[pygame.K_d]:
        display_scroll[0] += 5
        player.moving_right = True
    if keys[pygame.K_w]:
        display_scroll[1] -= 5
    if keys[pygame.K_s]:
        display_scroll[1] += 5

    player.main(display)

    clock.tick(60)
    pygame.display.update()
