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
var yourajax = {
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
        var success_src = args['success'];
        args['success'] = function(result){
            if (result['code'] === 200){
                success_src(result)
            }
            else{
                var messageObject = result['message'];
                console.log('messageObject',messageObject);
                if(typeof messageObject == 'string' || messageObject.constructor == string){
                    window.messageBox.showError(messageObject);
                }else{
                    // {"password":['密码最大长度不能超过20为！','xxx'],"telephone":['xx','x']}
                    for(var key in messageObject){
                        var messages = messageObject[key];
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