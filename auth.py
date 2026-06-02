import streamlit as st

SENHA_CORRETA = "bacon"

def validar_senha():
    senha = st.session_state.get("senha", "")
    if senha != SENHA_CORRETA:
        st.error("Acesso negado. Volte à página inicial e digite a senha correta.")
        st.stop()
