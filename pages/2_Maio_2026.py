import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide", page_title="Maio/2026")
st.markdown("<h2 style='text-align: center; color: #1E3A8A; font-weight: 700;'>🏆 DESEMPENHO — MAIO / 2026</h2>", unsafe_allow_html=True)
st.write("---")

data_maio = {
    'COD': [80001, 80002, 80003, 80005, 80006, 80007, 80010, 80011, 80012, 80021, 80022, 80039, 80048, 80052, 80053, 80055, 80057, 80058, 80060, 80061, 80062],
    'Vendedor': ['Homologação', 'Carlos', 'Valdinei', 'Luiz', 'Wesley', 'Celio', 'Helio', 'Raimundo', 'Mauricio', 'Rota BH', 'Rota BH (Int)', 'Frederico', 'Flavio', 'Wanderson', 'Daniel', 'Mauricio Jr', 'Gilbert', 'Natalia', 'Janete', 'RPA', 'Tallison'],
    'Meta_Fat': [56400.0, 324000.0, 348500.0, 292400.0, 369800.0, 441000.0, 217000.0, 274500.0, 540000.0, 672000.0, 23500.0, 54900.0, 262500.0, 255000.0, 295200.0, 82500.0, 1.0, 110400.0, 92000.0, 63000.0, 36000.0],
    'Real_Fat': [54797.90, 272753.40, 310243.50, 240808.16, 303155.06, 390857.55, 183655.70, 241545.44, 510365.90, 623626.00, 13736.00, 16695.40, 219409.08, 181683.75, 280912.75, 138636.30, 0.0, 101987.20, 114774.59, 96810.70, 8610.50],
    'Meta_Peso': [3000.0, 20000.0, 20500.0, 17000.0, 21500.0, 24500.0, 14000.0, 15000.0, 30000.0, 28000.0, 1000.0, 3000.0, 15000.0, 15000.0, 18000.0, 5000.0, 1.0, 6000.0, 5000.0, 3000.0, 2000.0],
    'Real_Peso': [3445.0, 17060.0, 18759.0, 13981.0, 17932.0, 21625.0, 11940.0, 13015.0, 29167.0, 26045.0, 575.0, 927.0, 12512.0, 10990.0, 16940.0, 8891.0, 0.0, 5711.0, 6362.0, 4695.0, 615.0],
    'Meta_PM': [18.80, 16.20, 17.00, 17.20, 17.20, 18.00, 15.50, 18.30, 18.00, 24.00, 23.50, 18.30, 17.50, 17.00, 16.40, 16.50, 1.0, 18.40, 18.40, 21.00, 18.00],
    'Real_PM': [15.91, 15.99, 16.54, 17.22, 16.91, 18.07, 15.38, 18.56, 17.50, 23.94, 23.94, 18.01, 17.54, 16.53, 16.58, 15.59, 0.0, 17.86, 18.04, 20.62, 14.00],
    'Meta_Pos': [4.0, 145.0, 149.0, 125.0, 153.0, 135.0, 116.0, 75.0, 8.0, 120.0, 4.0, 40.0, 150.0, 95.0, 95.0, 10.0, 1.0, 55.0, 15.0, 35.0, 15.0],
    'Real_Pos': [4.0, 143.0, 144.0, 122.0, 142.0, 128.0, 113.0, 69.0, 9.0, 117.0, 4.0, 20.0, 143.0, 89.0, 83.0, 14.0, 0.0, 50.0, 12.0, 40.0, 9.0],
    'Meta_Cad': [0.0, 3.0, 2.0, 4.0, 2.0, 4.0, 8.0, 8.0, 0.0, 0.0, 0.0, 10.0, 2.0, 8.0, 8.0, 0.0, 1.0, 8.0, 5.0, 10.0, 10.0],
    'Real_Cad': [0.0, 3.0, 3.0, 1.0, 2.0, 0.0, 3.0, 1.0, 1.0, 1.0, 0.0, 4.0, 3.0, 0.0, 1.0, 0.0, 0.0, 8.0, 1.0, 13.0, 2.0]
}

df = pd.DataFrame(data_maio)
codigos_filtrados = [80012, 80021, 80055, 80061, 80022, 80001, 80057]
df['Categoria'] = np.where(df['COD'].isin(codigos_filtrados), 'Especiais', 'Padrao')

mostrar_especiais = st.sidebar.checkbox("Mostrar Rotas Especiais / Homologação", value=True)
if not mostrar_especiais:
    df = df[df['Categoria'] == 'Padrao'].reset_index(drop=True)

df['At_Fat'] = (df['Real_Fat'] / df['Meta_Fat']) * 100
df['At_Peso'] = (df['Real_Peso'] / df['Meta_Peso']) * 100
df['At_PM'] = (df['Real_PM'] / df['Meta_PM']) * 100
df['At_Pos'] = (df['Real_Pos'] / df['Meta_Pos']) * 100
df['At_Cad'] = np.where(df['Meta_Cad'] <= 1.0, np.where(df['Real_Cad'] > 0, 115.0, 0.0), (df['Real_Cad'] / df['Meta_Cad']) * 100)

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
df_ranking = df.sort_values(by='Pontuacao_Total', ascending=False).reset_index(drop=True)

if len(df_ranking) > 0:
    col_t1, col_t2, col_t3, col_t4, col_t5 = st.columns(5)
    col_t1.metric(label="🥇 1º LUGAR", value=df_ranking.loc[0, 'Vendedor'], delta=f"{df_ranking.loc[0, 'Pontuacao_Total']:.2f} pts")
    if len(df_ranking) > 1: col_t2.metric(label="🥈 2º LUGAR", value=df_ranking.loc[1, 'Vendedor'], delta=f"{df_ranking.loc[1, 'Pontuacao_Total']:.2f} pts")
    if len(df_ranking) > 2: col_t3.metric(label="🥉 3º LUGAR", value=df_ranking.loc[2, 'Vendedor'], delta=f"{df_ranking.loc[2, 'Pontuacao_Total']:.2f} pts")
    if len(df_ranking) > 3: col_t4.metric(label="🏅 4º LUGAR", value=df_ranking.loc[3, 'Vendedor'], delta=f"{df_ranking.loc[3, 'Pontuacao_Total']:.2f} pts")
    if len(df_ranking) > 4: col_t5.metric(label="🏅 5º LUGAR", value=df_ranking.loc[4, 'Vendedor'], delta=f"{df_ranking.loc[4, 'Pontuacao_Total']:.2f} pts")
    st.write("---")

df_ranking.index += 1
st.markdown("### 📋 TABELA DE PONTOS POR KPI")
st.dataframe(df_ranking[['COD', 'Vendedor', 'Pontuacao_Total', 'P_Fat', 'P_Peso', 'P_PM', 'P_Pos', 'P_Cad']].rename(columns={'Pontuacao_Total': 'PONTUAÇÃO TOTAL'}), use_container_width=True)
st.write("---")
st.markdown("### 📊 PERCENTUAIS DE ATINGIMENTO METAS (%)")
st.dataframe(df_ranking[['COD', 'Vendedor', 'At_Fat', 'At_Peso', 'At_PM', 'At_Pos', 'At_Cad']].style.format({'At_Fat': '{:.1f}%', 'At_Peso': '{:.1f}%', 'At_PM': '{:.1f}%', 'At_Pos': '{:.1f}%', 'At_Cad': '{:.1f}%'}), use_container_width=True)
