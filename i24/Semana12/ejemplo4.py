import pygame
import sys

pygame.init()

#definiendo pantallada
size = 800,600
pantalla = pygame.display.set_mode((800,600))
pygame.display.set_caption("repaso")

fondo=pygame.image.load("./Semana12/img/fondo.jpg")
fondo_t=pygame.transform.smoothscale(fondo,(800,600))
pantalla.blit(fondo_t,(0,0))


enemigo = pygame.image.load("./Semana12/img/jugadorG.png")
enemigo_t = pygame.transform.smoothscale(enemigo,(300,300))
pantalla.blit(enemigo_t, (100,50))

nave = pygame.image.load("./Semana12/img/NAVE.png")
pygame.display.set_icon(nave)
pantalla.blit(nave,(450,300))
pygame.display.flip()


#bucle del juego
while True:
    for eventoCapturado in pygame.event.get():
        if eventoCapturado.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #pygame.display.update()