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

    """
                 y <= 0
                ---------
     x <= 0     |       *  x > window_width
                |       *
                |       *
                *********
                    y > window_height
    """

    def location_map(self, global_map):
        map_default, current_map_id = global_map.get_current_map()
        #print(str(self.para_x) + " " + str(self.para_y))

        if self.para_y <= 0:
            map_default, limite = global_map.set_current_map(0, current_map_id)
            if limite:
                self.para_y = 0
            else:
                self.para_y = 590
        if self.para_x >= global_map.get_window_width() - self.largura:
            map_default, limite = global_map.set_current_map(1, current_map_id)
            if limite:
                self.para_x = global_map.get_window_width() - self.largura
            else:
                self.para_x = 10
        if self.para_y >= global_map.get_window_height():
            map_default, limite = global_map.set_current_map(2, current_map_id)
            if limite:
                self.para_y = global_map.get_window_height()
            else:
                self.para_y = 10
        if self.para_x <= 0:
            map_default, limite = global_map.set_current_map(3, current_map_id)
            if limite:
                self.para_x = 0
            else:
                self.para_x = 790
        return map_default

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
