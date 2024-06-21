import pygame
from pygame.sprite import Sprite

class Explosion(Sprite):
    def __init__(self, contenedor, pos):
        Sprite.__init__(self)
        self.frames = [pygame.image.load("Imagenes/explosion.png") for n in range(1, 6)]
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.contenedor = contenedor
        self.animation_speed = 0.2  # Velocidad de la animación
        self.current_frame = 0

    def update(self):
        self.current_frame += self.animation_speed
        if self.current_frame >= len(self.frames):
            self.kill()  # Remover la explosión cuando la animación haya terminado
        else:
            self.frame_index = int(self.current_frame)
            self.image = self.frames[self.frame_index]
