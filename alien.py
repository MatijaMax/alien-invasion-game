import pygame
from pygame.sprite import Sprite
import random

class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()

        #init alien
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #load image
        #easter egg randomizer
        if (random.randint(1, 100) == 1):
            if (random.randint(1, 2) == 1):
                self.image = pygame.image.load('images/bill_cipher.png')
                self.image = pygame.transform.scale(self.image, (59, 89))
            else:
                self.image = pygame.image.load('images/easter_egg.png')
                self.image = pygame.transform.scale(self.image, (59, 89))

        else:
            self.image = pygame.image.load('images/invader.png')
            self.image = pygame.transform.scale(self.image, (69, 48)) 
        # self.image = pygame.image.load('images/easter_egg.png')
        # self.image = pygame.transform.scale(self.image, (149, 158))  
        # self.image = pygame.transform.scale(self.image, (89, 68)) 
        self.image = pygame.transform.scale(self.image, (69, 48)) 
        self.image.set_colorkey((0, 0, 0))  # Set black color as transparent
        self.rect = self.image.get_rect()

        #store horizontal
        self.x = float(self.rect.x)


    def update(self):
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
    