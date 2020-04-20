# -*- coding: utf-8 -*-
#呂宗霖:http://25.72.61.125:8070/
#張育誠:http://25.31.4.252:8070/
import pygame as pg, add_module_path as ModAdd, uuid, pygame_textinput

ModAdd.path_append()
import color, image, BGM, one_player as OneP, four_player as FourP

from sys import exit

from pygame.locals import *

pg.init()  # 初始化pygame
pg.mixer.init()  # 初始化音樂

pg.mixer.music.set_volume(0.0)

pg.display.set_caption("誰是牛頭王")
size = width, height = 1440, 720  # 設定視窗大小
screen = pg.display.set_mode(size)  # 顯示視窗

bg = pg.Surface(screen.get_size())
bg = bg.convert()

#標題畫面用的圖片
title_sence = pg.image.load(image.title_sence)#標題畫面背景
title_sence.convert()

#音樂選單的背景
SoundMenu = pg.Surface(image.SoundMenuSize)
SoundMenu = SoundMenu.convert()

#選擇模式的背景
ModeMenu = pg.Surface(image.ModeMenuSize)
ModeMenu = ModeMenu.convert()

#新手教學的背景
NTbg = pg.Surface(screen.get_size())
NT1 = pg.image.load(image.NT1)
NT2 = pg.image.load(image.NT2)
NT3 = pg.image.load(image.NT3)
NT4 = pg.image.load(image.NT4)

def t():
    # Create TextInput-object
    textinput = pygame_textinput.TextInput()

    box = pg.Surface((200, 300))
    clock = pg.time.Clock()

    while True:
        box.fill((225, 225, 225))

        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    return textinput.get_text()

        # Feed it with events every frame
        textinput.update(events)
        # Blit its surface onto the screen
        box.blit(textinput.get_surface(), (10, 10))
        bg.blit(box, (200, 300))
        screen.blit(bg, (0, 0))
        pg.display.update()
        clock.tick(30)

class System():

    def Title(self, Start_Game, Close_Game, BGMMenuOpen, BGMOption, SelectMenu, que, NT):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()# 退出pygame
                exit()
            if event.type == pg.MOUSEBUTTONUP:
                if Close_Game.isOver() and SelectMenu.show == False:
                    pg.quit()# 退出pygame
                    exit()
                if BGMMenuOpen.isOver():
                    BGMOption.ShowMenu()
                if BGMOption.isOver() == False and BGMMenuOpen.isOver() == False and BGMOption.show:
                    BGMOption.show = False
                if BGMOption.Right.isOver() and BGMOption.show:
                    BGMOption.ChangeBGM("R")
                if BGMOption.Left.isOver() and BGMOption.show:
                    BGMOption.ChangeBGM("L")
                if BGMOption.VolumeButton.isOver_None() and BGMOption.Silented == True:
                    BGMOption.Unsilent()
                elif BGMOption.VolumeButton.isOver_None():
                    BGMOption.Silent()
                if BGMOption.VolumeButton.isOverAll():
                    Volume = BGMOption.VolumeButton.isOverVolume()
                    if Volume != False:
                        Volume /=10
                        BGMOption.ChangeVolume(Volume)
                if SelectMenu.One and SelectMenu.FourPlayerButton.isOver() and SelectMenu.show:
                    SelectMenu.ChangeMode()
                if SelectMenu.Four and SelectMenu.OnePlayerButton.isOver() and SelectMenu.show:
                    SelectMenu.ChangeMode()
                if SelectMenu.Start.isOver() and SelectMenu.show:
                    usrid = str(uuid.uuid1())
                    self.fade_to_game(1440, 720)
                    SelectMenu.show = False
                    go = True
                    while go:
                        result = SelectMenu.StartGame(usrid)
                        if result == "close":
                            pg.quit()# 退出pygame
                            exit()
                        if result == "back":
                            go = False
                            self.fade_to_title(1440, 720)
                        if result == "again":
                            self.fade_to_game(1440, 720)
                            result = SelectMenu.StartGame(usrid)
                elif Start_Game.isOver() and SelectMenu.show == False:
                    SelectMenu.ShowMenu()
                elif SelectMenu.isOver() == False and SelectMenu.show:
                    SelectMenu.show = False
                elif que.isOver():
                    NT.ClickBack = False
                    NT.show = True
        #配置標題畫面
        bg.blit(title_sence, (0, 0))
        Start_Game.draw()
        Close_Game.draw()
        BGMMenuOpen.draw()
        que.draw()
        screen.blit(bg, (0, 0))
        if BGMOption.show:
            BGMOption.ShowMenu()
        if SelectMenu.show:
            SelectMenu.ShowMenu()
        if NT.show:
            NT.ShowPage()
        return True

    def fade_to_game(self, width, height):
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

    def fade_to_title(self, width, height):
        fade_out = pg.Surface((width, height))
        fade_out.fill((0,0,0))
        fade_in = pg.Surface((width, height))
        title = pg.image.load(image.fade_back)
        fade_in.blit(title, (0,0))
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

