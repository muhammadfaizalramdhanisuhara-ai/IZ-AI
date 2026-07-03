import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="FAIZAL AI", page_icon="🚀")
st.title("🚀 FAIZAL AI Proyek")

with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Masukkan API Key OpenRouter", type="password")

# INI PENGAMANNYA BRO 👇
if not api_key:
    st.warning("⚠️ Masukkan API Key di sidebar dulu baru bisa chat.")
    st.stop() # Stop disini, jadi gak lanjut ke client

client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Tanya apa saja..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Mikir..."):
            stream = client.chat.completions.create(
                model="meta-llama/llama-3.1-8b-instruct:free",
                messages=st.session_state.messages,
                stream=True,
            )
            response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
