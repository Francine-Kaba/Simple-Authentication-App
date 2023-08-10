import os
import smtplib
import traceback
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = os.getenv("HOST_EMAIL")
sender_password = os.getenv("HOST_PASSWORD")
smtp_server = os.getenv("SMTP_SERVER")
smtp_port = os.getenv("SMTP_PORT")


def send_email(details, html_body):
    try:
        # Create a MIMEText object for the email content
        html_content = html_body.format(**details)

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = details["recipient_email"]
        msg['Subject'] = details["subject"]
        msg.attach(MIMEText(html_content, "html"))

        # Connect to the SMTP server and start TLS encryption
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        # Login to the SMTP server
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, details["recipient_email"], msg.as_string())

        # Quit the SMTP server
        server.quit()

        print("Email sent successfully!")
    except Exception as e:
        traceback.print_exc()
        print("An error occurred while sending the email:", e)
