# standard Python
import socketio
sio = socketio.Client()
sio.connect('http://25.60.36.119:8070/')

@sio.event
def connect():
    print("I'm connected!")
@sio.event
def connect_error():
    print("The connection failed!")
@sio.event
def newmsg(data):
    print(data)
@sio.event
def tablejson(data):
    print(data)
    print(data["hand"])

while True:
    command=input()
    li=command.split(" ")
    sio.emit('action',{"name":li[0],"ac":li[1],"card":li[2]})