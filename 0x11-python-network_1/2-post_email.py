#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2].encode("utf-8")
    request_object = urllib.request.Request(url, data=email, method="POST")
    with urllib.request.urlopen(request_object) as response:
        print(response.read().decode("utf-8"))
