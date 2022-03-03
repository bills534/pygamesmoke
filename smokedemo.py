import pygame
import random


width = 800
height = 900
spawn_x = width // 2
spawn_y = height // 2 + 200

screen = pygame.display.set_mode((width,height))

clock = pygame.time.Clock()
FPS = 60


def scale(img: pygame.Surface, factor):
    w, h = img.get_width() * factor, img.get_height() * factor
    return pygame.transform.scale(img, (int(w), int(h)))


IMAGE = pygame.image.load('cloudsmall.png').convert_alpha()

class SmokeParticle:
    def __init__(self, x=spawn_x, y=spawn_y):
        self.x = x
        self.y = y
        self.scale_k = 0.1
        self.img = scale(IMAGE, self.scale_k)
        self.alpha = 255
        self.alpha_decay_rate = 3
        self.alive = True
        self.vx = 0
        self.vy = 4 + (random.randint(7,10) / 10)
        self.horizontal_velocity = 0.01 * random.random() * random.choice([-1,1])
        self.vertical_decay = 0.99
        if self.alpha < 0.5:
            self.alpha = 0
            self.alive = False

    def update(self):
        # setting the inital velocity of the particle
        self.x += self.vx
        self.y -= self.vy
        # then updating the horizontal\vertical velocity to it
        self.vx += self.horizontal_velocity
        self.vy *= self.vertical_decay

        self.scale_k += 0.005
        self.alpha -= self.alpha_decay_rate
        self.alpha_decay_rate -= 0.1
        if self.alpha_decay_rate < 1.5:
            self.alpha_decay_rate = 1.5
        self.img = scale(IMAGE, self.scale_k)
        self.img.set_alpha(self.alpha)


    def draw(self):
        screen.blit(self.img, self.img.get_rect(center=(self.x, self.y)))


class Smoke:
    def __init__(self, x = spawn_x, y = spawn_y):
        self.x = x
        self.y = y
        self.particles = []
        self.frames = 0
        self.particle_count = 0

    def update(self):
        # removing dead particles from the particle list
        self.particles = [i for i in self.particles if i.alpha > 0.5]
        self.partical_count = len(self.particles)
        self.frames += 1
        if self.frames % 3 ==0:
            self.frames = 0
            self.particles.append(SmokeParticle(self.x, self.y))

        for i in self.particles:
            i.update()
            

    def draw(self):
        for i in self.particles:
            i.draw()



smoke = Smoke()


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
        smoke.update()
        smoke.draw()
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption(f'FPS = {round(clock.get_fps(), 2)}: P = {smoke.partical_count}')


main_game()
