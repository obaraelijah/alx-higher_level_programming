#!/bin/bash
end request to URL and capture status code

curl -s  -w "%{http_code}" -o /dev/null "$1"
