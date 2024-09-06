#!/usr/bin/python3

import urllib.request

def fetch_status(url):
    """Fetches and displays the status of the given URL."""
    with urllib.request.urlopen(url) as response:
        body = response.read().decode('utf-8')
        print("Body response:")
        print(f"    - type: {type(body)}")
        print(f"    - content: {body}")
        print(f"    - utf8 content: {body}")

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    fetch_status(url)
