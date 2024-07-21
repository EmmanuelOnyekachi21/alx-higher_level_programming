#!/bin/bash
# sends a GET request to a URL and displays the body of the response if the status is 200
curl -s -o response.txt -w "%{http_code}" "$1" | grep -q "^200$" && cat response.txt
