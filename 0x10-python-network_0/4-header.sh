#!/bin/bash
#print body only if response code is 200
curl -sG -d "X-School-User-Id=98" "$1" 
