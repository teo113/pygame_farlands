import pygame
import random

pygame.init()

# clock
clock = pygame.time.Clock()

class Rain(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(rain_img, (16, 16))
        self.rect = self.image.get_rect()
        self.speedx = 3
        self.speedy = random.randint(5, 25)
        self.rect.x = random.randint(-100, win_width)
        self.rect.y = random.randint(-win_height, -5)
    
    def update(self):

        if self.rect.bottom > win_height:
            self.speedx = 3
            self.rect.x = random.randint(-100, win_width)
            self.rect.y = random.randint(-win_height, -5)
        
        self.rect.x = self.rect.x+self.speedx
        self.rect.y = self.rect.y+self.speedy

# colours
GREEN = (111, 115, 100)

# images
rain_img = pygame.image.load("demos/rain_drop_x1.png")

# set up window
win_width = 800
win_height = 600
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Rain test")

# create sprite group
rain_group = pygame.sprite.Group()

for i in range(100):
    rain = Rain()
    rain_group.add(rain)

# main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    # update
    rain_group.update()
    
    win.fill(GREEN)
    rain_group.draw(win)
    pygame.display.flip()
    clock.tick(60)

# quit
pygame.quit()
quit()