document.cookie="SameSite=None"
var audio = document.createElement("audio");


function boxdown(){
    if(event.keyCode == 13) {
        pname= $(namebox).val();
        $("#plsenter").text("歡迎"+pname)
        $("#namepage").delay(3000).fadeOut()
        audio.src = "https://aquaminato.moe/voices/a-71.mp3";
        audio.play();
    }
}

function solo(){
    alert("呼叫sole fn")
}
function muti(){
    alert("呼叫muti fn")
}