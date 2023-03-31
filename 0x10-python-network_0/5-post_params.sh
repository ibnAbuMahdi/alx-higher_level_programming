#!/bin/bash
#print body only if response code is 200
curl -s -d "email=test@gmail.com&subject='I will always be here for PLD'" "$1" 
