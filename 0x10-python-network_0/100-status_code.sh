#!/bin/bash
# Sends a request to a URL and displays the status code
curl -s -w "%{response_code}" -o /dev/null "$1"
