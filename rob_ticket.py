#!/usr/bin/python
#coding:UTF-8

import requests
import time
import random

#获取优惠券列表信息https://a.jd.com/indexAjax/getCouponListByCatalogId.html?callback=jQuery4342914&catalogId=19&page=1&pageSize=9&_=1534521129630
#优惠券需要从列表信息中获取rule key,然后发送下列请求即可

def get_request_header(cookie):
    requestHeaders = {'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Referer':'https://a.jd.com/?cateId=16',
    'Host':'a.jd.com',
    'X-Requested-With':'XMLHttpRequest',
    #add cookie first
    'Cookie':cookie
    }
    return requestHeaders

def ticket_rob(get_coupon_url='https://a.jd.com/indexAjax/getCoupon.html', get_cate_url='https://a.jd.com/indexAjax/getCouponListByCatalogId.html?callback=jQuery4342914&catalogId=19&page=1&pageSize=9&_=1534521129630'):
    requestHeaders=get_request_header(cookie='')
    send_code_url =get_coupon_url+'?callback=jQuery702161&key=124a025297d236857b920e3e9cf74ecacacf0bd9781c4c9dec45480ad8e35f6e3ca93b4d768649c2d493709d29b3cbea&type=1&_=1534516979499'
    
    response = requests.get(send_code_url, headers=requestHeaders,allow_redirects=False)
    print response.text
    result_str =response.text
    target_symbol ='"success":true'
    success_result= result_str.find(target_symbol,0,len(result_str))
    # print result_str[result_str.find(target_symbol,0,len(result_str))+len(target_symbol):len(result_str)]

    while success_result==-1:
        response = requests.get(send_code_url, headers=requestHeaders,allow_redirects=False)
        print response.text
        time.sleep(random.randint(0,2))
    else:
        print '抢券成功！'
        


if __name__ == '__main__':
    ticket_rob()