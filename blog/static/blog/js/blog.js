function randomColor() {
	//16进制方式表示颜色0-F
	var arrHex = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"];
	var strHex = "#";
	var index;
	for(var i = 0; i < 6; i++) {
		//取得0-15之间的随机整数
		index = Math.round(Math.random() * 15);
		strHex += arrHex[index];
	}
	return strHex;
}

function endWith(str1, str2) {
    if (str1 == null || str2 == null) {
        return false;
    }
    if (str1.length < str2.length) {
        return false;
    } else if (str1 == str2) {
        return true;
    } else if (str1.substring(str1.length - str2.length) == str2) {
        return true;
    }
    return false;
}

function rotate() {
    $('.img_title').addClass('circle-label-rotate');
//    $('.img_title').aanimate({"opacity":"0","margin-left":"510px"},1500,function(){ });
//    $('.img_title').animate({
//        top: 500,
//    opacity: 1
//}, 1000, 'easeOutBounce');

//    $('.img_title').slideUp({duration: 1000, easing: 'easeOutBounce'});

    $('.img_title').animate({ left: "666px" }, 3000, 'easeOutBounce');

}


//头部交互
var shrinkHeader = function(doShrink){
    if (doShrink) {
        $('.section_header').addClass('shrink');
    }else{
        $('.section_header').removeClass('shrink');
    }
};


