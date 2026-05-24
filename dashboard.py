import streamlit as st

st.set_page_config(
    page_title="Nexe-Agent Internship Portfolio",
    page_icon="🤖",
    layout="wide"
)

# Header
st.title("🤖 Nexe-Agent Internship Portfolio")
st.subheader("AI & Automation Projects by Khadija Maqsood")
st.markdown("---")

# Stats
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("✅ Tasks Completed", "6/6")
with col2:
    st.metric("🐍 Language", "Python")
with col3:
    st.metric("🏢 Company", "Nexe-Agent")

st.markdown("---")

# Task 1
with st.expander("🟢 Task 1 — Basic AI Chatbot", expanded=True):
    col1, col2 = st.columns([2,1])
    with col1:
        st.markdown("""
        **Features:**
        - ✅ Accept user input
        - ✅ Send to Groq AI API
        - ✅ Display Response
        - ✅ Error Handling
        - ✅ Multi-turn conversation
        
        **Tech:** Python, Groq AI, Streamlit
        """)
    with col2:
        st.success("✅ COMPLETE")
        st.link_button("🚀 Live Demo", "https://nexechatbot-eub7zvjgq8v6ujovkktgca.streamlit.app")
        st.link_button("📂 GitHub", "https://github.com/khadijamaqsood226-oss/nexe_chatbot/blob/main/app.py")

st.markdown("---")

# Task 2
with st.expander("🟢 Task 2 — Email Automation Script"):
    col1, col2 = st.columns([2,1])
    with col1:
        st.markdown("""
        **Features:**
        - ✅ Send Scheduled Emails
        - ✅ Use Gmail SMTP
        - ✅ Log Email History
        
        **Tech:** Python, Gmail SMTP, Schedule Library
        """)
    with col2:
        st.success("✅ COMPLETE")
        st.link_button("📂 GitHub", "https://github.com/khadijamaqsood226-oss/nexe_chatbot/blob/main/email_bot.py")

st.markdown("---")

# Task 3
with st.expander("🟡 Task 3 — Resume Screener AI"):
    col1, col2 = st.columns([2,1])
    with col1:
        st.markdown("""
        **Features:**
        - ✅ Upload Resumes (PDF/DOCX)
        - ✅ Extract Skills
        - ✅ Match with Job Description
        - ✅ Output Match Percentage
        
        **Tech:** Python, Groq AI, PyPDF2, Streamlit
        """)
    with col2:
        st.success("✅ COMPLETE")
        st.link_button("🚀 Live Demo", "https://nexechatbot-2krz8uculzhwanue5f4ocg.streamlit.app")
        st.link_button("📂 GitHub", "https://github.com/khadijamaqsood226-oss/nexe_chatbot/blob/main/resume_screener.py")

st.markdown("---")

# Task 4
with st.expander("🟡 Task 4 — WhatsApp Automation"):
    col1, col2 = st.columns([2,1])
    with col1:
        st.markdown("""
        **Features:**
        - ✅ Auto-Reply System
        - ✅ FAQ-based Bot
        - ✅ Log Conversations
        
        **Tech:** Python, pywhatkit
        """)
    with col2:
        st.success("✅ COMPLETE")
        st.link_button("📂 GitHub", "https://github.com/khadijamaqsood226-oss/nexe_chatbot/blob/main/whatsapp_bot.py")

st.markdown("---")

# Task 5
with st.expander("🔴 Task 5 — Multi-Tool AI Agent"):
    col1, col2 = st.columns([2,1])
    with col1:
        st.markdown("""
        **Features:**
        - ✅ Search Web
        - ✅ Save Notes
        - ✅ Send Email
        - ✅ Use Function Tools
        
        **Tech:** Python, Groq AI, Function Calling
        """)
    with col2:
        st.success("✅ COMPLETE")
        st.link_button("📂 GitHub", "https://github.com/khadijamaqsood226-oss/nexe_chatbot/blob/main/ai_agent.py")

st.markdown("---")

# Task 6
with st.expander("🔴 Task 6 — RAG Knowledge Assistant"):
    col1, col2 = st.columns([2,1])
    with col1:
        st.markdown("""
        **Features:**
        - ✅ Upload Company Docs
        - ✅ Store Embeddings
        - ✅ Query System
        - ✅ Return Contextual Answers
        
        **Tech:** Python, Groq AI, RAG, Streamlit
        """)
    with col2:
        st.success("✅ COMPLETE")
        st.link_button("🚀 Live Demo", "https://nexechatbot-mmdtkxnzuwoaievxxwfdjj.streamlit.app")
        st.link_button("📂 GitHub", "https://github.com/khadijamaqsood226-oss/nexe_chatbot/blob/main/rag_assistant.py")

st.markdown("---")

# Footer
st.markdown("""
<div style='text-align: center'>
    <h3>🎉 All 6 Tasks Complete!</h3>
    <p>Built with ❤️ by <b>Khadija Maqsood</b> | AI & Automation Intern at Nexe-Agent</p>
    <a href='https://github.com/khadijamaqsood226-oss/nexe_chatbot'>📂 View All Code on GitHub</a>
</div>
""", unsafe_allow_html=True)