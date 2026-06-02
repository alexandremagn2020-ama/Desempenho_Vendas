import streamlit as st
import pandas as pd
import numpy as np

# Configuração de página corporativa ampla
st.set_page_config(layout="wide", page_title="Painel de Performance Executivo")

# Título Principal Estilizado
st.markdown("<h2 style='text-align: center; color: #1E3A8A; font-weight: 700;'>🏆 PAINEL EXECUTIVO DE PERFORMANCE</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #6B7280;'>Campanha de Vendas — Pódio Geral Fixo e Tabelas por Período</p>", unsafe_allow_html=True)
st.write("---")

# -------------------------------------------------------------------------
# 1. BASES DE DADOS ORIGINAIS SINCRONIZADAS
# -------------------------------------------------------------------------

data_quad = {
    'COD': [80001, 80002, 80003, 80005, 80006, 80007, 80010, 80011, 80012, 80021, 80022, 80039, 80048, 80052, 80053, 80055, 80057, 80058, 80060, 80061, 80062],
    'Vendedor': ['Homologação', 'Carlos', 'Valdinei', 'Luiz', 'Wesley', 'Celio', 'Helio', 'Raimundo', 'Mauricio', 'Rota BH', 'Rota BH (Int)', 'Frederico', 'Flavio', 'Wanderson', 'Daniel', 'Mauricio Jr', 'Gilbert', 'Natalia', 'Janete', 'RPA', 'Tallison'],
    'Meta_Fat': [318880.0, 1171100.0, 1381200.0, 1136600.0, 1396000.0, 1658500.0, 751750.0, 1132500.0, 2315350.0, 2535200.0, 96000.0, 348750.0, 967250.0, 860500.0, 1293350.0, 664000.0, 90000.0, 479800.0, 331200.0, 241500.0, 1.0],
    'Real_Fat': [254754.40, 1091928.00, 1232846.85, 970745.58, 1251693.40, 1590120.70, 687613.80, 932907.49, 2280576.70, 2471894.88, 66186.00, 79820.22, 830930.82, 806371.35, 988358.30, 667041.86, 6598.00, 395428.14, 182194.05, 113946.15, 0.0],
    'Meta_Peso': [17000.0, 70000.0, 81000.0, 65000.0, 80000.0, 91000.0, 48500.0, 60000.0, 115500.0, 105000.0, 4000.0, 17500.0, 54500.0, 51500.0, 69500.0, 37500.0, 5000.0, 24000.0, 18000.0, 12000.0, 1.0],
    'Real_Peso': [14180.0, 67825.0, 73275.0, 56720.0, 73149.0, 87924.0, 45028.0, 50418.0, 115611.5, 102832.0, 2825.0, 4203.0, 47402.0, 47751.0, 63168.0, 38206.0, 530.0, 19999.0, 9969.0, 5370.0, 0.0],
    'Meta_PM': [18.76, 16.73, 17.05, 17.48, 17.45, 18.23, 15.50, 18.88, 20.05, 24.15, 24.00, 19.75, 17.75, 16.70, 18.60, 17.75, 18.00, 20.08, 18.40, 20.15, 1.0],
    'Real_PM': [17.97, 16.10, 16.82, 17.11, 17.11, 18.09, 15.27, 18.50, 19.73, 24.04, 23.43, 18.99, 17.53, 16.89, 15.65, 17.46, 12.45, 19.77, 18.28, 21.22, 0.0],
    'Meta_Pos': [13.0, 19.0, 54.0, 69.0, 46.0, 40.0, 34.0, 21.0, 13.0, 23.0, 17.0, 32.0, 21.0, 23.0, 71.0, 31.0, 5.0, 34.0, 31.0, 47.0, 1.0],
    'Real_Pos': [11.0, 13.0, 45.0, 42.0, 46.0, 39.0, 30.0, 13.0, 24.0, 24.0, 16.0, 25.0, 17.0, 22.0, 65.0, 30.0, 2.0, 27.0, 17.0, 50.0, 0.0],
    'Meta_Cad': [0.0, 12.0, 22.0, 20.0, 13.0, 17.0, 11.0, 4.0, 0.0, 3.0, 1.0, 40.0, 14.0, 30.0, 24.0, 6.0, 5.0, 25.0, 25.0, 5.0, 1.0],
    'Real_Cad': [3.0, 2.0, 30.0, 11.0, 21.0, 9.0, 6.0, 1.0, 10.0, 5.0, 0.0, 19.0, 17.0, 11.0, 8.0, 2.0, 0.0, 38.0, 13.0, 9.0, 0.0]
}

