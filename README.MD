# 📧 Nexe-Agent Email Automation Bot

Built during my AI & Automation Internship at **Nexe-Agent**.

---

## What is this?
An automated email bot that sends scheduled emails using Gmail SMTP and logs email history.

---

## ✅ Features
- 📧 Send emails via Gmail
- ⏰ Schedule daily emails automatically
- 📝 Log every email in a JSON file
- ❌ Error handling for failed emails

---

## 🛠️ Tech Stack
- Python 3.12
- Gmail SMTP
- Schedule Library
- Python-dotenv

---

## ⚙️ How to Run

### 1. Install dependencies
pip install schedule python-dotenv

### 2. Add your credentials in .env file
SENDER_EMAIL="your_gmail@gmail.com"
APP_PASSWORD="your_16_digit_app_password"

### 3. Run the bot
python email_bot.py

---

## 📝 How it workS
1. Bot starts and sends a test email immediately
2. Schedules daily email at 9:00 AM
3. Logs every email with timestamp and status

---

## 👩‍💻 Author
Khadija Maqsood
AI & Automation Intern at Nexe-Agent
