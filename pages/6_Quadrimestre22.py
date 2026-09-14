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

# Configuração Master de Controle de Códigos e Filtros (Padrão Oficial de Julho)
texto_master = ["80001", "80002", "80003", "80005", "80006", "80007", "80010", "80011", "80012", "80021", "80022", "80039", "80048", "80052", "80053", "80055", "80058", "80060", "80061", "80062", "80063"]
texto_filtrados = ["80012", "80021", "80055", "80061", "80022", "80001"]

lista_codigos = list(map(int, texto_master))
codigos_filtrados = list(map(int, texto_filtrados))

# Matrizes de Dados Brutos (Linhas = Vendedores na ordem master, Colunas = Maio, Junho, Julho, Agosto)
m_fat_meta = np.array([[56400,75200,66000,4000],[324000,309700,321750,20000],[348500,359100,369800,22000],[292400,288750,306000,17500],[369800,350000,358750,21000],[441000,420900,430050,23000],[217000,208000,231000,14500],[274500,264600,291000,15500],[540000,522000,531000,30000],[672000,677600,696000,30000],[23500,23500,24000,1000],[54900,36800,36800,2500],[262500,230100,254800,15000],[255000,221000,232200,14000],[295200,310800,327600,20500],[82500,96000,99000,6500],[110400,131600,136500,7500],[92000,129500,133000,7500],[63000,126000,90000,5000],[36000,36000,63000,4000],[0,54000,63000,4000]], dtype=float)
m_fat_real = np.array([[54797.9,74925.55,55718.05,62535.55],[272753.4,332596.55,295068.75,231934.56],[310243.5,359158.15,366127.85,280827.15],[240808.16,298921.9,274562.55,239176.87],[303155.06,355375.55,351301.05,296503.56],[390857.55,441361.9,449714.35,381824.9],[183655.7,246593.55,229787.6,192627.1],[241545.44,294028.09,248830.65,239371.61],[510365.9,567145.65,699003.45,500078.2],[623626,685743,694983,614048.5],[13736,16573,21504,17342.5],[16695.4,23287.9,22047.5,25650.8],[219409.08,291925.09,253083.73,198311.6],[181683.75,231502.1,234078.1,177473.3],[280912.75,348788.25,325428.65,297853.4],[138636.3,142088.41,125716.23,108419.92],[101987.2,124658.8,148081.96,148120.59],[114774.59,117299.95,125980.47,81573.78],[96810.7,67634.1,81582.9,128520.8],[8610.5,19112.5,13399.5,9184],[0,13035,13823.5,20098]], dtype=float)

m_peso_meta = np.array([[3000,4000,4000,66.8],[20000,19000,19500,334],[20500,21000,21500,380.6],[17000,16500,17000,318.5],[21500,20000,20500,371.7],[24500,23000,23500,423.2],[14000,13000,14000,256.6],[15000,14000,15000,302.2],[30000,29000,29500,546],[28000,28000,29000,726],[1000,1000,1000,24.2],[3000,2000,2000,46.2],[15000,13000,14000,276],[15000,13000,13500,243.6],[18000,18500,19500,348.5],[5000,6000,6000,108.5],[6000,7000,7000,146.2],[5000,7000,7000,142.5],[3000,6000,4500,100],[2000,2000,3500,72.4],[0,3000,3500,72]], dtype=float)
m_peso_real = np.array([[3445,4660,3540,4000],[17060,20517,17990,14113],[18759,21019,21025,16553],[13981,16779,15340,13893],[17932,20655,20348,17156],[21625,24304,24251,20452],[11940,15285,14310,12490],[13015,15292,12887,13323],[29167,31966,39592,30207],[26045,28955,29216,27375],[575,705,890,755],[927,1315,1160,1360],[12512,16205,14007,11168],[10990,13568,13575,10625],[16940,21785,19490,17836],[8891,8783,6808,5388],[5711,6457,7583,7937],[6362,6256,6489,4661],[4695,3510,3940,6350],[615,1130,855,690],[0,510,580,830]], dtype=float)

m_pm_meta = np.array([[18.8,18.8,16.5,16.7],[16.2,16.3,16.5,16.7],[17,17.1,17.2,17.3],[17.2,17.5,18,18.2],[17.2,17.5,17.5,17.7],[18,18.3,18.3,18.4],[15.5,16,16.5,17.7],[18.3,18.9,19.4,19.5],[18,18,18,18.2],[24,24.2,24,24.2],[23.5,23.5,24,24.2],[18.3,18.4,18.4,18.5],[17.5,17.7,18.2,18.4],[17,17,17.2,17.4],[16.4,16.8,16.8,17],[16.5,16,16.5,16.7],[18.4,18.8,19.5,19.5],[18.4,18.5,19,19],[21,21,20,20],[18,18,18,18.1],[0,18,18,18]], dtype=float)
m_pm_real = np.array([[15.91,16.08,15.74,15.63],[15.99,16.21,16.4,14.113],[16.54,17.09,17.41,16.97],[17.22,17.82,17.9,17.22],[16.91,17.21,17.26,17.28],[18.07,18.16,18.54,18.67],[15.38,16.13,16.06,15.42],[18.56,19.23,19.31,17.97],[17.5,17.74,17.66,16.56],[23.94,23.68,23.79,22.43],[23.89,23.51,24.16,22.97],[18.01,17.71,19.01,18.86],[17.54,18.01,18.07,17.76],[16.53,17.06,17.24,16.7],[16.58,16.01,16.7,16.7],[15.59,16.18,18.47,20.12],[17.86,19.31,19.53,18.66],[18.04,18.75,19.41,17.50],[20.62,19.27,20.71,20.24],[14,16.91,15.67,13.31],[0,25.56,23.83,24.21]], dtype=float)

