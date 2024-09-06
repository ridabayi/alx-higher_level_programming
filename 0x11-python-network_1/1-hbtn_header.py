#!/usr/bin/python3

import urllib.request
import sys

def fetch_request_id(url):
    """Fetches and displays the X-Request-Id from the response headers."""
    with urllib.request.urlopen(url) as response:
        # Retrieve the value of the X-Request-Id header
        request_id = response.getheader('X-Request-Id')
        print(request_id)

if __name__ == "__main__":
    # Get the URL from command line arguments
    url = sys.argv[1]
    fetch_request_id(url)
