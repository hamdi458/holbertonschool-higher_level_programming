#!/bin/bash
# bash script
curl -sI "$1" | grep 'Content-Length:' | cut -d ' ' -f2