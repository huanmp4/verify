function Course(){
    this.InputBtn = $('.InputBtn');
}


Course.prototype.initUEditor = function () {
    window.ue = UE.getEditor("editor",{
        'serverUrl': '/ueditor/upload/'
    });
};

Course.prototype.listenSubmitEvent = function () {
    var submitBtn = $("#submit-btn");
    submitBtn.click(function () {
        var title = $("#title-input").val();
        var category_id = $("#category-input").val();
        var teacher_id = $("#teacher-input").val();
        var video_url = $("#video-input").val();
        var cover_url = $("#cover-input").val();
        var price = $("#price-input").val();
        var duration = $("#duration-input").val();
        var profile = window.ue.getContent();

        yourajax.post({
            'url': '/cms/course_cms_add',
            'data': {
                'title': title,
                'video_url': video_url,
                'cover_url': cover_url,
                'price': price,
                'duration': duration,
                'profile': profile,
                'category_id': category_id,
                'teacher_id': teacher_id
            },
            'success': function (result) {
                if(result['code'] === 200){
                    window.location = window.location.href;
                }
            }
        });
    });
};


Course.prototype.listenInputEvent = function(){
    var self = this;
    document.getElementById("InputBtn").addEventListener("input", myFunction);
    function myFunction() {
        console.log('input event change')
    }
};

Course.prototype.consoleEvent = function(){
    console.log('input event change')
};

Course.prototype.Run = function(){
    this.initUEditor();
    this.listenSubmitEvent();
};




$(function(){
    var course = new Course();
    course.Run();
});