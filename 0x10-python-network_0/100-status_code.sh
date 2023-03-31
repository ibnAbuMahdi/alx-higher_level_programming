#!/bin/bash
#print body only if response code is 200
curl -sI -o "head.txt"  -w "%{http_code}" "$1"
