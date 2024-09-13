#!/usr/bin/python3
"""
Fetches and prints the content of a URL.

Usage: ./3-handle_error.py <URL>
  - Catches and displays HTTP error codes.
"""
import sys
import urllib.error
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as res:
            print(res.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        print(f"Error code: {error.code}")
