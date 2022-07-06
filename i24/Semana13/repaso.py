import pygame
import sys

pygame.init()

#pantalla
size = 700,500
pantalla = pygame.display.set_mode(size)
pygame.display.set_caption("mi primer juego")

#fondo
fondo = pygame.image.load("./Semana12/img/fondo.jpg")
fondo_t = pygame.transform.scale(fondo,(size))
pantalla.blit(fondo_t,(0,0))

#personaje
nave = pygame.image.load("./Semana12/img/NAVE.png")
pantalla.blit(nave,(350,250))

pygame.display.flip()

#bucle del juego
while 1==1:
    for eventoCapturado in pygame.event.get():
        if eventoCapturado.type==pygame.QUIT:
            pygame.quit()
            sys.exit()