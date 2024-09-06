#!/usr/bin/python3

import urllib.request
import urllib.parse
import sys

def post_email(url, email):
    """Sends a POST request with an email parameter and displays the response body."""
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    request = urllib.request.Request(url, data=data)
    
    with urllib.request.urlopen(request) as response:
        body = response.read().decode('utf-8')
        print(f"Your email is: {body}")

if __name__ == "__main__":
    # Get the URL and email from command line arguments
    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
