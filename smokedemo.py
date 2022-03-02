import pygame
import random


width = 800
height = 900

screen = pygame.display.set_mode((width,height))

clock = pygame.time.Clock()
FPS = 60


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
        pygame.display.update()
        clock.tick(FPS)


main_game()
