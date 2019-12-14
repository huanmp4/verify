

function Login(){
    this.button1 = $('.button1');
    this.button2 = $('.logup');
    this.button3 = $('.iconbaseline-close-px-copy');
    this.mainV = $('.mask-wrapper');
    this.taggle_logup = $('.toggle-logup');
    this.entourage = $('.entourage');
    this.taggle_login = $('.toggle-login-rich');

}

Login.prototype.hideEvent = function(){
    this.mainV.hide();
    console.log('show');
};

Login.prototype.showEvent = function(){
    this.mainV.show()
};

Login.prototype.toggleLogin = function(){
    var entourageLeft = this.entourage.css('left');
    var entourageLeft2 = parseInt(entourageLeft);
    console.log(entourageLeft);
    console.log('parse:'+entourageLeft2);
    if (entourageLeft2 < 0){
        this.entourage.animate({'left':0},500);
    }else{
        this.entourage.animate({'left':-300},500);
    }
};



Login.prototype.run = function(){
    var self = this;
    self.button2.click(function(){
    self.showEvent();
    });
    self.button1.click(function(){
        self.showEvent();
    });
    self.button3.click(function(){
        self.hideEvent()
    });
    self.taggle_login.click(function(){
        self.toggleLogin()
    });
    self.taggle_logup.click(function(){
        self.toggleLogin()
    })
};


$(function () {
    var banner = new Login();
    banner.run();
    console.log('run');
});