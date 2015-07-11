__author__ = 'Joao'

class Map(object):
    def __init__(self, color, enemies_map, elements_map):
        self.color = color
        self.enemies_map = enemies_map #com posicao
        self.elements_map = elements_map #com posicao

class MapElement(object):
    def __init__(self, type, x, y):
        self.type = type
        self.x = x
        self.y = y
