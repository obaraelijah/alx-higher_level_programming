#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with "You got me!"
curl -s -X PUT --data "user_id=98" 0.0.0.0:5000/catch_me -H "Origin: HolbertonSchool"

