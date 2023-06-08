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
            #PLANTA BAJA
            1: self.get_texture('resources/textures/1.png'),
            2: self.get_texture('resources/textures/PUERTACONPARED.png'),
            3: self.get_texture('resources/textures/2FPB.png'),
            7: self.get_texture('resources/textures/2ºDAM.png'),
            5: self.get_texture('resources/textures/1DAM.png'),
            6: self.get_texture('resources/textures/1FPB.png'),
            55: self.get_texture('resources/textures/BAÑOS.png'),
            8: self.get_texture('resources/textures/BAÑOS.png'),
            9: self.get_texture('resources/textures/BIBLIOTECA.png'),
            26: self.get_texture('resources/textures/BIBLIOTECA.png'),
            10: self.get_texture('resources/textures/COCINA.png'),
            11: self.get_texture('resources/textures/CONSERJERIA.png'),
            12: self.get_texture('resources/textures/DIRECCION.png'),
            13: self.get_texture('resources/textures/JEFATURA.png'),
            15: self.get_texture('resources/textures/LINCE.png'),
            16: self.get_texture('resources/textures/SALAPROFESORES.png'),
            54: self.get_texture('resources/textures/SALAPROFESORES.png'),
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
            #ESCALERAS PASILLO 1
            90: self.get_texture('resources/textures/PUERTASUBIRESCALERAS.jpg'),
            91: self.get_texture('resources/textures/PUERTASUBIRESCALERAS.jpg'),
            92: self.get_texture('resources/textures/PUERTASUBIRESCALERAS.jpg'),
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
            56: self.get_texture('resources/textures/PUERTACONPARED.png'),
            57: self.get_texture('resources/textures/PUERTACONPARED.png'),
            58: self.get_texture('resources/textures/COCINA.png'),
            #DECORACIONES
            47: self.get_texture('resources/textures/PUERTACONPARED.png'),
            48: self.get_texture('resources/textures/PAREDDECORADA.png'),
            49: self.get_texture('resources/textures/PAREDESPEJO.png'),
            50: self.get_texture('resources/textures/PAREDCUADRO.png'),
            51: self.get_texture('resources/textures/ventana.png'),
            52: self.get_texture('resources/textures/PUERTAEXIT.png'),
            53: self.get_texture('resources/textures/PUERTACONPARED.png'),
            #SEGUNDA PLANTA
            #ESCALERAS PASILLO 1
            93: self.get_texture('resources/textures/PUERTABAJARESCALERAS.jpg'),
            94: self.get_texture('resources/textures/PUERTASUBIRESCALERAS.jpg'),
            #PASILLO 1
            59: self.get_texture('resources/textures/PUERTACONPARED.png'),
            60: self.get_texture('resources/textures/PUERTACONPARED.png'),
            61: self.get_texture('resources/textures/PUERTACONPARED.png'),
            62: self.get_texture('resources/textures/PUERTACONPARED.png'),
            63: self.get_texture('resources/textures/PUERTACONPARED.png'),
            64: self.get_texture('resources/textures/PUERTACONPARED.png'),
            65: self.get_texture('resources/textures/PUERTACONPARED.png'),
            66: self.get_texture('resources/textures/PUERTABAJARESCALERAS.jpg'),
            67: self.get_texture('resources/textures/PUERTASUBIRESCALERAS.jpg'),
            68: self.get_texture('resources/textures/PUERTACONPARED.png'),
            69: self.get_texture('resources/textures/PUERTACONPARED.png'),
            70: self.get_texture('resources/textures/PUERTACONPARED.png'),
            71: self.get_texture('resources/textures/PUERTACONPARED.png'),
            72: self.get_texture('resources/textures/PUERTACONPARED.png'),
            73: self.get_texture('resources/textures/PUERTACONPARED.png'),
            74: self.get_texture('resources/textures/PUERTACONPARED.png'),
            75: self.get_texture('resources/textures/PUERTACONPARED.png'),
            #ESCALERAS PASILLO 2
            95: self.get_texture('resources/textures/PUERTABAJARESCALERAS.jpg'),
            96: self.get_texture('resources/textures/PUERTASUBIRESCALERAS.jpg'),
            #PASILLO 2
            76: self.get_texture('resources/textures/PUERTACONPARED.png'),
            77: self.get_texture('resources/textures/PUERTACONPARED.png'),
            78: self.get_texture('resources/textures/PUERTACONPARED.png'),
            79: self.get_texture('resources/textures/PUERTACONPARED.png'),
            80: self.get_texture('resources/textures/PUERTACONPARED.png'),
            81: self.get_texture('resources/textures/PUERTACONPARED.png'),
            82: self.get_texture('resources/textures/PUERTACONPARED.png'),
            83: self.get_texture('resources/textures/PUERTACONPARED.png'),
            84: self.get_texture('resources/textures/PUERTACONPARED.png'),
            85: self.get_texture('resources/textures/PUERTACONPARED.png'),
            86: self.get_texture('resources/textures/PUERTACONPARED.png'),
            87: self.get_texture('resources/textures/PUERTACONPARED.png'),
            88: self.get_texture('resources/textures/PUERTACONPARED.png'),
            89: self.get_texture('resources/textures/PUERTACONPARED.png'),
            
        }
