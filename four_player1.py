""" 
待修改問題：
    結算畫面分數背景
尚未完成：
    更酷的特效!!!
"""
# -*- coding: utf-8 -*-
import pygame as pg, random, sys, add_module_path as ModAdd
ModAdd.path_append()
import color as colors, image as image
import socketio
address = sys.argv[1]
Name = sys.argv[2]
try:
    sio = socketio.Client()
    sio.connect(address)
except:
    pass

data = {}
error = True
PlayerID = "NULL"

@sio.event
def connect():
    global error
    error = False
    print("I'm connected!")
@sio.event
def connect_error():
    global error
    error = True
    print("The connection failed!")
@sio.event
def tablejson(Input):
    global data
    global PlayerID
    data = Input
    if PlayerID != "NULL":
        a = data["score"].pop(PlayerID)
        data["score"].append(a)
        b = data["hand"].pop(PlayerID)
        data["hand"].append(b)
        c = data["facecard"].pop(PlayerID)
        data["facecard"].append(c)
        d = data["choosebase"].pop(PlayerID)
        data["choosebase"].append(d)
    print(data)

pg.init()

size = width, height = 1440, 720
sc = pg.display.set_mode(size)
# bg_hand = pg.Surface((600, 200))#手牌區塊背景
# bg_table = pg.Surface((800, 320))#桌面區塊背景
bg_process = pg.Surface((300, 50))#遊戲進程區塊背景
desk = pg.image.load(image.desk)
com1_desk = pg.image.load(image.com1_desk)
com2_desk = pg.image.load(image.com2_desk)
com3_desk = pg.image.load(image.com3_desk)
player1_desk = pg.image.load(image.player1_desk)
table_desk = pg.image.load(image.table_desk)
process_desk = pg.image.load(image.process_desk)
sc.blit(desk, (0, 0))
text = pg.font.SysFont("Arial", 24)
process_text = pg.font.Font("Chinese.ttf", 24)#24

card_base = [1]
card_dict = {1 : 1} 

def AntiCrash():
    for event in pg.event.get():
        if event == pg.QUIT:
            pg.quit()
            exit()

#卡牌屬性目錄設定
for i in range (2, 105, 1):
    card_base.append(i)
    if i % 5 == 0 and i % 10 != 0 and i != 55 :
        card_dict[i] = 2
    if i % 10 == 0:
        card_dict[i] = 3
    if i % 11 == 0 and i != 55:
        card_dict[i] = 5
    if i == 55:
        card_dict[i] = 7
    if i % 5 != 0 and i % 10 != 0 and i % 11 != 0:
        card_dict[i] = 1

