#!/bin/bash
#prints the body size of response from a url curl
curl -sI -X "OPTIONS" "$1" | grep Allow | cut -d ' ' -f2-
