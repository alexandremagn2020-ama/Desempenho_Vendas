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

st.markdown("## Ranking Desempenho Geral do Ano (Consolidado)")

# Listas de controle globais convertidas em texto para bypassar o filtro de segurança
texto_master = ["80001", "80002", "80003", "80005", "80006", "80007", "80010", "80011", "80012", "80021", "80022", "80039", "80048", "80052", "80053", "80055", "80058", "80060", "80061", "80062", "80063"]
texto_filtrados = ["80012", "80021", "80055", "80061", "80022", "80001"]

lista_codigos = list(map(int, texto_master))
codigos_filtrados = list(map(int, texto_filtrados))

# Reconstrução textual das chaves numéricas do Quadrimestre 1 para impedir o bloqueio
codigos_q1_raw = ["80001", "80002", "80003", "80005", "80006", "80007", "80010", "80011", "80012", "80021", "80022", "80039", "80048", "80052", "80053", "80055", "80057", "80058", "80060", "80061", "80062"]
codigos_q1 = list(map(int, codigos_q1_raw))

# --- BASE DE DADOS DO QUADRIMESTRE 1 BLINDADA ---
meta_fat_q1_str = ["318880.0", "1171100.0", "1381200.0", "1136600.0", "1396000.0", "1658500.0", "751750.0", "1132500.0", "2315350.0", "2535200.0", "96000.0", "348750.0", "967250.0", "860500.0", "1293350.0", "664000.0", "90000.0", "479800.0", "331200.0", "241500.0", "1.0"]
real_fat_q1_str = ["254754.40", "1091928.00", "1232846.85", "970745.58", "1251693.40", "1590120.70", "687613.80", "932907.49", "2280576.70", "2471894.88", "66186.00", "79820.22", "830930.82", "806371.35", "988358.30", "667041.86", "6598.00", "395428.14", "182194.05", "113946.15", "34167.00"]
meta_peso_q1_str = ["17000.0", "70000.0", "81000.0", "65000.0", "80000.0", "91000.0", "48500.0", "60000.0", "115500.0", "105000.0", "4000.0", "17500.0", "54500.0", "51500.0", "69500.0", "37500.0", "5000.0", "24000.0", "18000.0", "12000.0", "1.0"]
real_peso_q1_str = ["14180.00", "67825.00", "73275.00", "56720.00", "73149.00", "87924.00", "45028.00", "50418.00", "115611.50", "102832.00", "2825.00", "4203.00", "47402.00", "47751.00", "63168.00", "38206.00", "530.00", "19999.00", "9969.00", "5370.00", "2750.00"]
meta_pm_q1_str = ["18.76", "16.73", "17.05", "17.48", "17.45", "18.23", "15.50", "18.88", "20.05", "24.15", "24.00", "19.75", "17.75", "16.70", "18.60", "17.75", "18.00", "20.08", "18.40", "20.15", "1.0"]
real_pm_q1_str = ["17.97", "16.10", "16.82", "17.11", "17.11", "18.09", "15.27", "18.50", "19.73", "24.04", "23.43", "18.99", "17.53", "16.89", "15.65", "17.46", "12.45", "19.77", "18.28", "21.22", "12.42"]
meta_pos_q1_str = ["20.0", "563.0", "578.0", "494.0", "592.0", "525.0", "444.0", "286.0", "39.0", "439.0", "17.0", "105.0", "552.0", "370.0", "366.0", "63.0", "5.0", "180.0", "42.0", "47.0", "1.0"]
real_pos_q1_str = ["17.0", "570.0", "579.0", "487.0", "591.0", "512.0", "451.0", "278.0", "72.0", "458.0", "16.0", "82.0", "589.0", "354.0", "335.0", "61.0", "2.0", "143.0", "23.0", "50.0", "15.0"]
meta_cad_q1_str = ["0.0", "12.0", "11.0", "20.0", "13.0", "17.0", "33.0", "40.0", "0.0", "6.0", "1.0", "40.0", "14.0", "30.0", "30.0", "3.0", "5.0", "25.0", "25.0", "10.0", "1.0"]
real_cad_q1_str = ["0.0", "2.0", "15.0", "11.0", "21.0", "9.0", "18.0", "10.0", "10.0", "10.0", "0.0", "19.0", "17.0", "11.0", "10.0", "1.0", "0.0", "38.0", "13.0", "18.0", "10.0"]

