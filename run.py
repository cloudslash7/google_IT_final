#! /usr/bin/env python3

import os
import requests

root = "/home/student-02-b2e927b7fb52/supplier-data/descriptions"
data = []
labels = ("name", "weight", "description")
for f in os.listdir(root):
    if f.endswith(".txt"):
        fruit = {}
        i = 0
        with open(os.path.join(root,f),"r") as text_file:
            for line in text_file:
                try:
                    fruit[labels[i]] = line.strip()
                except IndexError:
                    print("{} has more than 3 lines. Please format correctly and try again".format(f))
                i += 1
            fruit["image_name"] = f
            data.append(fruit)

for item in data:
    response = requests.post("http://34.72.160.148/fruits/",json=item)
    print(response)
