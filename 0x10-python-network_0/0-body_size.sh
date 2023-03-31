#!/bin/bash
#prints the body size of response from a url curl
curl -sI "$1" | grep Content-Length | cut -d ' ' -f2

