function Demo() {
    this.delete_ip_btn = $('.btn-delete-ip');
}


Demo.prototype.listenDeleteIP = function(){
    var self = this;
    self.delete_ip_btn.click(function(event){
        event.preventDefault();
        var pk = $(this).parent().parent().attr('data-pk');
        console.log('pk',pk);
        yourajax.post({
            'url':'/cms/demo_cms_delete_ip',
            'data':{'pk':pk},
            'success':function(result){
                if( result['code'] === 200){
                    alertBox.alertConfirm({
                        'title':'确定要删除吗',
                        'confirmCallback':function(){
                            window.location.reload();
                        }
                    })
                }
            }
        })
    })
};


Demo.prototype.Run = function(){
    this.listenDeleteIP()
};

$(function(){
    var demo = new Demo();
    demo.Run();
});