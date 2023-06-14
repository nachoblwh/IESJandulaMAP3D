import pygame as pg

#Esta clase será la encargada del sonido del juego.

class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sound/'
        self.theme = pg.mixer.music.load(self.path + 'theme2.mp3')
        pg.mixer.music.set_volume(0.4)