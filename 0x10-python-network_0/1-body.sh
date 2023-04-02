#!/bin/bash
#print body only if response code is 200
me=$(curl -s -o resp.txt -w "%{http_code}" "$1"); [ "$me" == "200" ] && cat resp.txt;
