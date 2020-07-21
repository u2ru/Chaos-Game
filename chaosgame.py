import pygame as pg

import random
import time

pg.init()

pg.font.init()

font = pg.font.SysFont('Comic Sans MS', 16)

screen = (400,400)

black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)

dot1 = (200,100) # A
dot2 = (100,300) # B
dot3 = (random.randint(0,screen[0]), random.randint(0,screen[1])) # C

dots = (dot1, dot2, dot3)

display = pg.display.set_mode(screen)
display.fill(black)

display.set_at((dots[0][0], dots[0][1]), green)
display.set_at((dots[1][0], dots[1][1]), green)
display.set_at((dots[2][0], dots[2][1]), green)

a = font.render('A', False, red)
display.blit(a,(dots[0][0]-16,dots[0][1]-16))

b = font.render('B', False, red)
display.blit(b,(dots[1][0]-16,dots[1][1]-16))

c = font.render('C', False, red)
display.blit(c,(dots[2][0],dots[2][1]))

startx = random.randint(0,400)
starty = random.randint(0,400)

startpts = font.render("Starting points X: " + str(startx) + " Y: " + str(starty), False, white)
display.blit(startpts,(0,0))

ap = font.render('A('+str(dot1[0])+','+str(dot1[1])+')', False, green)
bp = font.render('B('+str(dot2[0])+','+str(dot2[1])+')', False, green)
cp = font.render('C('+str(dot3[0])+','+str(dot3[1])+')', False, green)
display.blit(ap,(0,60))
display.blit(bp,(0,80))
display.blit(cp,(0,100))

display.set_at((startx,startx), white)

def vert(x,y):
    global startx, starty
    r = random.randint(0,2) # random A B or C
    zx = x+(dots[r][0]-x)//2 # center between x2 and x1 || y2 and y1
    zy = y+(dots[r][1]-y)//2
    display.set_at((zx, zy), white) # ploting new dot
    startx = zx
    starty = zy

i=0

iteration = font.render("Iteration: " + str(i), False, white)
display.blit(iteration,(0,30))

iter=500

while i <= iter:
    if i == iter:
        pg.image.save(display, 'image.jpg')
    i = i + 1
    pg.display.flip()
    pg.draw.rect(display, black, (0,30,150,20))
    iteration = font.render("Iteration: " + str(i), False, white)
    display.blit(iteration,(0,30))
    time.sleep(0.03)
    vert(startx,starty)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()

    pg.display.update()