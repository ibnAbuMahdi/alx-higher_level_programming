#!/bin/bash
#print body only if response code is 200
curl -s -G -d "X%2DSchool%2DUser%2DId=98" "$1" 
