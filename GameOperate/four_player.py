import pygame as pg, os
import data_Path.color as colors, data_Path.image as image

pg.init()

size = width, height = 1440, 720
sc = pg.display.set_mode(size)
bg_hand = pg.Surface((600, 200)) # 手牌區塊背景
bg_table = pg.Surface((800, 320)) # 桌面區塊背景
desk = pg.image.load(image.desk)
player2_desk = pg.image.load(image.com1_desk)
player3_desk = pg.image.load(image.com2_desk)
player4_desk = pg.image.load(image.com3_desk)
player1_desk = pg.image.load(image.player1_desk)
table_desk = pg.image.load(image.table_desk)
sc.blit(desk, (0, 0))
number = pg.font.SysFont("Arial", 24)

PlayerPath = ("C:\project\PlayerFile")
RoomPath = ("C:\project\RoomFile")

card_base = [1]

card_dict = {1 : 1} 

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

class player:#玩家類別
    
    #設定變數
    # bull = 0
    point_card = [] # point_card = [0] 改為 point_card = []
    # selected_card = 1
    
    def __init__(self, num, card):#設定基本資料
        self.name = "player" + str(num)#設定玩家名稱
        self.card = card#設定玩家擁有的牌
        self.selected_card = 1 # 被選中的牌初始化
        self.bg_hand = pg.Surface((600, 200)) # 設定區塊
        self.bull = 0#分數初始化
            
    def get_card(self, table, list_num, card_num):#收回卡片#card_num為玩家選的卡
        if len(self.point_card) == 1:
            card_list = table1.list_give_player(list_num, card_num)#由函數取得該列並置換排頭 ## 第一個self刪除
            self.point_card = card_list
        else:
            card_list = table1.list_give_player(list_num, card_num)#由函數取得該列並置換排頭 ## 第一個self刪除
            self.point_card.extend(card_list)#加進持有的分數牌中
        table1.bg_table = pg.Surface((800, 320))
        table1.bg_table.blit(table_desk, (0, 0))
        table1.draw_table(False)
        pg.display.update()

    def count_bull(self):#算分數
        self.bull = 0
        for num in self.point_card:
            self.bull += card_dict[num]
            
    def select_card(self):#選擇卡片
        entered = False
        card_num = 0
        while entered == False:#當尚未按下enter時
            for event in pg.event.get():  # 遍歷所有事件
                if event.type == pg.KEYDOWN:#查看所有按鍵事件 ## 這裡少加.type
                    if event.key == pg.K_LEFT and card_num != 0:#按左鍵的時候，選取左一個的牌 ## 這裡的event.key不能加pg
                        card_num-=1 
                    if event.key == pg.K_RIGHT and card_num != len(self.card)-1:#按右鍵的時候，選取右一個的牌 # 這裡要-1
                        card_num+=1
                    if event.key == pg.K_KP_ENTER or event.key == pg.K_SPACE:#按Enter時 ## 只能叫K_KP_ENTER，不是K_ENTER
                        #變換「是否按下Enter」的變數以跳出迴圈                            ### enter不明原因無效，暫改SPACE
                        entered = True
                        self.selected_card = self.card[card_num]
                        self.draw_hand(False, self.selected_card)
                        # player1.draw_select(card_num)
                        pg.display.update()
                        # #從手牌list中移除選擇的牌
                        self.card.pop(card_num) # remove改成pop，remove是尋找匹配值，而非索引
                        #回傳選擇的牌
                        return self.selected_card
            self.draw_hand(False, False)
            self.draw_select(card_num)
            pg.display.update()
                    
    def select_list(self, table, card_num):#收回卡片#card_num是玩家出的牌
        list_num = 0
        entered = False
        while entered == False:#當尚未按下enter時 
            for event in pg.event.get():  # 遍歷所有事件
                if event.type == pg.KEYDOWN:#查看所有按鍵事件 ## 這裡少加.type
                    if event.key == pg.K_UP and list_num != 0:#按上鍵時，選取上一個列
                        list_num-=1
                    if event.key == pg.K_DOWN and list_num != 3:#按下鍵時，選取下一個列
                        list_num+=1
                    if event.key == pg.K_KP_ENTER or event.key == pg.K_SPACE:#按Enter時 ## 只能叫K_KP_ENTER，不是K_ENTER
                        #玩家拿走該列並且放置他出的牌                                     ### enter不明原因無效，暫改SPACE
                        self.get_card(table, list_num, card_num)
                        #計算分數
                        self.count_bull()
                        #變換「是否按下Enter」的變數以跳出迴圈
                        entered = True
            table1.bg_table = pg.Surface((800, 320))
            table1.bg_table.blit(table_desk, (0, 0))
            table1.draw_sel_list(list_num)
            table1.draw_table(False)
            pg.display.update()

    def draw_hand(self, gra, selected_card): # 手牌 ## gra:gradually 逐漸變化
        self.bg_hand = pg.Surface((600, 200)) # 區塊刷新
        SITE = (0,0) # 絕對座標
        if str(self.name) == "player1":
            SITE = (420, 520)
            self.bg_hand.blit(player1_desk, (0,0))
        if str(self.name) == "player2":
            SITE = (1240, 60)
            self.bg_hand.blit(player2_desk, (0,0))
        if str(self.name) == "player3":
            SITE = (420, 0)
            self.bg_hand.blit(player3_desk, (0,0))
        if str(self.name) == "player4":
            SITE = (0, 60)
            self.bg_hand.blit(player4_desk, (0,0))
        for card in self.card:
            # 出牌
            if selected_card != False :
                x, y = 278, 20
                pg.draw.rect(self.bg_hand, colors.WHITE, [x, y, 44, 60])
                num_font = number.render(str(selected_card), True, colors.BLACK) 
                self.bg_hand.blit(num_font, (x, y+15))
                for i in range(card_dict[selected_card]):
                    pg.draw.circle(self.bg_hand, colors.RED, (x+6+i*6, y+6), 2)
            # 手牌
            n = self.card.index(card) 
            dx = 28*(10-len(self.card)) # 偏移
            x, y = 55+dx+n*50, 120 # 相對座標
            pg.draw.rect(self.bg_hand, colors.WHITE, [x, y, 44, 60])
            num_font = number.render(str(card), True, colors.BLACK)
            self.bg_hand.blit(num_font, (x, y+15))
            # 牌牛頭數
            for i in range(card_dict[card]):
                pg.draw.circle(self.bg_hand, colors.RED, (x+6+i*6, y+6), 2)
            # 右上牛頭數
            x, y = 550, 50
            pg.draw.circle(self.bg_hand, colors.RED, (x, y),10)
            num_font = number.render(str(self.bull), True, colors.RED)
            self.bg_hand.blit(num_font, (x+10, y))
            # 畫布印上sc
            sc.blit(self.bg_hand, (420, 520))
            if gra:
                pg.display.update()
                pg.time.delay(20)

    def draw_select(self, card_num): # 選牌框 ## gra gradually 逐漸變化
        thick = 3
        dx = 28*(10-len(self.card)) # 偏移
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

