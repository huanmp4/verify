function Party() {
    this.call_me_in = $('.call-me-in');
    this.mask_wrapper2 = $('.mask-wrapper2');
    this.sunmit_party = $('#submit-party');
    this.deleteName = $('.delete-partyname');
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
        yourajax.get({
            'url':'/party/delete',
            'data':{'id':id},
            'success':function(result){
                if (result['code'] === 200){
                    window.location.reload()
                }
            }
        })
    })
};

Party.prototype.Run = function(){
    this.showCallmein();
    this.SubmitParty();
    this.deleteNameEvent();
};

$(function(){
    var party = new Party();
    party.Run()
});