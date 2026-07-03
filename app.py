import streamlit as st
from openai import OpenAI
import traceback

st.set_page_config(page_title="FAIZAL AI Proyek", page_icon="🚀", layout="wide")
st.title("🚀 FAIZAL AI Proyek - V1.0")
st.caption("Versi Tanpa Internet Dulu Biar Ijo")

with st.sidebar:
    api_key = st.text_input("OpenRouter API Key", type="password")
    model = st.selectbox("Pilih Otak AI", ["meta-llama/llama-3.1-8b-instruct:free", "google/gemini-flash-1.5", "openai/gpt-4o-mini"])
    if st.button("🗑️ Chat Baru", use_container_width=True): st.session_state.messages = []; st.rerun()

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "Kamu adalah FAIZAL AI. Jawab dalam Bahasa Indonesia."}]

if not api_key: st.warning("Masukkan API Key di sidebar dulu."); st.stop()
client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)

for msg in st.session_state.messages:
    if msg["role"] in ["user", "assistant"]: st.chat_message(msg["role"]).markdown(msg["content"])

if prompt := st.chat_input("Tanya apa saja..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)
    with st.chat_message("assistant"):
        message_placeholder = st.empty(); full_response = ""
        try:
            stream = client.chat.completions.create(model=model, messages=st.session_state.messages, stream=True)
            for chunk in stream: full_response += chunk.choices[0].delta.content or ""; message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
        except Exception as e:
            st.error(f"Error: {e}")
