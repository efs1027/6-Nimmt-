# -*- coding: utf-8 -*-
import pygame as pg

import data_Path.color as color, data_Path.image as image, data_Path.BGM as BGM

import Title_Operate.Buttons as Buttons

import GameOperate.one_player, GameOperate.four_player

from sys import exit

from pygame.locals import *

pg.init()  # 初始化pygame
pg.mixer.init()  # 初始化音樂

pg.mixer.music.set_volume(0.2)

pg.display.set_caption("誰是牛頭王")
size = width, height = 1440, 720  # 設定視窗大小
screen = pg.display.set_mode(size)  # 顯示視窗
ttttt = []
print(len(ttttt))

bg = pg.Surface(screen.get_size())
bg = bg.convert()

#標題畫面用的圖片
title_sence = pg.image.load(image.title_sence)#標題畫面背景
title_sence.convert()

#音樂選單的背景
Menu = pg.Surface(image.MenuSize)
Menu = Menu.convert()

#選擇模式畫面的圖

class Button:#按鈕類

    def __init__(self, upimage, downimage, position):
        self.imageUp = pg.image.load(upimage).convert_alpha()#滑鼠不在上面的圖
        self.imageDown = pg.image.load(downimage).convert_alpha()#滑鼠在上面的圖
        self.position = position#圖片左上角

    def isOver(self):
        point_x,point_y = pg.mouse.get_pos()#滑鼠位置
        x, y = self.position
        w, h = self.imageUp.get_size()#圖片大小

        in_x = x < point_x and x + w > point_x
        in_y = y < point_y and y + h > point_y
        return in_x and in_y

    def draw(self):
        x, y = self.position
        
        if self.isOver():
            bg.blit(self.imageDown, (x, y))
        else:
            bg.blit(self.imageUp, (x, y))

class BackGrondMusicMenuButton(Button):#音樂按鈕

    def isOver(self):
        point_x,point_y = pg.mouse.get_pos()#滑鼠位置
        x = self.position[0] + image.MenuPosition[0]
        y = self.position[1] + image.MenuPosition[1]
        w, h = self.imageUp.get_size()#圖片大小

        in_x = x < point_x and x + w > point_x
        in_y = y < point_y and y + h > point_y
        return in_x and in_y

    def draw(self):
        x, y = self.position
        
        if self.isOver():
            Menu.blit(self.imageDown, (x, y))
        else:
            Menu.blit(self.imageUp, (x, y))

class VolumeButton:

    def __init__(self):
        self.NonePosition = image.NoneVolumePosition
        self.NoneSize = image.NoneVolumeSize
        self.Position = image.VolumePosition
        self.Size = image.VolumeSize
    
    def isOver_None(self):
        point_x,point_y = pg.mouse.get_pos()#滑鼠位置
        x = self.NonePosition[0] + image.MenuPosition[0]
        y = self.NonePosition[1] + image.MenuPosition[1]
        w, h = self.NoneSize#大小

        in_x = x < point_x and x + w > point_x
        in_y = y < point_y and y + h > point_y
        return in_x and in_y

    def isOverAll(self):
        point_x,point_y = pg.mouse.get_pos()#滑鼠位置
        x = self.Position[0] + image.MenuPosition[0]
        y = self.Position[1] + image.MenuPosition[1]
        w, h = image.VolumeAllSize#圖片大小

        in_x = x < point_x and x + w > point_x
        in_y = y < point_y and y + h > point_y
        return in_x and in_y

    def isOverVolume(self):
        point_x,point_y = pg.mouse.get_pos()#滑鼠位置
        x = self.Position[0] + image.MenuPosition[0]
        y = self.Position[1] + image.MenuPosition[1]
        w, h = self.Size#大小
        for i in range (1, 11):
            x += self.Size[0]
            in_x = x < point_x and x + w > point_x
            in_y = y < point_y and y + h > point_y
            if in_x and in_y:
                return i

