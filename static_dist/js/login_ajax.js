function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    } return cookieValue;
}
var loginajax = {
    'get': function (args) {
        args['method'] = 'GET';
        this.ajax(args);
    },
    'success1':{'result':{'code':200,'message':'验证成功'}},
    'post': function (args) {
        args['method'] = 'POST';
        this._ajaxSetup();
        this.ajax(args);
    },
    'ajax': function (args) {
        var self = this;
        var success_src = args['success'];
        self.signinGroup = $('.signin-group');
        console.log('self.signinGroup',self.signinGroup);
        self.promptAccount = self.signinGroup.find('.prompt-account');
        self.promptPassword = self.signinGroup.find('.prompt-password');
        self.usernameBorder = self.signinGroup.find('input[name="username"]');
        self.passwordBorder = self.signinGroup.find('input[name="password"]');

        args['success'] = function(result){
            if (result['code'] === 200){
                success_src(result)
            }
            else if(result['code'] === 300){
                var messageObject = result['message'];
                for (var Key in messageObject){
                    var Messages = messageObject[Key];
                    var Message = Messages[0];
                    if ( Key === 'username'){
                        self.promptAccount.text(Message);
                        self.usernameBorder.css({'border':'1px solid red'});
                    }
                    else if ( Key === 'password'){
                        self.promptPassword.text(Message);
                        self.passwordBorder.css({'border':'1px solid red'})
                    }
                }
            }
            else if(result['code'] === 301){
                self.promptPassword.text(result['message']);
                self.passwordBorder.css({'border':'1px solid red'});
            }
            else if(result['code'] === 302){
                self.promptAccount.text(result['message']);
                self.usernameBorder.css({'border':'1px solid red'});
            }
            else if(result['code'] === 311){
                window.messageBox.show(result['message'])
            }
            else if(result['code'] === 401){
                self.promptPassword.text('code:401',result['message']);
                self.passwordBorder.css({'border':'1px solid red'});
            }
            else{
                var messageobject = result['message'];
                if ( typeof messageobject == 'string' || messageobject.constructor == String){
                    window.messageBox.showError(messageobject);
                }else{
                    // {"password":['密码最大长度不能超过20为！','xxx'],"telephone":['xx','x']}
                    for(var key in messageobject){
                        var messages = messageobject[key];
                        var message = messages[0];
                        window.messageBox.showError(message);
                    }
                }
                if (success_src){
                    success_src(result)
                }
            }
        };
        args['fail'] = function(error){
            console.log('内部错误，error信息:',error);
            window.messageBox.showError('服务器内部错误！请联系管理员');
        };
        $.ajax(args);
    },
    '_ajaxSetup': function () {
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!/^(GET|HEAD|OPTIONS|TRACE)$/.test(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                }
            }
        });
    }
};