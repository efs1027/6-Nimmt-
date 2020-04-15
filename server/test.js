var app = require('express')();
var server = require('http').Server(app);
var io = require('socket.io')(server);

server.listen(8070);
console.log("server is running!");
// WARNING: app.listen(80) will NOT work here!

app.get('/', function (req, res) {
  res.sendFile(__dirname + '/API_TEST.html');
});

function shuffle(array) {
  for (let i = array.length - 1; i > 0; i--) {
    let j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
}

var messages = [];
cardpool=[];
table={
"status":1,
"players":[],
"nowturn":0,
"choosebase":["NULL","NULL","NULL","NULL"],
"score":[[],[],[],[]],
"hand":[[],[],[],[]],
"base":[[],[],[],[]],
"facecard":[0,0,0,0]

};
for(i=1;i<=104;i++){
cardpool.push(i)
}
shuffle(cardpool);
//手排
for(i=0;i<4;i++){
  table.base[i].push(cardpool.shift())
  for(j=0;j<10;j++){
    table.hand[i].push(cardpool.shift())
  }
}
//主要接受操作API

//BASE
TESTMSG="8888";
loginnum=0;
io.on('connection', function(socket){
    //初始化...
    console.log("A user connected.");
    //io.emit("allMessage",messages);
    socket.on("login",function(obj){
      socket.emit("login",loginnum);
      loginnum+=1;
  })
    io.emit("chat","小豐泉婆霞");
    io.emit("tablejson",table);

    socket.on("tablejson",function(obj){
        io.emit("tablejson",table);
    })
    socket.on("chat", function(obj){
        console.log(obj)
    })
    socket.on("newmsg", function(obj){
      io.emit("newmsg",obj)
  })
    socket.on("login", function(obj){
      if (table.players.length<4){
      table.players.push(obj)
	  io.emit("tablejson",table);
      }
    })
    socket.on('sendMessage',function(obj){
      //get all message!
      messages.push(obj);
      console.log( obj.message + " - " + obj.name )
      io.emit('newMessage', obj);
    })


    socket.on("action",function(data){

      name=Number(data.name);
      card=Number(data.card);
      ac=Number(data.ac);
      console.log(name,ac,card);

      if (table.status==1){
        if(ac==1&&name>=0 && name<=3 && table.facecard[name]==0){
          console.log(table.hand[data.name]);
          if (table.hand[name].indexOf(Number(card))!=-1){
            table.hand[name].splice(table.hand[name].indexOf(Number(card)),1);
            msg=name+"將牌號"+card+"放入facecard";
            table.facecard[name]=card
            io.emit('newmsg', msg);

              if(table.facecard.indexOf(0)==-1){
                table.choosebase=["NULL","NULL","NULL","NULL"];
                table.status=2;
              }
          }
        }
        else{
          io.emit('newmsg', toString(name," ",card," ",ac));
        }
      }
      if (table.status==2){
        if(ac==2&&name>=0 && name<=3 && card>=0 && card<=3 &&table.facecard[name]!=0){
          table.base[card].push(table.facecard[name]);
          table.choosebase[name]=card;
          msg=name+"將牌號"+table.facecard[name]+"放入base"+card;
          table.facecard[name]=0;
        }
      }

      if(table.status == 2){
        all0=true;
        
        for(i=0;i<=3;i++){
            if(table.facecard[i]!=0){
              all0=false;
              
            }
        }
        if (all0==true){
          table.status=1;
        }
      }
      

      if(ac==3&&name>=0 && name<=3 && card>=0 && card<=3){
		table.choosebase[name]=card;
        for(i=0;i<=table.base[card].length;i++){
          table.score[name].push(table.base[card].shift());
        }
        if(table.facecard[name] != 0){
          table.base[card].push(table.facecard[name]);
        }
        table.facecard[name]=0;
      }
      if(ac==4&&name>=0 && name<=3 && card>=0 && card<=3){

        table.nowturn=card;
      }


  io.emit("tablejson",table);
  })
  })


