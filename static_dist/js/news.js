function News(){

    this.thumbnail = $('#thumbnail-btn');
    console.log('test News成功')

}




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
};




$(function(){
    var news = new News();
    news.Run();
});