
import streamlit as st
from agent_core import run_agent

st.set_page_config(page_title="Cosmo AI Agent", layout="wide")

st.title("🤖 Cosmo AI Agent Dashboard")
user_input = st.text_input("💬 Nhập câu hỏi:")

if user_input:
    with st.spinner("Đang xử lý..."):
        result = run_agent(user_input)
        st.success(result)
