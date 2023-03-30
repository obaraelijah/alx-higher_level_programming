#!/bin/bash
# This script takes a URL as an argument, sends a request to that URL using curl, and displays the size of the response body in bytes

# Check if URL argument is provided
if [ -z "$1" ]; then
  echo "Error: Please provide a URL as an argument"
  exit 1
fi

# Send curl request to URL and store response body in a variable
response=$(curl -sI "$1" | grep -i Content-Length | awk '{print $2}')

# Check if response is empty
if [ -z "$response" ]; then
  echo "Error: No response received from URL"
  exit 1
fi

# Print the size of the response body in bytes
echo "$response"
