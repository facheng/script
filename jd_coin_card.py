#!/usr/bin/python
# coding:UTF-8

'''
please install requests before run this script
like:
    sudo pip requests install
'''

import requests
import time
import ast
from file_read import convert_read_file
import codecs
import datetime


def convert_read_file(path, phone, start_char):
    with open(path, 'r') as files:
        lines = files.readlines()
        result = []
        flag = start_char
        trip_ = '\n'
        for file in lines:
            file_str = file.strip(trip_)
            cipher = {'cipher_no': file_str[file_str.find(flag, 0, len(file_str))+len(flag):len(
                file_str)], 'bindSource': 1, 'smsyzm': '777777', 'mobileNum': phone, 'rnd': 0.8444005282553888}
            result.append(cipher)
        return result


def send_request(request_info):
    print '=========start ============== request payload --> ', request_info.payload
    requestHeaders = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                      'Accept': 'application/json, text/javascript, */*; q=0.01',
                      'Host': 'coin.jd.com',
                      'Origin': 'https://coin.jd.com',
                      'Referer': 'https://coin.jd.com/',
                      'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
                      # add cookie first
                      'Cookie': request_info.cookie
                      }

    # 模拟http请求 /card/charge.html

    require_sms = request_info.request_sms
    for requestData in request_info.payload:

        print '=== request data == ', requestData
        if not require_sms:
            response = requests.post(
                request_info.charge_url, data=requestData, verify=True, headers=requestHeaders)
            print response.text
        else:
            response = requests.post(
                request_info.send_code_url, data=requestData, verify=False, headers=requestHeaders)
            print response.text
            temp_json = response.text
            requestData['smsyzm'] = temp_json[39:45]
            response = requests.post(
                request_info.check_code_url, data=requestData, verify=False, headers=requestHeaders)
            print response.text

        time.sleep(2)


class Request:
    payload = []
    cookie = ''
    send_code_url = 'https://coin.jd.com/sms/sendCode.html'
    charge_url = 'https://coin.jd.com/card/charge.html'
    check_code_url = 'https://coin.jd.com/card/checkCode.html'
    request_sms = False

    def __init__(self, payload, cookie, request_sms):
        self.payload = payload
        self.cookie = cookie
        self.request_sms = request_sms


if __name__ == '__main__':
    phone = '18302155350'
    request_sms = False  # 标识是否需要短信验证码
    cookie = ''
    start_char = '密钥'  # 正则表达式需要匹配的标识

    # path为钢镚密钥存放文件的路径，应与当前文件同一路径下
    payload = convert_read_file(path='text.txt', phone=phone, start_char=start_char)

    print "=========== start send request size ", len(payload), "==================="

    start_time = datetime.datetime.now()
    request = Request(payload=payload, cookie=cookie, request_sms=request_sms)
    send_request(request)

    print "============= end  send request size ", len(
        payload), "cost ", (datetime.datetime.now() - start_time).seconds, " seconds ==================="
