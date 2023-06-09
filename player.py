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
            self.x, self.y = 1.5, 9
            self.angle = 4.7
        if (wall_type_x == 3) or (wall_type_y == 3):
            
            self.game.change_map(SEGUNDOFPB)
            self.x, self.y = 6, 9
            self.angle = 4.7
        if (wall_type_x == 8) or (wall_type_y == 8):
            
            self.game.change_map(BANIOS)
            self.x, self.y = 5, 9
            self.angle = 4.7
        if (wall_type_x == 55) or (wall_type_y == 55):
            
            self.game.change_map(BANIOS2)
            self.x, self.y = 5, 9
            self.angle = 4.7
        if (wall_type_x == 9) or (wall_type_y == 9):
            
            self.game.change_map(BIBLIOTECA)
            self.x, self.y = 2, 8
            self.angle = 4.7
        if (wall_type_x == 26) or (wall_type_y == 26):
            
            self.game.change_map(BIBLIOTECA)
            self.x, self.y = 11, 8
            self.angle = 4.7
        if (wall_type_x == 10) or (wall_type_y == 10):
            
            self.game.change_map(COCINA)
            self.x, self.y = 2, 7
            self.angle = 4.7
        if (wall_type_x == 11) or (wall_type_y == 11):
            
            self.game.change_map(CONSERJERIA)
            self.x, self.y = 1.5, 5
            self.angle = 4.6
        if (wall_type_x == 12) or (wall_type_y == 12):
            
            self.x, self.y = 1.5, 9
            self.game.change_map(DIRECCION)
            self.angle = 36.2
        if (wall_type_x == 13) or (wall_type_y == 13):

            self.x, self.y = 1.5, 8
            self.game.change_map(JEFATURA)
            self.angle = 36.2
        if (wall_type_x == 15) or (wall_type_y == 15):
            
            self.x, self.y = 4, 9
            self.game.change_map(LINCE)   
            self.angle = 36.2
        if (wall_type_x == 16) or (wall_type_y == 16):
            
            self.game.change_map(SALAPROFESORES)
            self.x, self.y = 1.5, 7
            self.angle = 4.7  
        if (wall_type_x == 54) or (wall_type_y == 54):
            
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
            
            self.x, self.y = 1.5, 9
            self.game.change_map(SECRETARIA) 
            self.angle = 4.7       
        if (wall_type_x == 20) or (wall_type_y == 20):
          
            self.x, self.y = 3, 9
            self.game.change_map(ORIENTACION)
            self.angle = 36.2   
        if (wall_type_x == 21) or (wall_type_y == 21):
            
            self.x, self.y = 2 , 9.5
            self.game.change_map(ALMACEN)
            self.angle = 4.7 
        #SALIDAS
        if (wall_type_x == 28) or (wall_type_y == 28):
            
            self.x, self.y = 3, 2.6
            self.game.change_map(floor_zero)
            self.angle = 6.3
        if (wall_type_x == 29) or (wall_type_y == 29):
            
            self.x, self.y = 6, 5.6
            self.game.change_map(floor_zero)
            self.angle = 6.3
        if (wall_type_x == 30) or (wall_type_y == 30):
            
            self.x, self.y = 11.5, 4.0
            self.game.change_map(floor_zero)
            self.angle = 9.2
        if (wall_type_x == 31) or (wall_type_y == 31):
            
            self.x, self.y = 11.5, 6.0
            self.game.change_map(floor_zero)
            self.angle = 9.2
        if (wall_type_x == 32) or (wall_type_y == 32):
            
            self.x, self.y = 20.5, 25.5
            self.game.change_map(floor_zero)
            self.angle = 9.2
        if (wall_type_x == 33) or (wall_type_y == 33):
            
            self.x, self.y = 11.5, 13.0
            self.game.change_map(floor_zero)
            self.angle = 9.2
        if (wall_type_x == 34) or (wall_type_y == 34):
            
            self.x, self.y = 11.5, 12.0
            self.game.change_map(floor_zero)
            self.angle = 9.2 
        if (wall_type_x == 35) or (wall_type_y == 35):
            
            self.x, self.y = 20.6, 32
            self.game.change_map(floor_zero)
            self.angle = 9.2
        if (wall_type_x == 36) or (wall_type_y == 36):
            
            self.x, self.y = 20.6, 26
            self.game.change_map(floor_zero)
            self.angle = 4.6 
        if (wall_type_x == 37) or (wall_type_y == 37):
            
            self.x, self.y = 11.5, 11
            self.game.change_map(floor_zero)
            self.angle = 9.2
        if (wall_type_x == 38) or (wall_type_y == 38):
            
            self.x, self.y = 11.5, 9.0
            self.game.change_map(floor_zero)
            self.angle = 6.2
        if (wall_type_x == 39) or (wall_type_y == 39):
            
            self.x, self.y = 8.5, 5
            self.game.change_map(floor_zero)
            self.angle = 4.6
        if (wall_type_x == 40) or (wall_type_y == 40):
            
            self.x, self.y = 11.5, 8
            self.game.change_map(floor_zero)
            self.angle = 9.2  
        if (wall_type_x == 41) or (wall_type_y == 41):
            
            self.x, self.y = 11.5, 9
            self.game.change_map(floor_zero)
            self.angle = 9.2 
        if (wall_type_x == 42) or (wall_type_y == 42):
            
            self.x, self.y = 14.6, 23
            self.game.change_map(floor_zero)
            self.angle = 4.6  
        if (wall_type_x == 43) or (wall_type_y == 43):
            
            self.x, self.y = 11.5, 18
            self.game.change_map(floor_zero)
            self.angle = 6.2
        if (wall_type_x == 44) or (wall_type_y == 44):
            
            self.x, self.y = 11.5, 15.0
            self.game.change_map(floor_zero)
            self.angle = 6.2
        if (wall_type_x == 45) or (wall_type_y == 45):
            
            self.x, self.y = 11.5, 15.0
            self.game.change_map(floor_zero)
            self.angle = 9.2 
        if (wall_type_x == 46) or (wall_type_y == 46):
            
            self.x, self.y = 11.5, 13.0
            self.game.change_map(floor_zero)
            self.angle = 6.2 
        if (wall_type_x == 47) or (wall_type_y == 47):
            
            self.x, self.y = 20.6, 33.0
            self.game.change_map(floor_zero)
            self.angle = 6.2
        if (wall_type_x == 53) or (wall_type_y == 53):
            
            self.x, self.y = 11.5, 7
            self.game.change_map(floor_zero)
            self.angle = 6.2
        if (wall_type_x == 56) or (wall_type_y == 56):
            self.x, self.y = 20.6, 27.5
            self.game.change_map(floor_zero)
            self.angle = 9.2
        if (wall_type_x == 57) or (wall_type_y == 57):
            self.x, self.y = 20.6, 33.5
            self.game.change_map(floor_zero)
            self.angle = 9.2
        if (wall_type_x == 58) or (wall_type_y == 58):
            self.x, self.y = 8.5, 7
            self.game.change_map(COCINA)
            self.angle = 4.7
        # SEGUNDA PLANTA
        if (wall_type_x == 90) or (wall_type_y == 90):
            
            self.game.change_map(floor_one)
            self.x, self.y = 26, 4
            self.angle = 1.6
        if (wall_type_x == 91) or (wall_type_y == 91):
            
            self.game.change_map(floor_one)
            self.x, self.y = 26, 18
            self.angle = 4.7    
        if (wall_type_x == 92) or (wall_type_y == 92):
            
            self.game.change_map(floor_one)
            self.x, self.y = 3, 15
            self.angle = 4.7
        if (wall_type_x == 93) or (wall_type_y == 93):
            
            self.game.change_map(floor_zero)
            self.x, self.y = 11, 20
            self.angle = 6.2
        if (wall_type_x == 95) or (wall_type_y == 95):
            
            self.game.change_map(floor_zero)
            self.x, self.y = 20, 22
            self.angle = 9.2  
        if (wall_type_x == 66) or (wall_type_y == 66):
            
            self.game.change_map(floor_zero)
            self.x, self.y = 13, 2
            self.angle = 9.2      
                

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