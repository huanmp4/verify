function Signin(){
    this.signinSubmitBtn = $('#signin-submit-btn');
    this.signupSubmitBtn = $('#signup-submit-btn');
    this.logOutNow = $('.log-out-now2');
    this.signupButton = $('.signup-text');
    this.wrapper = $('.mask-wrapper');
    this.loginBtn = $('.login-text');
    this.loginToggle = $('.switch');
    this.logincloseBtn = $('.close-btn');
    this.loginPrompt = $('.login-prompt');
    this.signinGroup = $('.signin-group');
    this.promptAccount = this.signinGroup.find('.prompt-account');
    this.promptPassword = this.signinGroup.find('.prompt-password');
    this.usernameBorder = this.signinGroup.find('input[name="username"]');
    this.passwordBorder = this.signinGroup.find('input[name="password"]');
    this.smsCaptchaBtn = $('.sms-captcha-btn');
    this.signupGroup = $('.signup-group');
    this.signupTelephone = this.signupGroup.find('input[name="telephone"]');
    this.msCaptcha = this.signupGroup.find('input[name="img-captcha-code"]');
}





//发送验证码点击
Signin.prototype.listenSendMessageEvent = function(){
    var self = this;
    self.smsCaptchaBtn.click(function(event){
        event.preventDefault();
        var signupTelephoneNum = self.signupTelephone.val();
        var mscaptchaNum =  self.msCaptcha.val();
        self.smsCaptchaBtn.unbind('click');
        console.log('telephone',signupTelephoneNum);
        console.log('code',mscaptchaNum);
        var count = 10;
        self.smsCaptchaBtn.addClass('disableClass');
        var timer = setInterval(function(){
            self.smsCaptchaBtn.text(count+'s');
            count -= 1;
            if (count < 0){
                clearInterval(timer);
                self.smsCaptchaBtn.text('发送验证码');
                self.smsCaptchaBtn.removeClass('disableClass');
                self.listenSendMessageEvent();
            }
        },500);
        yourajax.get({
            'url':'/register/send',
            'data':{'telephone':signupTelephoneNum,'code':mscaptchaNum},
            'success':function(result){
                if (result['code'] === 200){
                    window.messageBox.show(result['message']);
                }
                else if (result['code'] === 311){
                    window.messageBox.show('未知错误1')
                }
            },
            'fail':function(error){
                console('错误',error)
            }
        })
    });
};



Signin.prototype.Otherwise = function(){
    this.logOutNow.css({'cursor':'pointer'});
    var logOutNow2 = $('.log-out-now2');
    logOutNow2.css({'color':'black'})
};


Signin.prototype.signinPromptHideEvent = function(){
    var self = this;
    self.usernameBorder.css({'border':'1px solid #ccc'});
    self.passwordBorder.css({'border':'1px solid #ccc'});
    self.promptAccount.text('');
    self.promptPassword.text('');
    self.promptAccount.hide();
    self.promptPassword.hide();
};

Signin.prototype.signinPromptShowEvent = function(){
    var self = this;
    self.promptAccount.show();
    self.promptPassword.show();
};



