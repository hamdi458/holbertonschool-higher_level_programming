#!/bin/bash
# bash script
curl -sI "$1" | grep [Cc]ontent-[Ll]ength: | awk '{ print $2 }'