import pygame

pygame.init()

size=600,400
pygame.display.set_mode(size)
pygame.display.set_caption("mi primer juego")

pantalla = True

while pantalla == True:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pantalla = False 

pygame.quit()