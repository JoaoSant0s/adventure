__author__ = 'Joao'

import pygame

class Link(object):
    def __init__(self, largura, altura, para_x, para_y):
        self.largura = largura
        self.altura = altura
        self.para_x = para_x
        self.para_y = para_y

    def get_altura(self):
        return self.altura

    def get_largura(self):
        return self.largura

    def set_position_x(self, adicional_value_x):
        self.para_x = self.para_x + adicional_value_x

    def set_position_y(self, adicional_value_y):
        self.para_y = self.para_y + adicional_value_y

    def get_position_x(self):
        return self.para_x

    def get_position_y(self):
        return self.para_y

    def move(self):
        pygame.event.pump()
        key = pygame.key.get_pressed()
        self.set_position_x(3 * (key[pygame.K_RIGHT] - key[pygame.K_LEFT]))
        self.set_position_y(3 * (key[pygame.K_DOWN] - key[pygame.K_UP]))


class Inimigo(object):
    def __init__(self, largura, altura,  para_x, para_y):
        self.largura = largura
        self.altura = altura
        self.para_x = para_x
        self.para_y = para_y

    def get_altura(self):
        return self.altura

    def get_largura(self):
        return self.largura

    def set_position_x(self, adicional_value_x):
        self.para_x = self.para_x + adicional_value_x

    def set_position_y(self, adicional_value_y):
        self.para_y = self.para_y + adicional_value_y

    def get_position_x(self):
        return self.para_x

    def get_position_y(self):
        return self.para_y
