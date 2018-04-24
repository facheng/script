#!/usr/bin/python
#coding:UTF-8

'''
please install requests before run this script
like:
    sudo Pip requests install
'''

import requests
import time
from file_read import convert_read_file 

def send_request(requestDatas, url = 'https://coin.jd.com/card/charge.html'):
    print '=========start ============== requestData --> ', requestDatas
    requestHeaders = {'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Host':'coin.jd.com',
    'Origin':'https://coin.jd.com',
    'Referer':'https://coin.jd.com/',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Cookie':'nu_UA-JR-YHST-GB_#banklist=A38F0C9A-B8A7-4A2C-96CB-FB8A1C21324C; sec_flag=4627232605490030e72547e8158f96eb; sec_addr=c0a803c4; user-key=5792bc0b-2f53-4cf3-8e4a-1c53775c26ad; nu_UA-JR-YHST-GB_#banklist?appinstall=0=17A872C6-26F4-46E1-A17A-9051238C3269; nu_UA-JR-YHST-GB_?from=singlemessage&isappinstalled=0#banklist?appinstall=0=AD2C3768-81A9-4059-830D-F566B248122C; PCSYCityID=2; cn=5; areaId=2; ipLoc-djd=2-2830-51800-0.601080205; ipLocation=%u4e0a%u6d77; mobilev=html5; mba_muid=14976028598102106973682; unpl=V2_ZzNtbRYAQkFxCBZXeElYUmJQRlkSA0NGfF8VAXIRDgEwBxpdclRCFXwUR1FnGlkUZwIZWEZcRxZFCHZXchBYAWcCGllyBBNNIEwHDCRSBUE3XHxcFVUWF3RaTwEoSVoAYwtBDkZUFBYhW0IAKElVVTUFR21yVEMldQl2VH4RWgJmABtZSl5DFHYIR1NzH14CbgAibUVncyVwDEVVehtsBFcCIh8WC0oTcQFOXTYZWQ1hBBNeS1NLHHUJRVR6HlQDZQQbXnJWcxY%3d; CCC_SE=ADC_0Q7gdjnKqtHc8LS4abgv4OhAejBYRfLHWD50ReydXad%2bG6pktS59wVLrhfd6rHkL4%2fHVT6U8Ed7MD%2fEODr7fjPuETmrSbMP6jN6C%2b6l3%2bfYviK7pH9BpZjmr1%2bodECu5wGISNF1P13d%2bjVvy5SbCEl%2bozDxr5COF6ZvrNtVQaIM3TPS3i1iMxAd8b10gb84EWyTSxobvJJXGNgWD0A7oIcg5ic3pdP3qPNS8dkafwEHLiM7CnyQIGuAUS7%2b09OfWgFFG9oOdS5PMGjd8Mtd8YBoc7ydz8Da7wdBZe7sKqah9e6efb8n8sE0Z0JIN6z4rFSMoTjGCbb50o4N%2b1CqOhkOF%2b3c8u%2blW3bhcRsOXQWujb9%2b7ElGcI8tIvNBa4%2bfl%2fwtllhrXOnMwZ5OfIY1S9VE48tygNAKQZDX3NdcTc5hORZ7lHbwOnbVNeaTYTre0UPqZaiRSzmLVc1I1kZRRR%2fuoSoXNyS0vx2RojWGHk37UoB0TNGnb%2fBOEowfa2tXiIm0abAg9YrI4lK3vSbPwNHKnYtjNoA3Ryfhb2Glb977J02TBNBvh96J03B0nd104q%2bsj8lWTrz9KQzgXFecgzEcNJb7wl3zP3aBfGWJGF2zY%2f0FgNLQJ0pLniLXoDRID; _jrda=16; wlfstk_smdl=vig3rikj330f09lms499aqljg65hv5kr; TrackID=11urjxNYedl8hwKaqEJ4wjYuMRaek7UmyJauh6D7J-RsI7N_ZhSf8oOWrDnOGIPu0serCUNhEAnGikgFsHUAeMYlEEK2GURbqXx8vsKA1ST0Um5j41xH799dg0EB-4o5V; pinId=AOWQA7bEiygQQKXsTz0Lt7V9-x-f3wj7; pin=jd_4fbb4d0a62d20; unick=jd_187219dfk; thor=310AB3624AAE7C114CD6938F5D57A0BE3EB8DE07F019A3F22AADF51A4E92A995A689B4824ED466F42592788D5D27AFC04534C5F2F331C132B4276BB124DEBDB1F2572BF80B553981DEDC6D44169EEC88A9961665404C6ECC5EBAC15A9DE17E1B963FED4DB4D4334EF043B3E417C39D8D3CE9534C6F6F930A85B4DC4316812A4AF4F698F14F2080913B4616D7C4F91BE753E0C14554785A010F1E62F7C12E94A6; _tp=PTliv%2BcvKZknaNcwR3Rv7qfCHDGn1XAtO2Pum9rnmiM%3D; _pst=jd_4fbb4d0a62d20; ceshi3.com=201; __jdv=122270672|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_ef0e51a22a5f4be5ae1b8fbd89c5f591|1524537967711; __jda=122270672.14976028598102106973682.1497602859.1524191468.1524537953.38; __jdb=122270672.5.14976028598102106973682|38.1524537953; __jdc=122270672; 3AB9D23F7A4B3C9B=5WNWQHCICJID5RWSQ3JHTBJUTDE7NXBIE2IMLPHASQ5FOBIVLIE6R7SD3JHG6YF5DGD4GCUQORFPI2CNLXKC5OIIFE; JSESSIONID=059C668C67C3B450BFB22CE1E2D400C9.s1; uv_UA-JR-YHST-GB_#banklist=64998550-A747-484A-92AF-AE90222B6379; nv_UA-JR-YHST-GB_#banklist=01C04BF5-3477-4AF3-9273-BCE2994FFD52; __jda=177095863.14976028598102106973682.1497602859.1524121241.1524123482.36; __jdb=177095863.6.14976028598102106973682|36.1524123482; __jdc=177095863; _jrdb=1524537980783; __jdu=14976028598102106973682'
    }
    
    #模拟http请求 /card/charge.html

    for requestData in requestDatas:
        response = requests.post(url, data=requestData, verify=False, headers= requestHeaders)
        print response.text
        time.sleep(2)

if __name__ == '__main__':
    print send_request(convert_read_file(path='/home/facheng/backup/test.txt'))
    print "===========end============="    