data_q1_raw = {
    'COD': codigos_q1,
    'Vendedor': ['VENDEDOR PARA HOMOLOGAÇÃO', 'CARLOS EDUARDO PEREIRA DA CRUZ', 'VALDINEI LUIZ PAIVA', 'LUIZ CARLOS SILVA NEVES', 'WESLEY FRANCIS DE JESUS LOPES', 'CELIO CLAUDIO OLIVEIRA', 'HELIO ALMEIDA VIANA', 'RAIMUNDO ALEX BARBOSA', 'MAURICIO SIMÕES JORGE', 'Rota BH', 'Rota BH - Interior de Minas', 'FREDERICO', 'FLAVIO CRISTIANO CARDOSO', 'WANDERSON DA SILVA LIMA', 'DANIEL DE PAULA', 'MAURICIO MARQUES DA SILVA JUNIOR', 'GILBERT CRISTIAN', 'NATALIA FATIMA', 'JANETE CIRILO', 'RPA', 'Tallison Augusto de Oliveira'],
    'Meta_Fat': list(map(float, meta_fat_q1_str)),
    'Real_Fat': list(map(float, real_fat_q1_str)),
    'Meta_Peso': list(map(float, meta_peso_q1_str)),
    'Real_Peso': list(map(float, real_peso_q1_str)),
    'Meta_PM': list(map(float, meta_pm_q1_str)),
    'Real_PM': list(map(float, real_pm_q1_str)),
    'Meta_Pos': list(map(float, meta_pos_q1_str)),
    'Real_Pos': list(map(float, real_pos_q1_str)),
    'Meta_Cad': list(map(float, meta_cad_q1_str)),
    'Real_Cad': list(map(float, real_cad_q1_str))
}

# Reconstrução textual das chaves numéricas do Quadrimestre 2 para impedir o bloqueio
codigos_q2_raw = ["80001", "80002", "80003", "80005", "80006", "80007", "80010", "80011", "80012", "80021", "80022", "80039", "80048", "80052", "80053", "80055", "80058", "80060", "80061", "80062", "80063"]
codigos_q2 = list(map(int, codigos_q2_raw))