data_maio = {
    'COD': [80001, 80002, 80003, 80005, 80006, 80007, 80010, 80011, 80012, 80021, 80022, 80039, 80048, 80052, 80053, 80055, 80057, 80058, 80060, 80061, 80062],
    'Vendedor': ['Homologação', 'Carlos', 'Valdinei', 'Luiz', 'Wesley', 'Celio', 'Helio', 'Raimundo', 'Mauricio', 'Rota BH', 'Rota BH (Int)', 'Frederico', 'Flavio', 'Wanderson', 'Daniel', 'Mauricio Jr', 'Gilbert', 'Natalia', 'Janete', 'RPA', 'Tallison'],
    'Meta_Fat': [56400.0, 324000.0, 348500.0, 292400.0, 369800.0, 441000.0, 217000.0, 274500.0, 540000.0, 672000.0, 23500.0, 54900.0, 262500.0, 255000.0, 295200.0, 82500.0, 1.0, 110400.0, 92000.0, 63000.0, 36000.0],
    'Real_Fat': [54797.90, 272753.40, 310243.50, 240808.16, 303155.06, 390857.55, 183655.70, 241545.44, 510365.90, 623626.00, 13736.00, 16695.40, 219409.08, 181683.75, 280912.75, 138636.30, 0.0, 101987.20, 114774.59, 96810.70, 8610.50],
    'Meta_Peso': [3000.0, 20000.0, 20500.0, 17000.0, 21500.0, 24500.0, 14000.0, 15000.0, 30000.0, 28000.0, 1000.0, 3000.0, 15000.0, 15000.0, 18000.0, 5000.0, 1.0, 6000.0, 5000.0, 3000.0, 2000.0],
    'Real_Peso': [3445.0, 17060.0, 18759.0, 13981.0, 17932.0, 21625.0, 11940.0, 13015.0, 29167.0, 26045.0, 575.0, 927.0, 12512.0, 10990.0, 16940.0, 8891.0, 0.0, 5711.0, 6362.0, 4695.0, 615.0],
    'Meta_PM': [18.80, 16.20, 17.00, 17.20, 17.20, 18.00, 15.50, 18.30, 18.00, 24.00, 23.50, 18.30, 17.50, 17.00, 16.40, 16.50, 1.0, 18.40, 18.40, 21.00, 18.00],
    'Real_PM': [15.91, 15.99, 16.54, 17.22, 16.91, 18.07, 15.38, 18.56, 17.50, 23.94, 23.89, 18.01, 17.54, 16.53, 16.58, 15.59, 0.0, 17.86, 18.04, 20.62, 14.00],
    'Meta_Pos': [4.0, 145.0, 149.0, 125.0, 153.0, 135.0, 116.0, 75.0, 8.0, 120.0, 4.0, 40.0, 150.0, 95.0, 95.0, 10.0, 1.0, 55.0, 15.0, 35.0, 15.0],
    'Real_Pos': [4.0, 143.0, 144.0, 122.0, 142.0, 128.0, 113.0, 69.0, 9.0, 117.0, 4.0, 20.0, 143.0, 89.0, 83.0, 14.0, 0.0, 50.0, 12.0, 40.0, 9.0],
    'Meta_Cad': [0.0, 3.0, 2.0, 4.0, 2.0, 4.0, 8.0, 8.0, 0.0, 0.0, 0.0, 10.0, 2.0, 8.0, 8.0, 0.0, 1.0, 8.0, 5.0, 10.0, 10.0],
    'Real_Cad': [0.0, 3.0, 3.0, 1.0, 2.0, 0.0, 3.0, 1.0, 1.0, 1.0, 0.0, 4.0, 3.0, 0.0, 1.0, 0.0, 0.0, 8.0, 1.0, 13.0, 2.0]
}

# -------------------------------------------------------------------------
# 2. MOTOR DE CÁLCULO GERAL FIXO (PARA OS CARDS DO ACUMULADO)
# -------------------------------------------------------------------------
df_geral = pd.DataFrame(data_quad).copy()
df_geral['At_Fat'] = (df_geral['Real_Fat'] / df_geral['Meta_Fat']) * 100
df_geral['At_Peso'] = (df_geral['Real_Peso'] / df_geral['Meta_Peso']) * 100
df_geral['At_PM'] = (df_geral['Real_PM'] / df_geral['Meta_PM']) * 100
df_geral['At_Pos'] = (df_geral['Real_Pos'] / df_geral['Meta_Pos']) * 100
df_geral['At_Cad'] = np.where(df_geral['Meta_Cad'] <= 1.0, np.where(df_geral['Real_Cad'] > 0, 115.0, 0.0), (df_geral['Real_Cad'] / df_geral['Meta_Cad']) * 100)

def motor_faixas(ating, pt90, pt100, pt110):
    if ating < 90.0: return 0.0
    elif ating < 100.0: return float(pt90)
    elif ating < 110.0: return float(pt100)
    else: return float(pt110)

df_geral['P_Fat'] = df_geral['At_Fat'].apply(lambda x: motor_faixas(x, 5, 10, 15))
df_geral['P_Peso'] = df_geral['At_Peso'].apply(lambda x: motor_faixas(x, 5, 10, 15))
df_geral['P_PM'] = df_geral['At_PM'].apply(lambda x: motor_faixas(x, 10, 15, 20))
df_geral['P_Pos'] = df_geral['At_Pos'].apply(lambda x: motor_faixas(x, 5, 7.5, 10))
df_geral['P_Cad'] = df_geral['At_Cad'].apply(lambda x: motor_faixas(x, 5, 7.5, 10))
df_geral['Total'] = df_geral['P_Fat'] + df_geral['P_Peso'] + df_geral['P_PM'] + df_geral['P_Pos'] + df_geral['P_Cad']

