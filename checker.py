#!/usr/bin/python

import urllib2, urllib, sys, time, socks, socket

BLACK = '\033[30m'
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
ORANGE_BG = '\033[43m'
END = '\033[0m'

sites = ['https://vk.com', 'https://ya.ru', 'https://facebook.com', 'https://instagram.com', 'https://youtube.com', 'https://google.com']
#sites = ['https://vk.com', 'https://instagram.com', 'https://facebook.com', 'https://mail.ru']
sites = ['https://vk.com']
sites = ['https://avito.ru']
sites = ['https://ya.ru']

f = open(sys.argv[2], 'r')
c = 1
for l in f:
  print (3 - len(str(c)))*' ' + str(c) + ' ',
  c = c + 1
  a = l.split(':')
  print a[0] + ':' + a[1],
  print (26 - len(str(c) + (4 - len(str(c)))*' ' + a[0] + ':' + a[1]))*' ',
  for site in sites:
    proto = site.split('://')
    if sys.argv[1] == "--http":
      proxy_support = urllib2.ProxyHandler({proto[0] : "http://" + a[2] + ":" + a[3].rstrip() + "@" + a[0] + ":" + a[1]})
      opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
    elif  sys.argv[1] == "--socks":
      socks.set_default_proxy(socks.SOCKS5, a[0], int(a[1]), True, a[2], a[3].rstrip())
      socket.socket = socks.socksocket
      opener = urllib2.build_opener(urllib2.HTTPHandler)
    else:
      break
    request = urllib2.Request(site, None, {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; ru; rv:1.8.1.8) Gecko/20071008 Firefox/2.0.0.8"})
    try:
      start = time.time() * 1000
      handle = opener.open(request, timeout=5)
      end = time.time() * 1000
    except urllib2.HTTPError as e:
      print proto[1] + ' (' + YELLOW + str(e.code) + END + ')',
    except Exception, detail:
      print proto[1] + ' (  ' + RED + 'ERROR' + END + '  ) ',
    else:
      if handle.code == 200:
	print proto[1] + ' ( ' + GREEN + 'OK' + END + ' ' + YELLOW + str(int((end - start))) + END + ' '*(4-len(str(int((end - start))))) + ' ) ',
      else:
        print proto[1] + ' (' + GREEN + str(handle.code) + END + ')',
  print ''
f.close()

