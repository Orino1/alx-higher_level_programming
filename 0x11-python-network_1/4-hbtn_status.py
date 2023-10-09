#!/usr/bin/env python3
"""fetches https://alx-intranet.hbtn.io/status"""
import requests

url = "https://alx-intranet.hbtn.io/status"
response = requests.get(url)
print("Body response:")
print(f"\t- type: {type(response)}")
print(f"\t-- content: {type(response.text)}")
