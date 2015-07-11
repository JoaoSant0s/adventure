__author__ = 'Joao'

from adventure.Mapa import Map

class GlobalMap(object):
    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.graph_map = []
        self.maps = []

    def popular(self):
        white = (255, 255, 255)
        black = (0, 0, 0)
        self.graph_map.append([True, [1, 2, 3, 4]])
        self.graph_map.append([False, [5, 6, 0, 7]])
        enemies_map = []
        elements_map = []
        map0 = Map(white, enemies_map, elements_map)
        map1 = Map(black, enemies_map, elements_map)
        map2 = Map(white, enemies_map, elements_map)
        map3 = Map(black, enemies_map, elements_map)
        map4 = Map(white, enemies_map, elements_map)
        map5 = Map(black, enemies_map, elements_map)
        map6 = Map(white, enemies_map, elements_map)
        map7 = Map(black, enemies_map, elements_map)
        self.maps = [map0, map1, map2, map3, map4, map5, map6, map7]

    def set_current_map(self, localization, current_map_id):
        next_map = None
        limite = True
        try:
            self.graph_map[current_map_id][0] = False
            next_map_id = self.graph_map[current_map_id][1][localization]
            self.graph_map[next_map_id][0] = True
            next_map = self.maps[next_map_id]
            limite = False
        except Exception:
            print("Essa localizacao nao existe")
        if next_map is None:
            self.graph_map[current_map_id][0] = True
            next_map = self.maps[current_map_id]
        return next_map, limite

    def get_current_map(self):
        for cont, mapC in enumerate(self.graph_map):
            if mapC[0]:
                return self.maps[cont], cont

    def get_window_width(self):
        return self.window_width

    def get_window_height(self):
        return self.window_height
