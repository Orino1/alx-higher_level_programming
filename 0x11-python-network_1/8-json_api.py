#!/usr/bin/python3
"""
takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the
letter as a parameter.
"""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    data = {
        'q': ""
    }
    if len(sys.argv) > 1:
        data['q'] = sys.argv[1]
    response = requests.post(url, data=data)
    try:
        recived_data = response.json()
        if len(recived_data) > 0:
            print(f"[{recived_data.get('id')}] {recived_data.get('name')}")
        else:
            print("No result")
    except:
        print("Not a valid JSON")
