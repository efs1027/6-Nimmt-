# -*- coding: utf-8 -*-
import os
up = os.getcwd()
imagefloder = up + "/image/"
#標題畫面用的圖片
title_sence = imagefloder + "title_sence.jpg"#標題畫面背景位置
desk = imagefloder + "desk.jpg"#桌子
fade_back =  imagefloder + "fade_back.jpg"#假的標題畫面
logo = imagefloder + "logo.jpg"

#標題畫面用的按鈕
start_game = imagefloder + "start_game_buttom.png"#開始遊戲按鍵
start_game_up = imagefloder + "start_game_buttom_pressed.png"#滑鼠在上面的開始遊戲按鍵
close_game = imagefloder + "close_buttom.png"#結束遊戲按鍵
close_game_up = imagefloder + "close_buttom_pressed.png"#滑鼠在上面的結束遊戲按鍵
music_bottom = imagefloder + "music_buttom.jpg"#更改BGM用按鍵

#標題畫面按鍵位置
start_game_position = (550, 250)#開始遊戲在 x = 550 ~ 860 , y = 250 ~ 410
close_game_position = (550, 440)#結束遊戲在 x = 550 ~ 860 , y = 440 ~ 600
music_position = (1350, 630)#更改BGM按鍵在 x = 1350 ~ 1400 , y = 630 ~ 680

#選擇遊戲模式畫面用的圖片
OP = imagefloder + "1P.jpg"#選擇單人模式時的畫面
one_player_sence_easy = imagefloder + "1PE.jpg"#選擇簡單單人模式時的畫面
one_player_sence_hard = imagefloder + "1PH.jpg"#選擇困難單人模式時的畫面 #未製作
FP = imagefloder + "4P.jpg"#選擇四人模式時的畫面
ModeMenuSize = (600, 230)
ModeMenuPosition = (420, 245)

#選擇遊戲模式畫面用的按鈕
One = imagefloder + "OnePlayer.jpg"
One_pressed = imagefloder + "OnePlayer_pressed.jpg"
One_position = (170, 45)
Four = imagefloder + "FourPlayer.jpg"
Four_pressed = imagefloder + "FourPlayer_pressed.jpg"
Four_position = (350, 45)
Menu_start = imagefloder + "start_buttom.png"
Menu_start_pressed = imagefloder + "start_buttom_pressed.png"
Menu_start_position = (270, 140)

#音樂選單用的圖
MusicMenu = [ imagefloder + "MusicMenu0.jpg", imagefloder + "MusicMenu1.jpg", imagefloder + "MusicMenu2.jpg", imagefloder + "MusicMenu3.jpg", imagefloder + "MusicMenu4.jpg"
, imagefloder + "MusicMenu5.jpg", imagefloder + "MusicMenu6.jpg", imagefloder + "MusicMenu7.jpg", imagefloder + "MusicMenu8.jpg", imagefloder + "MusicMenu9.jpg"
, imagefloder + "MusicMenu10.jpg"]#音樂選單
SoundMenuPosition = (1120, 510)
SoundMenuSize = (300, 120)
MusicName = [ imagefloder + "Name1.jpg", imagefloder + "Name2.jpg"]#歌曲名標籤
MusicNamePosition = (40, 40)

#音樂選單用的按鈕及位置
Left = imagefloder + "Left.jpg"#向左按鍵
Left_position = (20, 40)
Right = imagefloder + "Right.jpg"#向右按鍵
Right_position = (260, 40)
NoneVolumePosition = (20, 75)
NoneVolumeSize = (45, 30)
VolumePosition = (80, 80)
VolumeAllSize = (200, 20)
VolumeSize = (20, 20)

#暫停畫面用的圖
StopMenu = imagefloder + "StopMenu.jpg"#暫停畫面選單#未製作

#暫停畫面用的按鈕
restart = imagefloder + ".jpg"#重新開始按鍵#未製作
back = imagefloder + ".jpg"#回到標題畫面按鍵#未製作

#結束畫面
second_game = imagefloder + "new_game_buttom.png"
second_game_up = imagefloder + "new_game_buttom_pressed.png"
back =  imagefloder + "back_to_title_button.png"
back_up = imagefloder + "back_to_title_button_pressed.png"
second_game_position = (110, 500)
end_position = (600, 500)
back_position = (1090, 500)

#遊戲過程用的圖
com1_desk = imagefloder + "com1_desk.jpg"
com2_desk = imagefloder + "com2_desk.jpg"
com3_desk = imagefloder + "com3_desk.jpg"
player1_desk = imagefloder + "player1_desk.jpg"
table_desk = imagefloder + "table_desk.jpg"
process_desk = imagefloder + "process_desk.jpg"
poker = imagefloder + "poker.png"#卡背
bull_big = imagefloder + "bull_big.png"#大寫避免衝突
bull_small = imagefloder + "bull_small.png"#大寫避免衝突
card_face = imagefloder + "card_face.png"#卡面
# card_face = imagefloder + "card_face_big.png"#卡面

#新手教學用的圖
que = imagefloder + "que.png"#問號
NT0 = imagefloder + "NT0.jpg"#第一頁
NT1 = imagefloder + "NT1.jpg"#第一頁
NT2 = imagefloder + "NT2.jpg"#第二頁
NT3 = imagefloder + "NT3.jpg"#第三頁
NT4 = imagefloder + "NT4.jpg"#第四頁
NTback = imagefloder + "NTback.png"#新手教學返回鍵
NTback_pressed = imagefloder + "NTback_pressed.png"#新手教學返回鍵
NTback_position = (1100, 650)
nextpage = imagefloder + "nextpage.png"
nextpage_pressed = imagefloder + "nextpage_pressed.png"
nextpage_position = (1300, 650)
previous_pressed = imagefloder + "previous_pressed.png"
previous = imagefloder + "previous.png"
previous_pressed = imagefloder + "previous_pressed.png"
previous_position = (1200, 650)
que_position = (1250, 610)

#牌上的數字
number1 = imagefloder + "number1.png"
number2 = imagefloder + "number2.png"
number3 = imagefloder + "number3.png"
number4 = imagefloder + "number4.png"
number5 = imagefloder + "number5.png"
number6 = imagefloder + "number6.png"
number7 = imagefloder + "number7.png"
number8 = imagefloder + "number8.png"
number0 = imagefloder + "number0.png"
number9 = imagefloder + "number9.png"