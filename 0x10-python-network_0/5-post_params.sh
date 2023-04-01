#!/bin/bash
#print body only if response code is 200
curl -s -d "email=test@gmail.com&subject='I%20will%20always%20be%20here%20for%20PLD'" "$1" 