class table:#桌子類別
    
    def __init__(self, list1, list2, list3, list4):#設定基本資料
        self.list_group = [list1, list2, list3, list4]#把四列都放入一個list中
        
    def place_card(self, list_num, card_num):#玩家放置牌
        self.list_group[list_num].append(card_num)
        
    def list_give_player(self, list_num, card):#玩家收回一列
        give = self.list_group[list_num]#儲存該列資訊
        self.list_group[list_num] = [card]#放置之牌為排頭
        return give#回傳分數牌

    def draw_table(self, gra): # 桌面上之牌 ## gra gradually 逐漸變化
        # self.bg_table = pg.Surface((800, 320)) #畫面刷新，放置於函式外
        # self.bg_table.blit(table_desk, (0, 0)) #畫面刷新，放置於函式外
        for lists in self.list_group:
            col = self.list_group.index(lists)
            for card in lists:
                row = lists.index(card)
                x, y = 250+row*50, 20+col*75
                pg.draw.rect(self.bg_table, colors.WHITE, [x, y, 44, 60])
                num_font = number.render(str(card), True, colors.BLACK)
                self.bg_table.blit(num_font, (x, y+15))
                for i in range(card_dict[card]):
                    pg.draw.circle(self.bg_table, colors.RED, (x+6+i*6, y+6), 2)
                sc.blit(self.bg_table, (320, 200))
                if gra:
                    pg.display.update() 
                    pg.time.delay(40)

    def draw_sel_list(self, list_num): # 桌面收回牌列選擇
        x, y = 100, 50+list_num*75
        pg.draw.line(self.bg_table, colors.BLUE, (x, y), (x+100, y), 3)

