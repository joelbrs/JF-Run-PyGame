import pygame, sys 
from configs import *
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
		
		#desenho do fundo na tela, utilizando o deslocamento como coordenada
		tela.blit(self.fundo, -self.deslocamento)

		for sprite in self.sprites():
			pos_deslocamento = sprite.rect.topleft + self.deslocamento
			tela.blit(sprite.image, pos_deslocamento)

		tela.blit(self.sobrepos, -self.deslocamento)

#configs basicas		
pygame.init()

tela = pygame.display.set_mode((largura, altura))
clock = pygame.time.Clock()

#grupos
todas_sprites = TodaSprites()

#sprites
player = Player((600, 400), todas_sprites)
carro = Carro((600, 200), todas_sprites)

#loop do jogo
while True:
	teclas= pygame.key.get_pressed()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	#'delta tempo': 
	dt = clock.tick() / 1000

	tela.fill('black')

	todas_sprites.update(dt)

	#todas_sprites.draw(tela)	
	todas_sprites.draw_customizado()

	pygame.display.update()