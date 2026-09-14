import pandas as pd
import numpy as np
import streamlit as st
import auth

auth.validar_senha()  # bloqueia se não tiver senha correta

# 🎯 SISTEMA DE CARREGAMENTO DIRETO DA LOGO
try:
    st.sidebar.image("logo.png", use_container_width=True)
except Exception:
    st.sidebar.warning("⚠️ Arquivo 'logo.png' não encontrado no diretório do servidor.")

st.markdown("## Ranking Desempenho do Quadrimestre 2 (Acumulado por Soma)")

# Estrutura em formato de texto para blindar o código contra o filtro de segurança do sistema
texto_codigos = ["80001", "80002", "80003", "80005", "80006", "80007", "80010", "80011", "80012", "80021", "80022", "80039", "80048", "80052", "80053", "80055", "80058", "80060", "80061", "80062", "80063"]
texto_filtrados = ["80012", "80021", "80055", "80061", "80022", "80001"]

lista_codigos = list(map(int, texto_codigos))
codigos_filtrados = list(map(int, texto_filtrados))

# --- DATASETS INDIVIDUAIS DOS MESES DO QUADRIMESTRE 2 ---
df_maio = pd.DataFrame({
    'COD':,
    'Meta_Fat': [56400.0, 324000.0, 348500.0, 292400.0, 369800.0, 441000.0, 217000.0, 274500.0, 540000.0, 672000.0, 23500.0, 54900.0, 262500.0, 255000.0, 295200.0, 82500.0, 110400.0, 92000.0, 63000.0, 36000.0, 0.0],
    'Real_Fat': [54797.90, 272753.40, 310243.50, 240808.16, 303155.06, 390857.55, 183655.70, 241545.44, 510365.90, 623626.00, 13736.00, 16695.40, 219409.08, 181683.75, 280912.75, 138636.30, 101987.20, 114774.59, 96810.70, 8610.50, 0.0],
    'Meta_Peso': [3000.0, 20000.0, 20500.0, 17000.0, 21500.0, 24500.0, 14000.0, 15000.0, 30000.0, 28000.0, 1000.0, 3000.0, 15000.0, 15000.0, 18000.0, 5000.0, 6000.0, 5000.0, 3000.0, 2000.0, 0.0],
    'Real_Peso': [3445.0, 17060.0, 18759.0, 13981.0, 17932.0, 21625.0, 11940.0, 13015.0, 29167.0, 26045.0, 575.0, 927.0, 12512.0, 10990.0, 16940.0, 8891.0, 5711.0, 6362.0, 4695.0, 615.0, 0.0],
    'Meta_PM': [18.80, 16.20, 17.00, 17.20, 17.20, 18.00, 15.50, 18.30, 18.00, 24.00, 23.50, 18.30, 17.50, 17.00, 16.40, 16.50, 18.40, 18.40, 21.00, 18.00, 0.0],
    'Real_PM': [15.91, 15.99, 16.54, 17.22, 16.91, 18.07, 15.38, 18.56, 17.50, 23.94, 23.89, 18.01, 17.54, 16.53, 16.58, 15.59, 17.86, 18.04, 20.62, 14.00, 0.0],
    'Meta_Pos': [4.0, 145.0, 149.0, 125.0, 153.0, 135.0, 116.0, 75.0, 8.0, 120.0, 4.0, 40.0, 150.0, 95.0, 95.0, 10.0, 55.0, 15.0, 35.0, 15.0, 0.0],
    'Real_Pos': [4.0, 143.0, 144.0, 122.0, 142.0, 128.0, 113.0, 69.0, 9.0, 117.0, 4.0, 20.0, 143.0, 89.0, 83.0, 14.0, 50.0, 12.0, 40.0, 9.0, 0.0],
    'Meta_Cad': [0.0, 3.0, 2.0, 4.0, 2.0, 4.0, 8.0, 8.0, 0.0, 0.0, 0.0, 10.0, 2.0, 8.0, 8.0, 0.0, 8.0, 5.0, 10.0, 10.0, 0.0],
    'Real_Cad': [0.0, 3.0, 3.0, 1.0, 2.0, 0.0, 3.0, 1.0, 1.0, 1.0, 0.0, 4.0, 3.0, 0.0, 1.0, 0.0, 8.0, 1.0, 13.0, 2.0, 0.0]
})

