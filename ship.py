import pygame
from pygame.locals import *
from pygame.sprite import Sprite
import math
from bullet import *


class Ship(Sprite):
    def __init__(self, contenedor):
        self.puntos = 0
        self.angulo = 0
        self.radio = 8
        self.vida = 100
        self.velocidad = [0, 0]
        self.bullets = []
        self.contenedor = contenedor
        self.imagen_base = pygame.image.load('Imagenes/I4.png')
        self.imagen = self.imagen_base
        self.rect = self.imagen.get_rect()
        self.rect.move_ip(contenedor[0]/2, contenedor[1]/2)
        #self.impulso = pygame.mixer.Sound('sonidos/impulso.mp3')
        #self.impulso.set_volume(0.05)
        self.disparo = pygame.mixer.Sound('sonidos/bala.mp3')
        self.disparo.set_volume(1)


    def update(self):
        teclas = pygame.key.get_pressed()

        if teclas[K_LEFT]:
            self.rotar(2)
        elif teclas[K_RIGHT]:
            self.rotar(-2)
        elif teclas[K_UP]:
            self.acelerar()
        elif teclas[K_SPACE]:
            self.disparar()
        
        self.velocidad[0] *= 0.90
        self.velocidad[1] *= 0.90
        
        self.rect = self.rect.move(self.velocidad)
        self.rect.x %= self.contenedor[0]
        self.rect.y %= self.contenedor[1]
         
    def disparar(self):
        self.disparo.play()
        vector = [0,0]
        vector[0] += math.cos(math.radians((self.angulo)%360))
        vector[1] -= math.sin(math.radians((self.angulo)%360))
        pos = [self.rect.x + self.radio, self.rect.y + self.radio]
        vel = [self.velocidad[0] + 6 * vector[0], self.velocidad[1] + 6 * vector[1]]
        self.bullets.append(Bullet(pos,self.angulo,vel, self.contenedor))

    def acelerar(self):
        #self.impulso.play()
        self.velocidad[0] += 0.5 * math.cos(math.radians((self.angulo)%360))
        self.velocidad[1] -= 0.5 * math.sin(math.radians((self.angulo)%360))

    def rotar(self,angulo):
        self.angulo += angulo
        centro_x = self.rect.centerx
        centro_y = self.rect.centery
        self.imagen = pygame.transform.rotate(self.imagen_base, self.angulo)
        self.rect = self.imagen.get_rect()
        self.rect.centerx = centro_x
        self.rect.centery = centro_y