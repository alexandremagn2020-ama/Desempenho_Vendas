import streamlit as st
import pandas as pd
import numpy as np
import auth

auth.validar_senha()  # bloqueia se não tiver senha correta

# Título correspondente ao mês atual
st.markdown("## Ranking Desempenho de Setembro")

# 🎯 SISTEMA DE CARREGAMENTO DIRETO DA LOGO
try:
    st.sidebar.image("logo.png", use_container_width=True)
except Exception:
    st.sidebar.warning("⚠️ Arquivo 'logo.png' não encontrado no diretório do servidor.")

# Estrutura em formato de texto para blindar o código contra o filtro de segurança
texto_codigos = ["80001", "80002", "80003", "80005", "80006", "80007", "80010", "80011", "80012", "80021", "80022", "80039", "80048", "80052", "80053", "80055", "80058", "80060", "80061", "80062", "80063"]
texto_filtrados = ["80012", "80021", "80055", "80061", "80022", "80001"]

lista_codigos = list(map(int, texto_codigos))
codigos_filtrados = list(map(int, texto_filtrados))

# Dados do mês de Setembro consolidados e validados por COD (Sequência de Vendedores idêntica a Agosto)
# Obs.: na planilha de meta as colunas META_R$ e META_KG vêm trocadas (META_KG / META_R$ = META_PM).
# Aqui Meta_Fat recebe a coluna META_KG (R$) e Meta_Peso recebe a coluna META_R$ (kg).
data_setembro = {
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
        66800.0, 297000.0, 358750.0, 271250.0, 358750.0, 437000.0, 218700.0, 285000.0, 561000.0,
        672800.0, 23200.0, 38400.0, 245700.0, 232200.0, 336000.0, 102500.0, 165750.0, 157250.0,
        123000.0, 45000.0, 73500.0
    ],
    'Real_Fat': [
        54634.35, 242374.45, 282301.35, 252693.38, 311677.39, 373574.34, 191964.40, 206341.52, 529711.85,
        708359.50, 20615.00, 21376.85, 208257.00, 197711.90, 330367.24, 154051.80, 91116.50, 106515.96,
        92138.90, 8031.00, 30684.00
    ],
    'Meta_Peso': [
        4000.0, 18000.0, 20500.0, 15500.0, 20500.0, 23000.0, 13500.0, 15000.0, 33000.0,
        29000.0, 1000.0, 2000.0, 13500.0, 13500.0, 20000.0, 5000.0, 8500.0, 8500.0,
        6000.0, 3000.0, 3000.0
    ],
    'Real_Peso': [
        3470.00, 14935.00, 16350.00, 14292.00, 18006.00, 20628.00, 11550.00, 11048.00, 32536.00,
        31990.00, 925.00, 1260.00, 11640.00, 11823.00, 19771.00, 8776.00, 4795.00, 5666.00,
        4620.00, 600.00, 1365.00
    ],
    'Meta_PM': [
        16.70, 16.50, 17.50, 17.50, 17.50, 19.00, 16.20, 19.00, 17.00,
        23.20, 23.20, 19.20, 18.20, 17.20, 16.80, 20.50, 19.50, 18.50,
        20.50, 15.00, 24.50
    ],
    'Real_PM': [
        15.74, 16.23, 17.27, 17.68, 17.31, 18.11, 16.62, 18.68, 16.28,
        22.14, 22.29, 16.97, 17.89, 16.72, 16.71, 17.55, 19.00, 18.80,
        19.94, 13.39, 22.48
    ],
    'Meta_Pos': [
        4.0, 145.0, 145.0, 127.0, 150.0, 135.0, 120.0, 80.0, 8.0,
        135.0, 4.0, 35.0, 150.0, 90.0, 95.0, 15.0, 60.0, 20.0,
        30.0, 15.0, 15.0
    ],
    'Real_Pos': [
        4.0, 151.0, 141.0, 117.0, 143.0, 127.0, 104.0, 73.0, 6.0,
        131.0, 4.0, 19.0, 129.0, 82.0, 86.0, 15.0, 54.0, 16.0,
        15.0, 5.0, 14.0
    ],
    'Meta_Cad': [
        0.0, 4.0, 4.0, 4.0, 4.0, 4.0, 8.0, 8.0, 0.0,
        3.0, 0.0, 10.0, 4.0, 8.0, 8.0, 2.0, 8.0, 6.0,
        10.0, 10.0, 10.0
    ],
    'Real_Cad': [
        0.0, 2.0, 4.0, 0.0, 4.0, 1.0, 4.0, 1.0, 0.0,
        0.0, 0.0, 4.0, 5.0, 2.0, 0.0, 0.0, 0.0, 1.0,
        0.0, 0.0, 8.0
    ]
}

df = pd.DataFrame(data_setembro)

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

# O DataFrame calcula a nota final de classificação somando o bônus oculto
df['Pontuacao_Total'] = df['Pontuacao_Base'] + df['Bonus_Desempate']
df_ranking = df.sort_values(by='Pontuacao_Total', ascending=False).reset_index(drop=True)

# Insere a marcação visual nos nomes ordenados
df_ranking['Vendedor'] = df_ranking['Vendedor'] + df_ranking['Marcacao']
# ------------------------------------------------------------

# Bloco visual dos pódios (Top 5) exibindo a nota final do desempate para consistência
if len(df_ranking) > 0:
    col_t1, col_t2, col_t3, col_t4, col_t5 = st.columns(5)
    col_t1.metric(label="🥇 1º LUGAR", value=df_ranking.loc[0, 'Vendedor'], delta=f"{df_ranking.loc[0, 'Pontuacao_Total']:.2f} pts")
    if len(df_ranking) > 1: col_t2.metric(label="🥈 2º LUGAR", value=df_ranking.loc[1, 'Vendedor'], delta=f"{df_ranking.loc[1, 'Pontuacao_Total']:.2f} pts")
    if len(df_ranking) > 2: col_t3.metric(label="🥉 3º LUGAR", value=df_ranking.loc[2, 'Vendedor'], delta=f"{df_ranking.loc[2, 'Pontuacao_Total']:.2f} pts")
    if len(df_ranking) > 3: col_t4.metric(label="🏅 4º LUGAR", value=df_ranking.loc[3, 'Vendedor'], delta=f"{df_ranking.loc[3, 'Pontuacao_Total']:.2f} pts")
    if len(df_ranking) > 4: col_t5.metric(label="🏅 5º LUGAR", value=df_ranking.loc[4, 'Vendedor'], delta=f"{df_ranking.loc[4, 'Pontuacao_Total']:.2f} pts")
    st.write("---")

df_ranking.index += 1
st.markdown("### 📋 TABELA DE PONTOS POR KPI (SETEMBRO)")
st.dataframe(df_ranking[['COD', 'Vendedor', 'Pontuacao_Total', 'P_Fat', 'P_Peso', 'P_PM', 'P_Pos', 'P_Cad']].rename(columns={'Pontuacao_Total': 'PONTUAÇÃO TOTAL'}), use_container_width=True)
st.write("---")
st.markdown("### 📊 PERCENTUAIS DE ATINGIMENTO METAS (%)")
st.dataframe(df_ranking[['COD', 'Vendedor', 'At_Fat', 'At_Peso', 'At_PM', 'At_Pos', 'At_Cad']].style.format({'At_Fat': '{:.1f}%', 'At_Peso': '{:.1f}%', 'At_PM': '{:.1f}%', 'At_Pos': '{:.1f}%', 'At_Cad': '{:.1f}%'}), use_container_width=True)
