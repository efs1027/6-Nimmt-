<<<<<<< HEAD
import pygame as pg, random, os
import data_Path.color as colors, data_Path.image as image

pg.init()

class player():

    def __init__(self, RoomPath, No):#設定基本資料
        self.No = No
        self.RoomPath = RoomPath
        self.name = self.get_datas(0)
        self.card = self.get_basic()
        self.selected_card = 1 # 被選中的牌初始化
        self.bull = 0#分數初始化
        self.point_card = []
    
    def get_datas(self, line):
        f = open(self.RoomPath + '\PlayerData' + str(self.No) , 'r')
        Data = f.readlines()
        f.close()
        need = Data[line]
        now = ""
        operated = 0
        if line != 0:
            for i in need:
                if i == "\n":
                    operated = int(now)
                    now = ""
                elif i != " ":
                    now+=i
        else:
            for i in need:
                if i == "\n":
                    operated = now
                    now = ""
                elif i != " ":
                    now+=i
        return operated

    def give_datas(self, data, line):
        before = open(self.RoomPath + '\PlayerData' + str(self.No), 'r')
        file_datas = before.readlines()
        before.close()
        data_str = str(data)
        file_datas[line] = data_str[1:-1:1] + '\n'
        after = open(self.RoomPath + '\PlayerData' + str(self.No), 'w')
        after.writelines(file_datas)
        after.close()

    def reset_data(self):
        before = open(self.RoomPath + '\PlayerData' + str(self.No), 'r')
        file_datas = before.readlines()
        before.close()
        file_datas[1] = '\n'
        file_datas[2] = '\n'
        after = open(self.RoomPath + '\PlayerData' + str(self.No), 'w')
        after.writelines(file_datas)
        after.close()
    
    def get_basic(self):
        f = open(self.RoomPath + '\BasicData', 'r')
        Data = f.readlines()
        f.close()
        need = Data[self.No-1]
        now = ""
        operated = []
        for i in need:
            if i == "," or i == "\n":
                operated.append(int(now))
                now = ""
            elif i != " ":
                now+=i
        return operated

    def get_card(self, table, list_num, card_num):#收回卡片#card_num為玩家選的卡
        if len(self.point_card) == 1:
            card_list = table1.list_give_player(list_num, card_num)#由函數取得該列並置換排頭 ## 第一個self刪除
            self.point_card = card_list
        else:
            card_list = table1.list_give_player(list_num, card_num)#由函數取得該列並置換排頭 ## 第一個self刪除
            self.point_card.extend(card_list)#加進持有的分數牌中

    def count_bull(self):#算分數
        self.bull = 0
        for num in self.point_card:
            self.bull += card_dict[num]
        self.give_datas(self.bull, 3)

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
                        # player1.draw_select(card_num)
                        pg.display.update()
                        # #從手牌list中移除選擇的牌
                        self.card.pop(card_num) # remove改成pop，remove是尋找匹配值，而非索引
                        #回傳選擇的牌
                        self.give_datas(self.selected_card, 1)
                        return self.selected_card
    
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
                        #玩家拿走該列並且放置他出的牌                              ### enter不明原因無效，暫改SPACE
                        self.get_card(table, list_num, card_num)
                        self.give_datas(list_num, 2)
                        #計算分數
                        self.count_bull()
                        #變換「是否按下Enter」的變數以跳出迴圈
                        entered = True

