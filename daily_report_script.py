import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time
from datetime import datetime

def send_email(subject, body, to_email):
    # Set up the MIME
    msg = MIMEMultipart()
    msg['From'] = 'your_email@gmail.com'  # Replace with your Gmail email address
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the body to the email
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('your_email@gmail.com', 'your_password')  # Replace with your Gmail email and password
        server.sendmail('your_email@gmail.com', to_email, msg.as_string())

def generate_report():
    # Replace this with your actual report generation logic
    report = "Daily Report\nDate: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return report

def job():
    report = generate_report()
    send_email('Daily Report', report, 'recipient@example.com')  # Replace with the recipient's email address

# Schedule the job to run daily at a specific time (adjust as needed)
schedule.every().day.at("08:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
