jQuery(".slideBox").slide({mainCell:".bd ul",effect:"fold",autoPlay:true});
jQuery('.slideTxtBoxs').slide({effect:'fold', endFun:function( i,c,s ){
	var urlList = ['/news/','/news/gg/','/news/hd/','/news/mt/'];
		$('#newsContent .hd ul a').attr('href',''+urlList[i]);
	}
});
jQuery(".slideTxtBox").slide();
jQuery(".roles").slide({effect:"fold"});
jQuery(".gamedatum").slide({effect:"fold", endFun:function( i,c,s ){
	var urlList = ['/xszn/','/cyzl/','/tswf/'];
		$('.game_datum.game p a').attr('href',''+urlList[i]);
	}
});
jQuery(".gamepic").slide({effect:"fold", endFun:function( i,c,s ){
	var urlList = ['/jmjt/','/mnwj/'];
		$('.game_picture.game.mt10 p a').attr('href',''+urlList[i]);
	}
});
<!----------新加----------->
jQuery(".txtScroll-top").slide({titCell:".hd ul",mainCell:".bd ul",autoPage:true,effect:"topLoop",autoPlay:true,vis:2});
jQuery(".increases").slide();

function startGame(){if(document.removeEventListener){document.removeEventListener('DOMMouseScroll','onMouseWheel',false);}document.onmousewheel=null;if($(".bg01").is(":hidden")){var $navDiv=$("#nav"),$banBox=$(".banBox");$navDiv.removeClass("navFixed").addClass("navAbs");$navDiv.css("top","960px");$(window).scrollTop(0);$("a#aNext").remove();$("a#aPrv").remove();$(".banWrap").html("");$(".bg01").show();var $banner=$(".banner"),$f1=$(".f1"),$f2=$(".f2"),$f1W=$f1.width(),$f2W=$f2.width();$banBox.animate({"height":0},1000,function(){ $banBox.css("display","none")});$navDiv.animate({"top":0},1000,function(ev){ $(".logo").stop(true).animate({"top":0});$banner.addClass("fActive");aTab1({tabHandleList:".newsTab h3 a",tabBodyList:".newsList > ul",tabBody:"li",bind:"click",mobile:270,direction:"left",special:"true"})})}}