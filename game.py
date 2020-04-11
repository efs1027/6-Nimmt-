import pygame as pg, random

import GameOperate.one_player as OneP
pg.init()

pg.display.set_caption("誰是牛頭王")
size = WIDTH, HEIGHT = 1440, 720  # 設定視窗大小
sc = pg.display.set_mode(size)  # 顯示視窗

r_w = WIDTH/1440
r_h = HEIGHT/720
r = (r_w+r_h)/2  # 比例常數
card_base = [1]
card_dict = {1: 1}

game = True
game_start = False
Playing = False
start_stage = False
select_stage = False

def assign(): # 發牌動畫
    M = 8
    for n in range(M):
        sc.blit(desk, (0, 0))
        centerx = WIDTH/2-21*r_w
        centery = HEIGHT/2-29*r_h
        ds = (WIDTH+HEIGHT+100)/(2 * M)  # 取長寬的平均再分割做ds
        pg.draw.rect(sc, WHITE, [centerx, centery-ds*n*r_h-7*r_w, 42*r_w, 58*r_h])  # top
        pg.draw.rect(sc, WHITE, [centerx-ds*n*r_w*2-7*r_w, centery, 58*r_w, 42*r_h])  # left
        pg.draw.rect(sc, WHITE, [centerx, centery+ds*n*r_h-7*r_w, 42*r_w, 58*r_h])  # bottom
        pg.draw.rect(sc, WHITE, [centerx+ds*n*r_w*2-7*r_w, centery, 58*r_w, 42*r_h])  # right
        pg.display.update()

global update  # 偵測是否按下方向鍵
update = 1
number = pg.font.SysFont("simhei", int(36*r))
def draw4(n, upd): # 四方位單張攤牌
    if upd:
        pg.draw.rect(sc, WHITE, [r_w*(490+n*50), 10*r_h, 42*r_w, 58*r_h]) #top
        pg.draw.rect(sc, WHITE, [10*r_w, HEIGHT-r_h*(150+n*50), 58*r_w, 42*r_h]) #left
        pg.draw.rect(sc, WHITE, [WIDTH-r_w*(490+n*50), HEIGHT-70*r_h, 42*r_w, 58*r_h]) #bottom
        pg.draw.rect(sc, WHITE, [WIDTH-70*r_w, r_h*(110+n*50), 58*r_w, 42*r_h]) #right
        num = number.render(str(player_card[9-n]), True, BLACK)
        sc.blit(num, (WIDTH-r_w*(490+n*50), HEIGHT-(70-15)*r_h))

def draw_base(m, n, upd): # 四張牌頭
    if upd:
        x = 1100*r_w
        y = 200*r_h
        pg.draw.rect(sc, WHITE, [x-m*60*r_w, y+n*80*r_h, 42*r_w, 58*r_h])
        num = number.render(str(card_base[41+n]), True, BLACK)
        sc.blit(num, (1100*r_w, (200+15)*r_h+n*80*r_h))

def card_update(upd, gra): # upd: update 此函數內部專用的update變數, gra: gradually 逐漸變化
    for n in range(10):
        draw4(n, upd)
        if gra:
            pg.display.update()
            pg.time.delay(10)
    for n in range(4):
        draw_base(0, n, upd)
        if gra:
            pg.display.update()
            pg.time.delay(25)
    update = 0

clock = pg.time.Clock()
title = True
playing = False
while title: # 第一階段:logo與New Game
    for event in pg.event.get():
        if event.type == pg.QUIT:
            title = False
    start_game = pg.mouse.get_pressed()
    if start_game[0] and game_start == False:
        fade(1440, 720)
        start_stage = True
        game_start = True
    if game_start and start_stage:
        clock.tick(100)
        start_stage = False
        select_stage = True
        title = False
        playing = True

l = 0  # locate
def draw_sel(l):  # select 選牌框
    thick = 3
    x = WIDTH-(490+l*50+1)*r_w
    y = HEIGHT-(70+1)*r_h
    pg.draw.line(sc, RED, (x, y), (x+10*r_w, y), thick)
    pg.draw.line(sc, RED, (x, y), (x, y+20*r_h), thick)
    pg.draw.line(sc, RED, (x+32*r_w, y), (x+42*r_w, y), thick)
    pg.draw.line(sc, RED, (x+42*r_w, y), (x+42*r_w, y+20*r_h), thick)
    pg.draw.line(sc, RED, (x, y+58*r_h), (x+10*r_w, y+58*r_h), thick)
    pg.draw.line(sc, RED, (x, y+38*r_h), (x, y+58*r_h), thick)
    pg.draw.line(sc, RED, (x+32*r_w, y+58*r_h), (x+42*r_w, y+58*r_h), thick)
    pg.draw.line(sc, RED, (x+42*r_w, y+38*r_h), (x+42*r_w, y+58*r_h), thick)


OneP.play_easy()
player_card = card_base[31: 41: 1]
pile = card_base[45: 105: 1]
order = 0  # 牌堆順序

for n in range(10): # 發牌
    assign()
card_update(update, gra=1)
draw_sel(l)
pg.display.update()

while playing: # 第二階段:遊戲進行
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        sc.blit(desk, (0, 0))
        l += 1
        if l >= 10:
            l -= 1
        update = 1
        pg.time.delay(50)
    elif keys[pg.K_RIGHT]:
        sc.blit(desk, (0, 0))
        l -= 1
        if l <= -1:
            l += 1
        update = 1
        pg.time.delay(40)
    elif keys[pg.K_SPACE]:
        player_card[9-l] = pile[order]
        order += 1
        draw_base(order,1,update)
        num = number.render(str(player_card[9-l]), True, BLACK)
        sc.blit(num, ((1100-60*order)*r_w,(200+15)*r_h+1*80*r_h))
        update = 1
        pg.time.delay(150)
    card_update(update, gra=0)
    draw_sel(l)
    pg.display.update()
pg.quit()

