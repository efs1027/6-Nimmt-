import pygame as pg
import image
size = width, height = 400, 400  # ??????
sc = pg.display.set_mode(size)
table_desk = pg.image.load("C:/project/image/table_desk.jpg")
sc.fill((255, 255, 255))
rect = pg.Surface((100, 100))
running = True
while running:
   for event in pg.event.get():
      if event.type == pg.QUIT:
         running = False
   rect.blit(table_desk, (-300, -300))
   sc.blit(rect, (50, 50))
   pg.display.update()
pg.quit()  