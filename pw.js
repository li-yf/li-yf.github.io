function checkpassword(){    
    var inpa = $("#password").val();
    var md5password = hex_md5(inpa);
    //document.getElementById("show").value=md5password;
    var pwd="1e48c4420b7073bc11916c6c1de226bb";//约定的密码，加密的   
    if(pwd == md5password){ //判断一下是否一样
       window.location.href="English-Listening-"+inpa+".html";
    }
}