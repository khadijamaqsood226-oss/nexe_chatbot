import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
conversation_history = []

def chat(user_message):
    conversation_history.append({"role": "user", "content": user_message})
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "system", "content": "You are a helpful AI assistant."}] + conversation_history,
        max_tokens=500
    )
    reply = response.choices[0].message.content
    conversation_history.append({"role": "assistant", "content": reply})
    return reply

print("🤖 Nexe-Agent Chatbot - Type 'quit' to exit\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in ["quit", "exit"]:
        print("Goodbye!")
        break
    if not user_input:
        continue
    try:
        print(f"Bot: {chat(user_input)}\n")
    except Exception as e:
        print(f"Error: {e}\n")