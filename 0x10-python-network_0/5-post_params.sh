#!/bin/bash
# Takes in a URL, sends a POST request to the passed URL, and displays the body of the response with email and subject parameters
curl -s -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
