import pygame, sys 
from configs import *
from player import Player

pygame.init()

tela = pygame.display.set_mode((largura, altura))
clock = pygame.time.Clock()

#grupos
todas_sprites = pygame.sprite.Group()

#sprites
player = Player((600, 400), todas_sprites)

while True:
	teclas= pygame.key.get_pressed()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	dt = clock.tick() / 1000

	tela.fill('black')

	todas_sprites.update(dt)

	todas_sprites.draw(tela)	

	pygame.display.update()