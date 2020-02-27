function News(){
    this.commentImmediately = $('#submit-immediately');
    this.loadMorBtnMS = $('#load-more-btn');


}


News.prototype.listencommentImmediately = function(){
    var self = this;
    self.commentImmediately.click(function(event){
        event.preventDefault();
        var pk =self.commentImmediately.parent().attr('data-news-id');
        var author =self.commentImmediately.parent().attr('data-news-author');
        var text = self.commentImmediately.parent().parent().find('textarea[name="comment"]');
        var comment = text.val();
        var commentUlList = $('.comment-list');
        console.log('pk',pk);
        console.log('author',author);
        console.log('text_value',comment);
        yourajax.post({
            'url':'/news/news_comment',
            'data':{'news':pk,'author':author,'comment':comment},
            'success':function(result){
                if (result['code'] === 200){
                    console.log(result['data']);
                    var comments = result['data'];
                    window.messageBox.show('success');
                    var temp = template('comment-template',{'comments':comments});
                    commentUlList.prepend(temp);
                }
            }
        })
    })
};



News.prototype.getTimeEvent = function(){
    template.defaults.imports.time_since = function(dateValue){
        var dateSource = new Date(dateValue);
        var dateTimestamp = dateSource.getTime();
        var time = (new Date().getTime());

        var date = (time - dateTimestamp) / 1000;
        console.log('date',date);
        if (date <= 60){
            return '刚刚'
        }else if(date > 60 && date <= 60*60){
            minutes = parseInt( date/60);
            return minutes + '分钟前'
        }else if(date > 60*60 && date <= 60*60*24){
            hours = parseInt(date/60/60);
            return hours + '小时前'
        }else if(date > 60*60*24 && date <= 60*60*24*30){
            days = parseInt(date/60/60/24);
            return days + '天前'
        }else{
            year = dateSource.getFullYear();
            month = dateSource.getMonth();
            day = dateSource.getDay();
            hour = dateSource.getHours();
            minute = dateSource.getMinutes();
            wholeDate = (year + '/' + month + '/' + day + '/' + ' ' + hour + '时' + minute + '分');
            return wholeDate
        }
    }
};


News.prototype.listenMoreNewsBtnMs = function(){
    var self = this;
    var pages = 1;

    console.log('跑过来');
    self.loadMorBtnMS.click(function(event){
        event.preventDefault();
        yourajax.get({
            'url':'/news/news_list',
            'data':{'p':pages},
            'success':function(result){
                if (result['code'] === 200){
                    console.log('data.message',result.data.news);
                    console.log('data.message',result.data.news);
                    var datas = result['data']['news'];
                    var temp = template('template_each',{'newses':datas});
                    //listUrls要放在ajax中获取才有效
                    var listUrls = $('.list-inner-group');
                    listUrls.append(temp);
                    pages += 1;
                }
            }
        })
    })
};



News.prototype.Run = function(){
    this.getTimeEvent();
    this.listencommentImmediately();
    this.listenMoreNewsBtnMs();
};


$(function(){
    var news = new News();
    news.Run();
});