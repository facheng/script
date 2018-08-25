// Copyright 2018 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

'use strict';

$.extend({
    syncPost: function(request_url, request_data, callback) {
        $.ajax({
            type: 'POST',
            url: request_url,
            data: request_data,
            async: false,
            success: function(response) {
                callback(response)
            }
        })
    }
});

$.extend({
    myPost: function(request_data, request_sms, callback) {
        if (request_sms) {
            $.syncPost('https://coin.jd.com/sms/sendCode.html', request_data, function(data) {
                if (data.smsyzm == null) {
                    callback(data.msg)
                    return;
                }
                request_data.mobileNum = $('#phone').val()
                request_data.smsyzm = data.smsyzm
                $.syncPost('https://coin.jd.com/card/checkCode.html', request_data, function(data) {
                    callback(data.resultMessage)
                })
            })
        } else {
            $.syncPost('https://coin.jd.com/card/confirmCharge.html', request_data, function(data) {
                callback(data.resultMessage)
            })
        }

    }
});

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
        var tempCipherNos = cipher_nos
        var index = 0;
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

            $.myPost({ cipher_no: cipherNo }, requestSms, function(msg) {
                $('#result_' + index).html(msg)
            })

            index++
            if (tempCipherNos.length == index) {
                clearInterval(pid)
                $('#start').removeAttr('disabled')
            }

        }, 2500)

    })

    $('#reset').click(function() {
        $('#jd_coin_info').html('')
        cipher_nos = []
        $('#file').val('')
    })

    $('#file').click(function() {
        $('#jd_coin_info').html('')
        cipher_nos = []
        $('#file').val('')
    })

    $('#file').change(function() {
        $('#jd_coin_info').html('')
        cipher_nos = []

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

                jd_coin_result += ("<tr><td id = 'no'>" + (i + 1) + "</td><td id = 'coin'>" + n + "</td><td id='result_" + i + "'></td></tr>");
                cipher_nos.push(n)
            });
        }

        reader.onloadend = function(e) {
            $('#jd_coin_info').html(jd_coin_result)
        }

    })

    $(":radio").click(function() {
        if ($('input:checked').val() == 'true') {
            $('#phone_line').show()
        } else {
            $('#phone_line').hide()
        }
    });

})