def play():
    start_stage = True
    game_keep_going = False
    select_stage = False
    place_stage = False
    #開始遊戲時的設定
    if start_stage:
        #洗牌
        #random.shuffle(card_base)
        #發牌給四位玩家
        player1_card = card_base[1 : 11 : 1]
        player2_card = card_base[11 : 21 : 1]
        player3_card = card_base[21 : 31 : 1]
        player4_card = card_base[31 : 41 : 1]
        player1_card.sort()
        player2_card.sort()
        player3_card.sort()
        player4_card.sort()
        #設置四位玩家數值
        player1 = player("1", player1_card)
        player2 = player("2", player1_card)
        player3 = player("3", player1_card)
        player4 = player("4", player1_card)
        #翻開四張牌擺在桌上
        list1 = card_base[41 : 42 : 1]
        list2 = card_base[42 : 43 : 1]
        list3 = card_base[43 : 44 : 1]
        list4 = card_base[44 : 45 : 1]
        #設置桌面數值
        table1 = table(list1, list2, list3, list4)
        start_stage = False
        game_keep_going = True
        select_stage = True
    
    while game_keep_going:
        everyone_selected_card = {0 : 0}
        sorted_cards_num = []
        if select_stage:#選擇階段
            #讓玩家選牌
            card1 = player1.select_card()
            card2 = player2.select_card()
            card3 = player3.select_card()
            card4 = player4.select_card()
            #變換階段變數
            select_stage = False
            place_stage = True
            #建立可以用卡的數字檢索出的玩家的dict
            everyone_selected_card = {card1 : "player1", card2 : "player2", card3 : "player3", card4 : "player4"}
            #把四張卡存入list後排序
            sorted_cards_num = list(everyone_selected_card.keys())
            sorted_cards_num.sort()
            
        if place_stage:#放置階段
            for card in sorted_cards_num:#由小而大看
                distanse = [0]
                smaller = 0
                #看卡上數字與四列最後一張牌上的數字的距離
                distanse[0] = card - table.list_group[0][len(table1.list_group[0]) - 1]
                distanse[1] = card - table.list_group[1][len(table1.list_group[1]) - 1]
                distanse[2] = card - table.list_group[2][len(table1.list_group[2]) - 1]
                distanse[3] = card - table.list_group[3][len(table1.list_group[3]) - 1]
                for distanse in distanse:#檢查每個距離
                    #若小於零則計數增加一次
                    if distanse < 0:
                        smaller+=1
                #如果該牌不是小於所有列最後一張牌
                if smaller < 4:
                    closest = 106
                    closest_num = 0
                    #一列一列檢查哪一列符合
                    for i in range (0, 4):
                        #若距離為正且最小就選此列
                        if distanse[i] > 0 and distanse[i] < closest:
                            closest = distanse[i]
                            closest_num = i
                    table1.place_card(closest_num, card)#放置
                #若全部小於
                else:#檢查是哪個玩家然後讓玩家選排
                    if dict[card] == "player1":
                        player1.select_list(table1, card)
                    if dict[card] == "player2":
                        player2.select_list(table1, card)
                    if dict[card] == "player3":
                        player3.select_list(table1, card)
                    if dict[card] == "player4":
                        player4.select_list(table1, card)
         #沒有手牌時，結束遊戲
        if len(player1.card) == 0:
            game_keep_going = False
        else:
            #變換階段變數
            place_stage = False
            select_stage = True

    #結算
    player1.count_bull()
    player2.count_bull()
    player3.count_bull()
    player4.count_bull()
    #比較
    #建立用分數對照玩家名的字典
    score_dict = {player1.bull : "player 1", player2.bull : "player 2", player3.bull : "player 3", player4.bull : "player 4"}
    #提取分數部分後排序
    score_list = list(score_dict.keys())
    score_list.sort()
    #因為分數最小的最輸，所以翻轉list
    #score_list.reverse()
    #印出
    print("1 st : " + score_dict(score_list[0]) + "   " + score_list[0] + "pt")
    print("2 ed : " + score_dict(score_list[1]) + "   " + score_list[1] + "pt")
    print("3 rd : " + score_dict(score_list[2]) + "   " + score_list[2] + "pt")
    print("4 th : " + score_dict(score_list[3]) + "   " + score_list[3] + "pt")