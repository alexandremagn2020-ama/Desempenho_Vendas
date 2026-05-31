import streamlit as st
import pandas as pd
import numpy as np

# Configuração da página para aproveitar toda a largura da tela
st.set_page_config(layout="wide", page_title="Dashboard de Performance")
st.title("📊 Painel de Performance - Campanha de Vendas")

# Base de dados com os Primeiros Nomes dos vendedores
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
    'Meta_Pos': [110, 132, 132, 132, 132, 132, 110, 132, 132, 44, 44, 44, 110, 110, 110, 110, 44, 110, 110, 22],
    'Real_Pos': [81, 137, 139, 101, 140, 142, 111, 109, 112, 14, 5, 1, 115, 126, 118, 111, 0, 77, 45, 3],
    'Meta_Cad': [5, 10, 10, 10, 10, 10, 5, 10, 10, 2, 2, 2, 5, 5, 5, 5, 2, 5, 5, 1],
    'Real_Cad': [0, 1, 10, 0, 10, 4, 4, 0, 0, 0, 0, 0, 5, 3, 4, 0, 0, 0, 0, 0]
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

# Encontrar os campeões de cada KPI específico
campeao_geral = df_ranking.iloc[0]
campeao_fat = df.loc[df['P_Fat'].idxmax()]
campeao_peso = df.loc[df['P_Peso'].idxmax()]
campeao_pm = df.loc[df['P_PM'].idxmax()]
campeao_pos = df.loc[df['P_Pos'].idxmax()]
campeao_cad = df.loc[df['P_Cad'].idxmax()]

# --- ÁREA VISUAL DO DASHBOARD ---

# Bloco 1: Destaque do Campeão Geral
st.markdown("### 🥇 Classificação Máxima")
st.metric(
    label="🏆 CAMPEÃO GERAL DA CAMPANHA", 
    value=f"{campeao_geral['Vendedor']}", 
    delta=f"{campeao_geral['Pontuacao_Total']:.2f} pts Acumulados"
)

st.write("---")

# Bloco 2: Líderes por Categoria (Dividido em 5 colunas lado a lado)
st.markdown("### 🎖️ Líderes por Indicador (KPI)")
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("💰 Faturamento", f"{campeao_fat['Vendedor']}", f"{campeao_fat['P_Fat']:.2f} pts")
col2.metric("📦 Peso (KG)", f"{campeao_peso['Vendedor']}", f"{campeao_peso['P_Peso']:.2f} pts")
col3.metric("🎯 Preço Médio", f"{campeao_pm['Vendedor']}", f"{campeao_pm['P_PM']:.2f} pts")
col4.metric("🤝 Positivação", f"{campeao_pos['Vendedor']}", f"{campeao_pos['P_Pos']:.2f} pts")
col5.metric("📈 Novos Cadastros", f"{campeao_cad['Vendedor']}", f"{campeao_cad['P_Cad']:.2f} pts")

st.write("---")

# Bloco 3: Tabela Oficial de Classificação
st.subheader("📋 Tabela Consolidada do Ranking")
colunas_exibicao = ['COD', 'Vendedor', 'Pontuacao_Total', 'P_Fat', 'P_Peso', 'P_PM', 'P_Pos', 'P_Cad']
st.dataframe(
    df_ranking[colunas_exibicao].style.format({
        'Pontuacao_Total': '{:.2f}', 
        'P_Fat': '{:.2f}', 
        'P_Peso': '{:.2f}', 
        'P_PM': '{:.2f}', 
        'P_Pos': '{:.2f}', 
        'P_Cad': '{:.2f}'
    }), 
    use_container_width=True
)

# Bloco 4: Gráfico de Performance
st.subheader("📊 Comparativo Gráfico de Pontos")
st.bar_chart(data=df_ranking, x='Vendedor', y='Pontuacao_Total')
