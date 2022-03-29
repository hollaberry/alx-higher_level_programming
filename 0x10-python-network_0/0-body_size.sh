#!/bin/bash
# Script that takes in URL, sends a request to Url
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'
