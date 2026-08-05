import streamlit as st
import pandas as pd
import numpy as np
import auth

auth.validar_senha()  # bloqueia se não tiver senha correta

# Título corrigido para a página correspondente
st.markdown("## Ranking Desempenho de Julho")

# Estrutura alternativa que impede o sistema de truncar as listas
lista_codigos = [80001, 80002, 80003, 80005, 80006, 80007, 80010, 80011, 80012, 80021, 80022, 80039, 80048, 80052, 80053, 80055, 80058, 80060, 80061, 80062, 80063]
codigos_filtrados = [80012, 80021, 80055, 80061, 80022, 80001]

# Dados do mês de Julho consolidados e validados por COD (Metas + Realizados)
data_julho = {
    'COD': lista_codigos,
    'Vendedor': [
        'VENDEDOR PARA HOMOLOGAÇÃO', 'CARLOS EDUARDO PEREIRA DA CRUZ', 'VALDINEI LUIZ PAIVA', 
        'LUIZ CARLOS SILVA NEVES', 'WESLEY FRANCIS DE JESUS LOPES', 'CELIO CLAUDIO OLIVEIRA', 
        'HELIO ALMEIDA VIANA', 'RAIMUNDO ALEX BARBOSA', 'MAURICIO SIMÕES JORGE', 'Rota BH', 
        'Rota BH - Interior de Minas', 'FREDERICO', 'FLAVIO CRISTIANO CARDOSO', 'WANDERSON DA SILVA LIMA', 
        'DANIEL DE PAULA', 'MAURICIO MARQUES DA SILVA JUNIOR', 'NATALIA FATIMA', 'JANETE CIRILO', 
        'RPA', 'Tallison Augusto de Oliveira', 'VENDEDOR 80063'
    ],
    'Meta_Fat': [
        66000.0, 321750.0, 369800.0, 306000.0, 358750.0, 430050.0, 231000.0, 291000.0, 531000.0, 696000.0, 
        24000.0, 36800.0, 254800.0, 232200.0, 327600.0, 99000.0, 136500.0, 133000.0, 90000.0, 63000.0, 63000.0
    ],
    'Real_Fat': [
        55718.05, 295068.75, 366127.85, 274562.55, 351301.05, 449714.35, 229787.60, 248830.65, 699003.45, 694983.00, 
        21504.00, 22047.50, 253083.73, 234078.10, 325428.65, 125716.23, 148081.96, 125980.47, 81582.90, 13399.50, 13823.50
    ],
    'Meta_Peso': [
        4000.0, 19500.0, 21500.0, 17000.0, 20500.0, 23500.0, 14000.0, 15000.0, 29500.0, 29000.0, 
        1000.0, 2000.0, 14000.0, 13500.0, 19500.0, 6000.0, 7000.0, 7000.0, 4500.0, 3500.0, 3500.0
    ],
    'Real_Peso': [
        3540.0, 17990.0, 21025.0, 15340.0, 20348.0, 24251.0, 14310.0, 12887.0, 39592.0, 29216.0, 
        890.0, 1160.0, 14007.0, 13575.0, 19490.0, 6808.0, 7583.0, 6489.0, 3940.0, 855.0, 580.0
    ],
    'Meta_PM': [
        16.50, 16.50, 17.20, 18.00, 17.50, 18.30, 16.50, 19.40, 18.00, 24.00, 
        24.00, 18.40, 18.20, 17.20, 16.80, 16.50, 19.50, 19.00, 20.00, 18.00, 18.00
    ],
    'Real_PM': [
        15.74, 16.40, 17.41, 17.90, 17.26, 18.54, 16.06, 19.31, 17.66, 23.79, 
        24.16, 19.01, 18.07, 17.24, 16.70, 18.47, 19.53, 19.41, 20.71, 15.67, 23.83
    ],
    'Meta_Pos': [
        4.0, 149.0, 150.0, 130.0, 154.0, 138.0, 122.0, 80.0, 8.0, 125.0, 
        4.0, 40.0, 155.0, 100.0, 100.0, 15.0, 60.0, 15.0, 45.0, 12.0, 12.0
    ],
    'Real_Pos': [
        4.0, 135.0, 147.0, 124.0, 147.0, 128.0, 107.0, 71.0, 10.0, 122.0, 
        4.0, 18.0, 139.0, 89.0, 83.0, 15.0, 60.0, 16.0, 17.0, 9.0, 9.0
    ],
    'Meta_Cad': [
        0.0, 4.0, 4.0, 4.0, 4.0, 4.0, 8.0, 8.0, 0.0, 2.0, 
        0.0, 10.0, 4.0, 8.0, 8.0, 2.0, 8.0, 6.0, 10.0, 10.0, 10.0
    ],
    'Real_Cad': [
        0.0, 3.0, 1.0, 3.0, 3.0, 2.0, 2.0, 0.0, 1.0, 1.0, 
        0.0, 2.0, 1.0, 1.0, 2.0, 0.0, 5.0, 2.0, 0.0, 1.0, 2.0
    ]
}

df = pd.DataFrame(data_julho)

# ✂️ Filtro para deixar apenas o Primeiro Nome de cada vendedor
df['Vendedor'] = df['Vendedor'].apply(lambda x: str(x).split()[0] if str(x).strip() else "")

# Identificação das rotas especiais
df['Categoria'] = np.where(df['COD'].isin(codigos_filtrados), 'Especiais', 'Padrao')

mostrar_especiais = st.sidebar.checkbox("Mostrar Rotas Especiais / Homologação", value=True)
if not mostrar_especiais:
    df = df[df['Categoria'] == 'Especiais'].reset_index(drop=True)

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
st.markdown("### 📋 TABELA DE PONTOS POR KPI (JULHO)")
st.dataframe(df_ranking[['COD', 'Vendedor', 'Pontuacao_Total', 'P_Fat', 'P_Peso', 'P_PM', 'P_Pos', 'P_Cad']].rename(columns={'Pontuacao_Total': 'PONTUAÇÃO TOTAL'}), use_container_width=True)
st.write("---")
st.markdown("### 📊 PERCENTUAIS DE ATINGIMENTO METAS (%)")
st.dataframe(df_ranking[['COD', 'Vendedor', 'At_Fat', 'At_Peso', 'At_PM', 'At_Pos', 'At_Cad']].style.format({'At_Fat': '{:.1f}%', 'At_Peso': '{:.1f}%', 'At_PM': '{:.1f}%', 'At_Pos': '{:.1f}%', 'At_Cad': '{:.1f}%'}), use_container_width=True)
