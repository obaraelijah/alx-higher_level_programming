#!/bin/bash
# sends request to URL and capture status code

curl -s  -w "%{esponse_code}" -o /dev/null "$1"