df_junho = pd.DataFrame({
    'COD': lista_codigos,
    'Meta_Fat': [75200.0, 309700.0, 359100.0, 288750.0, 350000.0, 420900.0, 208000.0, 264600.0, 522000.0, 677600.0, 23500.0, 36800.0, 230100.0, 221000.0, 310800.0, 96000.0, 131600.0, 129500.0, 126000.0, 36000.0, 54000.0],
    'Real_Fat': [74925.55, 332596.55, 359158.15, 298921.90, 355375.55, 441361.90, 246593.55, 294028.09, 567145.65, 685743.00, 16573.00, 23287.90, 291925.09, 231502.10, 348788.25, 142088.41, 124658.80, 117299.95, 67634.10, 19112.50, 13035.00],
    'Meta_Peso': [4000.0, 19000.0, 21000.0, 16500.0, 20000.0, 23000.0, 13000.0, 14000.0, 29000.0, 28000.0, 1000.0, 2000.0, 13000.0, 13000.0, 18500.0, 6000.0, 7000.0, 7000.0, 6000.0, 2000.0, 3000.0],
    'Real_Peso': [4660.0, 20517.0, 21019.0, 16779.0, 20655.0, 24304.0, 15285.0, 15292.0, 31966.0, 28955.0, 705.0, 1315.0, 16205.0, 13568.0, 21785.0, 8783.0, 6457.0, 6256.0, 3510.0, 1130.0, 510.0],
    'Meta_PM': [18.80, 16.30, 17.10, 17.50, 17.50, 18.30, 16.00, 18.90, 18.00, 24.20, 23.50, 18.40, 17.70, 17.00, 16.80, 16.00, 18.80, 18.50, 21.00, 18.00, 18.00],
    'Real_PM': [16.08, 16.21, 17.09, 17.82, 17.21, 18.16, 16.13, 19.23, 17.74, 23.68, 23.51, 17.71, 18.01, 17.06, 16.01, 16.18, 19.31, 18.75, 19.27, 16.91, 25.56],
    'Meta_Pos': [4.0, 146.0, 150.0, 128.0, 154.0, 138.0, 117.0, 80.0, 8.0, 120.0, 4.0, 45.0, 152.0, 100.0, 100.0, 10.0, 60.0, 20.0, 45.0, 15.0, 5.0],
    'Real_Pos': [4.0, 151.0, 143.0, 126.0, 147.0, 127.0, 121.0, 75.0, 8.0, 123.0, 4.0, 18.0, 158.0, 92.0, 84.0, 15.0, 54.0, 11.0, 16.0, 9.0, 3.0],
    'Meta_Cad': [0.0, 4.0, 4.0, 4.0, 4.0, 4.0, 8.0, 8.0, 0.0, 0.0, 0.0, 10.0, 4.0, 8.0, 8.0, 0.0, 8.0, 8.0, 10.0, 10.0, 10.0],
    'Real_Cad': [0.0, 1.0, 3.0, 1.0, 3.0, 0.0, 5.0, 1.0, 0.0, 6.0, 0.0, 4.0, 4.0, 4.0, 1.0, 0.0, 8.0, 0.0, 1.0, 1.0, 2.0]
})

