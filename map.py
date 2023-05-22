import pygame as pg

class Map:
    def __init__(self, map_array):

        self.change_map(map_array)

    def draw(self):
        [pg.draw.rect(self.game.screen, 'darkgray', (pos[0] * 100, pos[1] * 100, 100, 100), 2)
         for pos in self.world_map]
        
    def change_map(self, new_map_array, ):

        self.map_array = new_map_array
        self.world_map = {}
        self.rows = len(self.map_array)
        self.cols = len(self.map_array[0])

        # We are going to get the map
        for j, row in enumerate(self.map_array):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value
