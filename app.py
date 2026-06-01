import streamlit as st
import pandas as pd
import numpy as np

# Configuração da página para visual limpo e amplo
st.set_page_config(layout="wide", page_title="Painel de Performance Executivo")

# Título Principal com estilo limpo
st.markdown("<h2 style='text-align: center; color: #1E3A8A; font-weight: 700;'>🏆 PAINEL EXECUTIVO DE PERFORMANCE</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #6B7280;'>Campanha de Vendas — Sistema Estrito de Faixas Fixas</p>", unsafe_allow_html=True)
st.write("---")

# Base de dados oficial unificada com os 5 KPIs mapeados
data = {
    'COD': [80001, 80002, 80003, 80005, 80006, 80007, 80010, 80011, 80012, 80021, 80022, 80039, 80048, 80052, 80053, 80055, 80057, 80058, 80060, 80061],
    'Vendedor': [
        'Homologação', 'Carlos', 'Valdinei', 'Luiz', 'Wesley', 
        'Celio', 'Helio', 'Raimundo', 'Mauricio', 'Rota BH', 
        'Rota BH (Int)', 'Frederico', 'Flavio', 'Wanderson', 'Daniel', 
        'Mauricio Jr', 'Gilbert', 'Natalia', 'Janete', 'RPA'
    ],
    'Meta_Fat': [318880.0, 1171100.0, 1381200.0, 1136600.0, 1396000.0, 1658500.0, 751750.0, 1132500.0, 2315350.0, 2535200.0, 96000.0, 348750.0, 967250.0, 860500.0, 1293350.0, 664000.0, 90000.0, 479800.0, 331200.0, 241500.0],
    'Real_Fat': [254754.40, 1091928.00, 1232846.85, 970745.58, 1251693.40, 1590120.70, 687613.80, 932907.49, 2280576.70, 2471894.88, 66186.00, 79820.22, 830930.82, 806371.35, 988358.30, 667041.86, 6598.00, 395428.14, 182194.05, 113946.15],
    'Meta_Peso': [17000.0, 70000.0, 81000.0, 65000.0, 80000.0, 91000.0, 48500.0, 60000.0, 115500.0, 105000.0, 4000.0, 17500.0, 54500.0, 51500.0, 69500.0, 37500.0, 5000.0, 24000.0, 18000.0, 12000.0],
    'Real_Peso': [14180.0, 67825.0, 73275.0, 56720.0, 73149.0, 87924.0, 45028.0, 50418.0, 115611.5, 102832.0, 2825.0, 4203.0, 47402.0, 47751.0, 63168.0, 38206.0, 530.0, 19999.0, 9969.0, 5370.0],
    'Meta_PM': [18.76, 16.73, 17.05, 17.48, 17.45, 18.23, 15.50, 18.88, 20.05, 24.15, 24.00, 19.75, 17.75, 16.70, 18.60, 17.75, 18.00, 20.08, 18.40, 20.15],
    'Real_PM': [17.97, 16.10, 16.82, 17.11, 17.11, 18.09, 15.27, 18.50, 19.73, 24.04, 23.43, 18.99, 17.53, 16.89, 15.65, 17.46, 12.45, 19.77, 18.28, 21.22],
    'Meta_Pos': [13.0, 19.0, 54.0, 69.0, 46.0, 40.0, 34.0, 21.0, 13.0, 23.0, 17.0, 32.0, 21.0, 23.0, 71.0, 31.0, 5.0, 34.0, 31.0, 47.0],
    'Real_Pos': [11.0, 13.0, 45.0, 42.0, 46.0, 39.0, 30.0, 13.0, 24.0, 24.0, 16.0, 25.0, 17.0, 22.0, 65.0, 30.0, 2.0, 27.0, 17.0, 50.0],
    'Meta_Cad': [0.0, 12.0, 22.0, 20.0, 13.0, 17.0, 11.0, 4.0, 0.0, 3.0, 1.0, 40.0, 14.0, 30.0, 24.0, 6.0, 5.0, 25.0, 25.0, 5.0],
    'Real_Cad': [3.0, 2.0, 30.0, 11.0, 21.0, 9.0, 6.0, 1.0, 10.0, 5.0, 0.0, 19.0, 17.0, 11.0, 8.0, 2.0, 0.0, 38.0, 13.0, 9.0]
}