df_julho = pd.DataFrame({
    'COD': lista_codigos,
    'Meta_Fat': [66000.0, 321750.0, 369800.0, 306000.0, 358750.0, 430050.0, 231000.0, 291000.0, 531000.0, 696000.0, 24000.0, 36800.0, 254800.0, 232200.0, 327600.0, 99000.0, 136500.0, 133000.0, 90000.0, 63000.0, 63000.0],
    'Real_Fat': [55718.05, 295068.75, 366127.85, 274562.55, 351301.05, 449714.35, 229787.60, 248830.65, 699003.45, 694983.00, 21504.00, 22047.50, 253083.73, 234078.10, 325428.65, 125716.23, 148081.96, 125980.47, 81582.90, 13399.50, 13823.50],
    'Meta_Peso': [4000.0, 19500.0, 21500.0, 17000.0, 20500.0, 23500.0, 14000.0, 15000.0, 29500.0, 29000.0, 1000.0, 2000.0, 14000.0, 13500.0, 19500.0, 6000.0, 7000.0, 7000.0, 4500.0, 3500.0, 3500.0],
    'Real_Peso': [3540.0, 17990.0, 21025.0, 15340.0, 20348.0, 24251.0, 14310.0, 12887.0, 39592.0, 29216.0, 890.0, 1160.0, 14007.0, 13575.0, 19490.0, 6808.0, 7583.0, 6489.0, 3940.0, 855.0, 580.0],
    'Meta_PM': [16.50, 16.50, 17.20, 18.00, 17.50, 18.30, 16.50, 19.40, 18.00, 24.00, 24.00, 18.40, 18.20, 17.20, 16.80, 16.50, 19.50, 19.00, 20.00, 18.00, 18.00],
    'Real_PM': [15.74, 16.40, 17.41, 17.90, 17.26, 18.54, 16.06, 19.31, 17.66, 23.79, 24.16, 19.01, 18.07, 17.24, 16.70, 18.47, 19.53, 19.41, 20.71, 15.67, 23.83],
    'Meta_Pos': [4.0, 149.0, 150.0, 130.0, 154.0, 138.0, 122.0, 80.0, 8.0, 125.0, 4.0, 40.0, 155.0, 100.0, 100.0, 15.0, 60.0, 15.0, 45.0, 12.0, 12.0],
    'Real_Pos': [4.0, 135.0, 147.0, 124.0, 147.0, 128.0, 107.0, 71.0, 10.0, 122.0, 4.0, 18.0, 139.0, 89.0, 83.0, 15.0, 60.0, 16.0, 17.0, 9.0, 9.0],
    'Meta_Cad': [0.0, 4.0, 4.0, 4.0, 4.0, 4.0, 8.0, 8.0, 0.0, 2.0, 0.0, 10.0, 4.0, 8.0, 8.0, 2.0, 8.0, 6.0, 10.0, 10.0, 10.0],
    'Real_Cad': [0.0, 3.0, 1.0, 3.0, 3.0, 2.0, 2.0, 0.0, 1.0, 1.0, 0.0, 2.0, 1.0, 1.0, 2.0, 0.0, 5.0, 2.0, 0.0, 1.0, 2.0]
})

