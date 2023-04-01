#!/bin/bash
#script to display size of body of response from a GET request
curl -s "$1" -X GET -H "X-School-User-Id: 98"
