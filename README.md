# 誰是牛頭王Update Log

# 事項
* 若需要測試請將project資料夾下載到C槽
* 所有程式碼皆使用Visual Studio Code編寫
* 影像檔案放在image資料夾，內含jpg,png以及用於再編輯的psd檔
*   BackGroundMusic，用於存放背景音樂檔，請後來加的音樂照著"musicx"命名原則加入，檔案格式一律為ogg檔
*   圖片路徑字串、背景音樂路徑字串以及顏色變數皆放於名為data_Path的資料夾中
*   遊戲進行用函式放於名為GameOperate的資料夾中
*   主程式進行在main.py
*   測試用檔案為test.py
*   FileTest.py是測試檔案處理用的
*   add_module_path.py為增加模組尋找路徑用，但不知為何一直沒有效果，所以data_Path才會是Package = =
*   PlayerFile和RoomFile為存放各種檔案的地方，沒事的話別動
*   遊玩前請於編譯器下載pygame、pyhton-socketio、requests
* 參考資料:
    https://www.youtube.com/watch?v=wqRlKVRUV_k&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk
    https://www.cnblogs.com/srl-southern/p/4949624.html
    https://ithelp.ithome.com.tw/users/20112078/ironman/1860?page=1
    https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/363393/
    https://blog.csdn.net/FourLeafCloverLLLS/article/details/78505387

## 2020/2/11 17:21更新日誌[1]
* 資料夾整理
* main.py:
    ### 新增:
        將一些變數和檔案路徑字串自main.py移置Package "data_Path"，使程式碼整體較為簡短
        完備class 按鈕，除了isOver()的判定以外都運作正常
        設立Welcome函式用於標題畫面的運算
    ### bug:
    ~~按鈕無法用isOver()判定滑鼠是否在按鈕上，無法用結束遊戲按鍵關閉視窗~~
    待發現
    ### 未來更新:
    ~~模式選擇畫面製作與放入~~
    ~~由標題畫面的運算接到遊戲運算~~

## 2020/2/12 12:05更新日誌[2]
* main.py:
    ### debug:
      解決按鈕無法用isOver()判定滑鼠是否在按鈕上的問題[1]
      原因:
        mouse_position是固定變數
    ### bug:
      待發現
  
  ## 20:48追記:
    ### 新增資料夾BackGroundMusic，用於存放背景音樂檔，請後來加的音樂照著"musicx"命名原則加入，檔案格式一律為ogg檔
        目前有「六兆年と一夜物語」和「God knows...」#別問為什麼都是宅歌，測試用而已
    * data_Path:
      新增BGM.py，用於存放背景音樂路徑字串
    *  main.py:
      新增:
        BGM類，用於呼叫以對背景音樂進行操作
        變換BGM按鍵功能實裝，點一下即可變換

## 2020/2/16 03:37更新日誌[3]
  * main.py:
    關於控制音樂選項的程式做好一半
    同上，圖片全部完成
  * data_Path:
     ### image.py:
          新增音樂選單底圖、歌曲名標籤串列、向左向右按鍵路徑字串
  * 未來更新:
    ~~模式選擇畫面製作與放入~~
    ~~由標題畫面的運算接到遊戲運算~~
    ~~音樂控制選單放大(因為原本設計的真的太小了)~~
    ~~實裝調音量功能~~
      ## 23:36追記
    * main.py:
          徹底完成主畫面所有功能(除開始遊戲)
    * 未來更新:
          ~~音樂控制選單放大(因為原本設計的真的太小了)
          實裝調音量功能~~

## 2020/2/18 19:26更新日誌[4]
  * main.py:
    * 新增:
      System類:處理後台運算
      徹底完成主畫面所有功能
  * 未來更新:
    ~~模式選擇畫面製作與放入~~

## 2020/3/20 22:41更新日誌[5]
  * main.py:
    ### 新增:
        System類:
            關於玩家資料的處理，含建造玩家資料、建造房間資料、搜尋房間、刪除玩家資料、
            刪除房間資料
      * bug:
        ~~如果有相同分數就會出現錯誤，大概是dict本身機制的問題~~
      * 未來更新:
        ~~四人模式完成(遠目~~

## 2020/3/26 02:31更新日誌[6]
  * 各個封包全部改用模組
      add_module_path.py終於有用了
  ### 新增:
    資料夾「程式碼、概念解釋文」:
      為了沒參與的兩位寫的解釋文都在裡面，我有空就寫，你們有空就看
  * debug:
    ~~解決如果有相同分數就會出現錯誤的問題，連解決後產生的bug都解決了，可喜可賀可喜可賀~~
  * 未來更新:
    ~~四人模式完成(遠目~~

## 2020/3/30 22:20更新日誌[7]
  ### 新增:
    Chinese.ttf:微軟正黑體(中文)，可以讓中文字正常顯示
  *  GameOperate.one_player:
      陽春的結算畫面
      因為找到中文字體，正式完成階段顯示了
  * 未來更新:
    ~~四人模式完成(遠目~~

## 2020/4/13 02:02更新日誌[8]
  ### 遲來的日誌以及突然的變化!!
    我們放棄用資料處理啦///
    改用node.js架的伺服器和socketio模組
    感謝技術支援
  ### 總之終於完全完成啦
      接下來只剩一些小地方的優化跟把卡面改成圖片而已了
