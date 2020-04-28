import eel, sys, os
pythonpath = sys.path[4]+"\\python.exe"
eel.init('web')


@eel.expose
def open_muti(ip,username):
    print(f"開啟多人遊戲函式已被呼叫 傳入值{ip} {username}")
    os.system(pythonpath + " four_player1.py " + ip + " " + username)

@eel.expose
def open_solo():
    print("開啟單人遊戲函式已被呼叫")
    os.system(pythonpath + " one_player.py")

eel.start('main.html',size=(1280,720))