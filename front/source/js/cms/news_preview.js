function NewsPreview() {
    this.time_start = $('#time-start');
    this.send_query_data = $('.btn-send-query-data');
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
    var form_inline = $('.form-inline-data');
    self.send_query_data.click(function(event){
        event.preventDefault();
        var start_time = form_inline.find('.start-time-input').val();
        var end_time = form_inline.find('.end-time-input').val();
        var category_value = form_inline.find('.category-value option:selected').val();
        var title = form_inline.find('#search').val();
        console.log('title',title);
        console.log('category_value',category_value);
        console.log('start_time',start_time);
        console.log('end_time',end_time);
        yourajax.post('')
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