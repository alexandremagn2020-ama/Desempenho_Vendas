import pandas as pd
import numpy as np
import streamlit as st
import auth

auth.validar_senha()

try:
    st.sidebar.image("logo.png", use_container_width=True)
except Exception:
    st.sidebar.warning("⚠️ Arquivo 'logo.png' não encontrado.")

st.markdown("## Ranking Desempenho do Quadrimestre 2 (Soma Absoluta de Pontos)")

txt_m = ["80001", "80002", "80003", "80005", "80006", "80007", "80010", "80011", "80012", "80021", "80022", "80039", "80048", "80052", "80053", "80055", "80058", "80060", "80061", "80062", "80063"]
txt_f = ["80012", "80021", "80055", "80061", "80022", "80001"]
lista_codigos = list(map(int, txt_m))
codigos_filtrados = list(map(int, txt_f))

cod_maio = list(map(int, ["80001", "80002", "80003", "80005", "80006", "80007", "80010", "80011", "80012", "80021", "80022", "80039", "80048", "80052", "80053", "80055", "80058", "80060", "80061", "80062"]))

df_maio = pd.DataFrame({
    'COD': cod_maio,
    'Meta_Fat': list(map(float, ["56400.0", "324000.0", "348500.0", "292400.0", "369800.0", "441000.0", "217000.0", "274500.0", "540000.0", "672000.0", "23500.0", "54900.0", "262500.0", "255000.0", "295200.0", "82500.0", "110400.0", "92000.0", "63000.0", "36000.0"])),
    'Real_Fat': list(map(float, ["54797.90", "272753.40", "310243.50", "240808.16", "303155.06", "390857.55", "183655.70", "241545.44", "510365.90", "623626.00", "13736.00", "16695.40", "219409.08", "181683.75", "280912.75", "138636.30", "101987.20", "114774.59", "96810.70", "8610.50"])),
    'Meta_Peso': list(map(float, ["3000.0", "20000.0", "20500.0", "17000.0", "21500.0", "24500.0", "14000.0", "15000.0", "30000.0", "28000.0", "1000.0", "3000.0", "15000.0", "15000.0", "18000.0", "5000.0", "6000.0", "5000.0", "3000.0", "2000.0"])),
    'Real_Peso': list(map(float, ["3445.0", "17060.0", "18759.0", "13981.0", "17932.0", "21625.0", "11940.0", "13015.0", "29167.0", "26045.0", "575.0", "927.0", "12512.0", "10990.0", "16940.0", "8891.0", "5711.0", "6362.0", "4695.0", "615.0"])),
    'Meta_PM': [18.8,16.2,17.0,17.2,17.2,18.0,15.5,18.3,18.0,24.0,23.5,18.3,17.5,17.0,16.4,16.5,18.4,18.4,21.0,18.0],
    'Real_PM': [15.91,15.99,16.54,17.22,16.91,18.07,15.38,18.56,17.5,23.94,23.89,18.01,17.54,16.53,16.58,15.59,17.86,18.04,20.62,14.0],
    'Meta_Pos': list(map(float, ["4.0", "145.0", "149.0", "125.0", "153.0", "135.0", "116.0", "75.0", "8.0", "120.0", "4.0", "40.0", "150.0", "95.0", "95.0", "10.0", "55.0", "15.0", "35.0", "15.0"])),
    'Real_Pos': list(map(float, ["4.0", "143.0", "144.0", "122.0", "142.0", "128.0", "113.0", "69.0", "9.0", "117.0", "4.0", "20.0", "143.0", "89.0", "83.0", "14.0", "50.0", "12.0", "40.0", "9.0"])),
    'Meta_Cad': list(map(float, ["0.0", "3.0", "2.0", "4.0", "2.0", "4.0", "8.0", "8.0", "0.0", "0.0", "0.0", "10.0", "2.0", "8.0", "8.0", "0.0", "8.0", "5.0", "10.0", "10.0"])),
    'Real_Cad': list(map(float, ["0.0", "3.0", "3.0", "1.0", "2.0", "0.0", "3.0", "1.0", "1.0", "1.0", "0.0", "4.0", "3.0", "0.0", "1.0", "0.0", "8.0", "1.0", "13.0", "2.0"]))
})

