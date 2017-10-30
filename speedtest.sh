#!/bin/sh

a=`cat /dev/urandom | tr -dc 'a-z0-9' | fold -w 20 | head -n 1`.txt

for i in `cat $1`;
  do
    login=`echo $i | awk -F: '{ print $3 }'`
    pass=`echo $i | awk -F: '{ print $4 }'`
    addr=`echo $i | awk -F: '{ print $1 }'` 
    port=`echo $i | awk -F: '{ print $2 }'`
    export http_proxy=http://$login:$pass@$addr:$port/
    /home/rayk/speedtest-cli --share #--server 5220
    unset http_proxy
  done
