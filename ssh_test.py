#!/usr/bin/python

import paramiko, sys, time
paramiko.util.log_to_file("/dev/null")

GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
END = '\033[0m'

ssh = ( { 'session' : 's1',  'server' : '94.242.54.121',   'color' : GREEN,  'id' : '33' },
        { 'session' : 's2',  'server' : '94.242.54.128',   'color' : YELLOW, 'id' : '34' },
        { 'session' : 's3',  'server' : '94.242.62.22',    'color' : GREEN,  'id' : '37' },
        { 'session' : 's4',  'server' : '45.33.87.204',    'color' : YELLOW, 'id' : '36' },
        { 'session' : 's5',  'server' : '194.63.143.144',  'color' : GREEN,  'id' : '4'  },
        { 'session' : 's6',  'server' : '217.106.239.118', 'color' : YELLOW, 'id' : '9'  },
        { 'session' : 's7',  'server' : '5.8.8.201',       'color' : GREEN,  'id' : '6'  },
        { 'session' : 's8',  'server' : '5.8.8.10',        'color' : YELLOW, 'id' : '15' },
        { 'session' : 's9',  'server' : '5.8.8.19',        'color' : GREEN,  'id' : '17' },
        { 'session' : 's10', 'server' : '109.248.250.127', 'color' : YELLOW, 'id' : '20' },
        { 'session' : 's11', 'server' : '93.170.131.243',  'color' : GREEN,  'id' : '21' }, 
        { 'session' : 's12', 'server' : '94.242.59.52',    'color' : YELLOW, 'id' : '5'  },
        { 'session' : 's13', 'server' : '94.242.57.185',   'color' : GREEN,  'id' : '6'  },
        { 'session' : 's14', 'server' : '217.29.53.110',   'color' : YELLOW, 'id' : '25' })

for key in ssh:
  key['session'] = paramiko.SSHClient()
  key['session'].set_missing_host_key_policy(paramiko.AutoAddPolicy())
  while True:
    try:
      key['session'].connect(key['server'], username='root', password='C527pfTZuoomex8sQ8aO', key_filename='/home/rayk/cmSsMGLu9g6slGX')
    except Exception, e:
      print key['server'] + '\t' + YELLOW + 'connecting' + END
      time.sleep(1)
    else:
      print key['server'] + '\t' + GREEN + 'connected' + END
      break

while True:
  print '\r ?> ',
  try:
    command = sys.stdin.readline().strip('\n')
  except KeyboardInterrupt:
    break
  if len(str(command)) < 2:
    continue
  if command == "df":
    command = "df -h | grep -E \'vda|sda|rootfs\' | grep -v boot | awk \'{ print $2 \"\t\" $3 \"\t\" $4 \"\t\" $5 }\'"
  if command in ['94.242.54.121',
                 '94.242.54.128',
                 '94.242.62.22',
                 '45.33.87.204',
                 '194.63.143.144',
                 '217.106.239.118',
                 '5.8.8.201',
                 '5.8.8.10',
                 '5.8.8.19',
                 '109.248.250.127',
                 '93.170.131.243',
                 '94.242.59.52',
                 '94.242.57.185',
                 '217.29.53.110']:
    for key in ssh:
      if key['server'] == command:
        break
    while True:
      print '\r     ' + BLUE + key['server'] + END + ' ?>> ',
      try:
        command = sys.stdin.readline().strip('\n')
      except KeyboardInterrupt:
        break
      if len(str(command)) < 2:
        continue
      stdin, stdout, stderr = key['session'].exec_command(command)
      for line in stdout.read().splitlines():
        print '\r     ' + BLUE + key['server'] + END + ' ?>> ' + key['color'] + line + END
  else:
    for key in ssh:
      stdin, stdout, stderr = key['session'].exec_command(command)
      for line in stdout.read().splitlines():
        print '\r   ' + key['server'] + ' '*(24-(3+len(str(key['server'])))) + key['color'] + line + END

for key in ssh:
  key['session'].close()

