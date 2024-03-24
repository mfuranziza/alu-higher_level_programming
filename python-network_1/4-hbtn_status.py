#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""

import requests

if __name__ == '__main__':
    # Sending a GET request to the specified URL
    res = requests.get("https://intranet.hbtn.io/status")

    # Printing the type of response content
    print("Body response:")
    print("\t- type: {}".format(type(res.text)))

    # Checking if the status code of the response is 200 (OK)
    if res.status_code == 200:
        # If the status code is 200, check if the content is exactly "OK"
        if res.text.strip() == "OK":
            print("\t- content: OK")
        else:
            # If the content is not "OK", print the actual content received in the response
            print("\t- content: {}".format(res.text))
    else:
        # If the status code is not 200, print the actual content received in the response
        print("\t- content: {}".format(res.text))
