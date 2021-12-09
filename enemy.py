import pygame
import color
import random

enemies = pygame.sprite.Group()

class Chaser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y

        self.width = 30
        self.height = 30

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(color.red)

        self.rect = (self.x, self.y)

        self.move_x = 0
        self.move_y = 0

        self.speed = 2

    def update(self, events, player):
        self.x += self.move_x
        self.y += self.move_y

        self.rect = (self.x, self.y)

        self.chasePlayer(player)
    
    def chasePlayer(self, player):
        if player.x + (player.width / 2) + (self.speed * 2) < self.x + (self.width / 2):
            self.move_x = -self.speed
        elif player.x + (player.width / 2) - (self.speed * 2) > self.x + (self.width / 2):
            self.move_x = self.speed
        else:
            self.move_x = 0

        if player.y + (player.height / 2) + (self.speed * 2) < self.y + (self.height / 2):
            self.move_y = -self.speed
        elif player.y + (player.height / 2) + (self.speed * 2) > self.y + (self.height / 2):
            self.move_y = self.speed
        else:
            self.move_y = 0

def spawnChaser(count):
    for c in range(count):
        c = Chaser(random.randint(100, 900), random.randint(100, 700))
        enemies.add(c)