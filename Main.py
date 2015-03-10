import pygame
import math

#personagem
paraX = 200
paraY = 533

chao = 590
altura = 57
pulo = 40

paraCima = False
paraBaixo = False
paraDireita = False
paraEsquerda = False

pygame.init()
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
FPS = 30
def jump(yPosition):
	if math.fabs(yPosition + altura - chao) <= pulo:
		yPosition -= 1
		gameDisplay.blit(img, (paraX, yPosition))
		#if yPosition + altura <= chao:
			#con = -1
		pygame.display.update()	
		

	
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("Slither")
#pygame.display.flip()

clock = pygame.time.Clock()

playerImg = pygame.image.load('player.png')
playerImgParado = pygame.image.load('player.gif')
img = playerImg
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
				img = pygame.transform.flip(playerImg, True, False)
			if event.key == pygame.K_RIGHT:
				direction = 'direita'
				img = playerImg
				posicoes = 1
				paraDireita = True
			if event.key == pygame.K_UP:
				jump = True
				#jump(paraY)
				#paraCima = True
			#if event.key == pygame.K_DOWN:
				#paraBaixo = True
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				direction = 'parado'
				paraEsquerda = False	
			if event.key == pygame.K_RIGHT:
				direction = 'parado'
				paraDireita = False
			#if event.key == pygame.K_DOWN:
				#paraBaixo = False
	if jump:
		if not gravidade and math.fabs(paraY + altura - chao) <= pulo:
			paraY -= 2
		else:
			gravidade = True
			if paraY + altura - chao <= 0:
				paraY += 1
			else:
				jump = False
				gravidade = False	
	if paraDireita:
		paraX +=3
	if paraEsquerda:
		paraX -=3
	

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
	gameDisplay.blit(img, (paraX, paraY))
	#pygame.draw.rect(gameDisplay, red, [,paraY, 10, 10])
	pygame.display.update()
	clock.tick(FPS)
pygame.quit()
quit()
