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
                      'X-Requested-With': 'XMLHttpRequest',
                      # add cookie first
                      'Cookie': cookie
                      }
    return requestHeaders


def ticket_rob(cookie, rule_key, get_coupon_url='https://a.jd.com/indexAjax/getCoupon.html', get_cate_url='https://a.jd.com/indexAjax/getCouponListByCatalogId.html?callback=jQuery4342914&catalogId=19&page=1&pageSize=9&_=1534521129630'):
    requestHeaders = get_request_header(cookie)
    send_code_url = get_coupon_url+'?callback=jQuery1355969&key=' + rule_key + '&type=1&_=1534554679960'

    target_symbol = '"success":true'
    success_result = -1

    now_timer = datetime.datetime.now()
    print now_timer
    sched_timer = datetime.datetime(2018, 8, 19, 22, 00, 00, 000100)

    while now_timer < sched_timer:
        print '不相等，继续轮询,now ->', now_timer, ' target ->', sched_timer
        now_timer = datetime.datetime.now()
    else:
        print '发送请求'
        response = requests.get(
            send_code_url, headers=requestHeaders, allow_redirects=False)
        print response.text


if __name__ == '__main__':
    cookie = ''
    # 通过getCouponListByCatalogId获得
    rule_key = 'dd5991b1d0c347f009366643800fb3873c65ca1b8e5dc241b942e49d3eeccd7a6199d8d64d121a921cc53bbd6d535cf2'
    ticket_rob(cookie, rule_key = rule_key)
