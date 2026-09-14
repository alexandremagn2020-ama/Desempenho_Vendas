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

# DADOS TOTAIS ACUMULADOS REALIZANDO A SOMA ABSOLUTA MÊS A MÊS DE MAIO, JUNHO, JULHO E AGOSTO
data_quadrimestre2 = {
    'COD': lista_codigos,
    'Vendedor': [
        'VENDEDOR PARA HOMOLOGAÇÃO', 'CARLOS EDUARDO PEREIRA DA CRUZ', 'VALDINEI LUIZ PAIVA', 
        'LUIZ CARLOS SILVA NEVES', 'WESLEY FRANCIS DE JESUS LOPES', 'CELIO CLAUDIO OLIVEIRA', 
        'HELIO ALMEIDA VIANA', 'RAIMUNDO ALEX BARBOSA', 'MAURICIO SIMÕES JORGE', 'Rota BH', 
        'Rota BH - Interior de Minas', 'FREDERICO', 'FLAVIO CRISTIANO CARDOSO', 'WANDERSON DA SILVA LIMA', 
        'DANIEL DE PAULA', 'MAURICIO MARQUES DA SILVA JUNIOR', 'NATALIA FATIMA', 'JANETE CIRILO', 
        'RPA', 'Tallison Augusto de Oliveira', 'VENDEDOR 80063'
    ],
    'Meta_Fat': [201600.0, 975450.0, 1100400.0, 904650.0, 1099550.0, 1315000.0, 670500.0, 845600.0, 1623000.0, 2075600.0, 72000.0, 131000.0, 762400.0, 722200.0, 954100.0, 284000.0, 385900.0, 361500.0, 284000.0, 107000.0, 121000.0],
    'Real_Fat': [248177.05, 1132333.32, 1316356.65, 1013469.49, 1306335.22, 1663758.70, 852723.95, 1023775.79, 2276592.50, 2618400.50, 68061.30, 88281.60, 961403.50, 824737.25, 1204014.20, 514863.07, 522850.55, 439628.79, 374437.30, 50216.50, 46956.50],
    'Meta_Peso': [11066.8, 58834.0, 63380.6, 50818.5, 62371.7, 72423.2, 41256.6, 44302.2, 89046.0, 114000.0, 4024.2, 7046.2, 56276.0, 52243.6, 73848.5, 22108.5, 27646.2, 26142.5, 23600.0, 11572.4, 13572.0],
    'Real_Peso': [15645.00, 69680.00, 77322.00, 60014.00, 76091.00, 90632.00, 54025.00, 54517.00, 130932.00, 111591.00, 3350.00, 4762.00, 53587.00, 51708.00, 76061.00, 29870.00, 30208.00, 23788.00, 16055.00, 3290.00, 2500.00],
    'Meta_PM': [17.70, 16.43, 17.15, 17.73, 17.48, 18.25, 16.43, 19.03, 18.05, 24.10, 23.80, 18.40, 17.95, 17.10, 16.75, 16.30, 19.05, 18.73, 20.50, 18.03, 18.00],
    'Real_PM': [15.82, 16.18, 17.00, 16.89, 17.17, 18.34, 15.78, 18.77, 17.39, 23.46, 20.31, 18.40, 17.80, 15.95, 15.83, 17.16, 19.17, 17.76, 23.79, 14.97, 24.36],
    'Meta_Pos': [16.0, 586.0, 600.0, 512.0, 616.0, 551.0, 480.0, 320.0, 32.0, 490.0, 16.0, 170.0, 610.0, 400.0, 400.0, 50.0, 240.0, 65.0, 175.0, 54.0, 44.0],
    'Real_Pos': [16.0, 581.0, 575.0, 493.0, 578.0, 510.0, 445.0, 288.0, 34.0, 492.0, 16.0, 74.0, 598.0, 352.0, 338.0, 59.0, 223.0, 54.0, 91.0, 35.0, 25.0],
    'Meta_Cad': [0.0, 15.0, 14.0, 16.0, 14.0, 16.0, 32.0, 32.0, 0.0, 4.0, 0.0, 40.0, 14.0, 32.0, 32.0, 4.0, 32.0, 25.0, 40.0, 40.0, 40.0],
    'Real_Cad': [0.0, 5.0, 9.0, 5.0, 11.0, 4.0, 12.0, 2.0, 3.0, 8.0, 0.0, 11.0, 10.0, 7.0, 5.0, 0.0, 22.0, 3.0, 14.0, 5.0, 6.0]
}

df = pd.DataFrame(data_quadrimestre2)

# ✂️ Filtro para deixar apenas o Primeiro Nome de cada vendedor
df['Vendedor'] = df['Vendedor'].apply(lambda x: str(x).split()[0] if str(x).strip() else "")

df['Categoria'] = np.where(df['COD'].isin(codigos_filtrados), 'Especiais', 'Padrao')

mostrar_especiais = st.sidebar.checkbox("Mostrar Todos Vendedores", value=False)
if not mostrar_especiais:
    df = df[df['Categoria'] == 'Padrao'].reset_index(drop=True)

# Cálculo de Atingimento (%) com base nas somas exatas acumuladas
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
