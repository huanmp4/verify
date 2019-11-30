function News(){
    this.releaseNewsBtn = $('#release-news-button');
    this.thumbnail = $('#thumbnail-btn');
    this.thumbnailBtn = $('.form-group-append').find('label[class="btn-file"]');
}

News.prototype.listenReleaseBTN = function(){
    var self = this;
    self.releaseNewsBtn.click(function(event){
        event.preventDefault();
        var name = $('#title-news').val();
        var category = $('#option-control').val();
        var content = $('#textarea-news').val();
        console.log('name',name);
        console.log('name',name);
        console.log('name',name);s
        console.log('content',content);
        console.log('category',category);
        yourajax.post({
            'url':'/cms/release_news',
            'data':{'name':name,'content':content},
            'success':function(result){
                if (result['code'] === 200){
                    window.alert('文章发表成功');
                    console.log('成功',result);
                }
                else{
                    console.log('result失败',result);
                    console.log('result失败',result['code']);
                }
            },
            'fail':function(error){
                console.log('error失败',error)
            }
        })

    });
    self.thumbnail.change(function(){
        var file = self.thumbnail[0].files[0];
        var formdata = new FormData();
        formdata.append('file',file);
        console.log('file',formdata);
        yourajax.post({
            'url':'/cms/category_thumbnail',
            'data':formdata,
            'processData':false,
            'contentType':false,
            'success':function(result){
                if (result.code ===200){
                    window.messageBox.show('成功')
                }
                if (result.code ===400){
                    window.messageBox.show('失败')
                }
            }
        })
    })
};

News.prototype.listenCategoryAdd = function(){
    var addNewCategory = $('#add-new-category');
    var btnConfirm = $('#btn-confirm');
    var formCategory = $('.form-category');
    var inputCategory = $('#inputHelpBlock');
    addNewCategory.click(function(){
        formCategory.show()
    });
    btnConfirm.click(function(event){
        var inputval = inputCategory.val();
        console.log('inputval',inputval);
        event.preventDefault();
        yourajax.post({
            'url':'/cms/category',
            'data':{'name':inputval},
            'success':function(result){
                if (result.code === 200){
                    window.messageBox.show('添加分类成功');

                    window.location.reload();
                }
                else{
                    window.messageBox.showError('添加失败');
                    console.log(result)
                }
            },
            'fail':function(){
                window.messageBox.show('error')
            }
        })
    })
};


News.prototype.Run = function(){
    this.listenCategoryAdd();
    this.listenReleaseBTN();
};




$(function(){
    var news = new News();
    news.Run();
});