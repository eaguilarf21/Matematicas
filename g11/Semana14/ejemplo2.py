import pygame
import sys

pygame.init()

negro = (0,0,0)
w,h = 600,400
pantalla = pygame.display.set_mode((w,h))
pygame.display.set_caption("Juego de naves 2D")
fondo = pygame.image.load("./Semana14/img/fondo.jpg")
reloj = pygame.time.Clock()

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./Semana14/img/jugadorG.png")
        self.image = pygame.transform.smoothscale(self.image,(100,100))
        self.image.set_colorkey(negro)
        self.rect = self.image.get_rect()
        self.rect.centerx = w//2
        self.rect.bottom = h-15

    def update(self):
        self.speed_x = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speed_x=-5
        if keys[pygame.K_RIGHT]:
            self.speed_x=5
        self.rect.x = self.rect.x+self.speed_x

        #limites de pantalla
        if self.rect.right>w:
            self.rect.right=w
        if self.rect.left<0:
            self.rect.left=0

all_sprites = pygame.sprite.Group()
player = Jugador()
all_sprites.add(player)

#bucle del juego
while True:
    reloj.tick(30)
    for eventoCapturado in pygame.event.get():
        if eventoCapturado.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #visualizar en pantalla
    all_sprites.update()
    pantalla.blit(fondo,(0,0))
    all_sprites.draw(pantalla)
    pygame.display.flip()