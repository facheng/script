#!/usr/bin/python
# coding:UTF-8

import requests
import time
import random
import datetime

# 获取优惠券列表信息https://a.jd.com/indexAjax/getCouponListByCatalogId.html?callback=jQuery4342914&catalogId=19&page=1&pageSize=9&_=1534521129630
# 优惠券需要从列表信息中获取rule key,然后发送下列请求即可


def get_request_header_common(cookie):
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

def get_request_header_11(cookie):
    requestHeaders = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                      'Accept': 'application/json, text/javascript, */*; q=0.01',
                      'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
                    #   'Host':'coupon.jd.com',
                      'X-Requested-With': 'XMLHttpRequest',
                      # add cookie first
                      'Cookie': cookie
                      }
    return requestHeaders

def get_request_header(cookie, is11rob):
    if is11rob:
        return get_request_header_11(cookie)
    else:
        return get_request_header_common(cookie)
    
def ticket_rob(url, target_timer, cookies, rule_key, get_coupon_url='https://a.jd.com/indexAjax/getCoupon.html', get_cate_url='https://a.jd.com/indexAjax/getCouponListByCatalogId.html?callback=jQuery4342914&catalogId=19&page=1&pageSize=9&_=1534521129630', triggerNow = False,is11rob = False):
    if triggerNow:
        print '发送请求'
        for cookie in cookies:
            requestHeaders = get_request_header(cookie, is11rob=is11rob)
            response = requests.get(
                url, headers=requestHeaders, allow_redirects=False)
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
                requestHeaders = get_request_header(cookie=cookie, is11rob=is11rob)
                response = requests.get(
                    url, headers=requestHeaders, allow_redirects=False)
                print response.text


if __name__ == '__main__':
    
    cookies = [] 
    first_cookie = ''
    sec_cookie = ''
    cookies.append(first_cookie)
    cookies.append(sec_cookie)
    
    # cookies.append(sec_cookie)
    # 通过getCouponListByCatalogId获得
    rule_key = '50dd4ddfd2d59bbbcd3a7f544aafb3636a11f0b49c95d69eff74e1fecae63464f0287689716a627c64e4470ab0835992'

    #150 c04ea570d27dc25e7cfbc00757ba205209b5ac63df4c8170283d6b941bde7bfa649492b57fcc20b371abef1145eb2205
    #100 3d0b0737f9ef5199730417a69e8ab16c842d53a1e4ef10962242ffd337450a3fbcc799beaf4a7ed051b1e9ca7cf786a6

    send_code_url = 'https://a.jd.com/indexAjax/getCoupon.html?callback=jQuery1355969&key=' + rule_key + '&type=1&_=1534554679960'

    ##双11抢劵
    #1111
    # send_code_url = "https://coupon.jd.com/ilink/couponSendFront/send_index.action?key=297e27e0b46c4af69b2abe915a9ddf27&roleId=15012289&to=www.jd.com&"

    #450
    send_code_url = "https://coupon.jd.com/ilink/couponSendFront/send_index.action?key=9bd4537e1ad544d59ad7b2a9292ba690&roleId=15557288&to=sale.jd.com/act/fpgmdSRPst.html&"

    #300
    # send_code_url = "https://coupon.jd.com/ilink/couponSendFront/send_index.action?key=297e27e0b46c4af69b2abe915a9ddf27&roleId=15012289&to=www.jd.com&"

    target_timer_arg = datetime.datetime(2018, 11, 9, 14, 00, 00, 000200)
    ticket_rob(is11rob = True, url = send_code_url, target_timer = target_timer_arg, cookies = cookies, rule_key = rule_key,triggerNow = True)
