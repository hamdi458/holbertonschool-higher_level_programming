#!/bin/bash
#   Bash script that makes a request to 0.0.0.0:5000/catch_me
curl -sL -X 0:5000/catch_me PUT "You got me!" -H "Origin: HolbertonSchool" -d "user_id=98"