class other_player():

    def __init__(self, RoomPath, No):#設定基本資料
        self.No = No
        self.RoomPath = RoomPath
        self.name = self.get_datas(0)
        self.bull = 0#分數初始化
    
    def get_datas(self, line):
        f = open(self.RoomPath + '\PlayerData' + str(self.No) , 'r')
        Data = f.readlines()
        f.close()
        need = Data[line]
        now = ""
        operated = 0
        if line != 0:
            for i in need:
                if i == "\n":
                    operated = int(now)
                    now = ""
                elif i != " ":
                    now+=i
        else:
            for i in need:
                if i == "\n":
                    operated = now
                    now = ""
                elif i != " ":
                    now+=i
        return operated

    def get_card(self, table, list_num, card_num):#收回卡片#card_num為玩家選的卡
        table1.list_give_player(list_num, card_num)#由函數取得該列並置換排頭 ## 第一個self刪除

    def count_bull(self):#算分數
        while self.get_datas(3) == 0:
            pg.display.update()
        self.bull = self.get_datas(3)

    def select_card(self):#選擇卡片
        while self.get_datas(1) == 0:
            pg.display.update()
        return self.get_datas(1)
    
    def select_list(self, table):#收回卡片#card_num是玩家出的牌
        #玩家拿走該列並且放置他出的牌
        while self.get_datas(2) == 0:
            pg.display.update()
        self.get_card(table, self.get_datas(2), self.get_datas(1))
        #計算分數
        self.count_bull()

class table:#桌子類別
    
    def __init__(self):#設定基本資料
        self.list_group = [self.get_basic(4), self.get_basic(5), self.get_basic(6), self.get_basic(7)]#把四列都放入一個list中 ## 雙層list
        self.bg_table = pg.Surface((800, 320))
        
    def get_basic(self, line):
        f = open(self.RoomPath + '\BasicData', 'r')
        Data = f.readlines()
        f.close()
        need = Data[line]
        now = ""
        operated = []
        for i in need:
            if i == "," or i == "\n":
                operated.append(int(now))
                now = ""
            elif i != " ":
                now+=i
        return operated
    
    def place_card(self, list_num, card_num):#玩家放置牌
        self.list_group[list_num].append(card_num)
        
    def list_give_player(self, list_num, card):#玩家收回一列
        give = self.list_group[list_num]#儲存該列資訊
        self.list_group[list_num] = [card]#放置之牌為排頭
        self.draw_table(True)
        return give#回傳分數牌

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

def play(RoomPath, PlayerNo):
    start_stage = True
    game_keep_going = False
    select_stage = False
    place_stage = False
    #開始遊戲時的設定
    if start_stage:
        all_No = [1, 2, 3, 4]
        SelfComPlayer = player(RoomPath, PlayerNo)
        all_No.remove(PlayerNo)
        OtherPlayer1 = other_player(RoomPath, all_No[0])
        OtherPlayer2 = other_player(RoomPath, all_No[1])
        OtherPlayer3 = other_player(RoomPath, all_No[2])
        global table1
        table1 = table()
        start_stage = False
        game_keep_going = True
        select_stage = True
    
    while game_keep_going:
        veryone_selected_card = {0 : 0}
        sorted_cards_num = []
        if select_stage:#選擇階段
            #讓玩家選牌
            card1 = SelfComPlayer.select_card()
            card2 = OtherPlayer1.select_card()
            card3 = OtherPlayer2.select_card()
            card4 = OtherPlayer3.select_card()
            #變換階段變數
            select_stage = False
            place_stage = True
            #建立可以用卡的數字檢索出的玩家的dict
            everyone_selected_card = {card1 : SelfComPlayer.name, card2 : OtherPlayer1.name, card3 : OtherPlayer2.name, card4 : OtherPlayer3.name}
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
                    if len(table1.list_group[closest_num]) == 6: # 新增接第六張時行為
                        if everyone_selected_card[card] == SelfComPlayer.name:
                            SelfComPlayer.get_card(table1, closest_num, card)
                            SelfComPlayer.count_bull()
                        if everyone_selected_card[card] == OtherPlayer1.name:
                            OtherPlayer1.get_card(table1, closest_num)
                            OtherPlayer1.count_bull()
                        if everyone_selected_card[card] == OtherPlayer2.name:
                            OtherPlayer2.get_card(table1, closest_num)
                            OtherPlayer2.count_bull()
                        if everyone_selected_card[card] == OtherPlayer3.name:
                            OtherPlayer3.get_card(table1, closest_num)
                            OtherPlayer3.count_bull()
                #若全部小於
                else:#檢查是哪個玩家然後讓玩家選排
                    if dict[card] == SelfComPlayer.name:
                        SelfComPlayer.select_list(table1, card)
                    if dict[card] == OtherPlayer1.name:
                        OtherPlayer1.select_list(table1, card)
                    if dict[card] == OtherPlayer2.name:
                        OtherPlayer2.select_list(table1, card)
                    if dict[card] == OtherPlayer3.name:
                        OtherPlayer3.select_list(table1, card)
         #沒有手牌時，結束遊戲
        if len(SelfComPlayer.card) == 0:
            game_keep_going = False
        else:
            #變換階段變數
            place_stage = False
            select_stage = True
            SelfComPlayer.reset_data()

    #結算
    SelfComPlayer.count_bull()
    OtherPlayer1.count_bull()
    OtherPlayer2.count_bull()
    OtherPlayer3.count_bull()
    #比較
    #建立用分數對照玩家名的字典 #無用= =
    #改用原始的list慢慢排
    Score_Name = [[SelfComPlayer.bull, SelfComPlayer.name], [OtherPlayer1.bull, OtherPlayer1.name], [OtherPlayer2.bull, OtherPlayer2.name], [OtherPlayer3.bull, OtherPlayer3.name]]
    Score_list = [SelfComPlayer.bull, OtherPlayer1.bull, OtherPlayer2.bull, OtherPlayer3.bull]
    result = []
    Score_list.sort()
    for score in Score_list:
        for i in range(0, 4, 1):
            if Score_Name[i][0] == score:
                result.append(Score_Name[i])
    #印出
    print("1 st : " + result[0][1] + "   " + str(result[0][0]) + "pt")
    print("2 ed : " + result[1][1] + "   " + str(result[1][0]) + "pt")
    print("3 rd : " + result[2][1] + "   " + str(result[2][0]) + "pt")
