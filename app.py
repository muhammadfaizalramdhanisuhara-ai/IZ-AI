import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Proyek AI FAIZAL", page_icon="🚀", layout="wide")
st.title("🚀 FAIZAL AI Proyek - V1.0")
st.caption("Versi Tanpa Internet Dulu Biar Ijo")

with st.sidebar:
    api_key = st.text_input("Masukkan API Key OpenRouter", type="password")
    model = st.selectbox("Pilih Otak AI", ["meta-llama/llama-3.1-8b-instruct:free"])
    if st.button("Obrolan Baru", use_container_width=True):
        st.session_state.messages = []

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "Kamu adalah FAIZAL AI. Jawab dalam Bahasa Indonesia."}]

if not api_key:
    st.warning("Masukkan API Key di sidebar dulu.")
    st.stop()

client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)

for pesan in st.session_state.messages:
    if pesan["role"] != "system":
        with st.chat_message(pesan["role"]):
            st.markdown(pesan["content"])

if prompt := st.chat_input("Tanya apa saja..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("FAIZAL AI mikir..."):
            stream = client.chat.completions.create(
                model=model,
                messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
                stream=True,
            )
            response = st.write_stream(stream)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