class computer:#電腦類別

    def __init__(self, num, comName, card):#設定基本資料
        self.num = int(num) - 1
        self.name = comName#設定電腦名稱
        self.card = card#設定電腦手牌
        self.selected_card = 0 # 被選中的牌初始化
        self.bg_hand = pg.Surface((600, 200))#設定區塊
        self.bull = 0#分數初始化
        self.point_card = []

    def select_card(self):#選擇卡片
        global data
        AllThrow = data["facecard"]
        Allhand = data["hand"]
        self.card = Allhand[self.num]
        self.selected_card = AllThrow[self.num]
        self.draw_hand(False)
        self.draw_throw(self.selected_card, False)
        pg.display.update()
        return self.selected_card#回傳
        
    def get_card(self, table, list_num):#收回卡片
        if len(self.point_card) == 1:
            card_list = table1.list_give_player(list_num, self.selected_card)#由函數取得該列並置換排頭
            self.point_card = card_list
        else:
            card_list = table1.list_give_player(list_num, self.selected_card)#由函數取得該列並置換排頭
            self.point_card.extend(card_list)#加進持有的分數牌中
        table1.bg_table = pg.Surface((800, 320))
        table1.bg_table.blit(table_desk, (0, 0))
        table1.draw_table(False)
        pg.display.update()

    def count_bull(self):#算分數
        self.bull = 0
        for num in self.point_card:
            self.bull += card_dict[num]
        
    def draw_throw(self, card, display):
        if str(self.name) == "電腦1":
            SITE = (1240, 60)
        if str(self.name) == "電腦2":
            SITE = (420, 0)
        if str(self.name) == "電腦3":
            SITE = (0, 60)
        x, y = 278, 20
        pg.draw.rect(self.bg_hand, colors.WHITE, [x, y, 44, 60])
        if display:
            num_font = text.render(str(card), True, colors.BLACK) 
            self.bg_hand.blit(num_font, (x, y+15))
            for i in range(card_dict[card]):
                pg.draw.circle(self.bg_hand, colors.RED, (x+6+i*6, y+6), 2)
        #旋轉區塊
        num = self.name.split("電腦",1)#從名字分割出編號
        new_bg_hand = pg.transform.rotate(self.bg_hand, 90*int(num[-1]))
        sc.blit(new_bg_hand, SITE)
        if card != False and display != True:#出牌階段延遲，亮牌階段不延遲
            pg.time.delay(50)#500

    def draw_hand(self, gradually):#手牌
        SITE = (0,0)#絕對座標
        if str(self.name) == "電腦1":
            SITE = (1240, 60)
            self.bg_hand.blit(com1_desk, (0,0))
        if str(self.name) == "電腦2":
            SITE = (420, 0)
            self.bg_hand.blit(com2_desk, (0,0))
        if str(self.name) == "電腦3":
            SITE = (0, 60)
            self.bg_hand.blit(com3_desk, (0,0))
        #玩家總牛頭數
        x, y = 550, 50
        pg.draw.circle(self.bg_hand, colors.RED, (x, y), 10)
        num_font = text.render(str(self.bull), True, colors.RED)
        self.bg_hand.blit(num_font, (x+10, y))
        for card in self.card:
            #手牌
            n = self.card.index(card) 
            dx = 26*(10-len(self.card))#偏移
            x, y = 55+dx+n*50, 120#相對座標
            pg.draw.rect(self.bg_hand, colors.WHITE, [x, y, 44, 60])
            #旋轉區塊
            num = self.name.split("電腦",1)#從名字分割出編號
            new_bg_hand = pg.transform.rotate(self.bg_hand, 90*int(num[-1]))
            sc.blit(new_bg_hand, SITE)
            if gradually:
                pg.display.update()
                pg.time.delay(20)
        if len(self.card) == 0:
            num = self.name.split("電腦",1)#從名字分割出編號
            new_bg_hand = pg.transform.rotate(self.bg_hand, 90*int(num[-1]))
            sc.blit(new_bg_hand, SITE)

