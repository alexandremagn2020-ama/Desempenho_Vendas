import streamlit as st

SENHA_CORRETA = "minha_senha_secreta"

# Campo de senha com chave fixa
senha = st.text_input("Digite a senha:", type="password", key="senha")

if senha != SENHA_CORRETA:
    st.warning("Senha incorreta ou não informada.")
    st.stop()

st.set_page_config(layout="wide", page_title="Portal de Performance")
st.success("✅ Bem-vindo ao painel!")