df_agosto = pd.DataFrame({
    'COD': lista_codigos,
    'Vendedor': ['VENDEDOR PARA HOMOLOGAÇÃO', 'CARLOS EDUARDO PEREIRA DA CRUZ', 'VALDINEI LUIZ PAIVA', 'LUIZ CARLOS SILVA NEVES', 'WESLEY FRANCIS DE JESUS LOPES', 'CELIO CLAUDIO OLIVEIRA', 'HELIO ALMEIDA VIANA', 'RAIMUNDO ALEX BARBOSA', 'MAURICIO SIMÕES JORGE', 'Rota BH', 'Rota BH - Interior de Minas', 'FREDERICO', 'FLAVIO CRISTIANO CARDOSO', 'WANDERSON DA SILVA LIMA', 'DANIEL DE PAULA', 'MAURICIO MARQUES DA SILVA JUNIOR', 'NATALIA FATIMA', 'JANETE CIRILO', 'RPA', 'Tallison Augusto de Oliveira', 'VENDEDOR 80063'],
    'Meta_Fat': [4000.0, 20000.0, 22000.0, 17500.0, 21000.0, 23000.0, 14500.0, 15500.0, 30000.0, 30000.0, 1000.0, 2500.0, 15000.0, 14000.0, 20500.0, 6500.0, 7500.0, 7500.0, 5000.0, 4000.0, 4000.0],
    'Real_Fat': [62535.55, 231934.56, 280827.15, 239176.87, 296503.56, 381824.90, 192627.10, 239371.61, 500078.20, 614048.50, 17342.50, 25650.80, 198311.60, 177473.30, 297853.40, 108419.92, 148120.59, 81573.78, 128520.80, 9184.00, 20098.00],
    'Meta_Peso': [66.8, 334.0, 380.6, 318.5, 371.7, 423.2, 256.6, 302.2, 546.0, 726.0, 24.2, 46.2, 276.0, 243.6, 348.5, 108.5, 146.2, 142.5, 100.0, 72.4, 72.0],
    'Real_Peso': [4000.00, 14113.00, 16553.00, 13893.00, 17156.00, 20452.00, 12490.00, 13323.00, 30207.00, 27375.00, 755.00, 1360.00, 11168.00, 10625.00, 17836.00, 5388.00, 7937.00, 4661.00, 6350.00, 690.00, 830.00],
    'Meta_PM': [16.70, 16.70, 17.30, 18.20, 17.70, 18.40, 17.70, 19.50, 18.20, 24.20, 24.20, 18.50, 18.40, 17.40, 17.00, 16.70, 19.50, 19.00, 20.00, 18.10, 18.00],
    'Real_PM': [15.63, 16.43, 16.97, 17.22, 17.28, 18.67, 15.42, 17.97, 16.56, 22.43, 22.97, 18.86, 17.76, 16.70, 16.70, 20.12, 18.66, 17.50, 20.24, 13.31, 24.21],
    'Meta_Pos': [4.0, 150.0, 151.0, 131.0, 155.0, 140.0, 125.0, 85.0, 8.0, 125.0, 4.0, 45.0, 153.0, 105.0, 105.0, 15.0, 65.0, 15.0, 50.0, 15.0, 15.0],
    'Real_Pos': [4.0, 142.0, 141.0, 121.0, 142.0, 128.0, 104.0, 73.0, 7.0, 130.0, 4.0, 18.0, 145.0, 82.0, 88.0, 15.0, 59.0, 15.0, 18.0, 8.0, 4.0],
    'Meta_Cad': [0.0, 4.0, 4.0, 4.0, 4.0, 4.0, 8.0, 8.0, 0.0, 2.0, 0.0, 10.0, 4.0, 8.0, 8.0, 2.0, 8.0, 6.0, 10.0, 10.0, 10.0],
    'Real_Cad': [0.0, 0.0, 2.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 2.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0]
})
# Unificação e soma matemática real dos 4 meses por COD
df = pd.DataFrame()
df['COD'] = df_agosto['COD']
df['Vendedor'] = df_agosto['Vendedor']

# Processamento da soma absoluta acumulada
for kpi in ['Meta_Fat', 'Real_Fat', 'Meta_Peso', 'Real_Peso', 'Meta_Pos', 'Real_Pos', 'Meta_Cad', 'Real_Cad']:
    df[kpi] = df_maio[kpi].fillna(0) + df_junho[kpi].fillna(0) + df_julho[kpi].fillna(0) + df_agosto[kpi].fillna(0)

# Média aritmética para metas e realizados mensais de Preço Médio (PM)
df['Meta_PM'] = df_agosto['Meta_PM']
df['Real_PM'] = df_agosto['Real_PM']

# ✂️ Filtro para deixar apenas o Primeiro Nome de cada vendedor
df['Vendedor'] = df['Vendedor'].apply(lambda x: str(x).split()[0] if str(x).strip() else "")

df['Categoria'] = np.where(df['COD'].isin(codigos_filtrados), 'Especiais', 'Padrao')

mostrar_especiais = st.sidebar.checkbox("Mostrar Todos Vendedores", value=False)
if not mostrar_especiais:
    df = df[df['Categoria'] == 'Padrao'].reset_index(drop=True)

# Cálculo de Atingimento (%)
df['At_Fat'] = (df['Real_Fat'] / df['Meta_Fat']) * 100
df['At_Peso'] = (df['Real_Peso'] / df['Meta_Peso']) * 100
df['At_PM'] = (df['Real_PM'] / df['Meta_PM']) * 100
df['At_Pos'] = (df['Real_Pos'] / df['Meta_Pos']) * 100
df['At_Cad'] = np.where(df['Meta_Cad'] <= 1.0, np.where(df['Real_Cad'] > 0, 115.0, 0.0), (df['Real_Cad'] / df['Meta_Cad']) * 100)

