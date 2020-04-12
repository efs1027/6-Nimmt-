#a = "電腦" + str(2)
#print(a)
#b = a.split("電腦",1)
#print(b[-1])

import pygame as pg
pg.display.set_caption("?????")
size = WIDTH, HEIGHT = 600, 600  # ??????
sc = pg.display.set_mode(size)  # ????

r_w = WIDTH/1440
r_h = HEIGHT/1440
r = (r_w+r_h)/2  # ????

def draw4(n): # ???????
   pg.draw.rect(sc, (255,255,255), [r_w*(500+n*50), 10*r_h, 42*r_w, 58*r_h]) #top
   pg.draw.rect(sc, (255,255,255), [10*r_w, HEIGHT-r_h*(500+n*50), 58*r_w, 42*r_h]) #left
   pg.draw.rect(sc, (255,255,255), [WIDTH-r_w*(500+n*50), HEIGHT-70*r_h, 42*r_w, 58*r_h]) #bottom
   pg.draw.rect(sc, (255,255,255), [WIDTH-70*r_w, r_h*(500+n*50), 58*r_w, 42*r_h]) #right
   # num = number.render(str(player_card[9-n]), True, (0,0,0))
   # sc.blit(num, (WIDTH-r_w*(490+n*50), HEIGHT-(70-15)*r_h))
   pg.display.update()
   pg.time.delay(30)

title = True
while title: # ????:logo?New Game
   for event in pg.event.get():
        if event.type == pg.QUIT:
            title = False
   for i in range(10):
      draw4(i)

    