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

    #metodo para el movimiento del personaje
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
            self.angle = 1.6
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
        #ENTRADA Y SALIDA CLASES PASILLO 1 
        if (wall_type_x == 75) or (wall_type_y == 75):
            
            self.game.change_map(COORDINACIONCONVIVENCIA)
            self.x, self.y = 6, 9
            self.angle = 4.6
        if (wall_type_x == 97) or (wall_type_y == 97):
            
            self.game.change_map(floor_one)
            self.x, self.y = 23, 16
            self.angle = 1.6
        if (wall_type_x == 69) or (wall_type_y == 69):
            
            self.game.change_map(SEGUNDOESOC)
            self.x, self.y = 1.5, 7
            self.angle = 4.6
        if (wall_type_x == 70) or (wall_type_y == 70):
            
            self.game.change_map(SEGUNDOESOC)
            self.x, self.y = 12.5, 7
            self.angle = 4.6
        if (wall_type_x == 100) or (wall_type_y == 100):
            
            self.game.change_map(floor_one)
            self.x, self.y = 9, 16
            self.angle = 1.6
        if (wall_type_x == 101) or (wall_type_y == 101):
            
            self.game.change_map(floor_one)
            self.x, self.y = 12, 16
            self.angle = 1.6
        if (wall_type_x == 71) or (wall_type_y == 71):
            
            self.game.change_map(SEGUNDOESOB)
            self.x, self.y = 1.5, 7
            self.angle = 4.6
        if (wall_type_x == 72) or (wall_type_y == 72):
            
            self.game.change_map(SEGUNDOESOB)
            self.x, self.y = 12.5, 7
            self.angle = 4.6
        if (wall_type_x == 102) or (wall_type_y == 102):
            
            self.game.change_map(floor_one)
            self.x, self.y = 13, 16
            self.angle = 1.6 
        if (wall_type_x == 103) or (wall_type_y == 103):
            
            self.game.change_map(floor_one)
            self.x, self.y = 16, 16
            self.angle = 1.6  
        if (wall_type_x == 73) or (wall_type_y == 73):
            
            self.game.change_map(SEGUNDOESOA)
            self.x, self.y = 1.5, 7
            self.angle = 4.6
        if (wall_type_x == 74) or (wall_type_y == 74):
            
            self.game.change_map(SEGUNDOESOA)
            self.x, self.y = 12.5, 7
            self.angle = 4.6
        if (wall_type_x == 104) or (wall_type_y == 104):
            
            self.game.change_map(floor_one)
            self.x, self.y = 17, 16
            self.angle = 1.6 
        if (wall_type_x == 105) or (wall_type_y == 105):
            
            self.game.change_map(floor_one)
            self.x, self.y = 21, 16
            self.angle = 1.6
        if (wall_type_x == 59) or (wall_type_y == 59):
            
            self.game.change_map(AULACONVIVENCIA)
            self.x, self.y = 1.5, 9
            self.angle = 4.6 
        if (wall_type_x == 106) or (wall_type_y == 106):
            
            self.game.change_map(floor_one)
            self.x, self.y = 23.5, 17
            self.angle = 4.6 
        if (wall_type_x == 61) or (wall_type_y == 61):
            
            self.game.change_map(CLASEUNOPASILLO1IZQUIERDA)
            self.x, self.y = 1.5, 7
            self.angle = 4.6
        if (wall_type_x == 107) or (wall_type_y == 107):
            
            self.game.change_map(floor_one)
            self.x, self.y = 21.5, 17
            self.angle = 4.6 
        if (wall_type_x == 108) or (wall_type_y == 108):
            
            self.game.change_map(floor_one)
            self.x, self.y = 18.5, 17
            self.angle = 4.6
        if (wall_type_x == 62) or (wall_type_y == 62):
            
            self.game.change_map(CLASEUNOPASILLO1IZQUIERDA)
            self.x, self.y = 12.5, 7
            self.angle = 4.6
        if (wall_type_x == 60) or (wall_type_y == 60):
            
            self.game.change_map(CLASEDOSPASILLO1IZQUIERDA)
            self.x, self.y = 1.5, 7
            self.angle = 4.6
        if (wall_type_x == 63) or (wall_type_y == 63):
            
            self.game.change_map(CLASEDOSPASILLO1IZQUIERDA)
            self.x, self.y = 12.5, 7
            self.angle = 4.6
        if (wall_type_x == 109) or (wall_type_y == 109):
            
            self.game.change_map(floor_one)
            self.x, self.y = 17.5, 17
            self.angle = 4.6
        if (wall_type_x == 110) or (wall_type_y == 110):
            
            self.game.change_map(floor_one)
            self.x, self.y = 14.5, 17
            self.angle = 4.6
        if (wall_type_x == 64) or (wall_type_y == 64):
            
            self.game.change_map(CLASETRESPASILLO1IZQUIERDA)
            self.x, self.y = 1.5, 7
            self.angle = 4.6
        if (wall_type_x == 65) or (wall_type_y == 65):
            
            self.game.change_map(CLASETRESPASILLO1IZQUIERDA)
            self.x, self.y = 12.5, 7
            self.angle = 4.6
        if (wall_type_x == 111) or (wall_type_y == 111):
            
            self.game.change_map(floor_one)
            self.x, self.y = 13.5, 17
            self.angle = 4.6
        if (wall_type_x == 112) or (wall_type_y == 112):
            
            self.game.change_map(floor_one)
            self.x, self.y = 10.5, 17
            self.angle = 4.6
        
        #ENTRADA Y SALIDA CLASES PASILLO 2
        if (wall_type_x == 83) or (wall_type_y == 83):
            
            self.game.change_map(BANIOPRIMEROSEGUNDAPLANTA)
            self.x, self.y = 2.5, 8
            self.angle = 4.6
        if (wall_type_x == 98) or (wall_type_y == 98):
            
            self.game.change_map(floor_one)
            self.x, self.y = 29.5, 4
            self.angle = 1.6
        if (wall_type_x == 84) or (wall_type_y == 84):
            
            self.game.change_map(BANIOSEGUNDOSEGUNDAPLANTA)
            self.x, self.y = 2.5, 8
            self.angle = 4.6
        if (wall_type_x == 99) or (wall_type_y == 99):
            
            self.game.change_map(floor_one)
            self.x, self.y = 30, 4
            self.angle = 1.6
        if (wall_type_x == 85) or (wall_type_y == 85):
            
            self.game.change_map(CLASEPRIMERAIZQUIERDA)
            self.x, self.y = 1.5, 7
            self.angle = 4.6
        if (wall_type_x == 86) or (wall_type_y == 86):
            
            self.game.change_map(CLASEPRIMERAIZQUIERDA)
            self.x, self.y = 8.5, 7
            self.angle = 4.6
        if (wall_type_x == 115) or (wall_type_y == 115):
            
            self.game.change_map(floor_one)
            self.x, self.y = 32, 5
            self.angle = 1.6
        if (wall_type_x == 116) or (wall_type_y == 116):
            
            self.game.change_map(floor_one)
            self.x, self.y = 36, 5
            self.angle = 1.6
        if (wall_type_x == 87) or (wall_type_y == 87):
            
            self.game.change_map(AULAINFORMATICA)
            self.x, self.y = 1.5, 9
            self.angle = 4.6
        if (wall_type_x == 117) or (wall_type_y == 117):
            
            self.game.change_map(floor_one)
            self.x, self.y = 37, 5
            self.angle = 1.6
        if (wall_type_x == 88) or (wall_type_y == 88):
            
            self.game.change_map(CLASETERCERAIZAQUIERDA)
            self.x, self.y = 1.5, 7
            self.angle = 4.6
        if (wall_type_x == 117) or (wall_type_y == 117):
            
            self.game.change_map(floor_one)
            self.x, self.y = 39, 5
            self.angle = 1.6
        if (wall_type_x == 89) or (wall_type_y == 89):
            
            self.game.change_map(CLASETERCERAIZAQUIERDA)
            self.x, self.y = 10.5, 7
            self.angle = 4.6
        if (wall_type_x == 118) or (wall_type_y == 118):
            
            self.game.change_map(floor_one)
            self.x, self.y = 42, 5
            self.angle = 1.6
        if (wall_type_x == 76) or (wall_type_y == 76):
            
            self.game.change_map(PRIMEROBCHA)
            self.x, self.y = 12.5, 7
            self.angle = 4.6
        if (wall_type_x == 77) or (wall_type_y == 77):
            
            self.game.change_map(PRIMEROBCHA)
            self.x, self.y = 1.5, 7
            self.angle = 4.6
        if (wall_type_x == 119) or (wall_type_y == 119):
            
            self.game.change_map(floor_one)
            self.x, self.y = 32.5, 6
            self.angle = 1.6
        if (wall_type_x == 120) or (wall_type_y == 120):
            
            self.game.change_map(floor_one)
            self.x, self.y = 28.5, 6
            self.angle = 4.6
        if (wall_type_x == 78) or (wall_type_y == 78):
            
            self.game.change_map(PRIMEROBCHB)
            self.x, self.y = 12.5, 7
            self.angle = 4.6
        if (wall_type_x == 79) or (wall_type_y == 79):
            
            self.game.change_map(PRIMEROBCHB)
            self.x, self.y = 1.5, 7
            self.angle = 4.6
        if (wall_type_x == 121) or (wall_type_y == 121):
            
            self.game.change_map(floor_one)
            self.x, self.y = 37, 6
            self.angle = 1.6
        if (wall_type_x == 122) or (wall_type_y == 122):
            
            self.game.change_map(floor_one)
            self.x, self.y = 33, 6
            self.angle = 4.6
        if (wall_type_x == 80) or (wall_type_y == 80):
            
            self.game.change_map(PRIMEROBCHC)
            self.x, self.y = 12.5, 7
            self.angle = 4.6
        if (wall_type_x == 81) or (wall_type_y == 81):
            
            self.game.change_map(PRIMEROBCHC)
            self.x, self.y = 1.5,7
            self.angle = 4.6
        if (wall_type_x == 123) or (wall_type_y == 123):
            
            self.game.change_map(floor_one)
            self.x, self.y = 42, 6
            self.angle = 1.6
        if (wall_type_x == 124) or (wall_type_y == 124):
            
            self.game.change_map(floor_one)
            self.x, self.y = 38, 6
            self.angle = 4.6
        
        
        

                

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