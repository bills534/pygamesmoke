import pygame
import random


width = 800
height = 900

screen = pygame.display.set_mode((width,height))

clock = pygame.time.Clock()
FPS = 60


def scale(img: pygame.Surface, factor):
    w, h = img.get_width() * factor, img.get_height() * factor
    return pygame.transform.scale(img, (int(w), int(h)))


IMAGE = pygame.image.load('cloudsmall.png')

class SmokeParticle:
    def __init__(self, x=width//2, y=height//2 + 200):
        self.x = x
        self.y = y
        self.scale_k = 0.1
        self.img = scale(IMAGE, self.scale_k)
        self.alpha = 255
        self.alpha_decay_rate = 4
        self.alive = True
        self.vx = 0
        self.vy = 4 + (random.randint(7,10) / 10)
        self.horizontal_velocity = 0.01 * random.random() * random.choice([-1,1])
        self.vertical_decay = 0.99

    def update(self):
        # setting the inital velocity of the particle
        self.x += self.vx
        # then adding the horizontal velocity to it
        self.vx += self.horizontal_velocity

        self.y -= self.vy
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
