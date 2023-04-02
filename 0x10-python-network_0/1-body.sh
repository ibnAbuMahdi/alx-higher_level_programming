#!/bin/bash
#print body only if response code is 200
me=$(curl -sL -o resp.txt -w "%{http_code}" "$1"); [ "$me" == "200" ] && cat resp.txt;
