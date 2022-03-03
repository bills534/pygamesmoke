import math

angle = math.radians(0)
velocity = 10

yvel = math.sin(angle) * velocity
xvel = math.cos(angle) * velocity

print(f'x: {xvel} y:{yvel}')