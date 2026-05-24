import os
import json
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Simple in-memory vector store
knowledge_base = []

def add_document(text, filename):
    """Split document into chunks and store"""
    chunks = [text[i:i+500] for i in range(0, len(text), 500)]
    for i, chunk in enumerate(chunks):
        knowledge_base.append({
            "id": len(knowledge_base) + 1,
            "filename": filename,
            "chunk": i + 1,
            "content": chunk
        })
    return len(chunks)

def search_knowledge_base(query, top_k=3):
    """Simple keyword-based search"""
    query_words = query.lower().split()
    scored = []
    
    for doc in knowledge_base:
        score = sum(1 for word in query_words if word in doc["content"].lower())
        if score > 0:
            scored.append((score, doc))
    
    scored.sort(key=lambda x: x[0], reverse=True)
    return [doc for _, doc in scored[:top_k]]

def get_answer(query, context_docs):
    """Get AI answer based on context"""
    if not context_docs:
        return "No relevant information found in the knowledge base. Please upload relevant documents first!"
    
    context = "\n\n".join([f"From {doc['filename']}:\n{doc['content']}" for doc in context_docs])
    
    prompt = f"""You are a helpful assistant. Answer the question based ONLY on the provided context.
    
Context:
{context}

Question: {query}

Answer based on the context above. If the answer is not in the context, say "I couldn't find this information in the uploaded documents." """
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )
    return response.choices[0].message.content

# Streamlit UI
st.title("📚 RAG Knowledge Assistant")
st.caption("Powered by Groq AI — Nexe-Agent Internship")

# Sidebar for uploading docs
with st.sidebar:
    st.header("📁 Upload Documents")
    uploaded_files = st.file_uploader(
        "Upload TXT or PDF files",
        type=["txt", "pdf"],
        accept_multiple_files=True
    )
    
    if uploaded_files:
        for file in uploaded_files:
            if file.name.endswith(".txt"):
                text = file.read().decode("utf-8")
            else:
                import PyPDF2
                reader = PyPDF2.PdfReader(file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text()
            
            chunks = add_document(text, file.name)
            st.success(f"✅ {file.name} — {chunks} chunks added!")
        
        st.info(f"📊 Total chunks in knowledge base: {len(knowledge_base)}")

# Main chat area
st.subheader("💬 Ask Questions")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask anything about your documents..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        if not knowledge_base:
            response = "⚠️ Please upload documents first from the sidebar!"
        else:
            with st.spinner("Searching knowledge base..."):
                relevant_docs = search_knowledge_base(prompt)
                response = get_answer(prompt, relevant_docs)
        
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})