=======
import pygame as pg, random, os
import data_Path.color as colors, data_Path.image as image

pg.init()

class player():

    def __init__(self, RoomPath, No):#設定基本資料
        self.No = No
        self.RoomPath = RoomPath
        self.name = self.get_datas(0)
        self.card = self.get_basic()
        self.selected_card = 1 # 被選中的牌初始化
        self.bull = 0#分數初始化
        self.point_card = []
    
    def get_datas(self, line):
        f = open(self.RoomPath + '\PlayerData' + str(self.No) , 'r')
        Data = f.readlines()
        f.close()
        need = Data[line]
        now = ""
        operated = 0
        if line != 0:
            for i in need:
                if i == "\n":
                    operated = int(now)
                    now = ""
                elif i != " ":
                    now+=i
        else:
            for i in need:
                if i == "\n":
                    operated = now
                    now = ""
                elif i != " ":
                    now+=i
        return operated

    def give_datas(self, data, line):
        before = open(self.RoomPath + '\PlayerData' + str(self.No), 'r')
        file_datas = before.readlines()
        before.close()
        data_str = str(data)
        file_datas[line] = data_str[1:-1:1] + '\n'
        after = open(self.RoomPath + '\PlayerData' + str(self.No), 'w')
        after.writelines(file_datas)
        after.close()

    def reset_data(self):
        before = open(self.RoomPath + '\PlayerData' + str(self.No), 'r')
        file_datas = before.readlines()
        before.close()
        file_datas[1] = '\n'
        file_datas[2] = '\n'
        after = open(self.RoomPath + '\PlayerData' + str(self.No), 'w')
        after.writelines(file_datas)
        after.close()
    
    def get_basic(self):
        f = open(self.RoomPath + '\BasicData', 'r')
        Data = f.readlines()
        f.close()
        need = Data[self.No-1]
        now = ""
        operated = []
        for i in need:
            if i == "," or i == "\n":
                operated.append(int(now))
                now = ""
            elif i != " ":
                now+=i
        return operated

    def get_card(self, table, list_num, card_num):#收回卡片#card_num為玩家選的卡
        if len(self.point_card) == 1:
            card_list = table1.list_give_player(list_num, card_num)#由函數取得該列並置換排頭 ## 第一個self刪除
            self.point_card = card_list
        else:
            card_list = table1.list_give_player(list_num, card_num)#由函數取得該列並置換排頭 ## 第一個self刪除
            self.point_card.extend(card_list)#加進持有的分數牌中

    def count_bull(self):#算分數
        self.bull = 0
        for num in self.point_card:
            self.bull += card_dict[num]
        self.give_datas(self.bull, 3)

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
                        # player1.draw_select(card_num)
                        pg.display.update()
                        # #從手牌list中移除選擇的牌
                        self.card.pop(card_num) # remove改成pop，remove是尋找匹配值，而非索引
                        #回傳選擇的牌
                        self.give_datas(self.selected_card, 1)
                        return self.selected_card
    
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
                        #玩家拿走該列並且放置他出的牌                              ### enter不明原因無效，暫改SPACE
                        self.get_card(table, list_num, card_num)
                        self.give_datas(list_num, 2)
                        #計算分數
                        self.count_bull()
                        #變換「是否按下Enter」的變數以跳出迴圈
                        entered = True

