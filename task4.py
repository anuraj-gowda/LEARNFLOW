pip install schedule

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

def send_email(subject, body, to_email):
    # Email configuration
    from_email = "meghanag2026@gmail.com"
    password = "Me@7676364573"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create the email message
    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, message.as_string())

def compose_and_send_email():
    # Compose your email
    subject = "Test Email"
    body = "This is a test email sent using the automated email sender script."

    # Set recipient email
    to_email = "ghanalakshmighanalakshmi@gmail.com"

    # Send the email
    send_email(subject, body, to_email)

# Schedule the email to be sent every day at a specific time
schedule.every().day.at("10:00").do(compose_and_send_email)

# Run the scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)