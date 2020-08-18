#!/bin/bash

curl -sI "$1" | grep [Cc]ontent-[Ll]ength: | awk '{ print $2 }'