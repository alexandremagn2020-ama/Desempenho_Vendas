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
    'COD':,
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
    'Meta_Pos':,
    'Real_Pos':,
    'Meta_Cad':,
    'Real_Cad':
}

df = pd.DataFrame(data)

# Cálculos exatos de atingimento %
df['At_Fat'] = df['Real_Fat'] / df['Meta_Fat']
df['At_Peso'] = df['Real_Peso'] / df['Meta_Peso']
df['At_PM'] = df['Real_PM'] / df['Meta_PM']
df['At_Pos'] = df['Real_Pos'] / df['Meta_Pos']

# Regra especial para Cadastros: se a meta for zero e houver realizado, ganha o teto de bônus
df['At_Cad'] = np.where(df['Meta_Cad'] == 0, np.where(df['Real_Cad'] > 0, 1.15, 0.0), df['Real_Cad'] / df['Meta_Cad'])

# Função de Degraus Rígidos da Campanha
def calcular_pontos_faixa(ating, pt90, pt100, pt110):
    if ating < 0.90: return 0.0
    elif ating < 1.00: return float(pt90)
    elif ating < 1.10: return float(pt100)
    else: return float(pt110)

df['P_Fat'] = df['At_Fat'].apply(lambda x: calcular_pontos_faixa(x, 5, 10, 15))
df['P_Peso'] = df['At_Peso'].apply(lambda x: calcular_pontos_faixa(x, 5, 10, 15))
df['P_PM'] = df['At_PM'].apply(lambda x: calcular_pontos_faixa(x, 10, 15, 20))
df['P_Pos'] = df['At_Pos'].apply(lambda x: calcular_pontos_faixa(x, 5, 7.5, 10))
df['P_Cad'] = df['At_Cad'].apply(lambda x: calcular_pontos_faixa(x, 5, 7.5, 10))

# Soma unificada de todos os 5 KPIs
df['Pontuacao_Total'] = df['P_Fat'] + df['P_Peso'] + df['P_PM'] + df['P_Pos'] + df['P_Cad']

# Ordenação do Ranking Geral (O índice vira 0 a 19 internamente)
df_ranking = df.sort_values(by='Pontuacao_Total', ascending=False).reset_index(drop=True)

# Geração de Campeões por KPI para os cards superiores
campeao_fat = df.loc[df['P_Fat'].idxmax()]['Vendedor'] if df['P_Fat'].max() > 0 else "Ninguém"
campeao_peso = df.loc[df['P_Peso'].idxmax()]['Vendedor'] if df['P_Peso'].max() > 0 else "Ninguém"
campeao_pm = df.loc[df['P_PM'].idxmax()]['Vendedor'] if df['P_PM'].max() > 0 else "Ninguém"
campeao_pos = df.loc[df['P_Pos'].idxmax()]['Vendedor'] if df['P_Pos'].max() > 0 else "Ninguém"
campeao_cad = df.loc[df['P_Cad'].idxmax()]['Vendedor'] if df['P_Cad'].max() > 0 else "Ninguém"

# --- VISUAL: TOP 5 GERAL (Correção aplicada aqui) ---
st.markdown("### 🏆 OS 5 MELHORES DA CLASSIFICAÇÃO GERAL")
col_t1, col_t2, col_t3, col_t4, col_t5 = st.columns(5)

col_t1.markdown(f"<div style='background-color:#FEF3C7; padding:15px; border-radius:10px; border-left:5px solid #F59E0B; text-align:center;'><b>🥇 1º Lugar</b><br><span style='font-size:20px; font-weight:bold; color:#B45309;'>{df_ranking.loc[0, 'Vendedor']}</span><br><small>{df_ranking.loc[0, 'Pontuacao_Total']:.2f} pts</small></div>", unsafe_allow_html=True)
col_t2.markdown(f"<div style='background-color:#F3F4F6; padding:15px; border-radius:10px; border-left:5px solid #9CA3AF; text-align:center;'><b>🥈 2º Lugar</b><br><span style='font-size:18px; font-weight:bold; color:#4B5563;'>{df_ranking.loc[1, 'Vendedor']}</span><br><small>{df_ranking.loc[1, 'Pontuacao_Total']:.2f} pts</small></div>", unsafe_allow_html=True)
col_t3.markdown(f"<div style='background-color:#FFEDD5; padding:15px; border-radius:10px; border-left:5px solid #EA580C; text-align:center;'><b>🥉 3º Lugar</b><br><span style='font-size:18px; font-weight:bold; color:#C2410C;'>{df_ranking.loc[2, 'Vendedor']}</span><br><small>{df_ranking.loc[2, 'Pontuacao_Total']:.2f} pts</small></div>", unsafe_allow_html=True)
col_t4.markdown(f"<div style='background-color:#EFF6FF; padding:15px; border-radius:10px; border-left:5px solid #3B82F6; text-align:center;'><b>🏅 4º Lugar</b><br><span style='font-size:16px; font-weight:bold; color:#1D4ED8;'>{df_ranking.loc[3, 'Vendedor']}</span><br><small>{df_ranking.loc[3, 'Pontuacao_Total']:.2f} pts</small></div>", unsafe_allow_html=True)
col_t5.markdown(f"<div style='background-color:#F5F3FF; padding:15px; border-radius:10px; border-left:5px solid #8B5CF6; text-align:center;'><b>🏅 5º Lugar</b><br><span style='font-size:16px; font-weight:bold; color:#6D28D9;'>{df_ranking.loc[4, 'Vendedor']}</span><br><small>{df_ranking.loc[4, 'Pontuacao_Total']:.2f} pts</small></div>", unsafe_allow_html=True)

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

# --- TABELA INTERATIVA FORMATADA COM TODOS OS 5 KPIS ---
st.markdown("### 📋 TABELA CONSOLIDADA DE CLASSIFICAÇÃO GERAL")

# Ajustar o índice para começar visualmente em 1º na tabela
df_exibir_base = df_ranking.copy()
df_exibir_base.index += 1

df_exibir = df_exibir_base[['COD', 'Vendedor', 'Pontuacao_Total', 'P_Fat', 'P_Peso', 'P_PM', 'P_Pos', 'P_Cad']].copy()
df_exibir.columns = ['CÓDIGO', 'VENDEDOR', 'PONTUAÇÃO TOTAL', 'PONTOS FAT.', 'PONTOS PESO', 'PONTOS P.M.', 'PONTOS POSIT.', 'PONTOS CADASTROS']

st.dataframe(
    df_exibir.style.format({
        'PONTUAÇÃO TOTAL': '{:.2f}', 'PONTOS FAT.': '{:.2f}', 'PONTOS PESO': '{:.2f}', 
        'PONTOS P.M.': '{:.2f}', 'PONTOS POSIT.': '{:.2f}', 'PONTOS CADASTROS': '{:.2f}'
    }).bar(subset=['PONTUAÇÃO TOTAL'], color='#93C5FD', vmin=0, vmax=70),
    use_container_width=True
)

)

