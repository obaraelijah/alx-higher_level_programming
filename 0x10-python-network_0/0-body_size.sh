#!/bin/bash
# Takes in a url and sends a request to that url and displays the size of the body of the response
curl -s -w '%{size_uploa}\n' -o /dev/null "$1"
