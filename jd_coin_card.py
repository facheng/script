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
    cookie = '__jdu=15084283349251591759680; __utmz=122270672.1530843446.1.1.utmcsr=trade.jd.com|utmccn=(referral)|utmcmd=referral|utmcct=/shopping/order/getOrderInfo.action; shshshfpa=f6e73d54-e616-8d34-03d6-7ea58ec56a89-1532744301; shshshfpb=07a4a67cff5ff63c1d7c3a72f160d4d38bfa9b21083448efc5ab2678f4; user-key=5a4a4e92-495d-4bac-9cc1-23da5097a54b; areaId=27; ipLoc-djd=27-2376-51881-0.546866999; ipLocation=%u9655%u897f; unpl=V2_ZzNtbUtXEEB3C0AALhAPUWILEwgSAEcWJg5GV3oQDlVuARRYclRCFXwUR11nGVsUZAMZXUVcQRdFCHZXchBYAWcCGllyBBNNIEwHDCRSBUE3XHxcFVUWF3RaTwEoSVoAYwtBDkZUFBYhW0IAKElVVTUFR21yVEMldQl2VH8YVQBkChBfR19AEXUMTlR9HVQCbgIibUVncyVwD0Zcfh9sBFcCIh8WC0cQdQ5FXTYZWARuBhFUQFVGHXYMRlBzGVoBbwQbXHJWcxY%3d; PCSYCityID=2; __jdv=122270672|direct|-|none|-|1534554762885; cn=20; pinId=Y5tlS1V9_CV9ao2-6idyxw; pin=Fcwang123; unick=ABCWang123; _tp=M3iNb1bItY7mplBeffgbjQ%3D%3D; _pst=Fcwang123; __jdc=122270672; TrackID=1K1Av4iFfjIGzE4dzt-nai_g6qeSyVPBRozqs6ggLWcwReXFakXZWWSuuzJUAn3do9lMKF-R8tgpv-FI6stJvy5gLV2_Y0nf8A2ndOaBB9oMP0B8ILhGvkg3REgFnYmj6; ceshi3.com=201; shshshfp=0a3a28bd7e8db0642394d594da321bd2; 3AB9D23F7A4B3C9B=RC5ZDSDG6STHB4C7DHATUKGGMW4JCX3RZY3QSUVYHR3YGEQJSRYQFILEFUMFXYVF7UMUSMWKOXBU6OUH6ZAVIEFMEI; JSESSIONID=559A541FC770697BABB1FCDC53FE7F45.s1; __jda=122270672.15084283349251591759680.1508428335.1534689394.1534746748.32; __jdb=122270672.1.15084283349251591759680|32.1534746748; thor=F6BD746C3FA1A9CC3E403B9A640BECB3403E00A25805FB079D891158F95FEB10012410CF8670B2B14F450134E3FFF105737E999A92241EA5E84745292A6A49460BCEF2D2CA3D675EABB957BE686A3F19AAC6708696E44DFCAB96C02CB8CEF925B2D86105FA4C74F6C19A0590CA40DDF3E65FB1A23F83B763C3397DF1355ADB8D9268A98DEA9A321E0D314E7D09AC4F26'
    start_char = '密钥'  # 正则表达式需要匹配的标识

    # path为钢镚密钥存放文件的路径，应与当前文件同一路径下
    payload = convert_read_file(path='text.txt', phone=phone, start_char=start_char)

    print "=========== start send request size ", len(payload), "==================="

    start_time = datetime.datetime.now()
    request = Request(payload=payload, cookie=cookie, request_sms=request_sms)
    send_request(request)

    print "============= end  send request size ", len(
        payload), "cost ", (datetime.datetime.now() - start_time).seconds, " seconds ==================="
