from curses import KEY_DC
import pygame,sys

pygame.init()

#variables
w,h = 800,600
negro = (0,0,0)
fondo = pygame.image.load("./Semana15/img/fondo.jpg")
clock = pygame.time.Clock()

#pantalla
pantalla = pygame.display.set_mode((w,h))
pygame.display.set_caption("Mi videojuego 2D")

#objeto jugador
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./Semana15/img/jugadorG.png")
        self.image = pygame.transform.smoothscale(self.image,(100,100))
        #self.image.set_colorkey(negro)
        self.rect = self.image.get_rect()
        self.rect.centerx = w//2
        self.rect.bottom = h-10
        self.speed_x=0

    def update(self):
        self.speed_x=0
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speed_x = -5
        if keys[pygame.K_RIGHT]:
            self.speed_x = 5
        self.rect.x = self.rect.x + self.speed_x

        if self.rect.right>w:
            self.rect.right=w
        if self.rect.left<0:
            self.rect.left=0

    def dispara(self):
        balita = Bala(self.rect.centerx,self.rect.top)
        all_sprites.add(balita)

#objeto bala
class Bala(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("./Semana15/img/laser.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y
        self.speed_y = -10
    
    def update(self):
        self.rect.y = self.rect.y + self.speed_y
        if self.rect.y<0:
            self.kill()

#coleccion principal
all_sprites = pygame.sprite.Group()
player = Jugador()
all_sprites.add(player)

#bucle del juego
while True:
    clock.tick(60)
    for eventoCapturado in pygame.event.get():
        if eventoCapturado.type == pygame.QUIT:                
            pygame.quit()
            sys.exit()
        elif eventoCapturado.type == pygame.KEYDOWN:
            if eventoCapturado.key==pygame.K_SPACE:
                player.dispara()
            

    all_sprites.update()
    pantalla.blit(fondo,(0,0))
    all_sprites.draw(pantalla)
    pygame.display.flip()