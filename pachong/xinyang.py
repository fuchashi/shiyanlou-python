#!/usr/bin/env python3.5
import requests

ssion=requests.session()
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'

referer='http://m.soyoung.com/passport/dologinnew'

headers={
        'User_Agent':user_agent,
        'Host':'m.soyoung.com',
        'Origin':'http://m.soyoung.com',
        'Referer':'http://m.soyoung.com',
        }


formatData={
        'username':'15976984640',
        'password':'tida2015',
        }

ssion.post(referer,data=formatData,headers=headers)

#print(requests.text)

import requests
strpub='http://www.soyoung.com/post/pub_reply?act=pub'
pubdata={
        'post_id':'15257230',
        'reply_content':'very good!!!!',
        }


headers={
        'User_Agent':user_agent,
        'Host':'www.soyoung.com',
        'Origin':'http://www.soyoung.com',
        'Referer':'http://www.soyoung.com/p151257230',
        'Pragma':'no-cache',
        }

requests=ssion.post(strpub,data=pubdata,headers=headers)

print(requests.text)
