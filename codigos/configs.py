import pygame 

largura, altura = 1280,720

tela = pygame.display.set_mode((largura, altura))

POSICOES_INICIAIS_CARROS = [(-100, 1312), (-100, 1632), (-100,1888), 
	(-100, 2471), (-100,2853), (-100, 3080), (3300, 1400), 
	(3300,1760), (3300, 1970), (3300, 2550), (3300, 2981)]

POSICOES_INICIAIS_MOEDA = [
	(2150, 3274), (1782, 2274)
]
