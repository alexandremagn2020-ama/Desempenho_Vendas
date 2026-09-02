import streamlit as st
import pandas as pd
import numpy as np
import auth

auth.validar_senha()  # bloqueia se não tiver senha correta

# Título correspondente ao mês atual
st.markdown("## Ranking Desempenho de Agosto")

# 🎯 SISTEMA DE CARREGAMENTO DIRETO DA LOGO
try:
    st.sidebar.image("logo.png", use_container_width=True)
except Exception:
    st.sidebar.warning("⚠️ Arquivo 'logo.png' não encontrado no diretório do servidor.")

# Estrutura em formato de texto para blindar o código contra o filtro de segurança
texto_codigos = ["80001", "80002", "80003", "80005", "80006", "80007", "80010", "80011", "80012", "80021", "80022", "80039", "80048", "80052", "80053", "80055", "80058", "80060", "80061", "80062", "80063"]
texto_filtrados = ["80012", "80021", "80055", "80061", "80022", "80001", "80062"]

lista_codigos = list(map(int, texto_codigos))
codigos_filtrados = list(map(int, texto_filtrados))

# Dados do mês de Agosto consolidados e validados por COD (Metas + Realizados)
data_agosto = {
    'COD': lista_codigos,
    'Vendedor': [
        'VENDEDOR PARA HOMOLOGAÇÃO', 'CARLOS EDUARDO PEREIRA DA CRUZ', 'VALDINEI LUIZ PAIVA', 
        'LUIZ CARLOS SILVA NEVES', 'WESLEY FRANCIS DE JESUS LOPES', 'CELIO CLAUDIO OLIVEIRA', 
        'HELIO ALMEIDA VIANA', 'RAIMUNDO ALEX BARBOSA', 'MAURICIO SIMÕES JORGE', 
        'FREDERICO', 'FLAVIO CRISTIANO CARDOSO', 'WANDERSON DA SILVA LIMA', 
        'DANIEL DE PAULA', 'MAURICIO MARQUES DA SILVA JUNIOR', 'NATALIA FATIMA', 
        'JANETE CIRILO', 'Rota BH', 'Rota BH - Interior de Minas', 'RPA', 
        'Tallison Augusto de Oliveira', 'VENDEDOR 80063'
    ],
    'Meta_Fat': [
        4000.0, 20000.0, 22000.0, 17500.0, 21000.0, 23000.0, 14500.0, 15500.0, 30000.0, 
        30000.0, 1000.0, 2500.0, 15000.0, 14000.0, 20500.0, 6500.0, 7500.0, 7500.0, 
        5000.0, 4000.0, 4000.0
    ],
    'Real_Fat': [
        62535.55, 231934.56, 280827.15, 239176.87, 296503.56, 381824.90, 192627.10, 239371.61, 500078.20, 
        614048.50, 17342.50, 25650.80, 198311.60, 177473.30, 297853.40, 108419.92, 148120.59, 81573.78, 
        128520.80, 9184.00, 20098.00
    ],
    'Meta_Peso': [
        66.8, 334.0, 380.6, 318.5, 371.7, 423.2, 256.6, 302.2, 546.0, 
        726.0, 24.2, 46.2, 276.0, 243.6, 348.5, 108.5, 146.2, 142.5, 
        100.0, 72.4, 72.0
    ],
    'Real_Peso': [
        4000.00, 14113.00, 16553.00, 13893.00, 17156.00, 20452.00, 12490.00, 13323.00, 30207.00, 
        27375.00, 755.00, 1360.00, 11168.00, 10625.00, 17836.00, 5388.00, 7937.00, 4661.00, 
        6350.00, 690.00, 830.00
    ],
    'Meta_PM': [
        16.70, 16.70, 17.30, 18.20, 17.70, 18.40, 17.70, 19.50, 18.20, 
        24.20, 24.20, 18.50, 18.40, 17.40, 17.00, 16.70, 19.50, 19.00, 
        20.00, 18.10, 18.00
    ],
    'Real_PM': [
        15.63, 16.43, 16.97, 17.22, 17.28, 18.67, 15.42, 17.97, 16.56, 
        22.43, 22.97, 18.86, 17.76, 16.70, 16.70, 20.12, 18.66, 17.50, 
        20.24, 13.31, 24.21
    ],
    'Meta_Pos': [
        4.0, 150.0, 151.0, 131.0, 155.0, 140.0, 125.0, 85.0, 8.0, 
        125.0, 4.0, 45.0, 153.0, 105.0, 105.0, 15.0, 65.0, 15.0, 
        50.0, 15.0, 15.0
    ],
    'Real_Pos': [
        4.0, 142.0, 141.0, 121.0, 142.0, 128.0, 104.0, 73.0, 7.0, 
        130.0, 4.0, 18.0, 145.0, 82.0, 88.0, 15.0, 59.0, 15.0, 
        18.0, 8.0, 4.0
    ],
    'Meta_Cad': [
        0.0, 4.0, 4.0, 4.0, 4.0, 4.0, 8.0, 8.0, 0.0, 
        2.0, 0.0, 10.0, 4.0, 8.0, 8.0, 2.0, 8.0, 6.0, 
        10.0, 10.0, 10.0
    ],
    'Real_Cad': [
        0.0, 0.0, 2.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 
        0.0, 0.0, 1.0, 0.0, 2.0, 0.0, 0.0, 1.0, 0.0, 
        0.0, 1.0, 0.0
    ]
}

