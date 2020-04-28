document.cookie="SameSite=None"
var audio = document.createElement("audio");

isconnected=false
isconnecting=false
ipAddr=""
pname=""
window.onload=function(){
    $("#bversion").text(navigator.userAgent);
}

function boxdown(){
    if(event.keyCode == 13) {
        pname= $(namebox).val();
        $(namebox).hide();
        $("#plsenter").text("歡迎 "+pname)
        $("#namepage").delay(3000).fadeOut()
        audio.src = "https://aquaminato.moe/voices/a-71.mp3";
        audio.play();
    }
}

async function solo(){
    alert("呼叫sole fn")
    await eel.open_sole();

}
async function muti(){
    if(isconnected==false){
        Swal.fire({
            icon: 'error',
            title: '錯誤',
            text: '請先連線至伺服器',
           // footer: ''
        })
    }
    else{
    await eel.open_muti(ipAddr,pname);
    alert("呼叫多人fn 傳入伺服器位置"+ipAddr+"和玩家ID:"+pname);
    
    }
}

async function btn_connect(){
    const ipAPI = '//api.ipify.org?format=json'

    const inputValue = fetch(ipAPI)
    .then(response => response.json())
    .then(data => data.ip)

    const { value: ipAddress } = await Swal.fire({
        title: '請輸入伺服器地址',
        input: 'text',
        inputValue: inputValue,
        showCancelButton: true,
        inputValidator: (value) => {
          if (!value) {
            return '該欄位不能為空'
          }
        }
      })
      
      if (ipAddress) {
        ipAddr=ipAddress;
        fn_connect(ipAddress);
        //跑秒
        let timerInterval
        Swal.fire({
        title: '連線中',
        html: '嘗試連線中 <b></b>',
        timer: 8000,
        timerProgressBar: true,
        onBeforeOpen: () => {
            Swal.showLoading()
            timerInterval = setInterval(() => {
                if (isconnected==true){
                    Swal.close()
                    Swal.fire({
                        // position: 'top-end',
                        icon: 'success',
                        title: '成功連線!',
                        showConfirmButton: false,
                        timer: 1500
                      })
                }
            const content = Swal.getContent()
            if (content) {
                const b = content.querySelector('b')
                if (b) {
                msg= Swal.getTimerLeft() /1000
                b.textContent = msg
                }
            }
            }, 100)
        },
        onClose: () => {
            clearInterval(timerInterval)
            console.log("等待連線視窗關閉")
        }
        }).then((result) => {
        /* Read more about handling dismissals below */
        if (result.dismiss === Swal.DismissReason.timer) {
            console.log('I was closed by the timer')
                Swal.fire({
                    icon: 'error',
                    title: '無法連線',
                    text: '發生了未知的網路錯誤',
                   // footer: ''
                })
        }
        })
        //跑秒結束
        console.log(ipAddress)
      }
}