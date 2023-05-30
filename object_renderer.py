import pygame as pg
from settings import *


class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        self.sky_image = self.get_texture('resources/textures/blacksky.png', (WIDTH, HALF_HEIGHT))
        self.sky_offset = 0
       

    def draw(self):
        self.draw_background()
        self.render_game_objects()

    def draw_background(self):
        self.sky_offset = (self.sky_offset + 4.5 * self.game.player.rel) % WIDTH
        self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        self.screen.blit(self.sky_image, (-self.sky_offset + WIDTH, 0))
        # floor
        pg.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGHT, WIDTH, HEIGHT))

    def render_game_objects(self):
        list_objects = sorted(self.game.raycasting.objects_to_render, key=lambda t: t[0], reverse=True)
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)

    def load_wall_textures(self):
        return {
            1: self.get_texture('resources/textures/1.png'),
            2: self.get_texture('resources/textures/PUERTACONPARED.png'),
            3: self.get_texture('resources/textures/2FPB.png'),
            7: self.get_texture('resources/textures/2ºDAM.png'),
            5: self.get_texture('resources/textures/1DAM.png'),
            6: self.get_texture('resources/textures/1FPB.png'),
            8: self.get_texture('resources/textures/BAÑOS.png'),
            9: self.get_texture('resources/textures/BIBLIOTECA.png'),
            26: self.get_texture('resources/textures/BIBLIOTECA.png'),
            10: self.get_texture('resources/textures/COCINA.png'),
            11: self.get_texture('resources/textures/CONSERJERIA.png'),
            12: self.get_texture('resources/textures/DIRECCION.png'),
            13: self.get_texture('resources/textures/JEFATURA.png'),
            15: self.get_texture('resources/textures/LINCE.png'),
            16: self.get_texture('resources/textures/SALAPROFESORES.png'),
            27: self.get_texture('resources/textures/SALAPROFESORES.png'),
            17: self.get_texture('resources/textures/SALAVISITAS.png'),
            18: self.get_texture('resources/textures/SALON DE ACTOS.png'),
            27: self.get_texture('resources/textures/SALON DE ACTOS.png'),
            19: self.get_texture('resources/textures/SECRETARIA.png'),
            20: self.get_texture('resources/textures/ORIENTACION.png'),
            21: self.get_texture('resources/textures/ALMACEN.png'),
            22: self.get_texture('resources/textures/UNIDADPUERTACRISTAL.png'),
            23: self.get_texture('resources/textures/UNIDADPUERTACRISTALALREVES.png'),
            24: self.get_texture('resources/textures/SECRETARIACRISTALERA.jpg'),
            25: self.get_texture('resources/textures/mitadpared.png'),
            #salidas de puerta cuando entras a habitacion
            28: self.get_texture('resources/textures/PUERTACONPARED.png'),
            29: self.get_texture('resources/textures/PUERTACONPARED.png'),
            30: self.get_texture('resources/textures/PUERTACONPARED.png'),
            31: self.get_texture('resources/textures/PUERTACONPARED.png'),
            32: self.get_texture('resources/textures/PUERTACONPARED.png'),
            33: self.get_texture('resources/textures/PUERTACONPARED.png'),
            34: self.get_texture('resources/textures/PUERTACONPARED.png'),
            35: self.get_texture('resources/textures/PUERTACONPARED.png'),
            36: self.get_texture('resources/textures/PUERTACONPARED.png'),
            37: self.get_texture('resources/textures/PUERTACONPARED.png'),
            38: self.get_texture('resources/textures/PUERTACONPARED.png'),
            39: self.get_texture('resources/textures/PUERTACONPARED.png'),
            40: self.get_texture('resources/textures/PUERTACONPARED.png'),
            41: self.get_texture('resources/textures/PUERTACONPARED.png'),
            42: self.get_texture('resources/textures/PUERTACONPARED.png'),
            43: self.get_texture('resources/textures/PUERTACONPARED.png'),
            44: self.get_texture('resources/textures/PUERTACONPARED.png'),
            45: self.get_texture('resources/textures/PUERTACONPARED.png'),
            46: self.get_texture('resources/textures/PUERTACONPARED.png'),
            #DECORACIONES
            47: self.get_texture('resources/textures/PUERTACONPARED.png'),
            48: self.get_texture('resources/textures/PAREDDECORADA.png'),
            49: self.get_texture('resources/textures/PAREDESPEJO.png'),
            50: self.get_texture('resources/textures/PAREDCUADRO.png'),
            51: self.get_texture('resources/textures/ventana.png'),
            52: self.get_texture('resources/textures/PUERTAEXIT.png'),
            53: self.get_texture('resources/textures/PUERTACONPARED.png')

        }