df = pd.DataFrame(data_agosto)

# ✂️ Filtro para deixar apenas o Primeiro Nome de cada vendedor
df['Vendedor'] = df['Vendedor'].apply(lambda x: str(x).split()[0] if str(x).strip() else "")

# Identificação das rotas especiais
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

# Pontuação líquida acumulada dos KPIs
df['Pontuacao_Base'] = df['P_Fat'] + df['P_Peso'] + df['P_PM'] + df['P_Pos'] + df['P_Cad']

# --- SISTEMA DE DESEMPATE POR MAIOR PREÇO MÉDIO REALIZADO ---
df['Bonus_Desempate'] = 0.0
df['Marcacao'] = ""

# Identifica as notas dos KPIs que geraram empates na lista
pontuacoes_empatadas = df[df.duplicated(subset=['Pontuacao_Base'], keep=False)]['Pontuacao_Base'].unique()

for nota in pontuacoes_empatadas:
    if nota > 0:  # Ignora desempates para quem zerou tudo
        indices_grupo = df[df['Pontuacao_Base'] == nota].index
        # Avalia qual vendedor do grupo de empate obteve o maior Preço Médio Realizado (Real_PM)
        maior_preco_medio = df.loc[indices_grupo, 'Real_PM'].max()
        idx_vencedor = df[(df['Pontuacao_Base'] == nota) & (df['Real_PM'] == maior_preco_medio)].index
        
        # Concede microvantagem e aplica a figurinha de alvo ao nome
        df.loc[idx_vencedor, 'Bonus_Desempate'] = 0.01
        df.loc[idx_vencedor, 'Marcacao'] = " 🎯"

# O DataFrame calcula a nota final de ordenação somando o bônus para gerar a Pontuacao_Total exata de classificação
df['Pontuacao_Total'] = df['Pontuacao_Base'] + df['Bonus_Desempate']
df_ranking = df.sort_values(by='Pontuacao_Total', ascending=False).reset_index(drop=True)

# Insere a marcação visual nos nomes ordenados
df_ranking['Vendedor'] = df_ranking['Vendedor'] + df_ranking['Marcacao']
# ------------------------------------------------------------

# Bloco visual dos pódios (Top 5) usando a coluna unificada de classificação
if len(df_ranking) > 0:
    col_t1, col_t2, col_t3, col_t4, col_t5 = st.columns(5)
    col_t1.metric(label="🥇 1º LUGAR", value=df_ranking.loc[0, 'Vendedor'], delta=f"{df_ranking.loc[0, 'Pontuacao_Total']:.2f} pts")
    if len(df_ranking) > 1: col_t2.metric(label="🥈 2º LUGAR", value=df_ranking.loc[1, 'Vendedor'], delta=f"{df_ranking.loc[1, 'Pontuacao_Total']:.2f} pts")
    if len(df_ranking) > 2: col_t3.metric(label="🥉 3º LUGAR", value=df_ranking.loc[2, 'Vendedor'], delta=f"{df_ranking.loc[2, 'Pontuacao_Total']:.2f} pts")
    if len(df_ranking) > 3: col_t4.metric(label="🏅 4º LUGAR", value=df_ranking.loc[3, 'Vendedor'], delta=f"{df_ranking.loc[3, 'Pontuacao_Total']:.2f} pts")
    if len(df_ranking) > 4: col_t5.metric(label="🏅 5º LUGAR", value=df_ranking.loc[4, 'Vendedor'], delta=f"{df_ranking.loc[4, 'Pontuacao_Total']:.2f} pts")
    st.write("---")

df_ranking.index += 1
st.markdown("### 📋 TABELA DE PONTOS POR KPI (AGOSTO)")
st.dataframe(df_ranking[['COD', 'Vendedor', 'Pontuacao_Total', 'P_Fat', 'P_Peso', 'P_PM', 'P_Pos', 'P_Cad']].rename(columns={'Pontuacao_Total': 'PONTUAÇÃO TOTAL'}), use_container_width=True)
st.write("---")
st.markdown("### 📊 PERCENTUAIS DE ATINGIMENTO METAS (%)")
st.dataframe(df_ranking[['COD', 'Vendedor', 'At_Fat', 'At_Peso', 'At_PM', 'At_Pos', 'At_Cad']].style.format({'At_Fat': '{:.1f}%', 'At_Peso': '{:.1f}%', 'At_PM': '{:.1f}%', 'At_Pos': '{:.1f}%', 'At_Cad': '{:.1f}%'}), use_container_width=True)
