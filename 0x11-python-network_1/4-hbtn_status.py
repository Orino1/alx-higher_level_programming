#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
import requests

if __name__ == "__main__":
    url = "http://orino.tech"
    response = requests.get(url)
    print("Body response:")
    print(f"\t- type: {type(response)}")
    print(f"\t-- content: {response.text}")
