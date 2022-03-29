#!/bin/bash
# takes in a url, sends a POST request to the passed URL
curl -s "$1" -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
