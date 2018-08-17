#!/usr/bin/python
#coding:UTF-8

'''
please install requests before run this script
like:
    sudo pip requests install
'''

import requests
import time
import ast
from file_read import convert_read_file 

def send_request(requestDatas, send_code_url = 'https://coin.jd.com/sms/sendCode.html', charge_url = 'https://coin.jd.com/card/charge.html', check_code_url='https://coin.jd.com/card/checkCode.html'):
    print '=========start ============== requestData --> ', requestDatas
    requestHeaders = {'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Host':'coin.jd.com',
    'Origin':'https://coin.jd.com',
    'Referer':'https://coin.jd.com/',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    #add cookie first
    'Cookie':''
    }

    #模拟http请求 /card/charge.html

    for requestData in requestDatas:
        
        
        print '===json request == ',requestData['cipher_no']

        #response = requests.post(charge_url, data=requestData, verify=False, headers= requestHeaders)
        #print response.text
        
        
        response = requests.post(send_code_url, data=requestData, verify=False, headers= requestHeaders)
        print response.text
        temp_json = response.text
        requestData['smsyzm']=temp_json[39:45]
        print '=== request =========',requestData
        response = requests.post(check_code_url, data=requestData, verify=False, headers= requestHeaders)
        print response.text
        
        time.sleep(2)
        
if __name__ == '__main__':
    print send_request(convert_read_file(path='/home/facheng/backup/test.txt'))
    print "===========end============="    


