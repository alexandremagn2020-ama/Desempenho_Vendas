import pandas as pd
import numpy as np
import streamlit as st
import auth

auth.validar_senha()  # bloqueia se não tiver senha correta

st.markdown("## Conteúdo da página Quadrimestre")

# Base de metas
df_meta = pd.DataFrame({
    'COD': [80001,80002,80003,80005,80006,80007,80010,80011,80012,80021,
            80022,80039,80048,80052,80053,80055,80057,80058,80060,80061],
    'Meta_Peso': [17000,70000,81000,65000,80000,91000,48500,60000,115500,105000,
                  4000,17500,54500,51500,69500,37500,5000,24000,18000,12000],
    'Meta_Fat': [318880,1171100,1381200,1136600,1396000,1658500,751750,1132500,2315350,2535200,
                 96000,348750,967250,860500,1293350,664000,90000,479800,331200,241500],
    'Meta_PM': [18.76,16.73,17.05,17.48,17.45,18.23,15.50,18.88,20.05,24.15,
                24.00,19.75,17.75,16.70,18.60,17.75,18.00,20.08,18.40,20.15],
    'Meta_Pos': [20,563,578,494,592,525,444,286,39,439,
                 17,105,552,370,366,63,5,180,42,47],
    'Meta_Cad': [0,12,11,20,13,17,33,40,0,6,
                 1,40,14,30,30,3,5,25,25,10]
})

# Base de realizados
df_real = pd.DataFrame({
    'COD': [80001,80002,80003,80005,80006,80007,80010,80011,80012,80021,
            80022,80039,80048,80052,80053,80055,80057,80058,80060,80061],
    'Vendedor': ['Homologação','Carlos','Valdinei','Luiz','Wesley','Celio','Helio','Raimundo','Mauricio',
                 'Rota BH','Rota BH (Int)','Frederico','Flavio','Wanderson','Daniel','Mauricio Jr',
                 'Gilbert','Natalia','Janete','RPA'],
    'Real_Peso': [14180,67825,73275,56720,73149,87924,45028,50418,115611.5,102832,
                  2825,4203,47402,47751,63168,38206,530,19999,9969,5370],
    'Real_Fat': [254754.4,1091928,1232846.85,970745.58,1251693.4,1590120.7,687613.8,932907.49,2280576.7,2471894.88,
                 66186,79820.22,830930.82,806371.35,988358.3,667041.86,6598,395428.14,182194.05,113946.15],
    'Real_PM': [17.97,16.10,16.82,17.11,17.11,18.09,15.27,18.50,19.73,24.04,
                23.43,18.99,17.53,16.89,15.65,17.46,12.45,19.77,18.28,21.22],
    'Real_Pos': [17,570,579,487,591,512,451,278,72,458,
                 16,82,589,354,335,61,2,143,23,50],
    'Real_Cad': [0,2,15,11,21,9,18,10,10,10,
                 0,19,17,11,10,1,0,38,13,18]
})

# Junta metas + realizados
df = df_meta.merge(df_real, on='COD')

# Categorias especiais
codigos_filtrados = [80012,80021,80055,80061,80022,80001,80057]
df['Categoria'] = np.where(df['COD'].isin(codigos_filtrados),'Especiais','Padrao')

mostrar_especiais = st.sidebar.checkbox("Mostrar Rotas Especiais / Homologação", value=True)
if not mostrar_especiais:
    df = df[df['Categoria']=='Padrao'].reset_index(drop=True)

# Percentuais de atingimento
df['At_Fat'] = (df['Real_Fat']/df['Meta_Fat'])*100
df['At_Peso'] = (df['Real_Peso']/df['Meta_Peso'])*100
df['At_PM'] = (df['Real_PM']/df['Meta_PM'])*100
df['At_Pos'] = (df['Real_Pos']/df['Meta_Pos'])*100
df['At_Cad'] = np.where(df['Meta_Cad']<=1.0,
                        np.where(df['Real_Cad']>0,115.0,0.0),
                        (df['Real_Cad']/df['Meta_Cad'])*100)

# Função de pontuação
def calcular_pontos_faixa(ating, pt90, pt100, pt110):
    if ating < 90.0: return 0.0
    elif ating < 100.0: return float(pt90)
    elif ating < 110.0: return float(pt100)
    else: return float(pt110)

# Aplicação das regras
df['P_Fat'] = df['At_Fat'].apply(lambda x: calcular_pontos_faixa(x,5,10,15))
df['P_Peso'] = df['At_Peso'].apply(lambda x: calcular_pontos_faixa(x,5,10,15))
df['P_PM'] = df['At_PM'].apply(lambda x: calcular_pontos_faixa(x,10,15,20))
df['P_Pos'] = df['At_Pos'].apply(lambda x: calcular_pontos_faixa(x,5,7.5,10))
df['P_Cad'] = df['At_Cad'].apply(lambda x: calcular_pontos_faixa(x,5,7.5,10))

df['Pontuacao_Total'] = df['P_Fat']+df['P_Peso']+df['P_PM']+df['P_Pos']+df['P_Cad']
df_ranking = df.sort_values(by='Pontuacao_Total',ascending=False).reset_index(drop=True)

# Ranking visual
if len(df_ranking)>0:
    col_t1,col_t2,col_t3,col_t4,col_t5 = st.columns(5)
    col_t1.metric("🥇 1º LUGAR",df_ranking.loc[0,'Vendedor'],f"{df_ranking.loc[0,'Pontuacao_Total']:.2f} pts")
    if len(df_ranking)>1: col_t2.metric("🥈 2º LUGAR",df_ranking.loc[1,'Vendedor'],f"{df_ranking.loc[1,'Pontuacao_Total']:.2f} pts")
    if len(df_ranking)>2: col_t3.metric("🥉 3º LUGAR",df_ranking.loc[2,'Vendedor'],f"{df_ranking.loc[2,'Pontuacao_Total']:.2f} pts")
    if len(df_ranking)>3: col_t4.metric("🏅 4º LUGAR",df_ranking.loc[3,'Vendedor'],f"{df_ranking.loc[3,'Pontuacao_Total']:.2f} pts")
    if len(df_ranking)>4: col_t5.metric("🏅 5º LUGAR",df_ranking.loc[4,'Vendedor'],f"{df_ranking.loc[4,'Pontuacao_Total']:.2f} pts")
    st.write("---")

df_ranking.index += 1
st.markdown("### 📋 TABELA DE PONTOS POR KPI")
st.dataframe(df_ranking[['COD','Vendedor','Pontuacao_Total','P_Fat','P_Peso','P_PM','P_Pos','P_Cad']].rename(columns={'Pontuacao_Total':'PONTUAÇÃO TOTAL'}),use_container_width=True)

st.write("---")
st.markdown("### 📊 PERCENTUAIS DE ATINGIMENTO METAS (%)")
st.dataframe(df_ranking[['COD','Vendedor','At_Fat','At_Peso','At_PM','At_Pos','At_Cad']].