class MenuButton:#按鈕類

    def __init__(self, bg, upimage, downimage, position, MenuPosition):
        self.bg = bg
        self.imageUp = pg.image.load(upimage).convert_alpha()#滑鼠不在上面的圖
        self.imageDown = pg.image.load(downimage).convert_alpha()#滑鼠在上面的圖
        self.position = position#圖片左上角
        self.MenuPosition = MenuPosition

    def isOver(self):
        point_x,point_y = pg.mouse.get_pos()#滑鼠位置
        x = self.position[0] + self.MenuPosition[0]
        y = self.position[1] + self.MenuPosition[1]
        w, h = self.imageUp.get_size()#圖片大小

        in_x = x < point_x and x + w > point_x
        in_y = y < point_y and y + h > point_y
        return in_x and in_y

    def draw(self):
        x, y = self.position
        
        if self.isOver():
            self.bg.blit(self.imageDown, (x, y))
        else:
            self.bg.blit(self.imageUp, (x, y))

class VolumeButton:

    def __init__(self):
        self.NonePosition = image.NoneVolumePosition
        self.NoneSize = image.NoneVolumeSize
        self.Position = image.VolumePosition
        self.Size = image.VolumeSize
    
    def isOver_None(self):
        point_x,point_y = pg.mouse.get_pos()#滑鼠位置
        x = self.NonePosition[0] + image.SoundMenuPosition[0]
        y = self.NonePosition[1] + image.SoundMenuPosition[1]
        w, h = self.NoneSize#大小

        in_x = x < point_x and x + w > point_x
        in_y = y < point_y and y + h > point_y
        return in_x and in_y

    def isOverAll(self):
        point_x,point_y = pg.mouse.get_pos()#滑鼠位置
        x = self.Position[0] + image.SoundMenuPosition[0]
        y = self.Position[1] + image.SoundMenuPosition[1]
        w, h = image.VolumeAllSize#圖片大小

        in_x = x < point_x and x + w > point_x
        in_y = y < point_y and y + h > point_y
        return in_x and in_y

    def isOverVolume(self):
        point_x,point_y = pg.mouse.get_pos()#滑鼠位置
        x = self.Position[0] + image.SoundMenuPosition[0] - self.Size[0]
        y = self.Position[1] + image.SoundMenuPosition[1]
        w, h = self.Size#大小
        for i in range (1, 11):
            x += self.Size[0]
            in_x = x < point_x and x + w > point_x
            in_y = y < point_y and y + h > point_y
            if in_x and in_y:
                return i
        return False

class Menu:

    show = False
    def __init__(self, bg, position, size):
        self.bg = bg
        self.position = position
        self.size = size

    def Setting(self):
        self.bg.fill(color.BLACK)

    def ShowMenu(self):
        self.show = True
        self.Setting()
        screen.blit(self.bg, self.position)
        pg.display.update()

    def isOver(self):
        point_x,point_y = pg.mouse.get_pos()#滑鼠位置
        x, y = self.position
        w, h = self.size#圖片大小

        in_x = x < point_x and x + w > point_x
        in_y = y < point_y and y + h > point_y
        return in_x and in_y

class BackGrondMusicMenu(Menu):#BGM操作類

    song = 0
    MenuP = 0
    Volume = 0.0
    show = False
    Silented = False
    SilentedMenuP = 0

    def __init__(self, bg, position, size, MusicList, MusicStart, MenuBackground, MusicName):
        self.bg = bg
        self.position = position
        self.size = size
        self.MusicList = MusicList
        self.MusicStart = MusicStart
        self.MenuBackground = MenuBackground
        self.MusicName = MusicName
        self.Right = MenuButton(self.bg, image.Right, image.Right, image.Right_position, self.position)
        self.Left = MenuButton(self.bg, image.Left, image.Left, image.Left_position, self.position)
        self.VolumeButton = VolumeButton()

    def Setting(self):
        MenuPicture = pg.image.load(self.MenuBackground[self.MenuP]).convert_alpha()
        self.bg.blit(MenuPicture, (0, 0))
        self.Right.draw()
        self.Left.draw()
        MusicName = pg.image.load(self.MusicName[self.song]).convert_alpha()
        self.bg.blit(MusicName, image.MusicNamePosition)

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
        self.bg.blit(MusicName, image.MusicNamePosition)

    def ChangeVolume(self, volume):
        self.Volume = volume
        self.MenuP = int(volume*10)
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

