"""
You will need to pass the following arguments to the reports.generate_report method: 
the text description processed from the text files as the paragraph argument, the report title as the title argument, 
and the file path of the PDF to be generated as the attachment argument (use /tmp/processed.pdf')

"""

#!/usr/bin/env python3

import email.message
import mimetypes
import os.path
import smtplib

def generate_email(sender, reciever, subject, body, attachment_path = None):
  #generate email
  # Basic Email formatting
  message = email.message.EmailMessage()
  message['Subject'] = subject
  message['From'] = sender
  message['To'] = reciever
  message.set_content(body)

  if attachment_path != None:
    attachment_name = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split("/", 1)
    with open(attachment_path, 'rb') as fp:
      message.add_attachment(fp.read(),
                            maintype=mime_type,
                            subtype=mime_subtype,
                            filename=attachment_name)
  return message

def send_email(package):
  """Sends the email package to the configured SMTP server."""
  mail_server = smtplib.SMTP('localhost')
  mail_server.send_message(package)
  mail_server.quit()
