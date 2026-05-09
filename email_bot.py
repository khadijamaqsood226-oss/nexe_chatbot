import smtplib
import schedule
import time
import json
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# Email Configuration
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")
LOG_FILE = "email_log.json"

def send_email(to_email, subject, body):
    """Send email using Gmail SMTP"""
    try:
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)
        server.quit()

        log_email(to_email, subject, "Success")
        print(f"✅ Email sent to {to_email} at {datetime.now()}")
        return True

    except Exception as e:
        log_email(to_email, subject, f"Failed: {str(e)}")
        print(f"❌ Error: {str(e)}")
        return False

def log_email(to_email, subject, status):
    """Log email history to JSON file"""
    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            logs = json.load(f)

    logs.append({
        "timestamp": str(datetime.now()),
        "to": to_email,
        "subject": subject,
        "status": status
    })

    with open(LOG_FILE, 'w') as f:
        json.dump(logs, f, indent=2)

def scheduled_email():
    """This function runs on schedule"""
    print(f"⏰ Sending scheduled email at {datetime.now()}")
    send_email(
        to_email=SENDER_EMAIL,
        subject="Scheduled Email - Nexe Agent",
        body="Hello! This is your scheduled email from Nexe-Agent Email Bot! 🤖"
    )

print("🤖 Nexe-Agent Email Bot Started!")
print("📧 Sending test email now...")

# Send one test email immediately
send_email(
    to_email=SENDER_EMAIL,
    subject="Test Email - Nexe Agent Bot",
    body="Hello! Your Nexe-Agent Email Bot is working perfectly! 🎉"
)

# Schedule email every day at 9:00 AM
print("\n⏰ Scheduling daily email at 9:00 AM...")
schedule.every().day.at("09:00").do(scheduled_email)

print("✅ Bot is running! Press Ctrl+C to stop.\n")
while True:
    schedule.run_pending()
    time.sleep(60)