class ModeSelectMenu(Menu):

    show = False
    One = True
    Four = False
    def __init__(self, bg, position, size, OnePlayerPic, FourPlayerPic):
        self.bg = bg
        self.position = position
        self.size = size
        self.OnePlayerPic = pg.image.load(OnePlayerPic).convert_alpha()
        self.FourPlayerPic = pg.image.load(FourPlayerPic).convert_alpha()
        self.Start = MenuButton(self.bg, image.Menu_start, image.Menu_start_pressed, image.Menu_start_position, self.position)
        self.FourPlayerButton = MenuButton(self.bg, image.Four, image.Four_pressed, image.Four_position, self.position)
        self.OnePlayerButton = MenuButton(self.bg, image.One, image.One_pressed, image.One_position, self.position)

    def Setting(self):
        if self.One:
            self.bg.blit(self.OnePlayerPic, (0, 0))
            self.Start.draw()
            self.FourPlayerButton.draw()
        if self.Four:
            self.bg.blit(self.FourPlayerPic, (0, 0))
            self.Start.draw()
            self.OnePlayerButton.draw()

    def ChangeMode(self):
        if self.One:
            self.Four = True
            self.One = False
        else:
            self.One = True
            self.Four = False
    
    def StartGame(self, ID):
        self.show = False
        if self.One:
            return OneP.play_easy()
        if self.Four:
            FourP.play(ID)

class NewbieTeach(Menu):
    
    def __init__ (self, bg, p1, p2, p3, p4):
        self.page = 1
        self.show = False
        self.ClickBack = False
        self.bg = bg
        self.page1 = p1
        self.page2 = p2
        self.page3 = p3
        self.page4 = p4
        self.back = MenuButton(self.bg, image.NTback, image.NTback, (720, 650), (0, 0))
        self.nextpage = MenuButton(self.bg, image.nextpage, image.nextpage, (1300, 650), (0, 0))
        self.previous = MenuButton(self.bg, image.previous, image.previous, (0, 650), (0, 0))
    
    def ShowPage(self):
        while self.ClickBack == False:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()# 退出pygame
                    exit()
                if event.type == pg.MOUSEBUTTONUP:
                    if self.nextpage.isOver() and self.page < 4:
                        self.page += 1
                    elif self.previous.isOver() and self.page > 1:
                        self.page -= 1
                    elif self.back.isOver():
                        self.ClickBack = True
                        self.page = 1
            if self.page == 1 and self.ClickBack != True:
                self.bg.blit(self.page1, (0, 0))
                self.back.draw()
                self.nextpage.draw()
            elif self.page == 2:
                self.bg.blit(self.page2, (0, 0))
                self.back.draw()
                self.nextpage.draw()
                self.previous.draw()
            elif self.page == 3:
                self.bg.blit(self.page3, (0, 0))
                self.back.draw()
                self.nextpage.draw()
                self.previous.draw()
            elif self.page == 4:
                self.bg.blit(self.page4, (0, 0))
                self.back.draw()
                self.previous.draw()
            screen.blit(self.bg, (0 ,0))
            pg.display.update()

OperateSystem = System()
def main():
    #建立標題畫面的按鈕
    OperateSystem.fade_to_title(1440, 720)
    Start_Game = MenuButton(bg, image.start_game, image.start_game_up, image.start_game_position, (0,0))
    Close_Game = MenuButton(bg, image.close_game, image.close_game_up, image.close_game_position, (0,0))
    BGMMenuOpen = MenuButton(bg, image.music_bottom, image.music_bottom, image.music_position, (0,0))
    que = MenuButton(bg, image.que, image.que, image.que_position, (0, 0))
    BGMOption = BackGrondMusicMenu(SoundMenu, image.SoundMenuPosition, image.SoundMenuSize, BGM.MusicList, BGM.MusicStart, image.MusicMenu, image.MusicName)
    SelectMenu = ModeSelectMenu(ModeMenu, image.ModeMenuPosition, image.ModeMenuSize, image.OP, image.FP)
    NT = NewbieTeach(NTbg, NT1, NT2, NT3, NT4)
    BGMOption.PlayBGM()
    while True:
        while OperateSystem.Title(Start_Game, Close_Game, BGMMenuOpen, BGMOption, SelectMenu, que, NT):
            pg.display.update()

main()

pg.quit()# 退出pygame
exit()