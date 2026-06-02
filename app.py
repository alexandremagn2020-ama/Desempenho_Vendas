import streamlit as st

# 🔐 Defina sua senha aqui
SENHA_CORRETA = "minha_senha_secreta"

# Captura parâmetros da URL
params = st.query_params
senha = params.get("senha", "")

# Validação
if senha != SENHA_CORRETA:
    st.error("Acesso negado. Informe a senha correta na URL.")
    st.stop()

# ✅ Se passou na validação, carrega o painel
st.set_page_config(layout="wide", page_title="Portal de Performance")

st.markdown("<h2 style='text-align: center; color: #1E3A8A; font-weight: 700;'>🎯 PORTAL DE CAMPANHAS DE VENDAS</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #6B7280;'>Bem-vindo ao sistema de apuração corporativo.</p>", unsafe_allow_html=True)
st.write("---")

st.info("💡 Use o menu lateral para navegar entre o **1º Quadrimestre** e **Maio/2026**.")
