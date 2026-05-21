import os
import streamlit as st
from groq import Groq
import PyPDF2
import docx

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_docx(file):
    doc = docx.Document(file)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

def analyze_resume(resume_text, job_description):
    prompt = f"""
    Analyze this resume against the job description and provide:
    1. List of skills found in resume
    2. Required skills from job description
    3. Match percentage (0-100%)
    4. Missing skills
    5. Short recommendation
    
    Resume:
    {resume_text}
    
    Job Description:
    {job_description}
    
    Respond in this exact format:
    SKILLS FOUND: [list skills]
    REQUIRED SKILLS: [list skills]
    MATCH PERCENTAGE: [number]%
    MISSING SKILLS: [list skills]
    RECOMMENDATION: [short text]
    """
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000
    )
    return response.choices[0].message.content

# Streamlit UI
st.title(" Resume Screener AI")
st.caption("Powered by Groq AI — Nexe-Agent Internship")

col1, col2 = st.columns(2)

with col1:
    st.subheader(" Upload Resume")
    uploaded_file = st.file_uploader("Upload PDF or DOCX", type=["pdf", "docx"])

with col2:
    st.subheader(" Job Description")
    job_desc = st.text_area("Paste job description here...", height=200)

if uploaded_file and job_desc:
    if st.button(" Analyze Resume", type="primary"):
        with st.spinner("Analyzing resume..."):
            if uploaded_file.name.endswith(".pdf"):
                resume_text = extract_text_from_pdf(uploaded_file)
            else:
                resume_text = extract_text_from_docx(uploaded_file)
            
            result = analyze_resume(resume_text, job_desc)
            
            lines = result.split('\n')
            for line in lines:
                if "MATCH PERCENTAGE:" in line:
                    percentage = line.split(":")[1].strip()
                    st.metric(" Match Score", percentage)
                elif "SKILLS FOUND:" in line:
                    st.success(line)
                elif "MISSING SKILLS:" in line:
                    st.error(line)
                elif "RECOMMENDATION:" in line:
                    st.info(line)
                elif line.strip():
                    st.write(line)
else:
    st.info(" Please upload a resume AND enter a job description to start!")
