#!/bin/bash
#print body only if response code is 200
curl -s -o resp.txt -w "%{http_code}" "$1" | { read me; [ "$me" == "200" ] && cat resp.txt; }
