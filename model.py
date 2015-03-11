import pygame

class Personagem(object):
	
	def __init__(self, altura, pulo, paraX, paraY):
		self.altura = altura
		self.pulo = pulo
		self.paraX = paraX
		self.paraY = paraY
		self.playerImg = pygame.image.load('player.png')
		
	def getAltura(self):
		return self.altura

	def getPulo(self):
		return self.pulo

	def setPositionX(self, adicionalValueX):
		self.paraX = self.paraX + adicionalValueX

	def setPositionY(self, adicionalValueY):
		self.paraY = self.paraY + adicionalValueY

	def getPositionX(self):
		return self.paraX

	def getPositionY(self):
		return self.paraY

	def getImage(self):
		return self.playerImg
		