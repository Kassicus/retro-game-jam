import pygame
import color

class Player():
    def __init__(self):
        self.x = 500
        self.y = 400

        self.width = 25
        self.height = 25

        self.move_x = 0
        self.move_y = 0

        self.speed = 5

    def draw(self, surface):
        pygame.draw.rect(surface, color.green, (self.x, self.y, self.width, self.height))

    def update(self, events):
        self.x += self.move_x
        self.y += self.move_y

        self.eventHandler(events)

    def eventHandler(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.move_x = -self.speed
                if event.key == pygame.K_d:
                    self.move_x = self.speed

                if event.key == pygame.K_w:
                    self.move_y = -self.speed
                if event.key == pygame.K_s:
                    self.move_y = self.speed

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    self.move_x = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    self.move_y = 0