#! /usr/bin/env python3

import os
import requests
import re

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
                    if i == 1:
                        line = re.sub("[^0-9]*", "", line)
                    fruit[labels[i]] = line.strip()
                except IndexError:
                    print("{} has more than 3 lines. Please format correctly and try again".format(f))
                i += 1
            fruit["image_name"] = f.replace(".txt",".jpeg")
            data.append(fruit)

for item in data:
    response = requests.post("http://34.72.160.148/fruits/",json=item)
    print(response.content)
