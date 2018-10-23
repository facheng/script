// Copyright 2018 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

'use strict';

$.extend({
    syncPost: function(request_url, request_data, callback, errorCallback) {
        $.ajax({
            type: 'POST',
            url: request_url,
            data: request_data,
            async: false,
            success: function(response) {
                callback(response)
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
                errorCallback();
            }
        })
    },
    jdCoinPost: function(request_data, request_sms, callback, errorCallback) {
        if (request_sms) {
            $.syncPost('https://coin.jd.com/sms/sendCode.html', request_data, function(data) {
                if (data.smsyzm == null) {
                    callback(data)
                    return;
                }
                request_data.mobileNum = $('#phone').val()
                request_data.smsyzm = data.smsyzm
                $.syncPost('https://coin.jd.com/card/checkCode.html', request_data, function(data) {
                    callback(data)
                }, errorCallback)
            }, errorCallback)
        } else {
            $.syncPost('https://coin.jd.com/card/charge.html', request_data, function(data) {
                callback(data)
            }, errorCallback)
        }

    }
});

var index = 0;
var clockPid
$(function() {
    $('#phone_line').hide()
    var cipher_nos = []
    $('#start').click(function() {
        if (cipher_nos.length == 0) {
            alert('请先选择钢镚!')
            return;
        }

        if ($('input:checked').val() == 'true' && $('#phone').val() == '') {
            alert('请填写手机号!')
            return;
        }

        $.each(cipher_nos, function(index, item) {
            $('#result_' + index).html('<span style="color:red;">请稍后。。。。。。</span>')
        })

        $('#start').attr('disabled', 'disabled')
        $('#reset').removeAttr('disabled')
        clockPid = triggerRequest(cipher_nos);

    })

    $('#reset').click(function() {
        var currentStatus = $('#reset').val()
        if (currentStatus == 'stop') {
            stopRequest(clockPid)
        } else {
            continueRequest(cipher_nos)
        }


    })

    $('#file').click(function() {
        $('#jd_coin_info').html('')
        cipher_nos = []
        $('#file').val('')
    })

    $('#file').change(function() {
        $('#jd_coin_info').html('')
        cipher_nos = []
        index = 0

        var fileInput = $('#file')
        if (!fileInput.val()) {
            alert('没有选择文件！')
            return;
        }

        var file = document.getElementById("file").files[0];
        var reader = new FileReader();
        reader.readAsText(file);
        var jd_coin_result = ''
        reader.onload = function(e) {
            var fileText = e.target.result.split("\n");
            $.each(fileText, function(i, n) {
                if (n == '') {
                    return;
                }

                jd_coin_result += ("<tr id='convert_info_" + i + "'><td>" + (i + 1) + "</td><td>" + n + "</td><td id='result_" + i + "'></td><td id='convert_time_" + i + "'></td></tr>");
                cipher_nos.push(n)
            });
        }

        reader.onloadend = function(e) {
            $('#jd_coin_info').html(jd_coin_result)
        }

        $('#start').removeAttr('disabled')
        $('#reset').val('stop').html('停止').attr('disabled', 'disabled')

    })

    $(":radio").click(function() {
        if ($('input:checked').val() == 'true') {
            $('#phone_line').show()
        } else {
            $('#phone_line').hide()
        }
    });
})

function stopRequest(clockPid) {
    $('#reset').text('继续')
    $('#reset').val('goon')
    clearInterval(clockPid)
}

function continueRequest(tempCipherNos) {
    $('#reset').text('停止')
    $('#reset').val('stop')
    clockPid = triggerRequest(tempCipherNos);
}

function triggerRequest(tempCipherNos) {
    var matcher = $('#matcher').val()
    var requestSms = $('input:checked').val() == 'true' ? true : false
    var pid = setInterval(() => {
        var tempCipherNo = tempCipherNos[index]
        var cipherNo
        if (matcher != null && matcher != undefined && matcher != '') {
            cipherNo = tempCipherNo.substr(tempCipherNo.lastIndexOf(matcher, tempCipherNo.length) + matcher.length, tempCipherNo.length)
        } else {
            cipherNo = tempCipherNo
        }

        send(requestSms, cipherNo);
        $('#convert_time_' + index).text(dateFormatter(new Date()));

        index++
        if (tempCipherNos.length == index) {
            clearInterval(clockPid)
            $('#start').removeAttr('disabled')
            index = 0
            $('#reset').val('stop').html('停止').attr('disabled', 'disabled')
        }

    }, 3000)
    return pid;
}

function send(requestSms, cipherNo) {
    $.jdCoinPost({ cipher_no: cipherNo, bindSource: '1' }, requestSms, function(data) {

        if (data.success === undefined) {
            stopRequest(clockPid);
            alert('请求失败，请检查京东登录状态！');
            $('#result_' + index).html("请求失败，请检查京东登录信息！<a href ='http://www.jd.com'　target='_blank'>京东登录</a>").attr('bgcolor', '#ff0011');
            return;
        }

        if (data.success) {
            $('#result_' + index).html(data.resultMessage)
        } else {
            $('#result_' + index).html(data.resultMessage).attr('bgcolor', '#ff0011');
            $('#convert_info_' + index).attr('bgcolor', '#ff0011');

        }
    }, function() {
        stopRequest(clockPid);
        alert('请求失败，请检查京东登录状态！');
        $('#result_' + index).html("请求失败，请检查京东登录信息！<a href ='http://www.jd.com'　target='_blank'>京东登录</a>").attr('bgcolor', '#ff0011');
    })
}

function dateFormatter(date) {
    var year = date.getFullYear();
    var month = change(date.getMonth() + 1);
    var day = change(date.getDate());
    var hour = change(date.getHours());
    var minute = change(date.getMinutes());
    var second = change(date.getSeconds());
    return year + '-' + month + '-' + day + ' ' + hour + ':' + minute + ':' + second;
}


function change(t) {
    if (t < 10) {
        return "0" + t;
    } else {
        return t;
    }
}