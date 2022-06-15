import pygame
import sys

pygame.init()
size=800,600
pantalla = pygame.display.set_mode(size)
pygame.display.set_caption("Repaso")

pantalla.fill((112,255,230))
pygame.display.flip()



while True==True:
    for eventoCapturado in pygame.event.get():
        if eventoCapturado.type==pygame.QUIT:
            sys.exit()
            pygame.quit()
            pygame.display.update()