class player:#玩家類別
    
    def __init__(self, card, ID, name):#設定基本資料
        self.ID = ID
        self.name = name#設定玩家名稱
        self.card = card#設定玩家擁有的牌
        self.selected_card = 0 # 被選中的牌初始化
        self.bg_hand = pg.Surface((600, 200))#設定區塊
        self.bull = 0#分數初始化
        self.point_card = []
        self.card_num = 0

    def get_card(self, table, list_num, card_num):#收回卡片#card_num為玩家選的卡
        if len(self.point_card) == 1:
            card_list = table1.list_give_player(list_num, card_num)#由函數取得該列並置換排頭
            self.point_card = card_list
        else:
            card_list = table1.list_give_player(list_num, card_num)#由函數取得該列並置換排頭
            self.point_card.extend(card_list)#加進持有的分數牌中
        sio.emit('action', {"name":self.ID, "ac":3, "card":list_num})
        table1.bg_table = pg.Surface((800, 320))
        table1.bg_table.blit(table_desk, (0, 0))
        table1.draw_table(False)
        pg.display.update()

    def count_bull(self):#算分數
        self.bull = 0
        for num in self.point_card:
            self.bull += card_dict[num]
            
    def select_card(self, a):#選擇卡片
        for event in pg.event.get():#遍歷所有事件
            if a == "NULL":
                if event.type == pg.KEYDOWN:#查看所有按鍵事件
                    if event.key == pg.K_LEFT:#按左鍵的時候，選取左一個的牌
                        if self.card_num != 0:
                            self.card_num-=1
                        else:
                            self.card_num = len(self.card)-1
                    if event.key == pg.K_RIGHT:#按右鍵的時候，選取右一個的牌 # 這裡要-1
                        if self.card_num != len(self.card)-1:
                            self.card_num+=1
                        else:
                            self.card_num = 0
                    if event.key == pg.K_RETURN:#按Enter時 
                        self.selected_card = self.card[self.card_num]
                        #從手牌list中移除選擇的牌
                        sio.emit('action',{"name":self.ID,"ac":1,"card":self.selected_card})
                        self.card.pop(self.card_num)
                        self.card_num = 0
                        self.draw_hand(False)
                        self.draw_throw(self.selected_card)
                        pg.display.update()
        self.draw_hand(False)
        if self.selected_card != 0:
            self.draw_throw(self.selected_card)
        else:
            self.draw_select(self.card_num)
        pg.display.update()
                    
    def select_list(self, table, card_num):#收回卡片#card_num是玩家出的牌
        list_num = 0
        entered = False
        while entered == False:#當尚未按下enter時 
            for event in pg.event.get():  # 遍歷所有事件
                if event.type == pg.KEYDOWN:#查看所有按鍵事件 ## 這裡少加.type
                    if event.key == pg.K_UP:#按上鍵時，選取上一個列
                        if list_num != 0:
                            list_num-=1
                        else:
                            list_num = 3
                    if event.key == pg.K_DOWN:#按下鍵時，選取下一個列
                        if list_num != 3:
                            list_num+=1
                        else:
                            list_num = 0
                    if event.key == pg.K_RETURN:#按Enter時 
                        #玩家拿走該列並且放置他出的牌
                        self.get_card(table, list_num, card_num)
                        table1.draw_table(False)
                        pg.display.update()
                        #計算分數
                        self.count_bull()
                        #變換「是否按下Enter」的變數以跳出迴圈
                        entered = True
            table1.bg_table = pg.Surface((800, 320))
            table1.bg_table.blit(table_desk, (0, 0))
            table1.draw_table(False)
            if entered == False:
                self.draw_sel_list(list_num)
            pg.display.update()

    def draw_throw(self, card):
        x, y = 278, 20
        pg.draw.rect(self.bg_hand, colors.WHITE, [x, y, 44, 60])
        num_font = text.render(str(card), True, colors.BLACK) 
        self.bg_hand.blit(num_font, (x, y+15))
        if card != False:
            for i in range(card_dict[card]):
                pg.draw.circle(self.bg_hand, colors.RED, (x+6+i*6, y+6), 2)
        sc.blit(self.bg_hand, (420, 520))

    def draw_hand(self, gradually):#手牌
        self.bg_hand = pg.Surface((600, 200))#區塊刷新
        self.bg_hand.blit(player1_desk, (0, 0))
        #玩家總牛頭數
        x, y = 550, 50
        pg.draw.circle(self.bg_hand, colors.RED, (x, y),10)
        num_font = text.render(str(self.bull), True, colors.RED)
        self.bg_hand.blit(num_font, (x+10, y))
        for card in self.card:
            #手牌
            n = self.card.index(card) 
            dx = 26*(10-len(self.card))#維持手牌在中央
            x, y = 55+dx+n*50, 120#相對座標
            pg.draw.rect(self.bg_hand, colors.WHITE, [x, y, 44, 60])
            num_font = text.render(str(card), True, colors.BLACK)
            self.bg_hand.blit(num_font, (x, y+15))
            #牌牛頭數
            for i in range(card_dict[card]):
                pg.draw.circle(self.bg_hand, colors.RED, (x+6+i*6, y+6), 2)
            #畫布印上sc
            sc.blit(self.bg_hand, (420, 520))
            if gradually:
                pg.display.update()
                pg.time.delay(20)
        if len(self.card) == 0:
            sc.blit(self.bg_hand, (420, 520))

    def draw_select(self, card_num):#選牌框 #gradually 逐漸變化
        thick = 3
        dx = 26*(10-len(self.card))#維持手牌在中央
        x, y = 55+dx+card_num*50, 120
        pg.draw.line(self.bg_hand, colors.RED, (x, y), (x+10, y), thick)
        pg.draw.line(self.bg_hand, colors.RED, (x, y), (x, y+20), thick)
        pg.draw.line(self.bg_hand, colors.RED, (x+32, y), (x+42, y), thick)
        pg.draw.line(self.bg_hand, colors.RED, (x+42, y), (x+42, y+20), thick)
        pg.draw.line(self.bg_hand, colors.RED, (x, y+58), (x+10, y+58), thick)
        pg.draw.line(self.bg_hand, colors.RED, (x, y+38), (x, y+58), thick)
        pg.draw.line(self.bg_hand, colors.RED, (x+32, y+58), (x+42, y+58), thick)
        pg.draw.line(self.bg_hand, colors.RED, (x+42, y+38), (x+42, y+58), thick)
        sc.blit(self.bg_hand, (420, 520))

    def draw_sel_list(self, list_num):#桌面收回牌列選擇
        col = table1.list_group[list_num]
        for card in col:
            row = col.index(card)
            x, y = 300+row*50, 20+list_num*75
        pg.draw.rect(table1.bg_table, colors.WHITE, [x, y, 44, 60])
        num_font = text.render(str(self.selected_card), True, colors.BLACK) 
        table1.bg_table.blit(num_font, (x, y+15))
        #牌牛頭數
        for i in range(card_dict[self.selected_card]):
            pg.draw.circle(table1.bg_table, colors.RED, (x+6+i*6, y+6), 2)
        sc.blit(table1.bg_table, (320, 200))
        
