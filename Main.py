import pygame
import math

from model import Personagem

#personagem
paraX = 200
paraY = 533

chao = 590
altura = 57
pulo = 50

paraCima = False
paraBaixo = False
paraDireita = False
paraEsquerda = False

pygame.init()
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
FPS = 30

                

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("Slither")
#pygame.display.flip()

clock = pygame.time.Clock()

#altura, pulo, paraX, paraY
player = Personagem(57, 50, 200, 533)
#playerImg = pygame.image.load('player.png')
img = player.getImage()
gameExit = False

global direction
direction = 'parado'
posicoes = 1
paradoVariacao = False
jump = False
gravidade = False

while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				direction = 'esquerda'
				paraEsquerda = True
				posicoes = 2
				img = pygame.transform.flip(player.getImage(), True, False)
			if event.key == pygame.K_RIGHT:
				direction = 'direita'
				img = player.getImage()
				posicoes = 1
				paraDireita = True
			if event.key == pygame.K_UP:
				jump = True
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				direction = 'parado'
				paraEsquerda = False	
			if event.key == pygame.K_RIGHT:
				direction = 'parado'
				paraDireita = False
	if jump:
		if not gravidade and math.fabs(player.getPositionY() + player.getAltura() - chao) <= player.getPulo():
			player.setPositionY(-3)
			#paraY -= 3
		else:
			gravidade = True
			if player.getPositionY() + player.getAltura() - chao <= 0:
				player.setPositionY(2)
				#paraY += 2
			else:
				jump = False
				gravidade = False	
	if paraDireita:
		player.setPositionX(3)
		#paraX +=3
	if paraEsquerda:
		player.setPositionX(-3)
		#paraX -=3
	

	#if direction == 'parado':
	#	if posicoes == 1:
	#		img = playerImgParado
	#	elif posicoes == 2:
	#		img = pygame.transform.flip(playerImgParado, True, False)
	#else:
	#	if posicoes == 1:
	#		img = playerImg
	#	elif posicoes == 2:
	#		img = pygame.transform.flip(playerImg, True, False)
		
	gameDisplay.fill(white)
	pygame.draw.rect(gameDisplay, black, [0,chao,800,20])
	gameDisplay.blit(img, (player.getPositionX(), player.getPositionY()))
	#pygame.draw.rect(gameDisplay, red, [,paraY, 10, 10])
	pygame.display.update()
	clock.tick(FPS)
pygame.quit()
quit()