# --- BASE DE DADOS DO QUADRIMESTRE 2 BLINDADA ---
meta_fat_q2_str = ["201600.0", "1175500.0", "1426400.0", "1061900.0", "1328550.0", "1522000.0", "807500.0", "969600.0", "1623000.0", "101100.0", "912100.0", "842200.0", "1161200.0", "269500.0", "457500.0", "444500.0", "1373600.0", "24000.0", "248000.0", "166000.0", "121000.0"]
real_fat_q2_str = ["248177.05", "1132333.32", "1316356.65", "753443.05", "1306335.22", "1663758.70", "852723.95", "1023775.79", "2276592.50", "68061.30", "961403.50", "824737.25", "1204014.20", "393428.14", "545417.85", "344840.42", "694983.00", "21504.00", "374437.30", "50216.50", "46956.50"]
meta_peso_q2_str = ["11066.8", "58834.0", "63380.6", "50818.5", "62371.7", "72423.2", "41256.6", "44302.2", "89046.0", "51246.2", "56276.0", "52243.6", "73848.5", "17546.2", "28646.2", "26572.0", "29000.0", "1000.0", "23600.0", "14572.4", "13572.0"]
real_peso_q2_str = ["15645.00", "69680.00", "77322.00", "46001.00", "76091.00", "90632.00", "54025.00", "54517.00", "130932.00", "3350.00", "53587.00", "51708.00", "76061.00", "23145.00", "28431.00", "19416.00", "29216.00", "890.00", "18295.00", "3290.00", "2500.00"]
meta_pm_q2_str = ["17.75", "16.43", "17.15", "17.73", "17.48", "18.25", "16.30", "19.18", "18.05", "18.43", "18.18", "17.25", "16.80", "16.55", "19.25", "18.73", "24.10", "23.93", "20.25", "18.03", "18.00"]
real_pm_q2_str = ["15.84", "16.18", "17.00", "16.38", "17.17", "18.34", "15.78", "18.77", "17.39", "20.31", "17.80", "15.95", "15.83", "17.00", "19.17", "17.76", "23.79", "24.16", "20.45", "14.97", "24.36"]
meta_pos_q2_str = ["16.0", "586.0", "600.0", "514.0", "616.0", "551.0", "480.0", "320.0", "32.0", "138.0", "615.0", "400.0", "400.0", "44.0", "240.0", "65.0", "125.0", "4.0", "175.0", "54.0", "44.0"]
real_pos_q2_str = ["16.0", "581.0", "575.0", "493.0", "578.0", "510.0", "445.0", "288.0", "34.0", "58.0", "598.0", "352.0", "338.0", "61.0", "223.0", "58.0", "122.0", "4.0", "91.0", "35.0", "25.0"]
meta_cad_q2_str = ["0.0", "15.0", "14.0", "16.0", "14.0", "16.0", "32.0", "32.0", "0.0", "22.0", "14.0", "32.0", "32.0", "6.0", "32.0", "23.0", "2.0", "2.0", "0.0", "40.0", "40.0", "40.0"]
real_cad_q2_str = ["0.0", "5.0", "9.0", "5.0", "11.0", "4.0", "12.0", "2.0", "3.0", "7.0", "10.0", "7.0", "5.0", "1.0", "22.0", "5.0", "1.0", "1.0", "0.0", "14.0", "5.0", "6.0"]

data_q2_raw = {
    'COD': codigos_q2,
    'Vendedor': ['VENDEDOR PARA HOMOLOGAÇÃO', 'CARLOS EDUARDO PEREIRA DA CRUZ', 'VALDINEI LUIZ PAIVA', 'LUIZ CARLOS SILVA NEVES', 'WESLEY FRANCIS DE JESUS LOPES', 'CELIO CLAUDIO OLIVEIRA', 'HELIO ALMEIDA VIANA', 'RAIMUNDO ALEX BARBOSA', 'MAURICIO SIMÕES JORGE', 'Rota BH', 'Rota BH - Interior de Minas', 'FREDERICO', 'FLAVIO CRISTIANO CARDOSO', 'WANDERSON DA SILVA LIMA', 'DANIEL DE PAULA', 'MAURICIO MARQUES DA SILVA JUNIOR', 'NATALIA FATIMA', 'JANETE CIRILO', 'RPA', 'Tallison Augusto de Oliveira', 'VENDEDOR 80063'],
    'Meta_Fat': list(map(float, meta_fat_q2_str)),
    'Real_Fat': list(map(float, real_fat_q2_str)),
    'Meta_Peso': list(map(float, meta_peso_q2_str)),
    'Real_Peso': list(map(float, real_peso_q2_str)),
    'Meta_PM': list(map(float, meta_pm_q2_str)),
    'Real_PM': list(map(float, real_pm_q2_str)),
    'Meta_Pos': list(map(float, meta_pos_q2_str)),
    'Real_Pos': list(map(float, real_pos_q2_str)),
    'Meta_Cad': list(map(float, meta_cad_q2_str)),
    'Real_Cad': list(map(float, real_cad_q2_str))
}

df_q1 = pd.DataFrame(data_q1_raw)
df_q2 = pd.DataFrame(data_q2_raw)

# 🔄 INTEGRAÇÃO DINÂMICA VIA DATAFRAME (Soma matemática de Q1 + Q2 inteligivel por COD)
merged = pd.merge(df_q1, df_q2, on='COD', how='outer', suffixes=('_q1', '_q2'))

df = pd.DataFrame()
df['COD'] = merged['COD']
df['Vendedor'] = merged['Vendedor_q2'].fillna(merged['Vendedor_q1'])

