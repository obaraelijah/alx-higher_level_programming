#!/bin/bash

# Takes in a URL, sends a GET request to that URL, and displays the body of the response
response=$(curl -s -o /dev/null -w "%{http_code}" "$1")  # Get the HTTP status code
if [[ "$response" == "200" ]]; then  # If the status code is 200 OK
  curl -s "$1"  # Display the body of the response
fi
