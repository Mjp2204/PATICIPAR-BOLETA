import pygame
from pygame.sprite import Sprite
import math

class Bullet(Sprite):
    def __init__(self, pos, angle, vel, cont):
        super().__init__()
        self.vel = vel
        self.alcance = 10  # Alcance máximo de la bala
        self.contenedor = cont
        self.image = pygame.image.load('Imagenes/bala.png')
        self.rect = self.image.get_rect()
        self.rect.center = pos  # Posición inicial de la bala
        self.angulo = angle

    def update(self):
        self.alcance -= 1  # Reducir el alcance en cada actualización
        self.vel[0] += math.cos(math.radians(self.angulo % 360))
        self.vel[1] -= math.sin(math.radians(self.angulo % 360))
        self.rect = self.rect.move(self.vel)
        self.rect.x %= self.contenedor[0]
        self.rect.y %= self.contenedor[1]

    def fuera_de_alcance(self):
        return self.alcance <= 0
