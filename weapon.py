import pygame
import color

bullets = pygame.sprite.Group()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, speed):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y

        self.width = 3
        self.height = 3

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(color.white)

        self.move_x = 0
        self.move_y = 0

        self.speed = speed

        if direction == 'up':
            self.move_y = -self.speed
        elif direction == 'down':
            self.move_y = self.speed
        elif direction == 'left':
            self.move_x = -self.speed
        elif direction == 'right':
            self.move_x = self.speed

        self.rect = (self.x, self.y)

    def update(self):
        self.x += self.move_x
        self.y += self.move_y

        self.rect = (self.x, self.y)

    