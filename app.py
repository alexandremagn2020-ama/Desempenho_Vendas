import streamlit as st

SENHA_CORRETA = "minha_senha_secreta"

# Se ainda não existe a chave "autenticado", cria como False
if "autenticado" not in st.session_state:
    st.session_state["autenticado"] = False

# Se não estiver autenticado, mostra campo de senha
if not st.session_state["autenticado"]:
    senha = st.text_input("Digite a senha:", type="password")
    if senha == SENHA_CORRETA:
        st.session_state["autenticado"] = True
        st.success("✅ Bem-vindo ao portal!")
    else:
        st.stop()

# Se autenticado, carrega o painel
st.set_page_config(layout="wide", page_title="Portal de Performance")
st.markdown("## 🎯 PORTAL DE CAMPANHAS DE VENDAS")
st.info("💡 Use o menu lateral para navegar entre o **1º Quadrimestre** e **Maio/2026**.")
