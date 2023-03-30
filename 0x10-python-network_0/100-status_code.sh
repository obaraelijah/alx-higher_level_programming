#!/bin/bash
# sends request to URL and capture status code

curl -s  -w "%{response_code}" -o /dev/null "$1"
