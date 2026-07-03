import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="FAIZAL AI", page_icon="🤖")
st.title("🤖 FAIZAL AI - Proyek Terbesarmu")

# API Key gratis dari OpenRouter atau Gemini
api_key = st.text_input("Masukkan API Key kamu:", type="password")

if api_key:
    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)

    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Halo, aku FAIZAL AI. Mau tanya apa?"}]

    for message in st.session_state.messages:
        st.chat_message(message["role"]).write(message["content"])

    if prompt := st.chat_input("Tanya apa aja..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        with st.chat_message("assistant"):
            response = client.chat.completions.create(
                model="meta-llama/llama-3.1-8b-instruct:free",
                messages=st.session_state.messages
            )
            reply = response.choices[0].message.content
            st.write(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})
