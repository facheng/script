#!/usr/bin/python
# coding:UTF-8

import requests
import time
import random
import datetime

# 获取优惠券列表信息https://a.jd.com/indexAjax/getCouponListByCatalogId.html?callback=jQuery4342914&catalogId=19&page=1&pageSize=9&_=1534521129630
# 优惠券需要从列表信息中获取rule key,然后发送下列请求即可


def get_request_header(cookie):
    requestHeaders = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                      'Accept': 'application/json, text/javascript, */*; q=0.01',
                      'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
                      'Referer': 'https://a.jd.com/?cateId=19',
                      'Host': 'a.jd.com',
                    #   'Host':'coupon.jd.com',
                      'X-Requested-With': 'XMLHttpRequest',
                      # add cookie first
                      'Cookie': cookie
                      }
    return requestHeaders


def ticket_rob(target_timer, cookies, rule_key, get_coupon_url='https://a.jd.com/indexAjax/getCoupon.html', get_cate_url='https://a.jd.com/indexAjax/getCouponListByCatalogId.html?callback=jQuery4342914&catalogId=19&page=1&pageSize=9&_=1534521129630', triggerNow = False):
    send_code_url = get_coupon_url+'?callback=jQuery1355969&key=' + rule_key + '&type=1&_=1534554679960'

    ##双11抢劵
    # send_code_url = "https://coupon.jd.com/ilink/couponSendFront/send_index.action?key=297e27e0b46c4af69b2abe915a9ddf27&roleId=15012289&to=www.jd.com&"

    if triggerNow:
        print '发送请求'
        for cookie in cookies:
            requestHeaders = get_request_header(cookie)
            response = requests.get(
                send_code_url, headers=requestHeaders, allow_redirects=False)
            print response.text
    else:
        now_timer = datetime.datetime.now()
        print now_timer

        sched_timer = target_timer + datetime.timedelta(seconds = -1)

        difference = time.mktime(sched_timer.timetuple()) - time.mktime(now_timer.timetuple())
        print 'now timer ',now_timer,' sched timer ',sched_timer,'还差 ',difference,'秒开始'
        time.sleep(difference)
        print '当前时间 ', datetime.datetime.now()
        now_timer = datetime.datetime.now()

        while now_timer < target_timer:
            print '不相等，继续轮询,now ->', now_timer, ' target ->', target_timer
            now_timer = datetime.datetime.now()
        else:
            print '发送请求'
            for cookie in cookies:
                requestHeaders = get_request_header(cookie)
                response = requests.get(
                    send_code_url, headers=requestHeaders, allow_redirects=False)
                print response.text


if __name__ == '__main__':
    
    cookies = [] 
    first_cookie = ''
    sec_cookie = ''
    cookies.append(first_cookie)
    
    # cookies.append(sec_cookie)
    # 通过getCouponListByCatalogId获得
    rule_key = 'eab4cea21752a961c8544153472518cf27d683d05cd69585b808bb951b0a724141fdd99132936d48f8aead96a1880a5a'

    #150 c04ea570d27dc25e7cfbc00757ba205209b5ac63df4c8170283d6b941bde7bfa649492b57fcc20b371abef1145eb2205
    #100 3d0b0737f9ef5199730417a69e8ab16c842d53a1e4ef10962242ffd337450a3fbcc799beaf4a7ed051b1e9ca7cf786a6
    target_timer_arg = datetime.datetime(2018, 11, 6, 21, 15, 00, 000200)
    ticket_rob(target_timer = target_timer_arg, cookies = cookies, rule_key = rule_key,triggerNow = True)
