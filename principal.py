import sys, pygame, random
from pygame.locals import *
from ship import *
from asteroid import *
from bullet import *

size = width, height = 800 , 600

screen = pygame.display.set_mode(size)

def iniciar_pygame():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("Sonidos/Fondo.mp3")
    pygame.mixer.music.play(1)

    background_image = pygame.image.load("Imagenes/play.jpg")
    background_rect = background_image.get_rect()

    pygame.display.set_caption("CANDY")

    ship = Ship(size)
    asteroids = []

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.blit(background_image, background_rect)
        fuente = pygame.font.SysFont('8-bit Arcade In', 45)
        texto_puntos = fuente.render("Puntos " + str(ship.puntos), 1, (250, 250, 250))
        texto_vida = fuente.render("Vida " + str(ship.vida), 1, (250, 250, 250))
        fuente_go = pygame.font.SysFont("8-bit Arcade In", 100)
        texto_fin = fuente_go.render("FIN DEL JUEGO", 1, (250, 250, 250))

        ship.update()

        if random.randint(0, 100) % 25 == 0 and len(asteroids) < 10:
            new_asteroid = Asteroid(size)
            asteroids.append(new_asteroid)
        # Actualizar y dibujar balas
        bullets_to_remove = []
        for bullet in ship.bullets:
            bullet.update()
            screen.blit(bullet.image, bullet.rect)
            if bullet.alcance == 0:
                bullets_to_remove.append(bullet)

        for bullet in bullets_to_remove:
            ship.bullets.remove(bullet)

        # Dibujar nave
        screen.blit(ship.imagen, ship.rect)

        # Actualizar y dibujar asteroides
        for asteroid in asteroids:
            asteroid.update()
            screen.blit(asteroid.image, asteroid.rect)

            # Colisiones entre balas y asteroides
            for bullet in ship.bullets:
                if asteroid.rect.colliderect(bullet.rect):
                    ship.puntos += 1
                    asteroid.explotar()
                    asteroids.remove(asteroid)
                    break  # Salir del bucle para evitar colisiones múltiples con la misma bala

            # Colisión entre nave y asteroides
            if ship.rect.colliderect(asteroid.rect):
                ship.vida -= 10
                asteroid.explotar()
                asteroids.remove(asteroid)
        
        # Mostrar puntos y vida
        if ship.vida > 0:
            screen.blit(texto_vida, (600, 10))
            screen.blit(texto_puntos, (600, 30))
        else:
            screen.blit(texto_fin, (130, 250))

        pygame.display.update()
        pygame.time.delay(10)

iniciar_pygame()
