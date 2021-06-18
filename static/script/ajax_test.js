// rewrite textarea with response
function success(text) {
    console.log('🐍 success!')
    var textarea = document.getElementById('test-response-text');
    textarea.value = text;
}

function fail(code) {
    console.log("🍷 failed!")
    var textarea = document.getElementById('test-response-text');
    textarea.value = 'Error code: ' + code;
}


var request = new XMLHttpRequest(); // 新建XMLHttpRequest对象

request.onreadystatechange = function () { // 状态发生变化时，函数被回调
    if (request.readyState === 4) { // 成功完成
        // 判断响应结果:
        if (request.status === 200) {
            // 成功，通过responseText拿到响应的文本:
            return success(request.responseText);
        } else {
            // 失败，根据响应码判断失败原因:
            return fail(request.status);
        }
    } else {
        // HTTP请求还在继续...
        var textarea = document.getElementById('test-response-text')
        textarea.value = 'Something..'
    }
}

// 发送请求:
function sender() {
    request.open('GET', '/api/');
    request.send();
    alert('请求已发送，请等待响应...');
}

