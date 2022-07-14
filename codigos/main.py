import pygame, sys 
from configs import *
from entidades import *
from random import choice
from player import Player

#criação câmera + grupo de spites
class TodaSprites(pygame.sprite.Group):
	def __init__(self):
		super().__init__()
		self.deslocamento = pygame.math.Vector2()
		self.fundo = pygame.image.load('sprites/main/mapa.png').convert()
		self.sobrepos = pygame.image.load('sprites/main/sobreposicao.png').convert_alpha()

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

pygame.display.set_caption('JF Run') #Joel Filho Run* (eu sou péssimo com nomes)
clock = pygame.time.Clock()

menu = True


#grupos
todas_sprites = TodaSprites()
obstaculos_sprites = pygame.sprite.Group()


#sprites/imagens
player = Player((2062,3274), todas_sprites, obstaculos_sprites)

reiniciar_bt = pygame.image.load('sprites/botoes/reiniciar_botao.png')
iniciar_bt = pygame.image.load('sprites/botoes/iniciar_botao.png')
sair_bt = pygame.image.load('sprites/botoes/sair_botao.png')


#botoes
botao_reiniciar = Botoes(largura // 2 - 70, altura // 2 + 100, reiniciar_bt)
botao_sair = Botoes(largura // 2 + 120, altura // 2 - 40, sair_bt)
botao_iniciar = Botoes(largura // 2 - 350, altura // 2 - 40, iniciar_bt)


#textin de vitoria
fonte = pygame.font.Font(None, 50)
texto = fonte.render('Honrou o batalhão, meu lindo!', True, 'White')
texto_retang = texto.get_rect(center = (largura / 2, altura /2 - 40))


#cronômetro
cronometro_carro = pygame.event.custom_type()
pygame.time.set_timer(cronometro_carro, 80)
lista_pos = []


#loop do jogo
while True:
	teclas= pygame.key.get_pressed()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		#implementa os carros no jogo de forma aleatória
		if event.type == cronometro_carro and player.game_over == 0:
			pos_aleatoria = choice(POSICOES_INICIAIS_CARROS)
			
			if pos_aleatoria not in lista_pos:
				lista_pos.append(pos_aleatoria)
				Carro(pos_aleatoria, [todas_sprites, obstaculos_sprites])
			
			if len(lista_pos) >= 5:
				del lista_pos[0]


	#'delta tempo': 
	dt = clock.tick() / 1000

	tela.fill('teal')


	if menu == True:
		if botao_sair.draw():
			pygame.quit()
			sys.exit()
		if botao_iniciar.draw():
			menu = False
		
	else:	
		if player.pos.y >= 1180 and player.game_over == 0:
			todas_sprites.update(dt)

			#todas_sprites.draw(tela)	
			todas_sprites.draw_customizado()
		

		elif player.game_over != 0:

			tela.fill('coral')
			tela.blit(player.texto_go, player.texto_go_retang)
			
			if botao_reiniciar.draw():
				player.reset((2062,3274), todas_sprites, obstaculos_sprites)
				player.game_over = 0

		else:
			tela.fill('black')
			tela.blit(texto, texto_retang)

		
	pygame.display.update()