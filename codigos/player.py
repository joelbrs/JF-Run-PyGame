import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, grupos):
        super().__init__(grupos)

        #sprites
        self.importar_sprites()
        self.image = self.animacao[0]
        self.rect = self.image.get_rect(center = pos)

        #relacionado a movimentação
        self.pos = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2()
        self.velocidade = 200

    #importa o caminho das sprites (não consegui totalmente ainda)
    def importar_sprites(self):
        caminho = 'sprites/player/down/'
        self.animacao = []

        for frame in range(4):
            superf = pygame.image.load(f'{caminho}{frame}.png').convert_alpha()
            self.animacao.append(superf)

    def movimentacao(self, dt):
        #p/ evitar o "bug" da movimentação na diagonal ser mais rápida que as outras
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        self.pos += self.direction * self.velocidade * dt     
        self.rect.center = (round(self.pos.x), round(self.pos.y))


    def teclas_movimentação(self):
        teclas = pygame.key.get_pressed()

        #teclas p/ movimentação no eixo y
        if teclas[pygame.K_w]:
            self.direction.y = -1
        elif teclas[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        
        #teclas p/ movimentação no eixo x
        if teclas[pygame.K_d]:
            self.direction.x = 1
        elif teclas[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0


    def update(self, dt):
        self.teclas_movimentação()
        self.movimentacao(dt)