class other_player():

    def __init__(self, RoomPath, No):#設定基本資料
        self.No = No
        self.RoomPath = RoomPath
        self.name = self.get_datas(0)
        self.bull = 0#分數初始化
    
    def get_datas(self, line):
        f = open(self.RoomPath + '\PlayerData' + str(self.No) , 'r')
        Data = f.readlines()
        f.close()
        need = Data[line]
        now = ""
        operated = 0
        if line != 0:
            for i in need:
                if i == "\n":
                    operated = int(now)
                    now = ""
                elif i != " ":
                    now+=i
        else:
            for i in need:
                if i == "\n":
                    operated = now
                    now = ""
                elif i != " ":
                    now+=i
        return operated

    def get_card(self, table, list_num, card_num):#收回卡片#card_num為玩家選的卡
        table1.list_give_player(list_num, card_num)#由函數取得該列並置換排頭 ## 第一個self刪除

    def count_bull(self):#算分數
        while self.get_datas(3) == 0:
            pg.display.update()
        self.bull = self.get_datas(3)

    def select_card(self):#選擇卡片
        while self.get_datas(1) == 0:
            pg.display.update()
        return self.get_datas(1)
    
    def select_list(self, table):#收回卡片#card_num是玩家出的牌
        #玩家拿走該列並且放置他出的牌
        while self.get_datas(2) == 0:
            pg.display.update()
        self.get_card(table, self.get_datas(2), self.get_datas(1))
        #計算分數
        self.count_bull()

class table:#桌子類別
    
    def __init__(self):#設定基本資料
        self.list_group = [self.get_basic(4), self.get_basic(5), self.get_basic(6), self.get_basic(7)]#把四列都放入一個list中 ## 雙層list
        self.bg_table = pg.Surface((800, 320))
        
    def get_basic(self, line):
        f = open(self.RoomPath + '\BasicData', 'r')
        Data = f.readlines()
        f.close()
        need = Data[line]
        now = ""
        operated = []
        for i in need:
            if i == "," or i == "\n":
                operated.append(int(now))
                now = ""
            elif i != " ":
                now+=i
        return operated
    
    def place_card(self, list_num, card_num):#玩家放置牌
        self.list_group[list_num].append(card_num)
        
    def list_give_player(self, list_num, card):#玩家收回一列
        give = self.list_group[list_num]#儲存該列資訊
        self.list_group[list_num] = [card]#放置之牌為排頭
        self.draw_table(True)
        return give#回傳分數牌

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

