function Party() {
    this.call_me_in = $('.call-me-in');
    this.mask_wrapper2 = $('.mask-wrapper2');
    this.mask_wrapper3 = $('.mask-wrapper3');
    this.sunmit_party = $('#submit-party');
    this.deleteName = $('.delete-partyname');
    this.editName = $('.edit-partyname');
    this.submitedit = $('#submit-party-edit');
}


Party.prototype.showCallmein = function(){
    var self = this;
    self.call_me_in.click(function(){
        self.mask_wrapper2.show();
    })
};

Party.prototype.SubmitParty = function(){
    var self = this;
    self.sunmit_party.click(function(){
        var memos = $('.party-memo');
        var name = memos.find('input[name="name"]').val();
        var cellphone = memos.find('input[name="cellphone"]').val();
        var memo = memos.find('input[name="memo"]').val();
        console.log('name',name);
        console.log('cellphone',cellphone);
        yourajax.get({
            'url':'/party/write',
            'data':{'name':name,'cellphone':cellphone,'memo':memo},
            'success':function(result){
                console.log('result',result);
                if (result['code'] === 200){
                    messageBox.showSuccess('ok');
                    window.location.reload()
                }
                if (result['code'] === 400){
                    console.log('已存在姓名');
                    messageBox.showError('姓名已存在')
                }
            }
        })
    })
};

Party.prototype.deleteNameEvent = function(){
    var self = this;
    self.deleteName.click(function(event){
        event.preventDefault();
        var parent = $(this);
        var id = parent.parent().parent().attr('data-id');
        console.log('id',id);
        alertBox.alertConfirm({'title':'确定删除吗','confirmCallback':function(){
                yourajax.get({
                    'url':'/party/delete',
                    'data':{'id':id},
                    'success':function(result){
                        if (result['code'] === 200){
                            window.location.reload()
                        }
                    }
                })
            }
        })
    })
};

Party.prototype.editEvent = function(){
    var self = this;
    self.editName.click(function(event){
        event.preventDefault();
        var parent = $(this);
        self.mask_wrapper3.show();
        var id = parent.parent().parent().attr('data-id');
        var memos = $('.party-memo');
        var name_v = memos.find('input[name="name"]');
        var cellphone_v = memos.find('input[name="cellphone"]');
        var memo_v = memos.find('input[name="memo"]');
        var money_v = memos.find('input[name="money"]');
        yourajax.get({
            'url':'/party/edit',
            'data':{'id':id},
            'success':function(result){
                if (result['code'] === 200){
                    var data = result['data']['party'];
                    console.log('data',data);
                    var cellphone = data.cellphone;
                    var name = data.name;
                    console.log('name',name);
                    console.log('name',data['name']);
                    var memo = data.memo;
                    var money = data.money;
                    name_v.val(name);
                    cellphone_v.val(cellphone);
                    memo_v.val(memo);
                    money_v.val(money);
                }
            }
        });
        self.submitedit.click(function(){
            console.log('post','id',id);
            var memos_b = $(this).parent().parent();
            var name_b = memos_b.find('input[name="name"]');
            var cellphone_b = memos_b.find('input[name="cellphone"]');
            var memo_b = memos_b.find('input[name="memo"]');
            var money_b = memos_b.find('input[name="money"]');
            yourajax.post({
                'url':'/party/edit',
                'data':{'id':id,'name':name_b.val(),'cellphone':cellphone_b.val(),'memo':memo_b.val(),'money':money_b.val()},
                'success':function(result){
                    if (result['code'] === 200){
                        alertBox.alertSuccess('OK',function(){
                            window.location.reload();
                        })
                    }
                }
            })
        })
    })
};


Party.prototype.editEventSubmit = function() {
    var self = this;
    self.submitedit.click(function(){

    })

};

Party.prototype.Run = function(){
    this.showCallmein();
    this.SubmitParty();
    this.deleteNameEvent();
    this.editEvent();
    this.editEventSubmit();
};

$(function(){
    var party = new Party();
    party.Run()
});