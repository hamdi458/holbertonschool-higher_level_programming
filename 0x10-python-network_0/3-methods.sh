#!/bin/bash
# get http methods
curl -sI "$1" | grep Allow | cut -d ' ' -f2-
