
  var customVarList = qiniu.filterParams(putExtra.params);

  for (var i = 0; i < customVarList.length; i++) {
    var k = customVarList[i];
    multipart_params_obj[k[0]] = k[1]
  }



var testalert2 = {'post':function(){
    console.log('成功test2222222222222222');
    qiniu.upload()
    }};