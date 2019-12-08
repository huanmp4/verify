function News(){
    this.releaseNewsBtn = $('#release-news-button');
    this.thumbnail = $('#thumbnail-btn');
    console.log('test News成功')

}



News.prototype.listenReleaseBTN = function() {
    var self = this;
    self.releaseNewsBtn.click(function (event) {
        event.preventDefault();
        var name = $('#title-news').val();
        var category = $('#option-control').val();
        var content = $('#textarea-news').val();
        yourajax.post({
            'url': '/cms/release_news',
            'data': {'name': name, 'content': content},
            'success': function (result) {
                if (result['code'] === 200) {
                    window.alert('文章发表成功');
                    console.log('成功', result);
                }
                else {
                    console.log('result失败', result);
                    console.log('result失败', result['code']);
                }
            },
            'fail': function (error) {
                console.log('error失败', error)
            }
        })
    });
};


News.prototype.listTest = function(){
    console.log('test News成功')
};

//文章添加
News.prototype.listenCategoryAdd = function(){
    var addNewCategory = $('#add-new-category');
    var btnConfirm = $('#btn-confirm');
    var formCategory = $('.form-category');
    var inputCategory = $('#inputHelpBlock');
    addNewCategory.click(function(){
        var inputval = inputCategory.val();
        event.preventDefault();
        alertBox.alertOneInput({
            'title':'新增标签',
            'confirmCallback':function(inputValue){
                yourajax.post({
                    'url':'/cms/category',
                    'data':{'name':inputValue},
                    'success':function(result){
                        if (result.code === 200){
                            window.messageBox.show('添加分类成功');
                            window.location.reload();
                        }
                    }
                })
            }
        });
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