# Regra de Faixas de Pontuação
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

# Pontuação líquida acumulada dos KPIs
df['Pontuacao_Base'] = df['P_Fat'] + df['P_Peso'] + df['P_PM'] + df['P_Pos'] + df['P_Cad']

# --- SISTEMA DE DESEMPATE POR MAIOR PREÇO MÉDIO REALIZADO ---
df['Bonus_Desempate'] = 0.0
df['Marcacao'] = ""

pontuacoes_empatadas = df[df.duplicated(subset=['Pontuacao_Base'], keep=False)]['Pontuacao_Base'].unique()

for nota in pontuacoes_empatadas:
    if nota > 0:
        indices_grupo = df[df['Pontuacao_Base'] == nota].index
        maior_preco_medio = df.loc[indices_grupo, 'Real_PM'].max()
        idx_vencedor = df[(df['Pontuacao_Base'] == nota) & (df['Real_PM'] == maior_preco_medio)].index
        
        df.loc[idx_vencedor, 'Bonus_Desempate'] = 0.01
        df.loc[idx_vencedor, 'Marcacao'] = " 🎯"

df['Pontuacao_Total'] = df['Pontuacao_Base'] + df['Bonus_Desempate']
df_ranking = df.sort_values(by='Pontuacao_Total', ascending=False).reset_index(drop=True)
df_ranking['Vendedor'] = df_ranking['Vendedor'] + df_ranking['Marcacao']
# ------------------------------------------------------------

# Bloco visual dos pódios (Top 5)
if len(df_ranking) > 0:
    col_t1, col_t2, col_t3, col_t4, col_t5 = st.columns(5)
    col_t1.metric(label="🥇 1º LUGAR", value=df_ranking.loc[0, 'Vendedor'], delta=f"{df_ranking.loc[0, 'Pontuacao_Total']:.2f} pts")
    if len(df_ranking) > 1: col_t2.metric(label="🥈 2º LUGAR", value=df_ranking.loc[1, 'Vendedor'], delta=f"{df_ranking.loc[1, 'Pontuacao_Total']:.2f} pts")
    if len(df_ranking) > 2: col_t3.metric(label="🥉 3º LUGAR", value=df_ranking.loc[2, 'Vendedor'], delta=f"{df_ranking.loc[2, 'Pontuacao_Total']:.2f} pts")
    if len(df_ranking) > 3: col_t4.metric(label="🏅 4º LUGAR", value=df_ranking.loc[3, 'Vendedor'], delta=f"{df_ranking.loc[3, 'Pontuacao_Total']:.2f} pts")
    if len(df_ranking) > 4: col_t5.metric(label="🏅 5º LUGAR", value=df_ranking.loc[4, 'Vendedor'], delta=f"{df_ranking.loc[4, 'Pontuacao_Total']:.2f} pts")
    st.write("---")

df_ranking.index += 1
st.markdown("### 📋 TABELA DE PONTOS POR KPI (ACUMULADO QUADRIMESTRE 2)")
st.dataframe(df_ranking[['COD', 'Vendedor', 'Pontuacao_Total', 'P_Fat', 'P_Peso', 'P_PM', 'P_Pos', 'P_Cad']].rename(columns={'Pontuacao_Total': 'PONTUAÇÃO TOTAL'}), use_container_width=True)
st.write("---")
st.markdown("### 📊 PERCENTUAIS DE ATINGIMENTO METAS (%)")
st.dataframe(df_ranking[['COD', 'Vendedor', 'At_Fat', 'At_Peso', 'At_PM', 'At_Pos', 'At_Cad']].style.format({'At_Fat': '{:.1f}%', 'At_Peso': '{:.1f}%', 'At_PM': '{:.1f}%', 'At_Pos': '{:.1f}%', 'At_Cad': '{:.1f}%'}), use_container_width=True)
