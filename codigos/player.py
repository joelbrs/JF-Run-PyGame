import pygame
from configs import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, grupos, sprites_carros, sprite_boost):
        self.reset(pos, grupos, sprites_carros, sprite_boost)
    
    
    def reset(self, pos, grupos, sprites_carros, sprite_boost):
        super().__init__(grupos)
        #sprites
        self.image = pygame.image.load('sprites/player/down/0.png')
        self.rect = self.image.get_rect(center = pos)
        self.grupos = grupos

        #relacionado a movimentação
        self.pos = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2()
        self.velocidade = 200

        #colisoes
        self.sprites_carros = sprites_carros
        self.sprite_boost = sprite_boost
        self.som_colisao_carro = pygame.mixer.Sound('musicas/colisao - (SUPER MARIO BROS).wav')
        pygame.mixer.Sound.set_volume(self.som_colisao_carro, 0.15)
        self.som_colisao_item = pygame.mixer.Sound('musicas/item(SUPER MARIO BROS).wav')

        self.score = 0

        #game over
        self.game_over = 0
        self.fonte = pygame.font.Font(None, 50)
        self.texto_go = self.fonte.render('Vacilou feio, meu patrão!', True, 'White')
        self.texto_go_retang = self.texto_go.get_rect(center = (largura / 2, altura /2 - 40))


    def colisao(self):
        
        if pygame.sprite.spritecollide(self, self.sprites_carros, False):
            self.game_over = 1
            self.som_colisao_carro.play()
        

        if pygame.sprite.spritecollide(self, self.sprite_boost, True):
               self.velocidade += 15
               self.score += 1
               self.som_colisao_item.play()
        

    def movimentacao(self, dt):
        #p/ evitar o "bug" da movimentação na diagonal ser mais rápida que as outras
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        #horizontal
        self.pos.x += self.direction.x * self.velocidade * dt     
        self.rect.centerx = (round(self.pos.x))
        self.colisao()

        #vertical
        self.pos.y += self.direction.y * self.velocidade * dt     
        self.rect.centery = (round(self.pos.y))
        self.colisao()


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
