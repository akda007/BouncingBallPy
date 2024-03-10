import pygame as pg
from random import randint
import math

class Ball:
    def __init__(self, x, y, vel_x = 300, vel_y= 300, radius = 30):
        self.pos = [x, y]
        self.r = radius
        self.float = 0
        self.speed_x, self.speed_y = vel_x, vel_y
        self.damping = 1.01 # Damping factor to gradually reduce speed
        self.color = (randint(0,255),randint(0,255),randint(0,255))


    def collision(self):
        None
        # self.r += 1

    def gravity(self, dt):
        
        self.speed_y += 1000 * dt

    def move(self, border_x, border_y, border_r, dt):
        distance = math.sqrt((self.pos[0] - border_x)**2 + (self.pos[1] - border_y)**2)
        
        if distance >= border_r - self.r:
            self.collision()
            
            
            n_x = (self.pos[0] - border_x) / distance
            n_y = (self.pos[1] - border_y) / distance

            product = 2 * (self.speed_x * n_x + self.speed_y * n_y)

            self.speed_x -= product * n_x
            self.speed_y -= product * n_y
            
            self.speed_x *= self.damping
            self.speed_y *= self.damping

            
            # self.pos[0] = self.pos[0] - (self.r if self.pos[0] >= 0 else -self.r)
            # self.pos[1] = self.pos[1] - (self.r if self.pos[1] >= 0 else -self.r)


        self.pos[0] += self.speed_x * dt
        self.pos[1] += self.speed_y * dt
        
    def draw(self, surface):
        pg.draw.circle(surface, self.color, self.pos, self.r)
        

        
    

    