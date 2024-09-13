#!/usr/bin/python3
"""Retrieves the content from https://alx-intranet.hbtn.io/status."""
import requests

if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status")
    print("Response details:")
    print("\t- Data type: {}".format(type(response.text)))
    print("\t- Content: {}".format(response.text))
