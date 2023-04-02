#!/bin/bash
#print body only if response code is 200
curl -s -H "X-School-User-Id:98" "$1" 
