function CMS(){


    this.thumbnail = $('#thumbnail-btn');
    this.progressGroup = $('#progress-group');
    this.buttonComplete = $('#thumbnail-btn-cancel');
    this.progress = $('.progress');
    this.releaseNewsBtn = $('#release-news-button');

}




//提交发表新闻表单
CMS.prototype.listenReleaseBTN = function() {
    var self = this;
    self.releaseNewsBtn.click(function (event) {
        event.preventDefault();
        var title = $('#title-news').val();
        var category = $('#option-control');
        var category_val = category.val();
        var category_text = $('#option-control option[value="'+category+'"]').text();
        var content = window.ue.getContent();
        var thumbnail = CMS.thumbnail.val();
        console.log('title',title);
        console.log('category_text',category_text);
        console.log('category',category);
        console.log('content',content);
        console.log('thumbnail',thumbnail);
        var border_white={'border':'#ced4da solid 1px'};
        var border_red={'border':'red solid 1px'};
        category.css(border_white);category.css(border_white);
        if (parseInt(category_val) === 404){
            category.css(border_red);
            window.messageBox.showError('请选择分类')
        }
        else {
            yourajax.post({
                'url': '/cms/release_news',
                'data': {'title': title, 'category': category_val, 'content': content, 'thumbnail': thumbnail},
                'success': function (result) {
                    if (result['code'] === 200) {
                        alertBox.alertSuccess('已完成');
                        console.log('成功', result);
                        console.log('成功', result);
                        console.log('成功', result);


                    }
                }
            })
        }
    });
};



//ueditor
CMS.prototype.initUeditor = function(){
    window.ue = UE.getEditor('editor',{
        'initialFrameWidth':'100%',
        'serverUrl':'/ueditor/upload/',
        'toolbars':[[
            'fullscreen','source', '|', 'undo', 'redo', '|',
            'bold', 'italic', 'underline', 'fontborder', 'strikethrough', 'superscript', 'subscript', 'removeformat', 'formatmatch', 'autotypeset', 'blockquote', 'pasteplain', '|', 'forecolor', 'backcolor', 'insertorderedlist', 'insertunorderedlist', 'selectall', 'cleardoc', '|',
            'rowspacingtop', 'rowspacingbottom', 'lineheight', '|',
            'customstyle', 'paragraph', 'fontfamily', 'fontsize', '|',
            'directionalityltr', 'directionalityrtl', 'indent', '|',
            'justifyleft', 'justifycenter', 'justifyright', 'justifyjustify', '|', 'touppercase', 'tolowercase', '|',
            'link', 'unlink', 'anchor', '|', 'imagenone', 'imageleft', 'imageright', 'imagecenter', '|',
            'simpleupload', 'insertimage', 'emotion', 'scrawl', 'insertvideo', 'music', 'attachment', 'map', 'gmap', 'insertframe', 'insertcode', 'webapp', 'pagebreak', 'template', 'background', '|',
            'horizontal', 'date', 'time', 'spechars', 'snapscreen', 'wordimage', '|',
            'inserttable', 'deletetable', 'insertparagraphbeforetable', 'insertrow', 'deleterow', 'insertcol', 'deletecol', 'mergecells', 'mergeright', 'mergedown', 'splittocells', 'splittorows', 'splittocols', 'charts', '|',
            'print', 'preview', 'searchreplace', 'drafts','help'
        ]]
    })
};


//获取新闻发布






//缩略图上传七牛云主程序
CMS.prototype.listenThumbnailUploadEvent = function(){
    var self = this;
    self.thumbnail.change(function(){
        var file = this.files[0];
        var key = new Date().getTime()+'.'+file.name.split('.')[1];
        var putExtra = {
            fname:key,
            params:{},
            mimeType:null
        };
        var config = {
            useCndDomain:true,
            retryCount:6.00,
            region:qiniu.region.z2
        };
        yourajax.get({
            'url':'/cms/thumbnail_process',
            'success':function(result){
                if (result['code'] === 200){
                    var token = result['data']['token'];
                    var observable = qiniu.upload(file,key,token,putExtra,config);
                    console.log('observable',observable);
                    var progress = $('.progress');
                    var progressGroup = CMS.progressGroup;
                    self.buttonComplete.text('取消');
                    self.buttonComplete.removeClass('btn-info');
                    self.buttonComplete.removeClass('btn-dark');
                    self.buttonComplete.addClass('btn-danger');
                    progressGroup.show();
                    progress.show();
                    self.subscription = observable.subscribe({
                        'next':self.handleFileUploadProcess,
                        'error':self.handleFileErrorProcess,
                        'complete':self.handleFileComplete
                    })
                }
            }
        })
    })
};

//七牛上传取消监听
CMS.prototype.listenCancelsubscription = function(){
    var self = this;
    self.buttonComplete.click(function(event){
        event.preventDefault();
        self.subscription.unsubscribe();
        self.progress.hide();
    })
};

//七牛上传处理中
CMS.prototype.handleFileUploadProcess = function(response){
    var self = this;
    var total = response.total;
    console.log('precent',total);
    var percent_temp = total.percent;
    var precentInt = parseFloat(percent_temp);
    var percentFloat = precentInt.toFixed(2);
    var percentInt = parseInt(percentFloat)+'%';
    self.progressBar = $('.progress-bar');
    self.progressBar.css({'width':percentInt});
    self.progressBar.text('已完成'+percentFloat+'%')
};

//七牛上传错误
CMS.prototype.handleFileErrorProcess = function(error){
    console.log('error',error);
    window.messageBox.show(error);
};

//七牛上传完成
CMS.prototype.handleFileComplete = function(response){
    console.log('complete_response',response);
    var self = this;
    var thumbnailCancelBtn = $('#thumbnail-btn-cancel');
    var progress = $('.progress');
    progress.hide();
    thumbnailCancelBtn.removeClass('btn-danger');
    thumbnailCancelBtn.addClass('btn-info');
    thumbnailCancelBtn.text('已完成');
    self.progressBar.css({'width':0});
    console.log('完成');
    var thumbnail = CMS.thumbnail;
    var domain = 'http://q1wvz08zi.bkt.clouddn.com/';
    var url = domain + response.key;
    thumbnail.val(url);
    window.messageBox.show('已完成')
};

//------------------------



CMS.prototype.Run = function(){
    this.listenThumbnailUploadEvent();
    this.listenCancelsubscription();
    this.listenReleaseBTN();
    this.initUeditor();
};

$(function(){
    var cms = new CMS();
    cms.Run();
    CMS.progressGroup = $('#progress-group');
    CMS.thumbnail = $('#picture');
});