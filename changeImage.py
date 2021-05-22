#!/usr/bin/env python3

import os
from PIL import Image

root = "/home/student-02-b2e927b7fb52/supplier-data/images"

for f in os.listdir(root):
    if not f.startswith(".") and f.endswith(".tiff"):
        with Image.open(os.path.join(root,f)) as image:
            image.convert("RGB").resize((600,400)).save(fp=os.path.join(root,f.replace("tiff","jpeg")),format="JPEG")
