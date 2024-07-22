#!/bin/bash
# sends a 'DELETE' request to the URL passed as the first argument and displays body of response
curl -s --request "DELETE" "$1"
