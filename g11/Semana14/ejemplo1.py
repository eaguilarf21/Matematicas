import pygame,sys

pygame.init()

#pantalla
w,h=800,600
pantalla = pygame.display.set_mode((w,h))
pygame.display.set_caption("mi videojuego 2D")
blanco = 255,255,255

#pelota
pelota = pygame.image.load("./Semana14/img/pelota.png")
pelota_t = pygame.transform.smoothscale(pelota,(100,100))
pelota_rect = pelota_t.get_rect()
incremento=[1,1]

#bucle del juego
while True:
    pygame.time.delay(5)
    for eventoCapturado in pygame.event.get():
        if eventoCapturado.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #ubicar pelota
    pelota_rect = pelota_rect.move(incremento)
    #rebote... ya no limite
    if pelota_rect.left<0 or pelota_rect.right>w:
        incremento[0]=-incremento[0]
    if pelota_rect.top<0 or pelota_rect.bottom>h:
        incremento[1]=-incremento[1]

    #refrescar pantalla
    pantalla.fill(blanco)
    pantalla.blit(pelota_t,pelota_rect)
    pygame.display.flip()