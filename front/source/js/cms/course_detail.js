
function Coursedetail(){
}




Coursedetail.prototype.listenInputEvent = function(){
    var videoInfoSpan = $("#video-info");
    var video_url = videoInfoSpan.attr("data-video-url");
    var cover_url = videoInfoSpan.attr("data-cover-url");
    var course_id = videoInfoSpan.attr('data-course-id');
    var player = cyberplayer("playercontainer").setup({
        width: '100%',
        height: '100%',
        file: video_url,
        image: cover_url,
        autostart: false,
        stretching: "uniform",
        repeat: false,
        volume: 100,
        controls: true,
        tokenEncrypt: true,
        ak:'50dac442cb1c4f8e94eb897075a1f408'
    });
    player.on('beforePlay',function (e) {
        if(!/m3u8/.test(e.file)){
            return;
        }
        yourajax.get({
            'url': '/course/course_token',
            'data': {
                'video': video_url,
                'course_id': course_id
            },
            'success': function (result) {
                if(result['code'] === 200){
                    var token = result['data']['token'];
                    player.setToken(e.file,token);
                }else{
                    window.messageBox.showInfo(result['message']);
                    player.stop();
                }
            },
            'fail': function (error) {
                console.log(error);
            }
        });
    });
};

Coursedetail.prototype.consoleEvent = function(){
    console.log('input event change')
};

Coursedetail.prototype.Run = function(){
    this.listenInputEvent();
};




$(function(){
    var course = new Coursedetail();
    course.Run();
});

