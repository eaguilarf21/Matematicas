import pygame
import sys

pygame.init()
size = 800,600
pygame.display.set_mode(size)
pygame.display.set_caption("repaso")

#demorate
#ventana = True
#while ventana==True:
#    for eventoCapturado in pygame.event.get():
#        if eventoCapturado.type == pygame.QUIT:
#            ventana=False

#pygame.quit()

#atento
while True:
    for eventoCapturado in pygame.event.get():
        if eventoCapturado.type == pygame.QUIT:
            pygame.quit()
            sys.exit()