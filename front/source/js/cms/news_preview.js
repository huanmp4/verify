function NewsPreview() {
    this.time_start = $('#time-start');
    this.send_query_data = $('.btn-send-query-data');
    this.form_inline = $('.form-inline');
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

NewsPreview.prototype.sendQueryDataBtn = function(){
    var self = this;
    self.send_query_data.click(function(){
        var start_time = this.form_inline.find('.start-time-input').val();
        var end_time = this.form_inline.find('.end-time-input').val();
        var category_value = this.form_inline.find('.category-value');
        yourajax.get({
            'url':'news_preview_cms_query',
            'data':{'start':start_time,'end':end_time,'category':category_value},
            'success':function(result){
                if (result['code'] === 200){
                    window.messageBox.showSuccess('查询中')
                }
                else{
                    window.messageBox.showError('查询失败');
                }
            }
        })
    })
};


NewsPreview.prototype.Run = function(){
    this.listenTimedatePicker();
    this.sendQueryDataBtn();
};

$(function(){
    var preview = new NewsPreview();
    preview.Run();
});