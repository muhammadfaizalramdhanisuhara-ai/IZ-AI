import streamlit as st
import os
from openai import OpenAI

st.set_page_config(page_title="FAIZAL AI", page_icon="🤖")
st.title("FAIZAL AI Proyek")

# 1. AMBIL API KEY DARI RAILWAY VARIABLES OTOMATIS
api_key = os.getenv("OPENAI_API_KEY") 

# 2. KALO KEY KOSONG LANGSUNG STOP + KASIH TAU
if not api_key:
    st.error("❌ OPENAI_API_KEY belum diset di Railway Variables")
    st.stop()

# 3. BIKIN CLIENT OPENROUTER
client = OpenAI(
    base_url="https://openrouter.ai/api/v1", 
    api_key=api_key
)

# 4. KOTAK CHAT
if prompt := st.chat_input("Tanya apa saja..."):
    with st.chat_message("user"):
        st.markdown(prompt)
        
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model="meta-llama/llama-3.1-8b-instruct:free",
            messages=[{"role": "user", "content": prompt}],
            stream=True,
        )
        st.write_stream(stream)
