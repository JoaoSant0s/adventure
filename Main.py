import pygame

from adventure.model import Link
from adventure.GlobalMap import GlobalMap

# personagem
para_x = 200
para_y = 500
altura = 40
largura = 20

para_direita = False
para_esquerda = False
para_cima = False
para_baixo = False



pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
link_color = (204, 158, 72)
FPS = 30
window_width = 800
window_height = 600

gameDisplay = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Slither")

clock = pygame.time.Clock()

player = Link(largura, altura, para_x, para_y)

globalMap = GlobalMap(window_width, window_height)
globalMap.popular()

gameExit = False

while not gameExit:
	player.move()
	gameDisplay.fill(player.location_map(globalMap).color)
	pygame.draw.rect(gameDisplay, link_color, [player.get_position_x(), player.get_position_y(), player.get_largura(), player.get_altura()])
	pygame.display.update()
	clock.tick(FPS)
pygame.quit()
quit()