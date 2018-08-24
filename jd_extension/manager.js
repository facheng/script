// Copyright 2018 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

'use strict';
$(function() {
    var cipher_no = []
    $('#start').click(function() {
        console.info(cipher_no)
    })
    $('#file').change(function() {
        var fileInput = $('#file')
        if (!fileInput.val()) {
            alert('没有选择文件！')
            return;
        }

        var file = document.getElementById("file").files[0];
        var reader = new FileReader();
        reader.readAsText(file, "gb2312");
        var jd_coin_result = ''
        reader.onload = function(e) {
            var fileText = e.target.result.split("\n");
            $.each(fileText, function(i, n) {
                if (n == '') {
                    return;
                }

                jd_coin_result += ("<tr><td id = 'coin'>" + n + "</td><td id='result_" + i + "'></td></tr>");
                console.log(n);
                cipher_no.push(n)
                $('#jd_coin_info').html(jd_coin_result)
            });
        }

    })

});