#!/usr/bin/env python3

from email.message import EmailMessage
import mimetypes
import smtplib
import os.path

def generate_message():
    sender = "automation@example.com"
    recipient = "student-02-b2e927b7fb52@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = """All fruits are uploaded to our website successfully. A detailed list is attached to this email."""
    attachment_path = "/tmp/processed.pdf"
    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)
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
    return message

def send_message(message):
    print(message)
    

def main():
    message = generate_message()
    send_message(message)

if __name__ == "__main__":
    main()
