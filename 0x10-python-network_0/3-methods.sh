#!/bin/bash
#script to display size of body of response from a DELETE request
curl -sI "$1" -X OPTIONS | grep "Allow:" | cut -d':' -f2 | sed 's/ //'
