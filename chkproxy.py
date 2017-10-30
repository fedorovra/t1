#!/usr/bin/python

import urllib2, urllib, sys, time, socks, socket

BLACK = '\033[30m'
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
ORANGE_BG = '\033[43m'
END = '\033[0m'

del sys.argv[0]
_param_prev = 0
for _param in sys.argv:
  if _param == "--http" or _param == "-h" or _param == "--socks" or _param == "-s":
    _proto = _param
  elif _param == "--file" or _param == "-f":
    _param_prev = _param
  else:
    if _param_prev == "--file" or _param_prev == "-f":
      _file_path = _param
    else:
      print "Bad parameter"
      sys.exit()
  _param_prev = _param

_file = open(_file_path, 'r')
_sites = ['https://vk.com', 
          'https://ya.ru', 
          'https://facebook.com', 
          'https://instagram.com', 
          'https://youtube.com', 
          'https://google.com']
_sites = ['https://ya.ru']
#_sites = ['https://vk.com']
_counter = 1

for _line in _file:
  print (3 - len(str(_counter)))*' ' + str(_counter) + ' ',
  _counter += 1

  _proxy_ip = _line.split(":")[0]
  _proxy_port = _line.split(":")[1]
  _proxy_login = _line.split(":")[2]
  _proxy_passw = _line.split(":")[3].rstrip()
  
  print _proxy_ip + ':' + _proxy_port,
  print (26 - len(str(_counter) + (4 - len(str(_counter)))*' ' + _proxy_ip + ':' + _proxy_port))*' ',
  
  for _site in _sites:
    
    if _proto == "--http" or _proto == "-h":
      _proxy_support = urllib2.ProxyHandler({_site.split('://')[0] : "http://" + _proxy_login + ":" + _proxy_passw + "@" + _proxy_ip + ":" + _proxy_port})
      _opener = urllib2.build_opener(_proxy_support, urllib2.HTTPHandler)
    elif _proto == "--socks" or _proto == "-s":
      socks.set_default_proxy(socks.SOCKS5, _proxy_ip, int(_proxy_port), True, _proxy_login, _proxy_passw)
      socket.socket = socks.socksocket
      _opener = urllib2.build_opener(urllib2.HTTPHandler)
    else:
      break
      
    _request = urllib2.Request(_site, None, {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; ru; rv:1.8.1.8) Gecko/20071008 Firefox/2.0.0.8"})
    try:
      _start = time.time() * 1000
      _handle = _opener.open(_request, timeout=2)
      _end = time.time() * 1000
    except urllib2.HTTPError as e:
      print _site.split('://')[1] + ' (' + YELLOW + str(e.code) + END + ')',
    except Exception, detail:
      print _site.split('://')[1] + ' (  ' + RED + 'ERROR' + END + '  ) ',
    else:
      if _handle.code == 200:
        print _site.split('://')[1] + ' ( ' + GREEN + 'OK' + END + ' ' + YELLOW + str(int((_end - _start))) + END + ' '*(4-len(str(int((_end - _start))))) + ' ) ',
      else:
        print _site.split('://')[1] + ' (' + GREEN + str(_handle.code) + END + ')',
  print ''
_file.close()
