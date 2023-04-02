#!/bin/bash
# post data
curl -s -d @$2 -H 'Content-Type: application/json' "$1"