# Ranking Geral Fixo
df_podio_fixo = df_geral.sort_values(by='Total', ascending=False).reset_index(drop=True)

# -------------------------------------------------------------------------
# 3. EXIBIÇÃO FIXA: OS CARDS DO TOP 5 ACUMULADO GERAL
# -------------------------------------------------------------------------
st.markdown("### 🏆 LÍDERES ACUMULADOS — RANKING GERAL DA CAMPANHA")
col_t1, col_t2, col_t3, col_t4, col_t5 = st.columns(5)

# Renderização estável nativa do Streamlit (Sem HTML complexo para não bugar)
col_t1.metric(label="🥇 1º LUGAR GERAL", value=df_podio_fixo.loc[0, 'Vendedor'], delta=f"{df_podio_fixo.loc[0, 'Total']:.2f} pts")
col_t2.metric(label="🥈 2º LUGAR GERAL", value=df_podio_fixo.loc[1, 'Vendedor'], delta=f"{df_podio_fixo.loc[1, 'Total']:.2f} pts")
col_t3.metric(label="🥉 3º LUGAR GERAL", value=df_podio_fixo.loc[2, 'Vendedor'], delta=f"{df_podio_fixo.loc[2, 'Total']:.2f} pts")
col_t4.metric(label="🏅 4º LUGAR GERAL", value=df_podio_fixo.loc[3, 'Vendedor'], delta=f"{df_podio_fixo.loc[3, 'Total']:.2f} pts")
col_t5.metric(label="🏅 5º LUGAR GERAL", value=df_podio_fixo.loc[4, 'Vendedor'], delta=f"{df_podio_fixo.loc[4, 'Total']:.2f} pts")

st.write("---")

# -------------------------------------------------------------------------
# 4. SEÇÃO DE FILTROS NA BARRA LATERAL (SIDEBAR)
# -------------------------------------------------------------------------
st.sidebar.header("⚙️ Filtros Dinâmicos")
periodo = st.sidebar.radio("Selecionar Período das Tabelas:", ["1º Quadrimestre", "Maio/2026"])

if periodo == "1º Quadrimestre":
    df_dinamico = pd.DataFrame(data_quad)
else:
    df_dinamico = pd.DataFrame(data_maio)

codigos_filtrados = [80012, 80021, 80055, 80061, 80022, 80001, 80057]
df_dinamico['Categoria'] = np.where(df_dinamico['COD'].isin(codigos_filtrados), 'Especiais', 'Padrao')

mostrar_especiais = st.sidebar.checkbox("Mostrar Rotas Especiais / Homologação nas Tabelas", value=True)
if not mostrar_especiais:
    df_dinamico = df_dinamico[df_dinamico['Categoria'] == 'Padrao'].reset_index(drop=True)

# -------------------------------------------------------------------------
# 5. PROCESSAMENTO DAS TABELAS DINÂMICAS (FILTRADAS PELO PERÍODO)
# -------------------------------------------------------------------------
df_dinamico['At_Fat'] = (df_dinamico['Real_Fat'] / df_dinamico['Meta_Fat']) * 100
df_dinamico['At_Peso'] = (df_dinamico['Real_Peso'] / df_dinamico['Meta_Peso']) * 100
df_dinamico['At_PM'] = (df_dinamico['Real_PM'] / df_dinamico['Meta_PM']) * 100
df_dinamico['At_Pos'] = (df_dinamico['Real_Pos'] / df_dinamico['Meta_Pos']) * 100
df_dinamico['At_Cad'] = np.where(df_dinamico['Meta_Cad'] <= 1.0, np.where(df_dinamico['Real_Cad'] > 0, 115.0, 0.0), (df_dinamico['Real_Cad'] / df_dinamico['Meta_Cad']) * 100)

df_dinamico['P_Fat'] = df_dinamico['At_Fat'].apply(lambda x: motor_faixas(x, 5, 10, 15))
df_dinamico['P_Peso'] = df_dinamico['At_Peso'].apply(lambda x: motor_faixas(x, 5, 10, 15))
df_dinamico['P_PM'] = df_dinamico['At_PM'].apply(lambda x: motor_faixas(x, 10, 15, 20))
df_dinamico['P_Pos'] = df_dinamico['At_Pos'].apply(lambda x: motor_faixas(x, 5, 7.5, 10))
df_dinamico['P_Cad'] = df_dinamico['At_Cad'].apply(lambda x: motor_faixas(x, 5, 7.5, 10))

df_dinamico['Pontuacao_Total'] = df_dinamico['P_Fat'] + df_dinamico['P_Peso'] + df_dinamico['P_PM'] + df_dinamico['P_Pos'] + df_dinamico['P_Cad']