class table:#桌子類別
    
    def __init__(self, list1, list2, list3, list4):#設定基本資料
        self.list_group = [list1, list2, list3, list4]#把四列都放入一個list中 ## 雙層list
        self.bg_table = pg.Surface((800, 320))
        
    def place_card(self, list_num, card_num, ThisComputer, OtherNum):#玩家放置牌
        global data
        global PlayerID
        global error
        num = OtherNum.split("com", 1)
        if ThisComputer:
            while error:
                AntiCrash()
            self.list_group[list_num].append(card_num)
            sio.emit('action', {"name":PlayerID, "ac":2, "card":list_num})
        else:
            while data["choosebase"][int(num[-1])-1] == "NULL" or error:
                AntiCrash()
            self.list_group[list_num].append(card_num)

    def list_give_player(self, list_num, card):#玩家收回一列
        give = self.list_group[list_num]#儲存該列資訊
        self.list_group[list_num] = [card]#放置之牌為排頭
        self.draw_table(True)
        return give#回傳分數牌

    def draw_table(self, gradually):#桌面上之牌 #gradually 逐漸變化
        # self.bg_table = pg.Surface((800, 320)) #畫面刷新，放置於函式外
        # self.bg_table.blit(table_desk, (0, 0)) #畫面刷新，放置於函式外
        for lists in self.list_group:
            col = self.list_group.index(lists)
            for card in lists: 
                if card == com1.selected_card:
                    com1.draw_hand(False)
                if card == com2.selected_card:
                    com2.draw_hand(False)
                if card == com3.selected_card:
                    com3.draw_hand(False)
                if card == player1.selected_card:
                    player1.draw_hand(False)
                row = lists.index(card)
                x, y = 250+row*50, 20+col*75
                pg.draw.rect(self.bg_table, colors.WHITE, [x, y, 44, 60])
                num_font = text.render(str(card), True, colors.BLACK)
                self.bg_table.blit(num_font, (x, y+15))
                for i in range(card_dict[card]):
                    pg.draw.circle(self.bg_table, colors.RED, (x+6+i*6, y+6), 2)
                sc.blit(self.bg_table, (320, 200))
                if gradually:
                    pg.display.update() 
                    pg.time.delay(10) #40

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

def process_font(process, turn):
    text_font1 = process_text.render("第"+str(turn)+"回合", True, colors.WHITE)
    text_font2 = process_text.render(process, True, colors.WHITE)
    bg_process.blit(process_desk, (0, 0))
    bg_process.blit(text_font1, (0, 0))
    bg_process.blit(text_font2, (100, 0))
    sc.blit(bg_process, (1140, 0))
    pg.display.update()

def assign():#發牌
    for i in range(10):
        M = 8#發牌速度，數值愈高，移動愈平滑，速度愈慢，太高易卡頓
        for n in range(M):
            sc.blit(table_desk, (0, 0))
            centerx, centery = width/2-22, height/2-30
            ds = (width+height+100)/(2 * M)#取長寬的平均再分割做ds
            pg.draw.rect(sc, colors.WHITE, [centerx, centery-ds*n-7, 44, 60])#top
            pg.draw.rect(sc, colors.WHITE, [centerx-ds*n*2-7, centery, 60, 44])#left
            pg.draw.rect(sc, colors.WHITE, [centerx, centery+ds*n-7, 44, 60])#bottom
            pg.draw.rect(sc, colors.WHITE, [centerx+ds*n*2-7, centery, 60, 44])#right
            pg.display.update()

