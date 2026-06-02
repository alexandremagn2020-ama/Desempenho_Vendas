import streamlit as st

# Tela inicial de login
senha = st.text_input("Digite a senha:", type="password", key="senha")

if senha != "minha_senha_secreta":
    st.warning("Senha incorreta ou não informada.")
    st.stop()

st.set_page_config(layout="wide", page_title="Portal de Performance")

st.markdown("<h2 style='text-align: center; color: #1E3A8A;'>🎯 PORTAL DE CAMPANHAS DE VENDAS</h2>", unsafe_allow_html=True)
st.info("💡 Use o menu lateral para navegar entre o **1º Quadrimestre** e **Maio/2026**.")
