// response callback
function success(text) {
    var status_text = '🐍 success!';
    console.log(status_text);
    var textarea = document.getElementById('test-response-text');
    textarea.value = text;
    document.getElementById('api-response-status').innerHTML = status_text;
}

function fail(code) {
    var status_text = "🍷 failed!";
    console.log(status_text);
    var textarea = document.getElementById('test-response-text');
    textarea.value = 'Error code: ' + code;
    document.getElementById('api-response-status').innerHTML = status_text;
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
        var textarea = document.getElementById('test-response-text');
        textarea.value = 'Something..'
    }
}

document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("api-window-url").textContent = window.location.href;
})

// 发送请求:
function sender() {
    var api_path = document.getElementById("test-api-path").value;
    request.open('GET', api_path);
    request.send();
    console.log("API requested, PATH: ", api_path)
    // alert('请求已发送，请等待响应...');
}

