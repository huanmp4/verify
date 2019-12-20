function Category(){
    this.categoryDelete = $('.btn-delete');
    this. categoryModify = $('.btn-modify');
}


Category.prototype.listenCategoryDeleted = function(){
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


Category.prototype.listenCategoryModify = function(){
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

//文章添加
Category.prototype.listenCategoryAdd = function(){
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


Category.prototype.Run = function(){
    this.listenCategoryDeleted();
    this.listenCategoryModify();
    this.listenCategoryAdd();
};


$(function(){
    var category = new Category();
    category.Run()
});