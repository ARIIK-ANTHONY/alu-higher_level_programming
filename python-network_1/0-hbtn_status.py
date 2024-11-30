#!/usr/bin/python3
"""
This script fetches the status of the provided URL and displays:
- The type of the response body
- The raw content of the response body
- The content of the response body decoded in utf-8
"""

import urllib.request
import urllib.error

if __name__ == "__main__":
    # Define the URL (can be changed based on your requirements)
    url = "https://intranet.hbtn.io/status"  # Or use "http://0.0.0.0:5050/status"
    
    # Set headers to simulate a request from a browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    # Create the request with the headers
    request = urllib.request.Request(url, headers=headers)

    try:
        # Send the request and handle the response
        with urllib.request.urlopen(request) as response:
            body = response.read()
            
            # Print the response details
            print("Body response:")
            print("\t- type: {}".format(type(body)))
            print("\t- content: {}".format(body))
            print("\t- utf8 content: {}".format(body.decode("utf-8")))
    
    except urllib.error.HTTPError as e:
        # Handle HTTPError (e.g., 403 Forbidden or other errors)
        print(f"HTTP Error {e.code}: {e.reason}")
    except urllib.error.URLError as e:
        # Handle URL errors (e.g., if the URL cannot be reached)
        print(f"URL Error: {e.reason}")
