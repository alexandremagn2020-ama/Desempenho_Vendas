import streamlit as st

def validar_senha():
    if not st.session_state.get("autenticado", False):
        st.error("Acesso negado. Volte à página inicial e digite a senha correta.")
        st.stop()
