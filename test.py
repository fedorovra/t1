#!/usr/bin/python

import requests

url = 'http://proxymania.ru/welcome/user_login_post'
head = { 'Host' : 'proxymania.ru',
         'Origin' : 'http://proxymania.ru',
         'Referer' : 'http : //proxymania.ru/ticketadmin/',
         'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36' }
payload = { 'xsrf' : 'fef5657aca3e6104c43cec63930afe53', 'login' : 'rayk', 'pass' : 'kgiFF89%9kf8jk' }
proxy = { 'http' : 'http://PWNrqIUDbc:Ub2RwXlknz@31.184.240.61:14050' }

session = requests.session()

d = session.post( url, proxies=proxy, headers=head, data=payload, auth=('rayk','kgiFF89%9kf8jk') )

print d.status_code

#print d.text
print "!!!"

HELLO!
