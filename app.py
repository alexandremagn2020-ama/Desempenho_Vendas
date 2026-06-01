import streamlit as st
import pandas as pd
import numpy as np

# Configuração da página para visual amplo e executivo
st.set_page_config(layout="wide", page_title="Painel de Performance Executivo")

# Título Principal Estilizado
st.markdown("<h2 style='text-align: center; color: #1E3A8A; font-weight: 700;'>🏆 PAINEL EXECUTIVO DE PERFORMANCE</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #6B7280;'>Campanha de Vendas — Sistema Estrito de Faixas Fixas por Período</p>", unsafe_allow_html=True)
st.write("---")

# -------------------------------------------------------------------------
# 1. MÓDULO DE DADOS: QUADRIMESTRE E MAIO/26 INTEGRADOS
# -------------------------------------------------------------------------

# Dados do Acumulado (1º Quadrimestre)
data_quad = {
    'COD': [80001, 80002, 80003, 80005, 80006, 80007, 80010, 80011, 80012, 80021, 80022, 80039, 80048, 80052, 80053, 80055, 80057, 80058, 80060, 80061, 80062],
    'Vendedor': ['Homologação', 'Carlos', 'Valdinei', 'Luiz', 'Wesley', 'Celio', 'Helio', 'Raimundo', 'Mauricio', 'Rota BH', 'Rota BH (Int)', 'Frederico', 'Flavio', 'Wanderson', 'Daniel', 'Mauricio Jr', 'Gilbert', 'Natalia', 'Janete', 'RPA', 'Tallison'],
    'Meta_Fat': [318880.0, 1171100.0, 1381200.0, 1136600.0, 1396000.0, 1658500.0, 751750.0, 1132500.0, 2315350.0, 2535200.0, 96000.0, 348750.0, 967250.0, 860500.0, 1293350.0, 664000.0, 90000.0, 479800.0, 331200.0, 241500.0, 1.0], # Ajustado para evitar divisão por zero
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

# Dados Isolados do Mês de Maio/2026
data_maio = {
    'COD': [80001, 80002, 80003, 80005, 80006, 80007, 80010, 80011, 80012, 80021, 80022, 80039, 80048, 80052, 80053, 80055, 80057, 80058, 80060, 80061, 80062],
    'Vendedor': ['Homologação', 'Carlos', 'Valdinei', 'Luiz', 'Wesley', 'Celio', 'Helio', 'Raimundo', 'Mauricio', 'Rota BH', 'Rota BH (Int)', 'Frederico', 'Flavio', 'Wanderson', 'Daniel', 'Mauricio Jr', 'Gilbert', 'Natalia', 'Janete', 'RPA', 'Tallison'],
    'Meta_Fat': [56400.0, 324000.0, 348500.0, 292400.0, 369800.0, 441000.0, 217000.0, 274500.0, 540000.0, 672000.0, 23500.0, 54900.0, 262500.0, 255000.0, 295200.0, 82500.0, 90000.0, 110400.0, 92000.0, 63000.0, 36000.0],
    'Real_Fat': [54797.90, 272753.40, 310243.50, 240808.16, 303155.06, 390857.55, 183655.70, 241545.44, 510365.90, 623626.00, 13736.00, 16695.40, 219409.08, 181683.75, 280912.75, 138636.30, 0.0, 101987.20, 114774.59, 96810.70, 8610.50],
    'Meta_Peso': [3000.0, 20000.0, 20500.0, 17000.0, 21500.0, 24500.0, 14000.0, 15000.0, 30000.0, 28000.0, 1000.0, 3000.0, 15000.0, 15000.0, 18000.0, 5000.0, 5000.0, 6000.0, 5000.0, 3000.0, 2000.0],
    'Real_Peso': [3445.0, 17060.0, 18759.0, 13981.0, 17932.0, 21625.0, 11940.0, 13015.0, 29167.0, 26045.0, 575.0, 927.0, 12512.0, 10990.0, 16940.0, 8891.0, 0.0, 5711.0, 6362.0, 4695.0, 615.0],
    'Meta_PM': [18.80, 16.20, 17.00, 17.20, 17.20, 18.00, 15.50, 18.30, 18.00, 24.00, 23.50, 18.30, 17.50, 17.00, 16.40, 16.50, 18.00, 18.40, 18.40, 21.00, 18.00],
    'Real_PM': [15.91, 15.99, 16.54, 17.22, 16.91, 18.07, 15.38, 18.56, 17.50, 23.94, 23.89, 18.01, 17.54, 16.53, 16.58, 15.59, 0.0, 17.86, 18.04, 20.62, 14.00],
    'Meta_Pos': [4.0, 145.0, 149.0, 125.0, 153.0, 135.0, 116.0, 75.0, 8.0, 120.0, 4.0, 40.0, 150.0, 95.0, 95.0, 10.0, 5.0, 55.0, 15.0, 35.0, 15.0],
    'Real_Pos': [4.0, 143.0, 144.0, 122.0, 142.0, 128.0, 113.0, 69.0, 9.0, 117.0, 4.0, 20.0, 143.0, 89.0, 83.0, 14.0, 0.0, 50.0, 12.0, 40.0, 9.0],
    'Meta_Cad': [0.0, 3.0, 2.0, 4.0, 2.0, 4.0, 8.0, 8.0, 0.0, 0.0, 0.0, 10.0, 2.0, 8.0, 8.0, 0.0, 5.0, 8.0, 5.0, 10.0, 10.0],
    'Real_Cad': [0.0, 3.0, 3.0, 1.0, 2.0, 0.0, 3.0, 1.0, 1.0, 1.0, 0.0, 4.0, 3.0, 0.0, 1.0, 0.0, 0.0, 8.0, 1.0, 13.0, 2.0]
}

# -------------------------------------------------------------------------
# 2. SEÇÃO DE FILTROS NA BARRA LATERAL (SIDEBAR)
# -------------------------------------------------------------------------
st.sidebar.header("⚙️ Configurações do Painel")

# Filtro 1: Seleção Dinâmica do Período de Análise
periodo = st.sidebar.radio("Selecionar Período:", ["1º Quadrimestre", "Maio/2026"])

if periodo == "1º Quadrimestre":
    df = pd.DataFrame(data_quad)
else:
    df = pd.DataFrame(data_maio)

# Mapeamento para ocultar/mostrar Rotas Especiais ou Homologações
codigos_filtrados = [80012, 80021, 80055, 80061, 80022, 80001, 80057]
df['Categoria'] = np.where(df['COD'].isin(codigos_filtrados), 'Rotas Especiais / Homologação', 'Vendedores Padrão')

# Filtro 2: Caixa para ativar ou remover categorias extras
mostrar_especiais = st.sidebar.checkbox("Mostrar Rotas Especiais / Homologação", value=True)

if not mostrar_especiais:
    df = df[df['Categoria'] == 'Vendedores Padrão'].reset_index(drop=True)

# -------------------------------------------------------------------------
# 3. CÁLCULOS DOS PERCENTUAIS E REGRAS DE TRAVA (DEGRAUS)
# -------------------------------------------------------------------------
df['At_Fat'] = (df['Real_Fat'] / df['Meta_Fat']) * 100
df['At_Peso'] = (df['Real_Peso'] / df['Meta_Peso']) * 100
df['At_PM'] = (df['Real_PM'] / df['Meta_PM']) * 100
df['At_Pos'] = (df['Real_Pos'] / df['Meta_Pos']) * 100

# Tratamento para metas zeradas em cadastro que obtiveram resultado
df['At_Cad'] = np.where(df['Meta_Cad'] == 0, np.where(df['Real_Cad'] > 0, 115.0, 0.0), (df['Real_Cad'] / df['Meta_Cad']) * 100)

# Função rígida de faixas da campanha
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

# Pontuação Total Acumulada por vendedor
df['Pontuacao_Total'] = df['P_Fat'] + df['P_Peso'] + df['P_PM'] + df['P_Pos'] + df['P_Cad']

# Ordenação do Ranking Geral
df_ranking = df.sort_values(by='Pontuacao_Total', ascending=False).reset_index(drop=True)

# -------------------------------------------------------------------------
# 4. BLOCOS VISUAIS: CARDS DO TOP 5 GERAL
# -------------------------------------------------------------------------
if len(df_ranking) > 0:
    st.markdown(f"### 🏆 OS 5 MELHORES DA CLASSIFICAÇÃO GERAL — {periodo.upper()}")
    col_t1, col_t2, col_t3, col_t4, col_t5 = st.columns(5)

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

    # -------------------------------------------------------------------------
    # 5. BLOCOS VISUAIS: LÍDERES DESTACADOS POR INDICADOR (KPI)
    # -------------------------------------------------------------------------
    st.markdown("### 🎖️ LÍDERES DESTACADOS POR INDICADOR (KPI)")
    campeao_fat = df.loc[df['P_Fat'].idxmax()]['Vendedor'] if df['P_Fat'].max() > 0 else "Ninguém"
    campeao_peso = df.loc[df['P_Peso'].idxmax()]['Vendedor'] if df['P_Peso'].max() > 0 else "Ninguém"
    campeao_pm = df.loc[df['P_PM'].idxmax()]['Vendedor'] if df['P_PM'].max() > 0 else "Ninguém"
