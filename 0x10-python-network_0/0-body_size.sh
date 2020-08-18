#!/bin/bash
# Displays the size of the body of the response
curl -sI "$1" | grep -i content-length | awk '{print $2}'