df = pd.DataFrame(data)

# Mapeando os códigos informados para a categoria "Rotas Especiais / Homologação"
codigos_filtrados = [80012, 80021, 80055, 80061, 80022, 80001, 80057]
df['Categoria'] = np.where(df['COD'].isin(codigos_filtrados), 'Rotas Especiais / Homologação', 'Vendedores Padrão')

# --- CONFIGURAÇÃO DO FILTRO NA BARRA LATERAL (SIDEBAR) ---
st.sidebar.header("⚙️ Filtros do Painel")
mostrar_especiais = st.sidebar.checkbox("Mostrar Rotas Especiais / Homologação", value=True)

# Aplicação do Filtro dinâmico na base de dados
if not mostrar_especiais:
    df = df[df['Categoria'] == 'Vendedores Padrão'].reset_index(drop=True)

# --- RECALCULANDO ATINGIMENTOS APÓS O FILTRO ---
df['At_Fat'] = (df['Real_Fat'] / df['Meta_Fat']) * 100
df['At_Peso'] = (df['Real_Peso'] / df['Meta_Peso']) * 100
df['At_PM'] = (df['Real_PM'] / df['Meta_PM']) * 100
df['At_Pos'] = (df['Real_Pos'] / df['Meta_Pos']) * 100

df['At_Cad'] = np.where(df['Meta_Cad'] == 0, np.where(df['Real_Cad'] > 0, 115.0, 0.0), (df['Real_Cad'] / df['Meta_Cad']) * 100)

def calcular_pontos_faixa(ating, pt90, pt100, pt110):
    if ating < 90.0: return 0.0
    elif ating < 100.0: return float(pt90)
    elif ating < 110.0: return float(pt100)
    else: return float(pt110)

df['P_Fat'] = df['At_Fat'].apply(lambda x: calcular_pontos_faixa(x, 5, 10, 15))
df['P_Peso'] = df['At_Peso'].apply(lambda x: calcular_pontos_faixa(x, 5, 10, 15))
df['P_PM'] = df['At_PM'].apply(lambda x: calcular_pontos_faixa(x, 10, 15, 20))
df['P_Pos'] = df['At_Pos'].apply(lambda x: calcular_pontos_faixa(x, 5, 7.5, 10))
df['P_Cad'] = df['At_Cad'].apply(lambda x: calcular_pontos_faixa(x, 5, 7.5, 10))

df['Pontuacao_Total'] = df['P_Fat'] + df['P_Peso'] + df['P_PM'] + df['P_Pos'] + df['P_Cad']

# Ordenação do Ranking baseado no filtro ativo
df_ranking = df.sort_values(by='Pontuacao_Total', ascending=False).reset_index(drop=True)

