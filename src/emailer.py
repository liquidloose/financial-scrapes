from email import encoders
from email.message import EmailMessage
from email.mime.base import MIMEBase
from fileinput import filename
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys

from secret import Secrets

# Creates the base text message. Enter your own credentials.
# Each field needs to be a string
sender_email = Secrets.sender_email
sender_password = Secrets.sender_password
receiver_email = Secrets.receiver_email

message = EmailMessage()
message['Subject'] = "Wall Street Journal Market Diary Update"
message['From'] = sender_email
message['To'] = receiver_email

# Creates the main body content
message.set_content("Today's Market Diary update.")

# Adds secondary content in the message
message.add_alternative("""\
<!DOCTYPE html>
<html>
  <head></head>
  <body>
  <div style="height:30%;width:60%;color:blue;border-style: solid; border-color: gray; border-size: \
    4px;text-align:center;background-color:black"> \
    <img src="https://murals-weblinc.netdna-ssl.com/product_images/wall-street-bull-nyc-wall-mural/5ecd44a6585ab7011b49a85b/product_large_image.jpg?c=1590510758"alt="Girl in a jacket" width=150px height=200px>
  </div>
  </body>
</html>
""", subtype='html')

# Accesses the file and then attaches it to the email object
with open('./assets/wsj.xlsx', 'rb') as f:
    file_data = f.read()
    file_name = f.name

message.add_attachment(file_data, maintype="octet-stream",
                       subtype="xlsx", filename=file_name)


context = ssl.create_default_context()  # Adds security
# Sends email
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, sender_password)
    server.send_message(message)
print("Email sent!")
