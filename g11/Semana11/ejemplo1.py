import pygame

pygame.init()
size=600,400

pantalla = pygame.display.set_mode(size)
pygame.display.set_caption("Mi primer juego")

player=pygame.image.load("jugador.png")
player_get_rect = player.get_rect()

pantalla.blit(player, player_get_rect)
pygame.display.flip()

activo=True

while activo == True:
    for eventoCapturado in pygame.event.get():
        if eventoCapturado.type == pygame.QUIT:
            activo=False


pygame.quit()