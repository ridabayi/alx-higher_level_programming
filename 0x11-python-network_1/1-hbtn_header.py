#!/usr/bin/python3
"""Fetches and prints the value of the X-Request-Id header from a URL.
Usage: ./1-hbtn_header.py <URL>
"""
import sys
import urllib.request

def fetch_request_id(url):
    """Fetches the X-Request-Id header from the provided URL."""
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        headers = dict(response.headers)
        return headers.get("X-Request-Id")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)
    
    url = sys.argv[1]
    print(fetch_request_id(url))
