import math
import pygame

angle = math.radians(0)
velocity = 10

yvel = math.sin(angle) * velocity
xvel = math.cos(angle) * velocity

print(f'x: {xvel} y:{yvel}')

print(f'{360 // 5}')

# print(pygame.font.get_fonts())