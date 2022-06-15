import pygame
import sys

#inicio de pantalla
icono = pygame.image.load("./Semana12/img/NAVE.png")
pygame.display.set_icon(icono)
pygame.init()
pantalla = pygame.display.set_mode((800,600))
pygame.display.set_caption("Nave")

#cargar fondo
fondo = pygame.image.load("./Semana12/img/fondo.jpg")
fondo_t = pygame.transform.scale(fondo,(800,600))
pantalla.blit(fondo_t, (0,0))

#carga jugador 1
enemigo=pygame.image.load("./Semana12/img/jugadorG.png")
enemigo_t = pygame.transform.scale(enemigo,(300,300))
pantalla.blit(enemigo_t, (100,50))


#cargar jugador 2
jugador = pygame.image.load("./Semana12/img/NAVE.png")
pantalla.blit(jugador, (500,400))

pygame.display.flip()

#bucle no cerrar
while True==True:
    for eventoCapturado in pygame.event.get():
        if eventoCapturado.type == pygame.QUIT:
            pygame.quit()
            sys.exit()            
    pygame.display.update()