df_junho = pd.DataFrame({
    'COD': lista_codigos,
    'Meta_Fat': list(map(float, ["75200.0", "309700.0", "359100.0", "288750.0", "350000.0", "420900.0", "208000.0", "264600.0", "522000.0", "677600.0", "23500.0", "36800.0", "230100.0", "221000.0", "310800.0", "96000.0", "131600.0", "129500.0", "126000.0", "36000.0", "54000.0"])),
    'Real_Fat': list(map(float, ["74925.55", "332596.55", "359158.15", "298921.90", "355375.55", "441361.90", "246593.55", "294028.09", "567145.65", "685743.00", "16573.00", "23287.90", "291925.09", "231502.10", "348788.25", "142088.41", "124658.80", "117299.95", "67634.10", "19112.50", "13035.00"])),
    'Meta_Peso': list(map(float, ["4000.0", "19000.0", "21000.0", "16500.0", "20000.0", "23000.0", "13000.0", "14000.0", "29000.0", "28000.0", "1000.0", "2000.0", "13000.0", "13000.0", "18500.0", "6000.0", "7000.0", "7000.0", "6000.0", "2000.0", "3000.0"])),
    'Real_Peso': list(map(float, ["4660.0", "20517.0", "21019.0", "16779.0", "20655.0", "24304.0", "15285.0", "15292.0", "31966.0", "28955.0", "705.0", "1315.0", "16205.0", "13568.0", "21785.0", "8783.0", "6457.0", "6256.0", "3510.0", "1130.0", "510.0"])),
    'Meta_PM': [18.8,16.3,17.1,17.5,17.5,18.3,16.0,18.9,18.0,24.2,23.5,18.4,17.7,17.0,16.8,16.0,18.8,18.5,21.0,18.0,18.0],
    'Real_PM': [16.08,16.21,17.09,17.82,17.21,18.16,16.13,19.23,17.74,23.68,23.51,17.71,18.01,17.06,16.01,16.18,19.31,18.75,19.27,16.91,25.56],
    'Meta_Pos': list(map(float, ["4.0", "146.0", "150.0", "128.0", "154.0", "138.0", "117.0", "80.0", "8.0", "120.0", "4.0", "45.0", "152.0", "100.0", "100.0", "10.0", "60.0", "20.0", "45.0", "15.0", "5.0"])),
    'Real_Pos': list(map(float, ["4.0", "151.0", "143.0", "126.0", "147.0", "127.0", "121.0", "75.0", "8.0", "123.0", "4.0", "18.0", "158.0", "92.0", "84.0", "15.0", "54.0", "11.0", "16.0", "9.0", "3.0"])),
    'Meta_Cad': list(map(float, ["0.0", "4.0", "4.0", "4.0", "4.0", "4.0", "8.0", "8.0", "0.0", "0.0", "0.0", "10.0", "4.0", "8.0", "8.0", "0.0", "8.0", "8.0", "10.0", "10.0", "10.0"])),
    'Real_Cad': list(map(float, ["0.0", "1.0", "3.0", "1.0", "3.0", "0.0", "5.0", "1.0", "0.0", "6.0", "0.0", "4.0", "4.0", "4.0", "1.0", "0.0", "8.0", "0.0", "1.0", "1.0", "2.0"]))
})

