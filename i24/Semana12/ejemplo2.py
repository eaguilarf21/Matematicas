import pygame
import sys

pygame.init()

#definiendo pantallada
size = 800,600
pantalla = pygame.display.set_mode((800,600))
pygame.display.set_caption("repaso")
color=(255,255,255)
pantalla.fill((240,130,200))
pygame.display.flip()

#bucle del juego
while True:
    for eventoCapturado in pygame.event.get():
        if eventoCapturado.type == pygame.QUIT:
            pygame.quit()
            sys.exit()