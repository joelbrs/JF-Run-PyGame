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
		self.fundo = pygame.image.load('sprites/mapa/mapa.png').convert()

	#onde eu realmente configurei a câmera 
	def draw_customizado(self):

		#atribuindo a posição do personagem (cada eixo de seu retângulo) ao vetor de deslocamento
		self.deslocamento.x = player.rect.centerx - largura / 2
		self.deslocamento.y = player.rect.centery - altura / 2
		
		#desenho do fundo na tela(mapa), utilizando o deslocamento como coordenada
		tela.blit(self.fundo, -self.deslocamento)

		for sprite in self.sprites():
			pos_deslocamento = sprite.rect.topleft - self.deslocamento
			tela.blit(sprite.image, pos_deslocamento)


#score
def score(score):
	fonte_score = pygame.font.Font(None, 30)
	texto = fonte_score.render('Itens pegos: ' + str(player.score), True, 'White')
	tela.blit(texto, [100, 35])


#configs basicas		
pygame.init()

pygame.display.set_caption('JF Run') #Joel Filho Run* (eu sou péssimo com nomes)
clock = pygame.time.Clock()

menu = True


#musicas
pygame.mixer.music.set_volume(0.15)
musica_fundo = pygame.mixer.music.load('musicas/principal -(UNDERTALE-Hotel).wav')
pygame.mixer.music.play(-1)
musica_game_over = pygame.mixer.Sound('musicas/game_over (SUPER MARIO BROS).wav')
musica_vitoria = pygame.mixer.Sound('musicas/vitoria.wav')
pygame.mixer.Sound.set_volume(musica_vitoria, 0.15)
pygame.mixer.Sound.set_volume(musica_game_over, 0.15)


#grupos
todas_sprites = TodaSprites()
obstaculos_sprites = pygame.sprite.Group()
item_boost = pygame.sprite.Group()


#itens/player
player = Player((2452,3274), todas_sprites, obstaculos_sprites, item_boost)
boost = ItemBoost((1856, 1856), [todas_sprites, item_boost])


#botoes
reiniciar_bt = pygame.image.load('sprites/botoes/reiniciar_botao.png')
iniciar_bt = pygame.image.load('sprites/botoes/iniciar_botao.png')
sair_bt = pygame.image.load('sprites/botoes/sair_botao.png')

botao_reiniciar = Botoes(largura // 2 - 70, altura // 2 + 100, reiniciar_bt)
botao_sair_menu = Botoes(largura // 2 + 120, altura // 2 - 40, sair_bt)
botao_iniciar_menu = Botoes(largura // 2 - 350, altura // 2 - 40, iniciar_bt)


#textin de vitoria
fonte_melhor_score = pygame.font.Font(None, 50)
texto_melhor_score = fonte_melhor_score.render('Honrou o batalhão, meu lindo!', True, 'White')
texto_retang = texto_melhor_score.get_rect(center = (largura / 2, altura /2 - 40))


#texto score = 1
fonte_score_1 = pygame.font.Font(None, 50)
texto_score_1 = fonte_score_1.render('Boa, mandou bem :)', True, 'White')
texto_retang_1 = texto_score_1.get_rect(center = (largura / 2, altura /2 - 40))


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
					
			if len(lista_pos) >= 7:
				del lista_pos[0]
			

	#'delta tempo': 
	dt = clock.tick() / 1000
	tela.fill('teal')


	if menu == True:

		if botao_sair_menu.draw():
			pygame.quit()
			sys.exit()
		if botao_iniciar_menu.draw():
			menu = False
		

	else:	
		if player.pos.y >= 1180 and player.game_over == 0:
			todas_sprites.update(dt)
	
			todas_sprites.draw_customizado()
			score(player.score)	
		
		elif player.game_over == 1:

			tela.fill('coral')
			tela.blit(player.texto_go, player.texto_go_retang)
			pygame.mixer.music.stop()
			musica_game_over.play()

			
			if botao_reiniciar.draw():
				player.reset((2062,3274), todas_sprites, obstaculos_sprites, item_boost)
				boost.reset((1856, 1856), [todas_sprites, item_boost])
				player.score = 0
				player.game_over = 0
				musica_game_over.stop()
				pygame.mixer.music.play(-1)

		else:
			pygame.mixer.music.stop()
			musica_vitoria.play()

			if player.score == 0:
				tela.fill('black')
				tela.blit(texto_melhor_score, texto_retang)
			if player.score == 1:
				tela.fill('cyan')
				tela.blit(texto_score_1, texto_retang_1)
			
	pygame.display.update()