df_julho = pd.DataFrame({
    'COD': lista_codigos,
    'Meta_Fat': list(map(float, ["66000.0", "321750.0", "369800.0", "306000.0", "358750.0", "430050.0", "231000.0", "291000.0", "531000.0", "696000.0", "24000.0", "36800.0", "254800.0", "232200.0", "327600.0", "99000.0", "136500.0", "133000.0", "90000.0", "63000.0", "63000.0"])),
    'Real_Fat': list(map(float, ["55718.05", "295068.75", "366127.85", "274562.55", "351301.05", "449714.35", "229787.60", "248830.65", "699003.45", "694983.00", "21504.00", "22047.50", "253083.73", "234078.10", "325428.65", "125716.23", "148081.96", "125980.47", "81582.90", "13399.50", "13823.50"])),
    'Meta_Peso': list(map(float, ["4000.0", "19500.0", "21500.0", "17000.0", "20500.0", "23500.0", "14000.0", "15000.0", "29500.0", "29000.0", "1000.0", "2000.0", "14000.0", "13500.0", "19500.0", "6000.0", "7000.0", "7000.0", "4500.0", "3500.0", "3500.0"])),
    'Real_Peso': list(map(float, ["3540.0", "17990.0", "21025.0", "15340.0", "20348.0", "24251.0", "14310.0", "12887.0", "39592.0", "29216.0", "890.0", "1160.0", "14007.0", "13575.0", "19490.0", "6808.0", "7583.0", "6489.0", "3940.0", "855.0", "580.0"])),
    'Meta_PM': [16.5,16.5,17.2,18.0,17.5,18.3,16.5,19.4,18.0,24.0,24.0,18.4,18.2,17.2,16.8,16.5,19.5,19.0,20.0,18.0,18.0],
    'Real_PM': [15.74,16.4,17.41,17.9,17.26,18.54,16.06,19.31,17.66,23.79,24.16,19.01,18.07,17.24,16.7,18.47,19.53,19.41,20.71,15.67,23.83],
    'Meta_Pos': list(map(float, ["4.0", "149.0", "150.0", "130.0", "154.0", "138.0", "122.0", "80.0", "8.0", "125.0", "4.0", "40.0", "155.0", "100.0", "100.0", "15.0", "60.0", "15.0", "45.0", "12.0", "12.0"])),
    'Real_Pos': list(map(float, ["4.0", "135.0", "147.0", "124.0", "147.0", "128.0", "107.0", "71.0", "10.0", "122.0", "4.0", "18.0", "139.0", "89.0", "83.0", "15.0", "60.0", "16.0", "17.0", "9.0", "9.0"])),
    'Meta_Cad': list(map(float, ["0.0", "4.0", "4.0", "4.0", "4.0", "4.0", "8.0", "8.0", "0.0", "2.0", "0.0", "10.0", "4.0", "8.0", "8.0", "2.0", "8.0", "6.0", "10.0", "10.0", "10.0"])),
    'Real_Cad': list(map(float, ["0.0", "3.0", "1.0", "3.0", "3.0", "2.0", "2.0", "0.0", "1.0", "1.0", "0.0", "2.0", "1.0", "1.0", "2.0", "0.0", "5.0", "2.0", "0.0", "1.0", "2.0"]))
})

