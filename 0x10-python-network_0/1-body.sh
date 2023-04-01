#!/bin/bash
#script to display size of body of response from a GET request
curl -sL "$1" -X GET -D ./header -o ./output; if grep -q "200 OK" ./header; then cat ./output; fi
