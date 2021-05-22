#!/usr/bin/env python3

from email.message import EmailMessage
import mimetypes
import smtplib
import os.path

def main():
    sender = "automation@example.com"
    recipient = "student-02-b2e927b7fb52@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = """All fruits are uploaded to our website successfully. A detailed list is attached to this email."""
    attachment_path = "/tmp/processed.pdf"
    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)
    print(mime_type)
    message = EmailMessage()

    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)
    with open(attachment_path, 'rb') as ap:
        message.add_attachment(ap.read(),
                                maintype=mime_type,
                                subtype=mime_subtype,
                                filename=attachment_filename)
    print(message)
    
if __name__ == "__main__":
    main()