class BackGrondMusicMenu:#BGM操作類

    song = 0
    MenuP = 2
    Volume = 0.2
    show = False
    Silented = False
    SilentedMenuP = 2

    def __init__(self, MusicList, MusicStart, MenuBackground, MusicName):
        self.MusicList = MusicList
        self.MusicStart = MusicStart
        self.MenuBackground = MenuBackground
        self.MusicName = MusicName
        self.Right = BackGrondMusicMenuButton(image.Right, image.Right, image.Right_position)
        self.Left = BackGrondMusicMenuButton(image.Left, image.Left, image.Left_position)
        self.VolumeButton = VolumeButton()

    def ShowMenu(self):
        self.show = True
        MenuPicture = pg.image.load(self.MenuBackground[self.MenuP]).convert_alpha()
        Menu.blit(MenuPicture, (0, 0))
        self.Right.draw()
        self.Left.draw()
        MusicName = pg.image.load(self.MusicName[self.song]).convert_alpha()
        Menu.blit(MusicName, image.MusicNamePosition)
        screen.blit(Menu, image.MenuPosition)
        pg.display.update()
    
    def isOver(self):
        point_x,point_y = pg.mouse.get_pos()#滑鼠位置
        x, y = image.MenuPosition
        w, h = image.MenuSize#圖片大小

        in_x = x < point_x and x + w > point_x
        in_y = y < point_y and y + h > point_y
        return in_x and in_y

    def ChangeBGM(self, RorL):
        Changed = False
        if -1 < self.song < len(self.MusicList)-1 and RorL == "R":
            self.song +=1
            Changed = True
            self.PlayBGM()
        if 0 < self.song < len(self.MusicList) and RorL == "L":
            self.song -= 1
            Changed = True
            self.PlayBGM()
        if self.song == len(self.MusicList)-1 and RorL == "R" and Changed == False:
            self.song = 0
            Changed = True
            self.PlayBGM()
        if self.song == 0 and RorL == "L" and Changed == False:
            self.song = len(self.MusicList)-1
            Changed = True
            self.PlayBGM()

    def PlayBGM(self):
        pg.mixer.music.load(self.MusicList[self.song])
        pg.mixer.music.fadeout(500)
        pg.mixer.music.stop()
        pg.mixer.music.play(-1, self.MusicStart[self.song])
        MusicName = pg.image.load(self.MusicName[self.song]).convert_alpha()
        Menu.blit(MusicName, image.MusicNamePosition)

    def ChangeVolume(self, volume):
        self.Volume = volume
        self.MenuP = volume*10
        self.Silented = False
        pg.mixer.music.set_volume(self.Volume)

    def Silent(self):
        self.Silented = True
        self.SilentedMenuP = self.MenuP
        self.MenuP = 0
        pg.mixer.music.set_volume(0)

    def Unsilent(self):
        self.Silented = False
        self.MenuP = self.SilentedMenuP
        pg.mixer.music.set_volume(self.Volume)

def Welcome(Start_Game, Close_Game, BGMMenu, BGMOption):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()# 退出pygame
            exit()
        if event.type == pg.MOUSEBUTTONUP:
            if Start_Game.isOver():
                return False
            elif Close_Game.isOver():
                pg.quit()# 退出pygame
                exit()
            elif BGMMenu.isOver():
                BGMOption.ShowMenu()
            elif BGMOption.isOver() == False:
                BGMOption.show = False
            elif BGMOption.Right.isOver() and BGMOption.show:
                BGMOption.ChangeBGM("R")
            elif BGMOption.Left.isOver() and BGMOption.show:
                BGMOption.ChangeBGM("L")
            elif BGMOption.VolumeButton.isOver_None() and BGMOption.Silented == True:
                BGMOption.Unsilent()
            elif BGMOption.VolumeButton.isOver_None():
                BGMOption.Silent()
            # elif BGMOption.VolumeButton.isOverAll():
            #     BGMOption.ChangeVolume(BGMOption.VolumeButton.isOverVolume())
    #配置標題畫面
    bg.blit(title_sence, (0, 0))
    Start_Game.draw()
    Close_Game.draw()
    BGMMenu.draw()
    screen.blit(bg, (0,0))
    if BGMOption.show:
        BGMOption.ShowMenu()
    return True

#def mode_select():


def fade_to_game(width, height):
    fade_out = pg.Surface((width, height))
    fade_out.fill((0,0,0))
    fade_in = pg.Surface((width, height))
    desk = pg.image.load(image.desk)
    fade_in.blit(desk, (0,0))
    for alpha in range(0, 50):
        fade_out.set_alpha(alpha)
        screen.blit(fade_out, (0,0))
        pg.display.update()
        pg.time.delay(5)
    for alpha in range(0, 50):
        fade_in.set_alpha(alpha)
        screen.blit(fade_in, (0,0))
        pg.display.update()
        pg.time.delay(5)

First_play = True

def main():
    #建立標題畫面的按鈕
    Start_Game = Button(image.start_game, image.start_game_up, image.start_game_position)
    Close_Game = Button(image.close_game, image.close_game_up, image.close_game_position)
    BGMMenu = Button(image.music_bottom, image.music_bottom, image.music_position)
    BGMOption = BackGrondMusicMenu(BGM.MusicList, BGM.MusicStart, image.MusicMenu, image.MusicName)
    pg.mixer.music.load(BGM.MusicList[0])
    pg.mixer.music.play(-1, BGM.MusicStart[0])
    while Welcome(Start_Game, Close_Game, BGMMenu, BGMOption):
        pg.display.update()
    
    #while True:
    #    nextmovement = mode_select()
    #    pg.display.update()

main()