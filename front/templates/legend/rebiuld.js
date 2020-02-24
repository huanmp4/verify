function BG(){

}

BG.prototype.animateEvent = function(){
    var self = this;
    var special = $('.special');
    console.log('what1');
    console.log('special',special);
    self.index = 0;
    special.animate({"left":-80},7000);
    setInterval(function(){
            if (self.index >= 7){
                special.css({"left":280});
                special.animate({"left":-80},7500);
                self.index = 0;
                console.log('开始index:',self.index);
            }else{
                self.index ++;
                console.log('index:',self.index);
            }
        },1000
    );
};

BG.prototype.Run = function(){
    this.animateEvent();
};

$(function(){
    var bg = new BG();
    bg.Run()
});