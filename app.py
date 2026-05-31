import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide", page_title="Campanha Anual Stiva")
st.title("🏆 Ranking de Performance - Campanha de Vendas Stiva")

# Base completa unificada com dados de Metas e Realizados
data = {
    'COD': [80001, 80002, 80003, 80005, 80006, 80007, 80010, 80011, 80012, 80021, 80022, 80039, 80048, 80052, 80053, 80055, 80057, 80058, 80060, 80061],
    'Vendedor': ['VENDEDOR PARA HOMOLOGAÇÃO', 'CARLOS EDUARDO PEREIRA DA CRUZ', 'VALDINEI LUIZ PAIVA', 'LUIZ CARLOS SILVA NEVES', 'WESLEY FRANCIS DE JESUS LOPES', 'CELIO CLAUDIO OLIVEIRA', 'HELIO ALMEIDA VIANA', 'RAIMUNDO ALEX BARBOSA', 'MAURICIO SIMÕES JORGE', 'ROTA BH', 'ROTA BH - INTERIOR DE MINAS', 'FREDERICO', 'FLAVIO CRISTIANO CARDOSO', 'WANDERSON DA SILVA LIMA', 'DANIEL DE PAULA', 'MAURICIO MARQUES DA SILVA JUNIOR', 'GILBERT CRISTIAN', 'NATALIA FATIMA', 'JANETE CIRILO', 'RPA'],
    'Meta_Fat': [318880.0, 1171100.0, 1381200.0, 1136600.0, 1396000.0, 1658500.0, 751750.0, 1132500.0, 2315350.0, 2535200.0, 96000.0, 348750.0, 967250.0, 860500.0, 1293350.0, 664000.0, 90000.0, 479800.0, 331200.0, 241500.0],
    'Real_Fat': [254754.40, 1091928.00, 1232846.85, 970745.58, 1251693.40, 1590120.70, 687613.80, 932907.49, 2280576.70, 2471894.88, 66186.00, 79820.22, 830930.82, 806371.35, 988358.30, 667041.86, 6598.00, 395428.14, 182194.05, 113946.15],
    'Meta_Peso': [17000.0, 70000.0, 81000.0, 65000.0, 80000.0, 91000.0, 48500.0, 60000.0, 115500.0, 105000.0, 4000.0, 17500.0, 54500.0, 51500.0, 69500.0, 37500.0, 5000.0, 24000.0, 18000.0, 12000.0],
    'Real_Peso': [14180.0, 67825.0, 73275.0, 56720.0, 73149.0, 87924.0, 45028.0, 50418.0, 115611.5, 102832.0, 2825.0, 4203.0, 47402.0, 47751.0, 63168.0, 38206.0, 530.0, 19999.0, 9969.0, 5370.0],
    'Meta_PM': [18.76, 16.73, 17.05, 17.48, 17.45, 18.23, 15.50, 18.88, 20.05, 24.15, 24.00, 19.75, 17.75, 16.70, 18.60, 17.75, 18.00, 20.08, 18.40, 20.15],
    'Real_PM': [17.97, 16.10, 16.82, 17.11, 17.11, 18.09, 15.27, 18.50, 19.73, 24.04, 23.43, 18.99, 17.53, 16.89, 15.65, 17.46, 12.45, 19.77, 18.28, 21.22],
    'Meta_Pos': [20, 563, 578, 494, 592, 525, 444, 286, 39, 439, 17, 105, 552, 370, 366, 63, 5, 180, 42, 47],
    'Real_Pos': [4, 143, 145, 122, 148, 128, 113, 70, 18, 115, 4, 21, 147, 89, 84, 15, 1, 36, 6, 13],
    'Meta_Cad': [0, 12, 11, 20, 13, 17, 33, 40, 0, 6, 1, 40, 14, 30, 30, 3, 5, 25, 25, 10],
    'Real_Cad': [0, 2, 15, 11, 21, 9, 18, 10, 10, 10, 0, 19, 17, 11, 10, 1, 0, 38, 13, 18]
}

df = pd.DataFrame(data)

# Cálculo de Atingimento por KPI
df['At_Fat'] = df['Real_Fat'] / df['Meta_Fat']
df['At_Peso'] = df['Real_Peso'] / df['Meta_Peso']
df['At_PM'] = df['Real_PM'] / df['Meta_PM']
df['At_Pos'] = np.where(df['Meta_Pos'] == 0, 1.0, df['Real_Pos'] / df['Meta_Pos'])
df['At_Cad'] = np.where(df['Meta_Cad'] == 0, np.where(df['Real_Cad'] > 0, 1.1, 1.0), df['Real_Cad'] / df['Meta_Cad'])

# Função para conversão linear de pontos por faixas
def calcular_pontos(ating, p90, p100, p110):
    if ating < 0.90: return 0.0
    elif ating <= 1.00: return p90 + ((ating - 0.90) / 0.10) * (p100 - p90)
    else: return p100 + ((ating - 1.00) / 0.10) * (p110 - p100)

# Aplicação das regras individuais de pontos
df['P_Fat'] = df['At_Fat'].apply(lambda x: calcular_pontos(x, 5, 10, 15))
df['P_Peso'] = df['At_Peso'].apply(lambda x: calcular_pontos(x, 5, 10, 15))
df['P_PM'] = df['At_PM'].apply(lambda x: calcular_pontos(x, 10, 15, 20))
df['P_Pos'] = df['At_Pos'].apply(lambda x: calcular_pontos(x, 5, 7.5, 10))
df['P_Cad'] = df['At_Cad'].apply(lambda x: calcular_pontos(x, 5, 7.5, 10))

# Pontuação Total Unificada
df['Pontuacao_Total'] = df['P_Fat'] + df['P_Peso'] + df['P_PM'] + df['P_Pos'] + df['P_Cad']

# Ordenação do Ranking Geral
df_ranking = df.sort_values(by='Pontuacao_Total', ascending=False).reset_index(drop=True)
df_ranking.index += 1

# Blocos visuais do Streamlit
col1, col2 = st.columns(2)
col1.metric("🏆 Líder Atual da Campanha", f"{df_ranking.iloc[0]['Vendedor']}", f"{df_ranking.iloc[0]['Pontuacao_Total']:.2f} pts")
col2.metric("🎯 Melhor Preço Médio", f"{df_ranking.loc[df_ranking['P_PM'].idxmax()]['Vendedor']}")

st.subheader("📋 Tabela Consolidada de Classificação")
colunas_exibicao = ['COD', 'Vendedor', 'Pontuacao_Total', 'P_Fat', 'P_Peso', 'P_PM', 'P_Pos', 'P_Cad']
st.dataframe(df_ranking[colunas_exibicao].style.format({'Pontuacao_Total': '{:.2f}', 'P_Fat': '{:.2f}', 'P_Sub_Peso': '{:.2f}', 'P_PM': '{:.2f}', 'P_Pos': '{:.2f}', 'P_Cad': '{:.2f}'}), use_container_width=True)

st.subheader("📊 Performance Visual Gráfica")
st.bar_chart(data=df_ranking, x='Vendedor', y='Pontuacao_Total')