df_agosto = pd.DataFrame({
    'COD': lista_codigos,
    'Vendedor': ['VENDEDOR PARA HOMOLOGAÇÃO', 'CARLOS EDUARDO PEREIRA DA CRUZ', 'VALDINEI LUIZ PAIVA', 'LUIZ CARLOS SILVA NEVES', 'WESLEY FRANCIS DE JESUS LOPES', 'CELIO CLAUDIO OLIVEIRA', 'HELIO ALMEIDA VIANA', 'RAIMUNDO ALEX BARBOSA', 'MAURICIO SIMÕES JORGE', 'Rota BH', 'Rota BH - Interior de Minas', 'FREDERICO', 'FLAVIO CRISTIANO CARDOSO', 'WANDERSON DA SILVA LIMA', 'DANIEL DE PAULA', 'MAURICIO MARQUES DA SILVA JUNIOR', 'NATALIA FATIMA', 'JANETE CIRILO', 'RPA', 'Tallison Augusto de Oliveira', 'VENDEDOR 80063'],
    'Meta_Fat': list(map(float, ["4000.0", "20000.0", "22000.0", "17500.0", "21000.0", "23000.0", "14500.0", "15500.0", "30000.0", "30000.0", "1000.0", "2500.0", "15000.0", "14000.0", "20500.0", "6500.0", "7500.0", "7500.0", "5000.0", "4000.0", "4000.0"])),
    'Real_Fat': list(map(float, ["62535.55", "231934.56", "280827.15", "239176.87", "296503.56", "381824.90", "192627.10", "239371.61", "500078.20", "614048.50", "17342.50", "25650.80", "198311.60", "177473.30", "297853.40", "108419.92", "148120.59", "81573.78", "128520.80", "9184.00", "20098.00"])),
    'Meta_Peso': list(map(float, ["66.8", "334.0", "380.6", "318.5", "371.7", "423.2", "256.6", "302.2", "546.0", "726.0", "24.2", "46.2", "276.0", "243.6", "348.5", "108.5", "146.2", "142.5", "100.0", "72.4", "72.0"])),
    'Real_Peso': list(map(float, ["4000.00", "14113.00", "16553.00", "13893.00", "17156.00", "20452.00", "12490.00", "13323.00", "30207.00", "27375.00", "755.00", "1360.00", "11168.00", "10625.00", "17836.00", "5388.00", "7937.00", "4661.00", "6350.00", "690.00", "830.00"])),
    'Meta_PM': [16.7,16.7,17.3,18.2,17.7,18.4,17.7,19.5,18.2,24.2,24.2,18.5,18.4,17.4,17.0,16.7,19.5,19.0,20.0,18.1,18.0],
    'Real_PM': [15.63,16.43,16.97,17.22,17.28,18.67,15.42,17.97,16.56,22.43,22.97,18.86,17.76,16.7,16.7,20.12,18.66,17.5,20.24,13.31,24.21],
    'Meta_Pos': list(map(float, ["4.0", "150.0", "151.0", "131.0", "155.0", "140.0", "125.0", "85.0", "8.0", "125.0", "4.0", "45.0", "153.0", "105.0", "105.0", "15.0", "65.0", "15.0", "50.0", "15.0", "15.0"])),
    'Real_Pos': list(map(float, ["4.0", "142.0", "141.0", "121.0", "142.0", "128.0", "104.0", "73.0", "7.0", "130.0", "4.0", "18.0", "145.0", "82.0", "88.0", "15.0", "59.0", "15.0", "18.0", "8.0", "4.0"])),
    'Meta_Cad': list(map(float, ["0.0", "4.0", "4.0", "4.0", "4.0", "4.0", "8.0", "8.0", "0.0", "2.0", "0.0", "10.0", "4.0", "8.0", "8.0", "2.0", "8.0", "6.0", "10.0", "10.0", "10.0"])),
    'Real_Cad': list(map(float, ["0.0", "0.0", "2.0", "0.0", "3.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "1.0", "0.0", "2.0", "0.0", "0.0", "1.0", "0.0", "0.0", "1.0", "0.0"]))})
def calc_p_mes(df_p):
    df_r = pd.DataFrame()
    df_r['COD'] = df_p['COD']
    af = (df_p['Real_Fat'] / df_p['Meta_Fat']) * 100
    ap = (df_p['Real_Peso'] / df_p['Meta_Peso']) * 100
    am = (df_p['Real_PM'] / df_p['Meta_PM']) * 100
    ao = (df_p['Real_Pos'] / df_p['Meta_Pos']) * 100
    ac = np.where(df_p['Meta_Cad'] <= 1.0, np.where(df_p['Real_Cad'] > 0, 115.0, 0.0), (df_p['Real_Cad'] / df_p['Meta_Cad']) * 100)
    def fx(at, p1, p2, p3): return np.where(at < 90.0, 0.0, np.where(at < 100.0, float(p1), np.where(at < 110.0, float(p2), float(p3))))
    df_r['P_Fat'] = fx(af, 5, 10, 15)
    df_r['P_Peso'] = fx(ap, 5, 10, 15)
    df_r['P_PM'] = fx(am, 10, 15, 20)
    df_r['P_Pos'] = fx(ao, 5, 7.5, 10)
    df_r['P_Cad'] = fx(ac, 5, 7.5, 10)
    return df_r

p_maio = calc_p_mes(df_maio)
p_junho = calc_p_mes(df_junho)
p_julho = calc_p_mes(df_julho)
p_agosto = calc_p_mes(df_agosto)

m1 = pd.merge(df_maio, df_junho, on='COD', how='outer', suffixes=('_maio', '_junho'))
m2 = pd.merge(df_julho, df_agosto, on='COD', how='outer', suffixes=('_julho', '_agosto'))
mv = pd.merge(m1, m2, on='COD', how='outer')

df_f = pd.DataFrame()
df_f['COD'] = mv['COD']
df_f['Vendedor'] = mv['Vendedor_agosto'].fillna(mv['Vendedor_julho'])

for c in ['Meta_Fat', 'Real_Fat', 'Meta_Peso', 'Real_Peso', 'Meta_Pos', 'Real_Pos', 'Meta_Cad', 'Real_Cad']:
    df_f[c] = mv[f'{c}_maio'].fillna(0) + mv[f'{c}_junho'].fillna(0) + mv[f'{c}_julho'].fillna(0) + mv[f'{c}_agosto'].fillna(0)

df_f['Meta_PM'] = mv[['Meta_PM_maio', 'Meta_PM_junho', 'Meta_PM_julho', 'Meta_PM_agosto']].mean(axis=1)
df_f['Real_PM'] = mv[['Real_PM_maio', 'Real_PM_junho', 'Real_PM_julho', 'Real_PM_agosto']].mean(axis=1)

mp1 = pd.merge(p_maio, p_junho, on='COD', how='outer', suffixes=('_maio', '_junho'))
mp2 = pd.merge(p_julho, p_agosto, on='COD', how='outer', suffixes=('_julho', '_agosto'))
mpt = pd.merge(mp1, mp2, on='COD', how='outer')

for k in ['P_Fat', 'P_Peso', 'P_PM', 'P_Pos', 'P_Cad']:
    df_f[k] = mpt[f'{k}_maio'].fillna(0) + mpt[f'{k}_junho'].fillna(0) + mpt[f'{k}_julho'].fillna(0) + mpt[f'{k}_agosto'].fillna(0)

df_f['Pontuacao_Base'] = df_f['P_Fat'] + df_f['P_Peso'] + df_f['P_PM'] + df_f['P_Pos'] + df_f['P_Cad']
df_f['Vendedor'] = df_f['Vendedor'].apply(lambda x: str(x).split()[0] if str(x).strip() else "")
df_f['Categoria'] = np.where(df_f['COD'].isin(codigos_filtrados), 'Especiais', 'Padrao')

mostrar_especiais = st.sidebar.checkbox("Mostrar Todos Vendedores", value=False)
if not mostrar_especiais:
    df_f = df_f[df_f['Categoria'] == 'Padrao'].reset_index(drop=True)

df_f['At_Fat'] = (df_f['Real_Fat'] / df_f['Meta_Fat']) * 100
df_f['At_Peso'] = (df_f['Real_Peso'] / df_f['Meta_Peso']) * 100
df_f['At_PM'] = (df_f['Real_PM'] / df_f['Meta_PM']) * 100
df_f['At_Pos'] = (df_f['Real_Pos'] / df_f['Meta_Pos']) * 100
df_f['At_Cad'] = np.where(df_f['Meta_Cad'] <= 1.0, np.where(df_f['Real_Cad'] > 0, 115.0, 0.0), (df_f['Real_Cad'] / df_f['Meta_Cad']) * 100)

df_f['Bonus_Desempate'] = 0.0
df_f['Marcacao'] = ""
emp = df_f[df_f.duplicated(subset=['Pontuacao_Base'], keep=False)]['Pontuacao_Base'].unique()

for n in emp:
    if n > 0:
        idx = df_f[df_f['Pontuacao_Base'] == n].index
        mx = df_f.loc[idx, 'Real_PM'].max()
        idx_v = df_f[(df_f['Pontuacao_Base'] == n) & (df_f['Real_PM'] == mx)].index
        df_f.loc[idx_v, 'Bonus_Desempate'] = 0.01
        df_f.loc[idx_v, 'Marcacao'] = " 🎯"

df_f['Pontuacao_Total'] = df_f['Pontuacao_Base'] + df_f['Bonus_Desempate']
df_r = df_f.sort_values(by='Pontuacao_Total', ascending=False).reset_index(drop=True)
df_r['Vendedor'] = df_r['Vendedor'].astype(str) + df_r['Marcacao'].astype(str)

if len(df_r) > 0:
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("🥇 1º LUGAR", df_r.loc[0, 'Vendedor'], f"{df_r.loc[0, 'Pontuacao_Total']:.2f} pts")
    if len(df_r) > 1: c2.metric("🥈 2º LUGAR", df_r.loc[1, 'Vendedor'], f"{df_r.loc[1, 'Pontuacao_Total']:.2f} pts")
    if len(df_r) > 2: c3.metric("🥉 3º LUGAR", df_r.loc[2, 'Vendedor'], f"{df_r.loc[2, 'Pontuacao_Total']:.2f} pts")
    if len(df_r) > 3: c4.metric("🏅 4º LUGAR", df_r.loc[3, 'Vendedor'], f"{df_r.loc[3, 'Pontuacao_Total']:.2f} pts")
    if len(df_r) > 4: c5.metric("🏅 5º LUGAR", df_r.loc[4, 'Vendedor'], f"{df_r.loc[4, 'Pontuacao_Total']:.2f} pts")
    st.write("---")

df_r.index += 1
st.markdown("### 📋 TABELA DE PONTOS POR KPI (SOMA DO QUADRIMESTRE 2)")
st.dataframe(df_r[['COD', 'Vendedor', 'Pontuacao_Total', 'P_Fat', 'P_Peso', 'P_PM', 'P_Pos', 'P_Cad']].rename(columns={'Pontuacao_Total': 'PONTUAÇÃO TOTAL'}), use_container_width=True)
st.write("---")
st.markdown("### 📊 PERCENTUAIS DE ATINGIMENTO METAS (%)")
st.dataframe(df_r[['COD', 'Vendedor', 'At_Fat', 'At_Peso', 'At_PM', 'At_Pos', 'At_Cad']].style.format({'At_Fat': '{:.1f}%', 'At_Peso': '{:.1f}%', 'At_PM': '{:.1f}%', 'At_Pos': '{:.1f}%', 'At_Cad': '{:.1f}%'}), use_container_width=True)
