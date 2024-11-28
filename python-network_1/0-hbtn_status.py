#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status."""
import urllib.request

if __name__ == "__main__":
    # Set a custom User-Agent header to avoid being blocked
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    # Prepare the request with headers
    request = urllib.request.Request("https://intranet.hbtn.io/status", headers=headers)
    
    # Fetch the response
    with urllib.request.urlopen(request) as response:
        body = response.read()
        
        # Print the response information
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
