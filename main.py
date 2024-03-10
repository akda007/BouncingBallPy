import random
import pygame as pg
from ball import *
from pygame import gfxdraw
import time

def get_time_mil():
    return time.time() * 1000.0

s_width, s_heigth = 1600, 900

circle_radius = (int)(s_heigth/2) - 30
x = (int)(s_width / 2)
y = (int)(s_heigth / 2)


balls = []


init_time = 56000

pg.init()
screen = pg.display.set_mode((s_width, s_heigth))
clock = pg.time.Clock()
running = True
dt = 0


while running:
    if (get_time_mil() - init_time > 5000):
        balls.append(Ball(x, y, random.randint(-300, 300), random.randint(-300,300), random.randint(20, 45)))
        init_time = get_time_mil()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    screen.fill('black')
    gfxdraw.circle(screen, x, y, circle_radius, (255, 255, 255, 255))




    dt = clock.tick(60) / 1000

    for ball in balls:
        ball.gravity(dt)
        ball.move(x, y, circle_radius, dt)
        ball.draw(screen)
    

    pg.display.flip()

