function CMS(){
    this. categoryModify = $('.btn-modify');
    this.categoryDelete = $('.btn-delete');
    this.thumbnail = $('#thumbnail-btn');

}
//
//     //后台文章图片上传
//     self.thumbnail.change(function(){
//         var file = self.thumbnail[0].files[0];
//         var formdata = new FormData();
//         var picture = $('#picture');
//         formdata.append('file',file);
//         console.log('file',formdata);
//         yourajax.post({
//             'url':'/cms/category_thumbnail',
//             'data':formdata,
//             'processData':false,
//             'contentType':false,
//             'success':function(result){
//                 if (result.code === 200){
//                     window.messageBox.show('成功');
//                     picture.val('上传成功')
//                 }
//                 if (result.code === 400){
//                     window.messageBox.show('失败')
//                 }
//             }
//         })
//     })
// };

CMS.prototype.listenThumbnailUploadEvent = function(){
    var self = this;
    self.thumbnail.change(function(){
        var file = this.files[0];
        var key = new Date().getTime()+'.'+file.name.split('.')[1];
        var putExtra = {
            fname:key,
            params:{},
            mimeType:['image/png','image/jpeg','image/gif','video/x-ms-wmv']
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
                    observable.subscribe({
                        'next':self.handleFileUploadProcess(),
                        'error':self.handleFileErrorProcess(),
                        'complete':self.handleFileComplete()
                    })
                }
            }
        })

    })
};


CMS.prototype.handleFileUploadProcess = function(response){
    var total = response.total();
    var percent = total.percent();
};

CMS.prototype.handleFileErrorProcess = function(error){
    console.log('error',error)
};

CMS.prototype.handleFileComplete = function(){
    console.log('完成')
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
};

$(function(){
    var cms = new CMS();
    cms.Run();
});