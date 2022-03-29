#!/bin/bash
#takes url as argument, sends a GET request, display body of response
curl -s "$1" -X GET -H "X-School-User-Id: 98"