m_pos_meta = np.array([[4,4,4,4],[145,146,149,150],[149,150,150,151],[125,128,130,131],[153,154,154,155],[135,138,138,140],[116,117,122,125],[75,80,80,85],[8,8,8,8],[120,120,125,125],[4,4,4,4],[40,45,40,45],[150,152,155,153],[95,100,100,105],[95,100,100,105],[10,10,15,15],[55,60,60,65],[15,20,15,15],[35,45,45,50],[15,15,12,15],[0,5,12,15]], dtype=float)
m_pos_real = np.array([[4,4,4,4],[143,151,135,142],[144,143,147,141],[122,126,124,121],[142,147,147,142],[128,127,128,128],[113,121,107,104],[69,75,71,73],[9,8,10,7],[117,123,122,130],[4,4,4,4],[20,18,139,18],[143,158,139,145],[89,92,89,82],[83,84,83,88],[14,15,15,15],[50,54,60,59],[12,11,16,15],[40,16,17,18],[9,9,9,8],[0,3,9,4]], dtype=float)

m_cad_meta = np.array([[0,0,0,0],[3,4,4,4],[2,4,4,4],[4,4,4,4],[2,4,4,4],[4,4,4,4],[8,8,8,8],[8,8,8,8],[0,0,0,0],[0,0,0,0],[0,0,0,0],[10,10,10,10],[2,4,4,4],[8,8,8,8],[8,8,8,8],[0,0,2,2],[8,8,8,8],[5,8,6,6],[10,10,10,10],[10,10,10,10],[0,10,10,10]], dtype=float)
m_cad_real = np.array([[0,0,0,0],[3,1,3,0],[3,3,1,2],[1,1,3,0],[2,3,3,3],[0,0,2,0],[3,5,2,0],[1,1,0,0],[1,0,1,0],[1,6,1,0],[0,0,0,0],[4,4,2,1],[3,4,1,0],[0,4,1,2],[1,1,2,0],[0,0,0,0],[8,8,5,1],[1,0,2,0],[13,1,0,0],[2,1,1,1],[0,2,2,0]], dtype=float)
# Geração do DataFrame estrutural somando de forma fidedigna as linhas (Eixo das Colunas)
df = pd.DataFrame()
df['COD'] = lista_codigos
df['Vendedor'] = [
    'VENDEDOR PARA HOMOLOGAÇÃO', 'CARLOS EDUARDO PEREIRA DA CRUZ', 'VALDINEI LUIZ PAIVA', 
    'LUIZ CARLOS SILVA NEVES', 'WESLEY FRANCIS DE JESUS LOPES', 'CELIO CLAUDIO OLIVEIRA', 
    'HELIO ALMEIDA VIANA', 'RAIMUNDO ALEX BARBOSA', 'MAURICIO SIMÕES JORGE', 'Rota BH', 
    'Rota BH - Interior de Minas', 'FREDERICO', 'FLAVIO CRISTIANO CARDOSO', 'WANDERSON DA SILVA LIMA', 
    'DANIEL DE PAULA', 'MAURICIO MARQUES DA SILVA JUNIOR', 'NATALIA FATIMA', 'JANETE CIRILO', 
    'RPA', 'Tallison Augusto de Oliveira', 'VENDEDOR 80063'
]

# Somas Acumuladas Puras por Linha (Eixo 1)
df['Meta_Fat'] = np.sum(m_fat_meta, axis=1)
df['Real_Fat'] = np.sum(m_fat_real, axis=1)
df['Meta_Peso'] = np.sum(m_peso_meta, axis=1)
df['Real_Peso'] = np.sum(m_peso_real, axis=1)
df['Meta_Pos'] = np.sum(m_pos_meta, axis=1)
df['Real_Pos'] = np.sum(m_pos_real, axis=1)
df['Meta_Cad'] = np.sum(m_cad_meta, axis=1)
df['Real_Cad'] = np.sum(m_cad_real, axis=1)

# Média fidedigna de Preço Médio (PM) dos meses ativos
df['Meta_PM'] = np.mean(m_pm_meta, axis=1)
df['Real_PM'] = np.mean(m_pm_real, axis=1)

# ✂️ Filtro para deixar apenas o Primeiro Nome de cada vendedor
df['Vendedor'] = df['Vendedor'].apply(lambda x: str(x).split() if str(x).strip() else "")

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
