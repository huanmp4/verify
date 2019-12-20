function CMSbanner(){
    this.addBannerBtnOption = $('#add-banner-btn-option');
    this.saveBtn = $('.btn-save-all-banner');
    this.column = $('.cloumn');

}


//后端获取banner图列表
CMSbanner.prototype.getBannerDate = function(){
    var self = this;
    yourajax.get({
        'url':'/cms/banner_cms_manager_get',
        'success':function(result){
            if (result['code'] === 200){
                var banners = result['data']['banners'];
                console.log('banners data',banners);
                console.log('banners.length;',banners.length);
                for(var i=0; i < banners.length;i++){
                    var banner = banners[i];
                    var banner_template = template('add-banner-template',{'banner':banner});
                    self.column.append(banner_template);
                    var bannerItems = self.column.find('.banner-items:last');
                    self.bannerAddClickEvent(bannerItems);
                    self.bannerSaveEvent(bannerItems);
                    self.closeItemsBtn(bannerItems);
                }
            }
        }
    })
};

//banner关闭按钮
CMSbanner.prototype.closeItemsBtn = function(bannerItems){
    var self = this;
    var closeBtn = bannerItems.find('.btn-tool-to-css');
    closeBtn.click(function(event){
        event.preventDefault();
        console.log('close');
        var banner_id = bannerItems.attr('data-banner-id');
        if (banner_id){
            console.log('有banner_id');
            alertBox.alertConfirm({
                'title':'确定永久删除这条轮播图吗',
                'confirmCallback':function(){
                    yourajax.post({
                        'url':'/cms/banner_cms_manager_delete',
                        'data':{'banner_id':banner_id},
                        'success':function(result){
                            if (result['code'] === 200){
                                bannerItems.remove();
                                window.messageBox.show('删除成功');
                            }else{
                                window.messageBox.showError('没有这条数据')
                            }
                        }
                    })
                }
            })
        }else{
            bannerItems.remove();
        }
    })
};


//banner图点击添加
CMSbanner.prototype.bannerAddClickEvent = function(bannerItems){
    var bannerClickA_input = bannerItems.find('#images-click-A');
    var bannerClickB = bannerItems.find('#images-click-B');
    bannerClickB.click(function(){
        bannerClickA_input.click()
    });
    bannerClickA_input.change(function(){
        var file = this.files[0];
        var formdata_new = new FormData();
        formdata_new.append('file',file);
        console.log('formdata_new.name',formdata_new.name);
        yourajax.post({
            'url':'/cms/image_upload_to_local',
            'data':formdata_new,
            'processData':false,
            'contentType':false,
            'success':function(result){
                if (result['code'] === 200){
                    var data_url = result['data']['url'];
                    var url_address = bannerItems.find('.url-address');
                    var url_jump = bannerItems.find('.url-jump');
                    url_address.val('');
                    url_address.val(data_url);
                    var image_banner_item = bannerClickB.children('.image-banner-temp');
                    image_banner_item.attr('src',data_url);
                }
            }
        })
    })
};

//待开发
CMSbanner.prototype.bannerFalseClickEvent = function(){
    this.saveBtn.click(function(){
        console.log('save btn');
    })
};

//保存
CMSbanner.prototype.bannerSaveEvent = function(bannerItems){
    var self = this;
    self.bannerSaveBtn = bannerItems.find('.btn-save-all-banner');

    self.bannerSaveBtn.click(function(event){
        event.preventDefault();
        var image_url = bannerItems.find('.image-banner-temp').attr('src');
        console.log('image_url',image_url);
        var link_to = bannerItems.find('.url-jump').val();
        console.log('link_to',link_to);
        var priority = bannerItems.find('.priority_by_banner').val();
        console.log('priority',priority);
        var banner_id = bannerItems.attr('data-banner-id');
        var priority_text = bannerItems.find('.text-blue');
        if(banner_id){
            url = '/cms/banner_cms_manager_edit'
        }else{
            url = '/cms/banner_cms_manager_add'
        }
        yourajax.post({
            'url':url,
            'data':{'image_url':image_url,'link_to':link_to,'priority':priority,'banner_id':banner_id},
            'success':function(result){
                if (result['code'] === 200){
                    if(banner_id){
                        console.log('bannerid if',banner_id);
                        window.messageBox.showSuccess('编辑成功');
                        priority_text.text('当前位置：'+priority);
                    }else{
                        banner_id = result['data']['banner_id'];
                        bannerItems.attr('data-banner-id',banner_id);
                        window.messageBox.showSuccess('保存成功');
                        priority_text.text('(数字越大越排前)当前优先级：'+priority);
                    }
                }
            }
        })
    })
};


//新增items按钮
CMSbanner.prototype.AddBannerOptionEvent = function(){
    var self = this;
    self.addBannerBtnOption.click(function(){
        var ul_length = self.column.children().length;
        if (ul_length < 6){
            var temp = template('add-banner-template');
            self.column.prepend(temp);
            var bannerItems = self.column.find('.banner-items:first');
            console.log('ul有：',+ ul_length +'记录');
            self.bannerAddClickEvent(bannerItems);
            self.bannerSaveEvent(bannerItems);
            self.closeItemsBtn(bannerItems);
        }
        else{
            window.messageBox.showError('不能超过6个banner')
        }
    })
};

CMSbanner.prototype.Run = function(){
    this.getBannerDate();
    this.AddBannerOptionEvent();

};

$(function(){
    var cmsbanner = new CMSbanner();
    cmsbanner.Run();
});