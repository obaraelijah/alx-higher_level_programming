#!/bin/bash
# Takes in a url and sends a GET Irequest to that url and displays the body of the response
curl -s -L "$1"
