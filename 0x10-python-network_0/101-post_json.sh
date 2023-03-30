#!/usr/bin/bash
# sends a JSON POST request to a URL and displays the body of the response

curl -s -H "Content-Type: application/json" -X POST -d @$2 "$1"
