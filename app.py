import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="FAIZAL AI", page_icon="🚀")
st.title("🚀 FAIZAL AI Proyek")

with st.sidebar:
    api_key = st.text_input("Masukkan API Key OpenRouter", type="password")

if not api_key: # <-- TUGAS DIA: NGE-BLOCK KALO KEY KOSONG
    st.info("👈 Masukkan API Key di sidebar dulu ya")
    st.stop() # <-- BERHENTI DISINI. GAK LANJUT KE BAWAH
   
client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key) # <-- AMAN, KARENA DI BAWAH

if prompt := st.chat_input("Tanya apa saja..."):
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model="meta-llama/llama-3.1-8b-instruct:free",
            messages=[{"role": "user", "content": prompt}], stream=True,
        )
        st.write_stream(stream)
