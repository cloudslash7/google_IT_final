#!/usr/bin/env python3
import requests
import os

# This example shows how a file can be uploaded using
# The Python Requests module

root = "/home/student-02-b2e927b7fb52/supplier-data/images"
url = "http://localhost/upload/"
for f in os.listdir(root):
    if f.endswith(".jpeg"):
        with open(os.path.join(root,f), 'rb') as opened:
            r = requests.post(url, files={'file': opened})
