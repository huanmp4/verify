function NewsPreview() {
    this.time_start = $('#time-start');
    this.delete_news_btn = $('.btn-delete-news');
}


NewsPreview.prototype.listenTimedatePicker = function(){
    var self = this;
    var today = new Date();
    var time_end = $('#time-end');
    var endtDate = today.getFullYear() + '/' + today.getMonth() + '/' + today.getDay() + 1;
    var options = {
        'showButtonPanel':true,
        'format':'yyyy/mm/dd',
        'language':'zh-CN',
        'todayBtn':'linked',
        'heightLightloday':true,
        'clearBtn':true,
        'autoclose':true
    };
    self.time_start.datepicker(options);
    time_end.datepicker(options);
};


NewsPreview.prototype.listDeleteNewsBtn = function(){
    var self = this;
    self.delete_news_btn.click(function(){
        alertBox.alertConfirm({
            'title':'确定要删除吗',
            'confirmCallback':function(){
                var news_id = self.delete_news_btn.attr('data-news-id');
                console.log('news_id',news_id);
                yourajax.post({
                    'url':'news_preview_cms_delete',
                    'data':{'news_id':news_id},
                    'success':function(result){
                        if (result['code'] === 200) {
                            window.messageBox.showSuccess('删除成功')
                        }
                    }
                })
            }
        });
    })
};

NewsPreview.prototype.Run = function(){
    this.listenTimedatePicker();
    this.listDeleteNewsBtn();
};

$(function(){
    var preview = new NewsPreview();
    preview.Run();
});