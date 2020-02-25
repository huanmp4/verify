// JavaScript Document
$(window).scroll(function() {		
		if($(window).scrollTop() >= 1010){
			$('.g_fr').css({"position":"fixed","top":"0px"}); 
		}else{
            $('.g_fr').css({ "position": "absolute", "top": "1010px" });    
		}  
});

//返回顶部
$(function(){	
	$('.g_backTop').click(function(){$('html,body').animate({scrollTop: '0px'}, 800);});	
}); 

//左浮动
$(function(){	
	setTimeout(function(){$(".g_fl").css("top","0px")},1000);
	$('.fl_closeBtn a').click(function(){$(".g_fl").css({top:"-833px"}, 200);});	
}); 