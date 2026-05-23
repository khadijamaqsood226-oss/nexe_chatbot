import pywhatkit
import datetime
import json
import os

LOG_FILE = "whatsapp_log.json"

# FAQ responses
FAQ = {
    "hello": "Hello! Welcome to Nexe-Agent WhatsApp Bot! How can I help you? 🤖",
    "hi": "Hi there! I am Nexe-Agent Bot. How can I assist you? 😊",
    "services": "We offer AI & Automation services including Chatbots, Email Automation, Resume Screening and more!",
    "contact": "You can reach us at nexeagent@gmail.com or visit our LinkedIn: Nexe-Agent",
    "price": "Please contact us at nexeagent@gmail.com for pricing details.",
    "help": "I can answer questions about: services, contact, price. Just type any of these!",
}

def log_conversation(phone, message, response):
    """Log conversations to JSON file"""
    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            logs = json.load(f)
    
    logs.append({
        "timestamp": str(datetime.datetime.now()),
        "phone": phone,
        "message": message,
        "response": response
    })
    
    with open(LOG_FILE, 'w') as f:
        json.dump(logs, f, indent=2)
    print(f"✅ Conversation logged!")

def get_faq_response(message):
    """Get FAQ based response"""
    message_lower = message.lower()
    for keyword, response in FAQ.items():
        if keyword in message_lower:
            return response
    return "Sorry, I didn't understand. Type 'help' to see what I can answer! 🤖"

def send_whatsapp_message(phone_number, message):
    """Send WhatsApp message"""
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute + 2
    
    if minute >= 60:
        minute = minute - 60
        hour = hour + 1
    
    print(f"📱 Sending WhatsApp message to {phone_number}...")
    pywhatkit.sendwhatmsg(phone_number, message, hour, minute)
    print(f"✅ Message scheduled!")

def auto_reply(phone_number, incoming_message):
    """Auto reply based on FAQ"""
    response = get_faq_response(incoming_message)
    log_conversation(phone_number, incoming_message, response)
    send_whatsapp_message(phone_number, response)
    return response

# Demo - Test the bot
print("🤖 Nexe-Agent WhatsApp Bot")
print("=" * 40)
print("\n📋 FAQ System Test:")

test_messages = ["hello", "services", "price", "help"]
for msg in test_messages:
    response = get_faq_response(msg)
    print(f"\nQ: {msg}")
    print(f"A: {response}")

print("\n" + "=" * 40)
print("✅ FAQ Bot is working!")
print("\n📱 To send actual WhatsApp message:")

phone = input("\nEnter phone number with country code (e.g. +923001234567): ")
message = input("Enter your message: ")

confirm = input(f"\nSend '{message}' to {phone}? (yes/no): ")
if confirm.lower() == "yes":
    auto_reply(phone, message)
    print("\n✅ Check WhatsApp Web — message will be sent in 2 minutes!")
else:
    print("❌ Cancelled!")
    log_conversation(phone, message, "Cancelled by user")

print("\n📝 Check whatsapp_log.json for conversation history!")