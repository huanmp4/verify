function CoursePay(){
    this.submitbtn = $('#submit-btn');
}

CoursePay.prototype.listenBTNsubmitEvent = function(){
    var self = this;
    self.submitbtn.click(function(event){
        event.preventDefault();
        var payform = $('#pay-form');
        var course_id = payform.find('input[name="course_id"]').val();
        var course_name = payform.find('input[name="goodsname"]').val();
        var istype = payform.find('input[name="istype"]:checked').val();
        var istype_first = payform.find('input[name="istype"]:first');
        var price = payform.find('input[name="price"]').val();
        var orderid = payform.find('input[name="orderid"]').val();
        var notify_url = payform.find('input[name="notify_url"]');
        var return_url = payform.find('input[name="return_url"]');
        var key = payform.find('input[name="key"]');

        console.log('course_id'+course_id);
        console.log(' course_name ' + course_name);
        console.log('istype' + istype);
        console.log('price' + price);
        console.log('orderid' + orderid);

        yourajax.get({
            'url':'/course/course_order_key',
            'data':{'course_id':course_id,'course_name':course_name,'istype':istype,'price':price,'orderid':orderid},
            'success':function(result){
                if (result['code'] === 200){
                    key_data = result['data']['key'];
                    return_url_return = result['data']['return_url'];
                    notify_url_return = result['data']['notify_url'];
                    istype_return = result['data']['istype'];
                    return_url.val(return_url_return);
                    notify_url.val(notify_url_return);
                    istype_first.val(istype_return);
                    key.val(key_data);
                    $('#pay-form').submit();
                }
            }
        })
    })
};

CoursePay.prototype.Run = function(){
    this.listenBTNsubmitEvent();
};

$(function(){
    var coursepay = new CoursePay();
    coursepay.Run()
});