//所有登录注册监听时间
Signin.prototype.ListenClick = function(){
    var self = this;

    //mask登录菜单显示
    self.loginBtn.click(function() {
        self.wrapper.show();
        self.loginPrompt.hide();
    });

    //登录按钮
    self.signinSubmitBtn.click(function(event){
        console.log('submitBtn');
        event.preventDefault();
        var username = self.signinGroup.find('input[name="username"]').val();
        var password = self.signinGroup.find('input[name="password"]').val();
        console.log('username',username);
        self.signinPromptHideEvent();
        self.signinPromptShowEvent();

        yourajax.post({
            'url':'/register/loginView',
            'data':{'username':username,'password':password},
            'success':function(result){
                console.log('result总信息',result);
                if (result['code'] === 200){
                    window.messageBox.show('成功登录');
                    window.location.reload();
                }
                else if(result['code'] === 301){
                    self.promptPassword.text(result['message']);
                    self.passwordBorder.css({'border':'1px solid red'});
                }
                else if(result['code'] === 302){
                    self.promptAccount.text(result['message']);
                    self.usernameBorder.css({'border':'1px solid red'});
                }
                else if(result['code'] === 401){
                    self.promptPassword.text('code:401',result['message']);
                    self.passwordBorder.css({'border':'1px solid red'});
                }
                else{
                    console.log('else');
                    var messageObject = result['message'];
                    console.log('other messing',messageObject);
                    for (var key in messageObject){
                        var messages = messageObject[key];
                        var message = messages[0];
                        if ( key === 'username'){
                            self.promptAccount.text(message);
                            self.usernameBorder.css({'border':'1px solid red'});
                        }
                        else if ( key === 'password'){
                            self.promptPassword.text(message);
                            self.passwordBorder.css({'border':'1px solid red'})
                        }
                        else{
                            this.promptAccount.text('错误,请联系管理员,代码3301');
                        }
                    }
                }
            },
            'fail':function(error){
                console.log(error)
            }
        })
    });

    //退出登录
    self.logOutNow.click(function(event){
        console.log('logoutClick');
        event.preventDefault();
        yourajax.post({
            'url': '/register/logoutView',
            'success':function(){
                console.log('成功');
                window.location.reload()
            }
        })
    });

    //注册点击展开
    self.signupButton.click(function(){
        var mask_wrapper = $('.mask-wrapper');
        var scroll = $('.scroll-wrapper');
        scroll.css({'left':'-400px'});
        mask_wrapper.show();
    });


    //图片验证码点击
    self.signupGroup = $('.input-group-addon');
    self.imageCaptcha = self.signupGroup.find('img[class="img-captcha"]');
    self.imageCaptcha.click(function(){
        var randomNum = "/register/img_captcha/"+"?random="+Math.random();
        console.log('randomNum:',randomNum);
        self.imageCaptcha.attr('src',randomNum);
    });




    //注册登录按钮
    self.signupSubmitBtn.click(function(event){
        console.log('submitBtn');
        event.preventDefault();
        var signup_group = $('.signup-group');
        var username_temp = signup_group.find('input[name="username"]').val();
        var telephone_temp = signup_group.find('input[name="telephone"]').val();
        var password_temp1 = signup_group.find('input[name="password1"]').val();
        var password_temp2 = signup_group.find('input[name="password2"]').val();
        var telephone_code = signup_group.find('input[name="sms_captcha"]').val();
        yourajax.post({
            'url':'/register/signupView',
            'data':{'username':username_temp,'telephone':telephone_temp,'password1':password_temp1,'password2':password_temp2,'telephone_code':telephone_code},
            'success':function(result){
                if (result['code'] === 200){
                    window.messageBox.show('注册成功');
                    window.location.reload();
                }
                else if (result['code'] === 311){
                    window.messageBox.show(result['message']);
                }
                else{
                    var messageObject = result['message'];
                    if (messageObject == 'String' || messageObject.constructor == String){

                        window.messageBox.show(messageObject);
                    }else{
                        console.log('messageObject',messageObject);

                        //打印出来
                    }
                }
            },
            'fail':function(error){
                console.log(error)
            }
        })
    });

    //关闭登录注册框
    self.logincloseBtn.click(function(){
        self.wrapper.hide();
        self.signinPromptHideEvent();
    });

    //登录注册切换
    self.loginToggle.click(function(){
        var scroll = $('.scroll-wrapper');
        var scrollLeft = scroll.css('left');
        var heightNum = $('.auth-wrapper');
        console.log('scrollLeft:',scrollLeft);
        var scrollLeftNum = parseInt(scrollLeft);
        console.log('scrollLeftNum:',scrollLeftNum);
        if (scrollLeftNum === -400){
            scroll.animate({'left':'0px'},500);
            heightNum.css({'margin-top':'-180px'});
        }
        if(scrollLeftNum === 0){
            scroll.animate({'left':'-400px'},500);
            heightNum.css({'margin-top':'-260px'});
        }
        self.signinPromptHideEvent();
    });
};

$(function(){
    var signin = new Signin();
    signin.ListenClick();
    signin.Otherwise();
    signin.listenSendMessageEvent();

});