# Prevenção de erro caso o filtro zere a lista (muito raro)
if len(df_ranking) > 0:
    # Geração de Campeões por KPI para os cards superiores
    campeao_fat = df.loc[df['P_Fat'].idxmax()]['Vendedor'] if df['P_Fat'].max() > 0 else "Ninguém"
    campeao_peso = df.loc[df['P_Peso'].idxmax()]['Vendedor'] if df['P_Peso'].max() > 0 else "Ninguém"
    campeao_pm = df.loc[df['P_PM'].idxmax()]['Vendedor'] if df['P_PM'].max() > 0 else "Ninguém"
    campeao_pos = df.loc[df['P_Pos'].idxmax()]['Vendedor'] if df['P_Pos'].max() > 0 else "Ninguém"
    campeao_cad = df.loc[df['P_Cad'].idxmax()]['Vendedor'] if df['P_Cad'].max() > 0 else "Ninguém"

    # --- VISUAL: TOP 5 GERAL ---
    st.markdown("### 🏆 OS 5 MELHORES DA CLASSIFICAÇÃO GERAL")
    col_t1, col_t2, col_t3, col_t4, col_t5 = st.columns(5)

    # Função auxiliar para renderizar os cards do topo sem estourar índice
    def render_card(col, posicao, label, bg, border, text_color, dark_text):
        if len(df_ranking) > posicao:
            col.markdown(f"<div style='background-color:{bg}; padding:15px; border-radius:10px; border-left:5px solid {border}; text-align:center;'><b style='color:{text_color};'>{label}</b><br><span style='font-size:18px; font-weight:bold; color:{dark_text};'>{df_ranking.loc[posicao, 'Vendedor']}</span><br><b style='color:{dark_text};'>{df_ranking.loc[posicao, 'Pontuacao_Total']:.2f} pts</b></div>", unsafe_allow_html=True)
        else:
            col.markdown(f"<div style='background-color:#F3F4F6; padding:15px; border-radius:10px; text-align:center; color:#9CA3AF;'>Sem dados</div>", unsafe_allow_html=True)

    render_card(col_t1, 0, "🥇 1º Lugar", "#FEF3C7", "#F59E0B", "#B45309", "#78350F")
    render_card(col_t2, 1, "🥈 2º Lugar", "#E5E7EB", "#9CA3AF", "#4B5563", "#1F2937")
    render_card(col_t3, 2, "🥉 3º Lugar", "#FFEDD5", "#EA580C", "#C2410C", "#7C2D12")
    render_card(col_t4, 3, "🏅 4º Lugar", "#DBEAFE", "#3B82F6", "#1D4ED8", "#1E3A8A")
    render_card(col_t5, 4, "🏅 5º Lugar", "#EDE9FE", "#8B5CF6", "#6D28D9", "#4C1D95")

    st.write("---")

    # --- VISUAL: CAMPEÕES POR KPI ---
    st.markdown("### 🎖️ LÍDERES DESTACADOS POR INDICADOR (KPI)")
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("💰 Faturamento", f"{campeao_fat}", f"{df['P_Fat'].max():.2f} pts")
    col2.metric("📦 Peso (KG)", f"{campeao_peso}", f"{df['P_Peso'].max():.2f} pts")
    col3.metric("🎯 Preço Médio", f"{campeao_pm}", f"{df['P_PM'].max():.2f} pts")
    col4.metric("🤝 Positivação", f"{campeao_pos}", f"{df['P_Pos'].max():.2f} pts")
    col5.metric("📈 Novos Cadastros", f"{campeao_cad}", f"{df['P_Cad'].max():.2f} pts")

    st.write("---")

# --- TABELA INTERATIVA FORMATADA COM TODOS OS KPIS E PERCENTUAIS ---
st.markdown("### 📋 TABELA CONSOLIDADA — PONTUAÇÕES E PERCENTUAIS DE ATINGIMENTO")

df_exibir_base = df_ranking.copy()
if len(df_exibir_base) > 0:
    df_exibir_base.index += 1
    colunas_finais = ['COD', 'Vendedor', 'Pontuacao_Total', 'At_Fat', 'P_Fat', 'At_Peso', 'P_Peso', 'At_PM', 'P_PM', 'At_Pos', 'P_Pos', 'At_Cad', 'P_Cad']
    df_exibir = df_exibir_base[colunas_finais].copy()
    df_exibir.columns = ['CÓDIGO', 'VENDEDOR', 'PONTUAÇÃO TOTAL', 'FATURAMENTO (%)', 'PONTOS FAT.', 'PESO KG (%)', 'PONTOS PESO', 'PREÇO MÉDIO (%)', 'PONTOS P.M.', 'POSITIVAÇÃO (%)', 'PONTOS POSIT.', 'CADASTROS (%)', 'PONTOS CADASTROS']

    st.dataframe(
        df_exibir.style.format({
            'PONTUAÇÃO TOTAL': '{:.2f}', 
            'FATURAMENTO (%)': '{:.1f}%', 'PONTOS FAT.': '{:.1f}', 
            'PESO KG (%)': '{:.1f}%', 'PONTOS PESO': '{:.1f}', 
            'PREÇO MÉDIO (%)': '{:.1f}%', 'PONTOS P.M.': '{:.1f}', 
            'POSITIVAÇÃO (%)': '{:.1f}%', 'PONTOS POSIT.': '{:.1f}', 
            'CADASTROS (%)': '{:.1f}%', 'PONTOS CADASTROS': '{:.1f}'
        }), 
        use_container_width=True
    )
else:
    st.warning("Nenhum vendedor selecionado nos filtros.")
