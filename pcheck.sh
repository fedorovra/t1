#!/bin/sh

a=`cat /dev/urandom | tr -dc 'a-z0-9' | fold -w 20 | head -n 1`.txt

case $1 in
  "-4")
    case $2 in
      "-h")
        cat $3 | awk '{ print $2 ":" $4 ":" $5 }' > /tmp/$a
        ./checker.py --http /tmp/$a
        ;;
      "-s")
        cat $3 | awk '{ print $3 ":" $4 ":" $5 }' > /tmp/$a
        ./checker.py --socks /tmp/$a
        ;;
      *)
        echo 'Bad parameter'
        ;;
    esac
    rm /tmp/$a
    ;;
  "-6")
    case $2 in
      "-h")
        ./checker.py --http $3
        ;;
      "-s")
        ./checker.py --socks $3
        ;;
      *)
        echo 'Bad parameter'
        ;;
    esac
    ;;
  *)
    echo 'Bad parameter'
    ;;
esac

