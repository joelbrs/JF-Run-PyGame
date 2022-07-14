import pygame, sys 
from configs import *
from random import choice
from carros import Carro
from player import Player

#criação da câmera
class TodaSprites(pygame.sprite.Group):
	def __init__(self):
		super().__init__()
		self.deslocamento = pygame.math.Vector2()
		self.fundo = pygame.image.load('sprites/main/map.png').convert()
		self.sobrepos = pygame.image.load('sprites/main/overlay.png').convert_alpha()


	def draw_customizado(self):

		#atribuindo a posição do personagem (cada eixo de seu retângulo) ao vetor de deslocamento
		self.deslocamento.x = player.rect.centerx - largura / 2
		self.deslocamento.y = player.rect.centery - altura / 2
		
		#desenho do fundo na tela(mapa), utilizando o deslocamento como coordenada
		tela.blit(self.fundo, -self.deslocamento)

		for sprite in self.sprites():
			pos_deslocamento = sprite.rect.topleft - self.deslocamento
			tela.blit(sprite.image, pos_deslocamento)

		tela.blit(self.sobrepos, -self.deslocamento)


#configs basicas		
pygame.init()

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('JF Run') #Joel Filho Run* (eu sou péssimo com nomes)
clock = pygame.time.Clock()

#grupos
todas_sprites = TodaSprites()
obstaculos_sprites = pygame.sprite.Group()

#sprites
player = Player((2062,3274), todas_sprites, obstaculos_sprites)
vitoria = pygame.image.load('sprites/vitoria/vitoria.png')
vitoria_retang = vitoria.get_rect(center = (largura / 2, altura /2))

#cronômetro
cronometro_carro = pygame.event.custom_type()
pygame.time.set_timer(cronometro_carro, 100)
lista_pos = []

#loop do jogo
while True:
	teclas= pygame.key.get_pressed()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		#implementa os carros no jogo de forma aleatória
		if event.type == cronometro_carro:
			pos_aleatoria = choice(POSICOES_INICIAIS_CARROS)
			
			if pos_aleatoria not in lista_pos:
				lista_pos.append(pos_aleatoria)
				Carro(pos_aleatoria, [todas_sprites, obstaculos_sprites])
			
			if len(lista_pos) >= 5:
				del lista_pos[0]

	#'delta tempo': 
	dt = clock.tick() / 1000

	tela.fill('black')

	if player.pos.y >= 1180:
		todas_sprites.update(dt)

		#todas_sprites.draw(tela)	
		todas_sprites.draw_customizado()
	else:
		tela.fill('salmon')
		tela.blit(vitoria, vitoria_retang)
		
	pygame.display.update()