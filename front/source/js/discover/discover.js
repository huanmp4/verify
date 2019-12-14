function Discover(){
    this.btnDiscover = $('#btn-discover');
}


Discover.prototype.createUediter = function(){
    var self = this;
    self.ue = UE.getEditor('editor',{
        'initFrameWidth':'100%',
        'serverUrl':'/ueditor/upload'
    });
};

Discover.prototype.formSubmission = function(){
    var self = this;
    self.btnDiscover.click(function(event){
        event.preventDefault();
        var content = self.ue.getContent();
        console.log('content',content);
        yourajax.post({
            'url':'/news/discover',
            'data':{'content':content},
            'success':function(result){
                if (result['code'] === 200){
                    window.messageBox.showSuccess('留言成功');
                    window.location.reload()
                }
            }
        })
    })
};

Discover.prototype.Run = function(){
    this.createUediter();
    this.formSubmission()
};

$(function(){
    var discover = new Discover();
    discover.Run();
});