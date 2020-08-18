#!/bin/bash
# bash script
curl --head --silent --location "$URL" | grep -i "content-length:" | tr -d " \t" | cut -d ':' -f 2