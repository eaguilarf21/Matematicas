import pygame
import sys

pygame.init()

#pantalla
w,h = 700,500
pantalla = pygame.display.set_mode([w,h])
pygame.display.set_caption("mi primer juego")

#fondo
fondo = pygame.image.load("./Semana12/img/fondo.jpg")
fondo_t = pygame.transform.scale(fondo,(w,h))
#pantalla.blit(fondo_t,(0,0))

#personaje
nave = pygame.image.load("./Semana12/img/NAVE.png")
nave_rect = nave.get_rect()
#pantalla.blit(nave,(350,250))
nave_rect.move_ip(350,250)

#pygame.display.flip()

#bucle del juego
while True:
    for eventoCapturado in pygame.event.get():
        if eventoCapturado.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        nave_rect=nave_rect.move(0,-1)
    if keys[pygame.K_DOWN]:
        nave_rect=nave_rect.move(0,1)
    if keys[pygame.K_LEFT]:
        nave_rect=nave_rect.move(-1,0)
    if keys[pygame.K_RIGHT]:
        nave_rect=nave_rect.move(1,0)
    
    if nave_rect.right>w:
        nave_rect.right=w
    if nave_rect.left<0:
        nave_rect.left=0
    pantalla.blit(fondo_t,(0,0))        
    pantalla.blit(nave,nave_rect)
    pygame.display.flip()