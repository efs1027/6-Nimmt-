# standard Python
import pygame as pg, add_module_path as ModAdd

ModAdd.path_append()
import color as colors, image, BGM

from sys import exit

from pygame.locals import *

pg.init()  # 初始化pygame

pg.display.set_caption("誰是牛頭王")
size = width, height = 1440, 720  # 設定視窗大小
screen = pg.display.set_mode(size)  # 顯示視窗

bg = pg.Surface(screen.get_size())
bg = bg.convert()

desk = pg.image.load(image.desk)
desk.convert()
logo = pg.image.load(image.logo)
logo.convert()
text = pg.font.SysFont("Arial", 72)
t1 = text.render("New Game", True, colors.BLACK)

bg.blit(desk, (0, 0))
bg.blit(logo, (500, 170))
bg.blit(t1, (600, 600))
screen.blit(bg, (0, 0))
pg.display.update()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()