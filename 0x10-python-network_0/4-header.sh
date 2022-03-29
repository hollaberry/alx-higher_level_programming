#!/bin/bash
#takes url as argument, sends a GET request, display body of response
# define and set header variable withh value 98
curl -s "$1" -X GET -H "X-School-User-Id: 98"