def play(ID):
    global data
    global PlayerID
    global error
    sc.blit(desk, (0, 0))
    start_stage = True
    game_keep_going = False
    select_stage = False
    place_stage = False
    #開始遊戲時的設定
    if start_stage:
        turn = 0
        sio.emit('login',ID)
        while len(data["players"]) < 4:
            AntiCrash()
            process_font("等待其他玩家", turn)
            if ID in data["players"]:
                PlayerID = data["players"].index(ID)
            if data["players"] == 4:
                com1Name = data["players"][0]
                com2Name = data["players"][1]
                com3Name = data["players"][2]
        #發牌給電腦及玩家
        numlist = [0, 1, 2, 3]
        numlist.remove(PlayerID)
        hands = data["hand"]
        player_card = hands[3]
        player_card.sort()
        #設置電腦與玩家數值
        global table1, com1, com2, com3, player1
        com1 = computer("1", com1Name, hands[0])
        com2 = computer("2", com2Name, hands[1])
        com3 = computer("3", com3Name, hands[2])
        player1 = player(player_card, PlayerID, ID)
        #翻開四張牌擺在桌上
        listgroup = data["base"]
        #設置桌面數值
        table1 = table(listgroup[0], listgroup[1], listgroup[2], listgroup[3])
        #動畫
        # assign()
        process_font("發牌中", turn)
        com1.draw_hand(True)
        com2.draw_hand(True)
        com3.draw_hand(True)
        player1.draw_hand(True)
        player1.draw_select(0)
        table1.bg_table.blit(table_desk, (0, 0))
        table1.draw_table(True)
        process_font("發牌完成", turn)
        turn+=1
        #舞台開關
        start_stage = False
        game_keep_going = True
        select_stage = True
    while game_keep_going :
        everyone_selected_card = {0 : 0}
        sorted_cards_num = [0]
        if select_stage:#選擇階段
            #讓電腦和玩家選牌
            process_font("請選擇你要出的牌", turn)
            sorted_cards_num = ["NULL", "NULL", "NULL", "NULL"]
            count = 0
            player1.selected_card = 0
            while count != 4 or error:
                AllThrow = data["facecard"]
                if AllThrow[0] != 0 and sorted_cards_num[0] == "NULL":
                    sorted_cards_num[0] = com1.select_card()
                    count+=1
                if AllThrow[1] != 0 and sorted_cards_num[1] == "NULL":
                    sorted_cards_num[1] = com2.select_card()
                    count+=1
                if AllThrow[2] != 0 and sorted_cards_num[2] == "NULL":
                    sorted_cards_num[2] = com3.select_card()
                    count+=1
                player1.select_card(sorted_cards_num[3])
                if player1.selected_card != 0 and sorted_cards_num[3] == "NULL":
                    sorted_cards_num[3] = player1.selected_card
                    count+=1
                    process_font("等待其他玩家出牌", turn)
            com1.draw_throw(sorted_cards_num[0], True)
            com2.draw_throw(sorted_cards_num[1], True)
            com3.draw_throw(sorted_cards_num[2], True)
            pg.display.update()
            #變換階段變數
            select_stage = False
            place_stage = True
            #建立可以用卡的數字檢索出的玩家的dict
            everyone_selected_card = {sorted_cards_num[0] : "com1", sorted_cards_num[1] : "com2", sorted_cards_num[2] : "com3", sorted_cards_num[3] : "player"}
            #把四張卡排序
            sorted_cards_num.sort()
        if place_stage:#放置階段
            for card in sorted_cards_num:#由小而大看
                distanse = [0,0,0,0]
                smaller = 0
                #看卡上數字與四列最後一張牌上的數字的距離
                distanse[0] = card - table1.list_group[0][len(table1.list_group[0]) - 1]
                distanse[1] = card - table1.list_group[1][len(table1.list_group[1]) - 1]
                distanse[2] = card - table1.list_group[2][len(table1.list_group[2]) - 1]
                distanse[3] = card - table1.list_group[3][len(table1.list_group[3]) - 1]
                for distanses in distanse:#檢查每個距離
                    #若小於零則計數增加一次
                    if distanses < 0:
                        smaller+=1
                #如果該牌不是小於全部列最後一張牌
                if smaller < 4:
                    closest = 106
                    closest_num = 0
                    #一列一列檢查哪一列符合
                    for i in range (0, 4):
                        #若距離為正且最小就選此列
                        if distanse[i] > 0 and distanse[i] < closest:
                            closest = distanse[i]
                            closest_num = i
                    ThisComputer = everyone_selected_card[card] == "player"
                    table1.place_card(closest_num, card, ThisComputer, everyone_selected_card[card])#放置
                    table1.draw_table(True)
                    process_font("自動排序中", turn)
                    pg.display.update()
                    if len(table1.list_group[closest_num]) == 6:#接第六張時
                        if everyone_selected_card[card] == "player":
                            process_font("收回第"+str(closest_num+1)+"排", turn)
                            player1.get_card(table1, closest_num, card)
                            player1.count_bull()
                        if everyone_selected_card[card] == "com1":
                            com1.get_card(table1, closest_num)
                            com1.count_bull()
                        if everyone_selected_card[card] == "com2":
                            com2.get_card(table1, closest_num)
                            com2.count_bull()
                        if everyone_selected_card[card] == "com3":
                            com3.get_card(table1, closest_num)
                            com3.count_bull()
                        table1.draw_table(True)
                        pg.display.update()
                #若全部小於
                else:
                    #若是玩家就自己選
                    if everyone_selected_card[card] == "player": # dict 改成 everyone_selected_card
                        process_font("請選擇一排收回", turn)
                        while error:
                            AntiCrash()
                        player1.select_list(table1, card)
                        table1.draw_table(True)
                        pg.display.update()
                    #若不是玩家則隨機選擇
                    else:
                        process_font("其他玩家選擇一排收回", turn)
                        if everyone_selected_card[card] == "com1":
                            while data["choosebase"][0] == "NULL" or error:
                                AntiCrash()
                            list_num = data["choosebase"][0]
                            com1.get_card(table1, list_num)
                            com1.count_bull()
                        if everyone_selected_card[card] == "com2" or error:
                            while data["choosebase"][1] == "NULL":
                                AntiCrash()
                            list_num = data["choosebase"][1]
                            com2.get_card(table1, list_num)
                            com2.count_bull()
                        if everyone_selected_card[card] == "com3" or error:
                            while data["choosebase"][2] == "NULL":
                                AntiCrash()
                            list_num = data["choosebase"][2]
                            com3.get_card(table1, list_num)
                            com3.count_bull()
                        table1.draw_table(True)
                        pg.display.update()
            #變換階段變數
            place_stage = False
            select_stage = True
            turn+=1

        #第10回合結束時，結束遊戲
        if turn == 11:
            table1.draw_table(True)
            pg.display.update()
            process_font("遊戲結束", 10)
            pg.time.delay(500)
            game_keep_going = False
        
    #結算
    process_font("結算中", turn)
    com1.count_bull()
    com2.count_bull()
    com3.count_bull()
    player1.count_bull()
    pg.time.delay(500)
    #比較
    Score_Name = [[player1.bull, player1.name], [com1.bull, com1.name], [com2.bull, com2.name], [com3.bull, com3.name]]
    Score_list = [player1.bull, com1.bull, com2.bull, com3.bull]
    result = []
    Score_list.sort()
    print(Score_list)
    for score in Score_list:
        for i in range(0, 4, 1):
            if Score_Name[i][0] == score and Score_Name[i] not in result:
                result.append(Score_Name[i])
    #印出
    process_text = pg.font.Font("Chinese.ttf", 48)#48
    sc.blit(desk, (0, 0))
    for name in result:
        score_rect = pg.Surface((60, 60))
        name_text = process_text.render(str(name[1]), True, colors.WHITE)
        # score_text = process_text.render(str(name[0]), True, colors.WHITE)
        sc.blit(name_text, (625, 100 + 100*result.index(name)))
        for n in range(0, name[0]+1):
            score_text = process_text.render(str(n), True, colors.WHITE)
            sc.blit(score_rect, (825, 100 + 100*result.index(name)))
            sc.blit(score_text, (825, 100 + 100*result.index(name)))
            pg.time.delay(25)
            pg.display.update()
    pg.display.update()
    again = MenuButton(sc, image.second_game, image.second_game_up, image.second_game_position, (0, 0))
    close = MenuButton(sc, image.close_game, image.close_game_up, image.end_position, (0, 0))
    back = MenuButton(sc, image.back, image.back_up, image.back_position, (0, 0))
    pause = True
    while pause:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return "close"
            if event.type == pg.MOUSEBUTTONUP:
                if again.isOver():
                    pause = False
                    return "again"
                if close.isOver():
                    pause = False
                    return "close"
                if back.isOver():
                    pause = False
                    return "back"
        again.draw()
        close.draw()
        back.draw()
        pg.display.update()
    #出現「重新遊玩」和「結束遊戲」按鈕，選擇後回傳結果
while error:
    pass
play(Name)