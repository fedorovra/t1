#!/bin/sh

a=`cat /dev/urandom | tr -dc 'a-z0-9' | fold -w 20 | head -n 1`.txt

case $1 in
  "-4")
    cat $2 | awk '{ print $2 ":" $4 ":" $5 }' > /tmp/$a
    for i in `cat /tmp/$a`;
    do
      login=`echo $i | awk -F: '{ print $3 }'`
      pass=`echo $i | awk -F: '{ print $4 }'`
      addr=`echo $i | awk -F: '{ print $1 }'`
      port=`echo $i | awk -F: '{ print $2 }'`
      export http_proxy=http://$login:$pass@$addr:$port/
      /home/rayk/speedtest-cli --share # --server 5220
      unset http_proxy
    done
    rm /tmp/$a
    ;;
  "-6")
    for i in `cat $2`;
    do
      login=`echo $i | awk -F: '{ print $3 }'`
      pass=`echo $i | awk -F: '{ print $4 }'`
      addr=`echo $i | awk -F: '{ print $1 }'` 
      port=`echo $i | awk -F: '{ print $2 }'`
      export http_proxy=http://$login:$pass@$addr:$port/
      /home/rayk/speedtest-cli --share # --server 5220
      unset http_proxy
    done
    ;;
  *)
    echo 'Bad parameter'
esac

