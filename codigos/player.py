import pygame,sys

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, grupos, sprites_colisao):
        super().__init__(grupos)

        #sprites
        self.importar_sprites()
        self.image = self.animacao[0]
        self.rect = self.image.get_rect(center = pos)

        #relacionado a movimentação
        self.pos = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2()
        self.velocidade = 200

        #colisoes
        self.sprites_colisao = sprites_colisao

    
    def colisao(self, direcao):
        #pygame.sprite.spritecollide(self, self.sprites_colisao, True)

        #checando a direção no eixo x e y, de acordo com o que está escrito no método de movimentação (abaixo)
        if direcao == 'horizontal':
            for sprite in self.sprites_colisao.sprites():
                if sprite.rect.colliderect(self.rect):
                    if hasattr(sprite, 'nome') and sprite.nome == 'carro': #checa se a colisão foi com a sprite do carro (se sim, game over)
                        pygame.quit()
                        sys.exit()
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left
                        self.pos.x = self.rect.centerx
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right
                        self.pos.x = self.rect.centerx
        else:
            if direcao == 'vertical':
                for sprite in self.sprites_colisao.sprites():
                    if sprite.rect.colliderect(self.rect):
                        if hasattr(sprite, 'nome') and sprite.nome == 'carro': #checa se a colisão foi com a sprite do carro (se sim, game over)
                            pygame.quit()
                            sys.exit()
                        if self.direction.y > 0:
                            self.rect.bottom = sprite.rect.top
                            self.pos.y = self.rect.centery
                        if self.direction.y < 0:
                            self.rect.top = sprite.rect.bottom
                            self.pos.y = self.rect.centery
                            

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
        
        #horizontal
        self.pos.x += self.direction.x * self.velocidade * dt     
        self.rect.centerx = (round(self.pos.x))
        self.colisao('horizontal')

        #vertical
        self.pos.y += self.direction.y * self.velocidade * dt     
        self.rect.centery = (round(self.pos.y))
        self.colisao('vertical')


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


    def restringir_movimento(self):
        if self.rect.left < 640:
            self.pos.x = 640 + self.rect.width / 2

    def update(self, dt):
        self.teclas_movimentação()
        self.movimentacao(dt)
