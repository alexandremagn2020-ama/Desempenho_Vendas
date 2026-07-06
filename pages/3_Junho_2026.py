import streamlit as st
import pandas as pd
import numpy as np
import auth

auth.validar_senha()  # bloqueia se não tiver senha correta

# Título corrigido para a página correspondente
st.markdown("## Conteúdo da página Junho")

# Dados do mês de Junho consolidados e validados por COD (Metas + Realizados)
data_junho = {
    'COD': [
        80001, 80002, 80003, 80005, 80006, 80007, 80010, 80011, 80012, 80021, 
        80022, 80039, 80048, 80052, 80053, 80055, 80058, 80060, 80061, 80062, 80063
    ],
    'Vendedor': [
        'VENDEDOR PARA HOMOLOGAÇÃO', 'CARLOS EDUARDO PEREIRA DA CRUZ', 'VALDINEI LUIZ PAIVA', 
        'LUIZ CARLOS SILVA NEVES', 'WESLEY FRANCIS DE JESUS LOPES', 'CELIO CLAUDIO OLIVEIRA', 
        'HELIO ALMEIDA VIANA', 'RAIMUNDO ALEX BARBOSA', 'MAURICIO SIMÕES JORGE', 'Rota BH', 
        'Rota BH - Interior de Minas', 'FREDERICO', 'FLAVIO CRISTIANO CARDOSO', 'WANDERSON DA SILVA LIMA', 
        'DANIEL DE PAULA', 'MAURICIO MARQUES DA SILVA JUNIOR', 'NATALIA FATIMA', 'JANETE CIRILO', 
        'RPA', 'Tallison Augusto de Oliveira', 'Marcelo 80063'
    ],
    'Meta_Fat': [
        75200.0, 309700.0, 359100.0, 288750.0, 350000.0, 420900.0, 208000.0, 264600.0, 522000.0, 677600.0, 
        23500.0, 36800.0, 230100.0, 221000.0, 310800.0, 96000.0, 131600.0, 129500.0, 126000.0, 36000.0, 54000.0
    ],
    'Real_Fat': [
        74925.55, 332596.55, 359158.15, 298921.90, 355375.55, 441361.90, 246593.55, 294028.09, 567145.65, 685743.00, 
        16573.00, 23287.90, 291925.09, 231502.10, 348788.25, 142088.41, 124658.80, 117299.95, 67634.10, 19112.50, 13035.00
    ],
    'Meta_Peso': [
        4000.0, 19000.0, 21000.0, 16500.0, 20000.0, 23000.0, 13000.0, 14000.0, 29000.0, 28000.0, 
        1000.0, 2000.0, 13000.0, 13000.0, 18500.0, 6000.0, 7000.0, 7000.0, 6000.0, 2000.0, 3000.0
    ],
    'Real_Peso': [
        4660.0, 20517.0, 21019.0, 16779.0, 20655.0, 24304.0, 15285.0, 15292.0, 31966.0, 28955.0, 
        705.0, 1315.0, 16205.0, 13568.0, 21785.0, 8783.0, 6457.0, 6256.0, 3510.0, 1130.0, 510.0
    ],
    'Meta_PM': [
        18.80, 16.30, 17.10, 17.50, 17.50, 18.30, 16.00, 18.90, 18.00, 24.20, 
        23.50, 18.40, 17.70, 17.00, 16.80, 16.00, 18.80, 18.50, 21.00, 18.00, 18.00
    ],
    'Real_PM': [
        16.08, 16.21, 17.09, 17.82, 17.21, 18.16, 16.13, 19.23, 17.74, 23.68, 
        23.51, 17.71, 18.01, 17.06, 16.01, 16.18, 19.31, 18.75, 19.27, 16.91, 25.56
    ],
    'Meta_Pos': [
        4.0, 146.0, 150.0, 128.0, 154.0, 138.0, 117.0, 80.0, 8.0, 120.0, 
        4.0, 45.0, 152.0, 100.0, 100.0, 10.0, 60.0, 20.0, 45.0, 15.0, 5.0
    ],
    'Real_Pos': [
        4.0, 151.0, 143.0, 126.0, 147.0, 127.0, 121.0, 75.0, 8.0, 123.0, 
        4.0, 18.0, 158.0, 92.0, 84.0, 15.0, 54.0, 11.0, 16.0, 9.0, 3.0
    ],
    'Meta_Cad': [
        0.0, 4.0, 4.0, 4.0, 4.0, 4.0, 8.0, 8.0, 0.0, 0.0, 
        0.0, 10.0, 4.0, 8.0, 8.0, 0.0, 8.0, 8.0, 10.0, 10.0, 10.0
    ],
    'Real_Cad': [
        0.0, 1.0, 3.0, 1.0, 3.0, 0.0, 5.0, 1.0, 0.0, 6.0, 
        0.0, 4.0, 4.0, 4.0, 1.0, 0.0, 8.0, 0.0, 1.0, 1.0, 2.0
    ]
}

df = pd.DataFrame(data_junho)

# ✂️ Filtro para deixar apenas o Primeiro Nome de cada vendedor
df['Vendedor'] = df['Vendedor'].apply(lambda x: str(x).split()[0] if str(x).strip() else "")

# Identificação das rotas especiais
codigos_filtrados = [80012, 80021, 80055, 80061, 80022, 80001]
df['Categoria'] = np.where(df['COD'].isin(codigos_filtrados), 'Especiais', 'Padrao')

mostrar_especiais = st.sidebar.checkbox("Mostrar Rotas Especiais / Homologação", value=True)
if not mostrar_especiais:
    df = df[df['Categoria'] == 'Padrao'].reset_index(drop=True)

# Cálculo de Atingimento (%)
df['At_Fat'] = (df['Real_Fat'] / df['Meta_Fat']) * 100
df['At_Peso'] = (df['Real_Peso'] / df['Meta_Peso']) * 100
df['At_PM'] = (df['Real_PM'] / df['Meta_PM']) * 100
df['At_Pos'] = (df['Real_Pos'] / df['Meta_Pos']) * 100
df['At_Cad'] = np.where(df['Meta_Cad'] <= 1.0, np.where(df['Real_Cad'] > 0, 115.0, 0.0), (df['Real_Cad'] / df['Meta_Cad']) * 100)

# Regra de Faixas de Pontuação conforme tabela de campanha fornecida
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
st.markdown("### 📋 TABELA DE PONTOS POR KPI (JUNHO)")
st.dataframe(df_ranking[['COD', 'Vendedor', 'Pontuacao_Total', 'P_Fat', 'P_Peso', 'P_PM', 'P_Pos', 'P_Cad']].rename(columns={'Pontuacao_Total': 'PONTUAÇÃO TOTAL'}), use_container_width=True)
st.write("---")
st.markdown("### 📊 PERCENTUAIS DE ATINGIMENTO METAS (%)")
st.dataframe(df_ranking[['COD', 'Vendedor', 'At_Fat', 'At_Peso', 'At_PM', 'At_Pos', 'At_Cad']].style.format({'At_Fat': '{:.1f}%', 'At_Peso': '{:.1f}%', 'At_PM': '{:.1f}%', 'At_Pos': '{:.1f}%', 'At_Cad': '{:.1f}%'}), use_container_width=True)
