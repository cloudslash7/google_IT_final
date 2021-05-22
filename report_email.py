#!/usr/bin/env python3

import os
import datetime
import reports

def main():
    root = "/home/student-02-b2e927b7fb52/supplier-data/descriptions"
    attachment = "/tmp/processed.pdf"
    title = "Processed Update on " + datetime.datetime.now().strftime("%B %d, %Y")
    paragraph = ""
    for f in os.listdir(root):
        if f.endswith(".txt"):
            with open(os.path.join(root,f), "r") as item:
                lines = item.readlines()
                name = lines[0]
                weight = lines[1]
                paragraph += name + "<br/>" + weight + "<br/>" + "<br/>"

    reports.generate_report(attachment, title, paragraph)

if __name__ == "__main__":
    main()
