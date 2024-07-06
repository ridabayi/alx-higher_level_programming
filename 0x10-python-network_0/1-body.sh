#!/bin/bash
# Sends a GET request to a URL and displays the body of a 200 status code response
curl -sL -w "%{http_code}" "$1" -o temp_response.txt | grep -q "200" && cat temp_response.txt
