import os
import json
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")
NOTES_FILE = "agent_notes.json"

# ============ TOOLS ============

def search_web(query):
    """Simulate web search"""
    print(f"🔍 Searching web for: {query}")
    results = {
        "AI trends": "AI is growing rapidly in 2025. LLMs, Agents and Automation are top trends.",
        "Python": "Python is the most popular programming language for AI and automation.",
        "Nexe-Agent": "Nexe-Agent is an AI-powered software solutions company based in Pakistan.",
    }
    for key in results:
        if key.lower() in query.lower():
            return results[key]
    return f"Search results for '{query}': Found relevant information about {query} in latest news."

def save_note(title, content):
    """Save notes to JSON file"""
    notes = []
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'r') as f:
            notes = json.load(f)
    
    notes.append({
        "id": len(notes) + 1,
        "title": title,
        "content": content,
        "timestamp": str(datetime.datetime.now())
    })
    
    with open(NOTES_FILE, 'w') as f:
        json.dump(notes, f, indent=2)
    
    return f"✅ Note saved: '{title}'"

def send_email(to_email, subject, body):
    """Send email via Gmail"""
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
        return f"✅ Email sent to {to_email}!"
    except Exception as e:
        return f"❌ Email failed: {str(e)}"

def get_notes():
    """Get all saved notes"""
    if not os.path.exists(NOTES_FILE):
        return "No notes saved yet!"
    with open(NOTES_FILE, 'r') as f:
        notes = json.load(f)
    return json.dumps(notes, indent=2)

# ============ AI AGENT ============

tools = [
    {
        "type": "function",
        "function": {
            "name": "search_web",
            "description": "Search the web for information",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search query"}
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "save_note",
            "description": "Save a note with title and content",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {"type": "string", "description": "Note title"},
                    "content": {"type": "string", "description": "Note content"}
                },
                "required": ["title", "content"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "send_email",
            "description": "Send an email",
            "parameters": {
                "type": "object",
                "properties": {
                    "to_email": {"type": "string", "description": "Recipient email"},
                    "subject": {"type": "string", "description": "Email subject"},
                    "body": {"type": "string", "description": "Email body"}
                },
                "required": ["to_email", "subject", "body"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_notes",
            "description": "Get all saved notes",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    }
]

def run_tool(tool_name, tool_args):
    """Execute the tool called by AI"""
    if tool_name == "search_web":
        return search_web(tool_args["query"])
    elif tool_name == "save_note":
        return save_note(tool_args["title"], tool_args["content"])
    elif tool_name == "send_email":
        return send_email(tool_args["to_email"], tool_args["subject"], tool_args["body"])
    elif tool_name == "get_notes":
        return get_notes()

def run_agent(user_message):
    """Run the AI Agent"""
    print(f"\n👤 You: {user_message}")
    messages = [{"role": "user", "content": user_message}]
    
    while True:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            tools=tools,
            tool_choice="auto",
            max_tokens=1000
        )
        
        choice = response.choices[0]
        
        if choice.finish_reason == "tool_calls":
            tool_calls = choice.message.tool_calls
            messages.append(choice.message)
            
            for tool_call in tool_calls:
                tool_name = tool_call.function.name
                tool_args = json.loads(tool_call.function.arguments)
                print(f"🛠️  Using tool: {tool_name}")
                
                result = run_tool(tool_name, tool_args)
                print(f"✅ Tool result: {result}")
                
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(result)
                })
        else:
            final_response = choice.message.content
            print(f"🤖 Agent: {final_response}")
            return final_response

# ============ MAIN ============

print("=" * 50)
print("  🤖 Nexe-Agent Multi-Tool AI Agent")
print("=" * 50)
print("Commands: search, note, email, notes, quit")
print("\nExamples:")
print("  - Search for AI trends")
print("  - Save a note about Python")
print("  - Send email to someone@gmail.com")
print("  - Show my notes")
print()

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in ["quit", "exit"]:
        print("👋 Goodbye!")
        break
    if not user_input:
        continue
    try:
        run_agent(user_input)
    except Exception as e:
        print(f"❌ Error: {str(e)}")
    