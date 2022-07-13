import pygame
from os import walk
from random import choice

class Carro(pygame.sprite.Sprite):
    def __init__(self, pos, grupos):
        super().__init__(grupos)

        #pegar as sprites dos carros de forma aleatória 
        for _, _, lista_imgs in walk('sprites/carros/'):
            carro = choice(lista_imgs)

        self.image = pygame.image.load('sprites/carros/' + carro).convert_alpha()
        self.rect = self.image.get_rect(center = pos)

        #relacionado a movimentação
        self.pos = pygame.math.Vector2(self.rect.center)

        #condição p/ caso o carro venha de um lado ou de outro (esquerda ou direita)
        if pos[0] < 200:
            self.direction = pygame.math.Vector2(1, 0)
        else:
            self.direction = pygame.math.Vector2(-1, 0)
            self.image = pygame.transform.flip(self.image, True, False)
        
        self.velocidade = 300

    def update(self, dt):
        self.pos += self.direction * self.velocidade * dt   
        self.rect.center = (round(self.pos.x), round(self.pos.y))

        #caso o carro saia do alcance do mapa em até 200px (direita ou esquerda), a sprite desaparece
        if not -200 < self.rect.x < 3400:
            self.kill()