def play(RoomPath, PlayerNo):
    start_stage = True
    game_keep_going = False
    select_stage = False
    place_stage = False
    #開始遊戲時的設定
    if start_stage:
        all_No = [1, 2, 3, 4]
        SelfComPlayer = player(RoomPath, PlayerNo)
        all_No.remove(PlayerNo)
        OtherPlayer1 = other_player(RoomPath, all_No[0])
        OtherPlayer2 = other_player(RoomPath, all_No[1])
        OtherPlayer3 = other_player(RoomPath, all_No[2])
        global table1
        table1 = table()
        start_stage = False
        game_keep_going = True
        select_stage = True
    
    while game_keep_going:
        veryone_selected_card = {0 : 0}
        sorted_cards_num = []
        if select_stage:#選擇階段
            #讓玩家選牌
            card1 = SelfComPlayer.select_card()
            card2 = OtherPlayer1.select_card()
            card3 = OtherPlayer2.select_card()
            card4 = OtherPlayer3.select_card()
            #變換階段變數
            select_stage = False
            place_stage = True
            #建立可以用卡的數字檢索出的玩家的dict
            everyone_selected_card = {card1 : SelfComPlayer.name, card2 : OtherPlayer1.name, card3 : OtherPlayer2.name, card4 : OtherPlayer3.name}
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
                    if len(table1.list_group[closest_num]) == 6: # 新增接第六張時行為
                        if everyone_selected_card[card] == SelfComPlayer.name:
                            SelfComPlayer.get_card(table1, closest_num, card)
                            SelfComPlayer.count_bull()
                        if everyone_selected_card[card] == OtherPlayer1.name:
                            OtherPlayer1.get_card(table1, closest_num)
                            OtherPlayer1.count_bull()
                        if everyone_selected_card[card] == OtherPlayer2.name:
                            OtherPlayer2.get_card(table1, closest_num)
                            OtherPlayer2.count_bull()
                        if everyone_selected_card[card] == OtherPlayer3.name:
                            OtherPlayer3.get_card(table1, closest_num)
                            OtherPlayer3.count_bull()
                #若全部小於
                else:#檢查是哪個玩家然後讓玩家選排
                    if dict[card] == SelfComPlayer.name:
                        SelfComPlayer.select_list(table1, card)
                    if dict[card] == OtherPlayer1.name:
                        OtherPlayer1.select_list(table1, card)
                    if dict[card] == OtherPlayer2.name:
                        OtherPlayer2.select_list(table1, card)
                    if dict[card] == OtherPlayer3.name:
                        OtherPlayer3.select_list(table1, card)
         #沒有手牌時，結束遊戲
        if len(SelfComPlayer.card) == 0:
            game_keep_going = False
        else:
            #變換階段變數
            place_stage = False
            select_stage = True
            SelfComPlayer.reset_data()

    #結算
    SelfComPlayer.count_bull()
    OtherPlayer1.count_bull()
    OtherPlayer2.count_bull()
    OtherPlayer3.count_bull()
    #比較
    #建立用分數對照玩家名的字典 #無用= =
    #改用原始的list慢慢排
    Score_Name = [[SelfComPlayer.bull, SelfComPlayer.name], [OtherPlayer1.bull, OtherPlayer1.name], [OtherPlayer2.bull, OtherPlayer2.name], [OtherPlayer3.bull, OtherPlayer3.name]]
    Score_list = [SelfComPlayer.bull, OtherPlayer1.bull, OtherPlayer2.bull, OtherPlayer3.bull]
    result = []
    Score_list.sort()
    for score in Score_list:
        for i in range(0, 4, 1):
            if Score_Name[i][0] == score:
                result.append(Score_Name[i])
    #印出
    print("1 st : " + result[0][1] + "   " + str(result[0][0]) + "pt")
    print("2 ed : " + result[1][1] + "   " + str(result[1][0]) + "pt")
    print("3 rd : " + result[2][1] + "   " + str(result[2][0]) + "pt")
>>>>>>> cff7b2da62e72a81d78374e72cfd2c3e9be20bac
    print("4 th : " + result[3][1] + "   " + str(result[3][0]) + "pt")