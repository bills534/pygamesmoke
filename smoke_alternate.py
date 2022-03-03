import pygame
import random
import math


width = 800
height = 900
spawn_x = width // 2
spawn_y = height // 2
rotation_speed = 5
starting_velocity = 2

screen = pygame.display.set_mode((width,height))

clock = pygame.time.Clock()
FPS = 60


def scale(img: pygame.Surface, factor):
    w, h = img.get_width() * factor, img.get_height() * factor
    return pygame.transform.scale(img, (int(w), int(h)))


IMAGE = pygame.image.load('cloudsmall.png').convert_alpha()

class Particle:
    def __init__(self, x=spawn_x, y=spawn_y, angle=0, velocity=2):
        self.x = x
        self.y = y
        self.scale_k = 0.1
        self.img = scale(IMAGE, self.scale_k)
        self.alpha = 255
        self.alpha_decay_rate = 3
        self.alive = True

        self.angle = angle
        self.velocity = velocity
        self.vx = 0
        self.vy = 0
        self.velocity_decay = 0.1
    

    def update(self):
        # setting the inital velocity of the particle
        self.x += self.vx
        self.y -= self.vy
        # then updating the horizontal\vertical velocity using trigonometry
        self.vx += math.cos(math.radians(self.angle)) * self.velocity
        self.vy += math.sin(math.radians(self.angle)) * self.velocity

        self.velocity *= self.velocity_decay

        self.scale_k += 0.005
        self.alpha -= self.alpha_decay_rate
        if self.alpha < 0:
            self.alpha = 0
            self.alive = False
        self.alpha_decay_rate -= 0.1
        if self.alpha_decay_rate < 1.5:
            self.alpha_decay_rate = 1.5
        self.img = scale(IMAGE, self.scale_k)
        self.img.set_alpha(self.alpha)


    def draw(self):
        screen.blit(self.img, self.img.get_rect(center=(self.x, self.y)))


class Smoke:
    def __init__(self, x = spawn_x, y = spawn_y, rotation_speed=rotation_speed, starting_v=starting_velocity):
        self.x = x
        self.y = y
        self.particles = []
        self.frames = 0
        self.particle_count = 0
        self.angle = 0
        self.rotation_speed = rotation_speed
        self.starting_v = starting_v
        self.dx = 0
        self.dy = 0

    def update(self):
        # removing dead particles from the particle list
        self.particles = [i for i in self.particles if i.alive]
        self.partical_count = len(self.particles)
        self.frames += 1
        if self.frames % 2 ==0:
            self.frames = 0
            self.particles.append(Particle(self.x, self.y, self.angle, self.starting_v))
            self.angle += self.rotation_speed
            # this is just for me to display the x and y velocity for fun
            self.dx = round(math.cos(math.radians(self.angle)) * self.starting_v, 2)
            self.dy = round(math.sin(math.radians(self.angle)) * self.starting_v, 2)

        for i in self.particles:
            i.update()
            

    def draw(self):
        for i in self.particles:
            i.draw()


def main_game():

    smoke = Smoke()

    set_vel = starting_velocity

    while True:

        # indirectly updating the partical starting velocity for smoother looking transitions
        if set_vel > smoke.starting_v:
            smoke.starting_v += 0.01
        if set_vel < smoke.starting_v:
            smoke.starting_v -= 0.01
        
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                quit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    quit()
                if e.key == pygame.K_LEFT:
                    smoke.rotation_speed += 0.33
                if e.key == pygame.K_RIGHT:
                    smoke.rotation_speed -= 0.33
                # velocity setting is indirectly updated for smoothness
                if e.key == pygame.K_UP:
                    set_vel += 0.5
                if e.key == pygame.K_DOWN:
                    set_vel -= 0.5
        
        screen.fill((0,0,0))
        smoke.update()
        smoke.draw()
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption(f'FPS = {round(clock.get_fps())} | Particle Count = {smoke.partical_count} | X/Y: {smoke.dx}/{smoke.dy}')


main_game()
