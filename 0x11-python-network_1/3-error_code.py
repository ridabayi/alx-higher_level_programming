#!/usr/bin/python3
"""
Fetches the content of a URL and prints the body of the response, decoded in UTF-8.
"""

import urllib.request
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
    except:
        pass
