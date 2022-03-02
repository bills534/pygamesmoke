import pygame
import random


width = 800
height = 900

screen = pygame.display.set_mode((width,height))

clock = pygame.time.Clock()
FPS = 60

IMAGE = pygame.image.load('cloudsmall.png')


class SmokeParticle:
    def __init__(self, x=width//2, y=height//2):
        self.x = x
        self.y = y
        self.img = IMAGE

    def update(self):
        pass

    def draw(self):
        screen.blit(self.img, self.img.get_rect(center=(self.x, self.y)))


smoke_particle = SmokeParticle()


def main_game():
    while True:
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                quit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    quit()
        
        screen.fill((0,0,0))
        smoke_particle.update()
        smoke_particle.draw()
        pygame.display.update()
        clock.tick(FPS)


main_game()
