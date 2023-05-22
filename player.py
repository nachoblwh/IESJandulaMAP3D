from settings import *
import pygame as pg
import math

from maps import * 
from settings import PLAYER_POS


class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.rel = 0
        self.time_prev = pg.time.get_ticks()
        # diagonal movement correction
        self.diag_move_corr = 1 / math.sqrt(2)


    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()
        num_key_pressed = -1
        if keys[pg.K_w]:
            num_key_pressed += 1
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            num_key_pressed += 1
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            num_key_pressed += 1
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            num_key_pressed += 1
            dx += -speed_sin
            dy += speed_cos

        # diag move correction
        if num_key_pressed:
            dx *= self.diag_move_corr
            dy *= self.diag_move_corr

        wall_type_x, wall_type_y = self.check_wall_collision(dx, dy)

        print(f'wall_type_x: {wall_type_x}, wall_type_y: {wall_type_y}')
        #if (wall_type_x != -1 and wall_type_x != 1) or (wall_type_y != -1 and wall_type_y != 1):
        if (wall_type_x == 5) or (wall_type_y == 5):

            self.game.change_map(PRIMERODAM)
            self.x, self.y = 7.5, 10
            self.angle = 4.7
        if (wall_type_x == 7) or (wall_type_y == 7):

            self.game.change_map(SEGUNDODAM)
            self.x, self.y = 6.5, 9
            self.angle = 4.7
        if (wall_type_x == 6) or (wall_type_y == 6):

            self.game.change_map(PRIMEROFPB)
            self.x, self.y = 1, 9
            self.angle = 4.7
        if (wall_type_x == 3) or (wall_type_y == 3):
            
            self.game.change_map(SEGUNDOFPB)
            self.x, self.y = 6, 9
            self.angle = 4.7
        if (wall_type_x == 8) or (wall_type_y == 8):
            
            self.game.change_map(BANIOS)
            self.x, self.y = 5, 9
            self.angle = 4.7
        if (wall_type_x == 9) or (wall_type_y == 9):
            
            self.game.change_map(BIBLIOTECA)
            self.x, self.y = 11, 9
        if (wall_type_x == 10) or (wall_type_y == 10):
            
            self.game.change_map(COCINA)
            self.x, self.y = 2, 7
            self.angle = 4.7
        if (wall_type_x == 11) or (wall_type_y == 11):
            
            self.game.change_map(CONSERJERIA)
            self.x, self.y = 1.5, 5
            self.angle = 4.6
        if (wall_type_x == 12) or (wall_type_y == 12):
            
            self.game.change_map(DIRECCION)
        if (wall_type_x == 13) or (wall_type_y == 13):
            
            self.game.change_map(JEFATURA)
        if (wall_type_x == 15) or (wall_type_y == 15):
            
            self.game.change_map(LINCE)   
        if (wall_type_x == 16) or (wall_type_y == 16):
            
            self.game.change_map(SALAPROFESORES)
            self.x, self.y = 1, 7
            self.angle = 4.7  
        if (wall_type_x == 27) or (wall_type_y == 27):
            
            self.game.change_map(SALAPROFESORES)
            self.x, self.y = 11, 7
            self.angle = 4.7     
        if (wall_type_x == 17) or (wall_type_y == 17):
            
            self.game.change_map(SALAVISITAS) 
            self.x, self.y = 2, 6       
            self.angle = 4.8
        if (wall_type_x == 18) or (wall_type_y == 18):
            
            self.x, self.y = 2.5, 9
            self.game.change_map(SALONDEACTOS)
            self.angle = 4.7
        if (wall_type_x == 27) or (wall_type_y == 27):
            
            self.x, self.y = 12, 9
            self.game.change_map(SALONDEACTOS) 
            self.angle = 4.7       
        if (wall_type_x == 19) or (wall_type_y == 19):
            
            self.game.change_map(SECRETARIA)       
        if (wall_type_x == 20) or (wall_type_y == 20):
          
            self.game.change_map(ORIENTACION)    
        if (wall_type_x == 21) or (wall_type_y == 21):
            
            self.game.change_map(ALMACEN)           
        self.angle %= math.tau


    # COLLISIONS 
    def check_walk_available(self, x, y):
        
        walk_available = (x, y) not in self.game.map.world_map
        wall_type      = -1

        if not walk_available:

            wall_type = self.game.map.world_map[(x, y)]
        
        return walk_available, wall_type

    def check_wall_collision(self, dx, dy):
        scale = PLAYER_SIZE_SCALE / self.game.delta_time
        
        walk_available, wall_type_x = self.check_walk_available(int(self.x + dx * scale), int(self.y))
        if walk_available:
            self.x += dx
        
        walk_available, wall_type_y = self.check_walk_available(int(self.x), int(self.y + dy * scale))
        if walk_available:
            self.y += dy
        
        return wall_type_x, wall_type_y

    def mouse_control(self):
        mx, my = pg.mouse.get_pos()
        if mx < MOUSE_BORDER_LEFT or mx > MOUSE_BORDER_RIGHT:
            pg.mouse.set_pos([HALF_WIDTH, HALF_HEIGHT])
        self.rel = pg.mouse.get_rel()[0]
        self.rel = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, self.rel))
        self.angle += self.rel * MOUSE_SENSITIVITY * self.game.delta_time

    def update(self):
        self.movement()
        self.mouse_control()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)