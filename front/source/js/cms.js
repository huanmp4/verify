function CMS(){
    this. categoryModify = $('.btn-modify');
    this.categoryDelete = $('.btn-delete');
    this.thumbnail = $('#thumbnail-btn');
    this.progressGroup = $('#progress-group');
    this.buttonComplete = $('#thumbnail-btn-cancel');
    this.progress = $('.progress');
}


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
CMS.prototype.handleFileComplete = function(){
    var self = this;
    var thumbnailCancelBtn = $('#thumbnail-btn-cancel');
    var progress = $('.progress');
    progress.hide();
    thumbnailCancelBtn.removeClass('btn-danger');
    thumbnailCancelBtn.addClass('btn-info');
    thumbnailCancelBtn.text('已完成');
    self.progressBar.css({'width':0});
    console.log('完成');
    window.messageBox.show('已完成')
};

CMS.prototype.listenCategoryDeleted = function(){
    var self = this;
    self.categoryDelete.click(function(event){
        event.preventDefault();
        var parent = $(this);
        var tr = parent.parent().parent();
        var id = tr.attr('data-id');
        console.log('id',id);
        alertBox.alertConfirm({
            'title':'确定要删除吗',
            'text':'删除后无法恢复',
            'confirmCallback':function(){
                yourajax.post({
                    'url':'/cms/category_delete',
                    'data':{'id':id},
                    'success':function(result){
                        if (result['code'] === 200){
                            window.location.reload()
                        }
                    }
                })
            }
        });

    })
};


CMS.prototype.listenCategoryModify = function(){
    var self = this;
    self.categoryModify.click(function(event){
        event.preventDefault();
        console.log('点击');
        var btn = $(this);
        var tr = btn.parent().parent();
        var id = tr.attr('data-id');
        var name = tr.attr('data-name');
        console.log(name);
        alertBox.alertOneInput({
            'title': '修改分类名称',
            'placeholder': '请输入新的分类名称',
            'value':name,
            'confirmCallback':function(inputValue){
                yourajax.post({
                    'url':'/cms/category_modify',
                    'data':{'id':id,'name':inputValue},
                    'success':function(result){
                        if (result['code'] === 200){
                            window.location.reload();
                        }else{
                            alertBox.close();
                            messageBox.showError(result['message'])
                        }
                    }
                })
            }
        })
        
    })
};

CMS.prototype.Run = function(){
    this.listenCategoryModify();
    this.listenCategoryDeleted();
    this.listenThumbnailUploadEvent();
    this.listenCancelsubscription();
};

$(function(){
    var cms = new CMS();
    cms.Run();
    CMS.progressGroup = $('#progress-group');
});