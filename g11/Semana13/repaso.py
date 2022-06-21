import pygame
import sys

pygame.init()

#pantalla
pantalla = pygame.display.set_mode((700,500))
pygame.display.set_caption("mi videojuego en 2D")

#icono
icono = pygame.image.load("./Semana12/img/NAVE.png")
pygame.display.set_icon(icono)

#fondo
fondo = pygame.image.load("./Semana12/img/fondo.jpg")
fondo_t = pygame.transform.scale(fondo,(700,500))
#pantalla.blit(fondo_t,(0,0))

#jugador
nave = pygame.image.load("./Semana12/img/NAVE.png")
#pantalla.blit(nave,(300,200))

nave_rect = nave.get_rect()
nave_rect.move_ip(300,200)


#mostrar imagenes en pantalla
#pygame.display.flip()

#bucle del juego
while 1==1:
    for eventoCapturado in pygame.event.get():
        if eventoCapturado.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            nave_rect = nave_rect.move(0,-1)
        if keys[pygame.K_DOWN]:
            nave_rect = nave_rect.move(0,1) 
        if keys[pygame.K_RIGHT]:
            nave_rect = nave_rect.move(1,0)
        if keys[pygame.K_LEFT]:
            nave_rect = nave_rect.move(-1,0)

    pantalla.blit(fondo_t,(0,0))
    pantalla.blit(nave,nave_rect)
    pygame.display.flip()