import pygame
import sys
import random

pygame.init()

negro = (0,0,0)
w,h = 600,400
pantalla = pygame.display.set_mode((w,h))
pygame.display.set_caption("Juego de naves 2D")
fondo = pygame.image.load("./Semana15/img/fondo.jpg")
reloj = pygame.time.Clock()

#crear nave
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./Semana15/img/jugadorG.png")
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

    def dispara(self):
        bala=Bala(self.rect.centerx, self.rect.y)#        
        all_sprites.add(bala)
        bala=Bala(self.rect.x, self.rect.y)#        
        all_sprites.add(bala)


#crear balas
class Bala(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("./Semana15/img/laser.png")
        self.image.set_colorkey(negro)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.centerx = x

    def update(self):
        self.rect.y = self.rect.y-10
        if self.rect.y<0:
            self.kill()

#crear piedra
class Piedra(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./Semana15/img/piedra.png")
        self.image = pygame.transform.smoothscale(self.image,(60,60))
        self.image.set_colorkey(negro)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(w)
        self.rect.y = random.randrange(-140,-100)
        self.speedx = random.randrange(-5,5)
        self.speedy = random.randrange(1,10)

    def update(self):
        self.rect.x = self.rect.x + self.speedx
        self.rect.y = self.rect.y + self.speedy
        if self.rect.y>h or (self.rect.x>w or self.rect.x<0):
            self.rect.x = random.randrange(w)
            self.rect.y = random.randrange(-140,-100)
            self.speedx = random.randrange(-5,5)
            self.speedy = random.randrange(1,10)



#grupo de juego
all_sprites = pygame.sprite.Group()
lista_meteorito = pygame.sprite.Group()
player = Jugador()
all_sprites.add(player)

for contador in range(5):
    meteorito = Piedra()
    all_sprites.add(meteorito)
    lista_meteorito.add(meteorito)

#bucle del juego
while True:
    reloj.tick(50)
    for eventoCapturado in pygame.event.get():
        if eventoCapturado.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if eventoCapturado.type == pygame.KEYDOWN:
            if  eventoCapturado.key == pygame.K_SPACE:
                player.dispara()
    
    hits = pygame.sprite.spritecollide(player,lista_meteorito,True)
    if hits:
        pygame.quit()
        sys.exit()

    #visualizar en pantalla
    all_sprites.update()
    pantalla.blit(fondo,(0,0))
    all_sprites.draw(pantalla)
    pygame.display.flip()