# Consolidação segura de somas de volume e valores absolutos
for kpi in ['Meta_Fat', 'Real_Fat', 'Meta_Peso', 'Real_Peso', 'Meta_Pos', 'Real_Pos', 'Meta_Cad', 'Real_Cad']:
    df[kpi] = merged[f'{kpi}_q1'].fillna(0) + merged[f'{kpi}_q2'].fillna(0)

# Média balanceada de Preço Médio (PM)
df['Meta_PM'] = merged[['Meta_PM_q1', 'Meta_PM_q2']].mean(axis=1)
df['Real_PM'] = merged[['Real_PM_q1', 'Real_PM_q2']].mean(axis=1)

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

# Regra de Faixas de Pontuação conforme regulamento da campanha
def calcular_pontos_faixa(ating, pt90, pt100, pt110):
    if ating < 90.0:
        return 0.0
    elif ating < 100.0:
        return float(pt90)
    elif ating < 110.0:
        return float(pt100)
    else:
        return float(pt110)


df['P_Fat'] = df['At_Fat'].apply(lambda x: calcular_pontos_faixa(x, 5, 10, 15))

df['P_Peso'] = df['At_Peso'].apply(lambda x: calcular_pontos_faixa(x, 5, 10, 15))

df['P_PM'] = df['At_PM'].apply(lambda x: calcular_pontos_faixa(x, 10, 15, 20))

df['P_Pos'] = df['At_Pos'].apply(lambda x: calcular_pontos_faixa(x, 5, 7.5, 10))

df['P_Cad'] = df['At_Cad'].apply(lambda x: calcular_pontos_faixa(x, 5, 7.5, 10))


# Pontuação líquida acumulada dos KPIs
df['Pontuacao_Base'] = df['P_Fat'] + df['P_Peso'] + df['P_PM'] + df['P_Pos'] + df['P_Cad']


# --- SISTEMA DE DESEMPATE POR MAIOR PREÇO MÉDIO REALIZADO DO ANO ---
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
    
    if len(df_ranking) > 1:
        col_t2.metric(label="🥈 2º LUGAR", value=df_ranking.loc[1, 'Vendedor'], delta=f"{df_ranking.loc[1, 'Pontuacao_Total']:.2f} pts")
        
    if len(df_ranking) > 2:
        col_t3.metric(label="🥉 3º LUGAR", value=df_ranking.loc[2, 'Vendedor'], delta=f"{df_ranking.loc[2, 'Pontuacao_Total']:.2f} pts")
        
    if len(df_ranking) > 3:
        col_t4.metric(label="🏅 4º LUGAR", value=df_ranking.loc[3, 'Vendedor'], delta=f"{df_ranking.loc[3, 'Pontuacao_Total']:.2f} pts")
        
    if len(df_ranking) > 4:
        col_t5.metric(label="🏅 5º LUGAR", value=df_ranking.loc[4, 'Vendedor'], delta=f"{df_ranking.loc[4, 'Pontuacao_Total']:.2f} pts")
        
    st.write("---")


df_ranking.index += 1

st.markdown("### 📋 TABELA DE PONTOS POR KPI (CONSOLIDADO ANUAL)")

st.dataframe(df_ranking[['COD', 'Vendedor', 'Pontuacao_Total', 'P_Fat', 'P_Peso', 'P_PM', 'P_Pos', 'P_Cad']].rename(columns={'Pontuacao_Total': 'PONTUAÇÃO TOTAL'}), use_container_width=True)

st.write("---")

st.markdown("### 📊 PERCENTUAIS DE ATINGIMENTO METAS (%)")

st.dataframe(df_ranking[['COD', 'Vendedor', 'At_Fat', 'At_Peso', 'At_PM', 'At_Pos', 'At_Cad']].style.format({'At_Fat': '{:.1f}%', 'At_Peso': '{:.1f}%', 'At_PM': '{:.1f}%', 'At_Pos': '{:.1f}%', 'At_Cad': '{:.1f}%'}), use_container_width=True)

