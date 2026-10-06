import pandas as pd
import numpy as np
import streamlit as st
import auth

auth.validar_senha()  # bloqueia se não tiver senha correta

try:
    st.sidebar.image("logo.png", use_container_width=True)
except Exception:
    st.sidebar.warning("⚠️ Arquivo 'logo.png' não encontrado.")

st.markdown("## 🏆 Ranking Consolidado do Ano (Quadrimestre 1 + Quadrimestre 2)")


# ============================================================
# FUNÇÃO GENÉRICA DE PONTUAÇÃO POR FAIXA (igual às páginas originais)
# ============================================================
def calcular_pontos_faixa(ating, pt90, pt100, pt110):
    if ating < 90.0:
        return 0.0
    elif ating < 100.0:
        return float(pt90)
    elif ating < 110.0:
        return float(pt100)
    else:
        return float(pt110)


def calcular_at_cad(meta, real):
    return np.where(meta <= 1.0, np.where(real > 0, 115.0, 0.0), (real / meta) * 100)


# ============================================================
# BLOCO 1 — RECONSTRUÇÃO DOS DADOS DO QUADRIMESTRE 1
# ============================================================
def montar_df_q1():
    texto_codigos = ["80001", "80002", "80003", "80005", "80006", "80007", "80010", "80011",
                      "80012", "80021", "80022", "80039", "80048", "80052", "80053", "80055",
                      "80057", "80058", "80060", "80061", "80062"]

    lista_codigos = list(map(int, texto_codigos))

    data_quadrimestre = {
        'COD': lista_codigos,
        'Vendedor': [
            'VENDEDOR PARA HOMOLOGAÇÃO', 'CARLOS EDUARDO PEREIRA DA CRUZ', 'VALDINEI LUIZ PAIVA',
            'LUIZ CARLOS SILVA NEVES', 'WESLEY FRANCIS DE JESUS LOPES', 'CELIO CLAUDIO OLIVEIRA',
            'HELIO ALMEIDA VIANA', 'RAIMUNDO ALEX BARBOSA', 'MAURICIO SIMÕES JORGE',
            'Rota BH', 'Rota BH - Interior de Minas', 'FREDERICO', 'FLAVIO CRISTIANO CARDOSO',
            'WANDERSON DA SILVA LIMA', 'DANIEL DE PAULA', 'MAURICIO MARQUES DA SILVA JUNIOR',
            'GILBERT CRISTIAN', 'NATALIA FATIMA', 'JANETE CIRILO', 'RPA', 'Tallison Augusto de Oliveira'
        ],
        'Meta_Fat': [318880.0, 1171100.0, 1381200.0, 1136600.0, 1396000.0, 1658500.0, 751750.0, 1132500.0,
                     2315350.0, 2535200.0, 96000.0, 348750.0, 967250.0, 860500.0, 1293350.0, 664000.0,
                     90000.0, 479800.0, 331200.0, 241500.0, 1.0],
        'Real_Fat': [254754.40, 1091928.00, 1232846.85, 970745.58, 1251693.40, 1590120.70, 687613.80,
                     932907.49, 2280576.70, 2471894.88, 66186.00, 79820.22, 830930.82, 806371.35,
                     988358.30, 667041.86, 6598.00, 395428.14, 182194.05, 113946.15, 34167.00],
        'Meta_Peso': [17000.0, 70000.0, 81000.0, 65000.0, 80000.0, 91000.0, 48500.0, 60000.0, 115500.0,
                      105000.0, 4000.0, 17500.0, 54500.0, 51500.0, 69500.0, 37500.0, 5000.0, 24000.0,
                      18000.0, 12000.0, 1.0],
        'Real_Peso': [14180.00, 67825.00, 73275.00, 56720.00, 73149.00, 87924.00, 45028.00, 50418.00,
                      115611.50, 102832.00, 2825.00, 4203.00, 47402.00, 47751.00, 63168.00, 38206.00,
                      530.00, 19999.00, 9969.00, 5370.00, 2750.00],
        'Meta_PM': [18.76, 16.73, 17.05, 17.48, 17.45, 18.23, 15.50, 18.88, 20.05, 24.15, 24.00, 19.75,
                    17.75, 16.70, 18.60, 17.75, 18.00, 20.08, 18.40, 20.15, 1.0],
        'Real_PM': [17.97, 16.10, 16.82, 17.11, 17.11, 18.09, 15.27, 18.50, 19.73, 24.04, 23.43, 18.99,
                    17.53, 16.89, 15.65, 17.46, 12.45, 19.77, 18.28, 21.22, 12.42],
        'Meta_Pos': [20.0, 563.0, 578.0, 494.0, 592.0, 525.0, 444.0, 286.0, 39.0, 439.0, 17.0, 105.0,
                     552.0, 370.0, 366.0, 63.0, 5.0, 180.0, 42.0, 47.0, 1.0],
        'Real_Pos': [17.0, 570.0, 579.0, 487.0, 591.0, 512.0, 451.0, 278.0, 72.0, 458.0, 16.0, 82.0,
                     589.0, 354.0, 335.0, 61.0, 2.0, 143.0, 23.0, 50.0, 15.0],
        'Meta_Cad': [0.0, 12.0, 11.0, 20.0, 13.0, 17.0, 33.0, 40.0, 0.0, 6.0, 1.0, 40.0, 14.0, 30.0,
                     30.0, 3.0, 5.0, 25.0, 25.0, 10.0, 1.0],
        'Real_Cad': [0.0, 2.0, 15.0, 11.0, 21.0, 9.0, 18.0, 10.0, 10.0, 10.0, 0.0, 19.0, 17.0, 11.0,
                     10.0, 1.0, 0.0, 38.0, 13.0, 18.0, 10.0],
    }

    df = pd.DataFrame(data_quadrimestre)

    df['At_Fat'] = (df['Real_Fat'] / df['Meta_Fat']) * 100
    df['At_Peso'] = (df['Real_Peso'] / df['Meta_Peso']) * 100
    df['At_PM'] = (df['Real_PM'] / df['Meta_PM']) * 100
    df['At_Pos'] = (df['Real_Pos'] / df['Meta_Pos']) * 100
    df['At_Cad'] = calcular_at_cad(df['Meta_Cad'].values, df['Real_Cad'].values)

    df['P_Fat'] = df['At_Fat'].apply(lambda x: calcular_pontos_faixa(x, 5, 10, 15))
    df['P_Peso'] = df['At_Peso'].apply(lambda x: calcular_pontos_faixa(x, 5, 10, 15))
    df['P_PM'] = df['At_PM'].apply(lambda x: calcular_pontos_faixa(x, 10, 15, 20))
    df['P_Pos'] = df['At_Pos'].apply(lambda x: calcular_pontos_faixa(x, 5, 7.5, 10))
    df['P_Cad'] = df['At_Cad'].apply(lambda x: calcular_pontos_faixa(x, 5, 7.5, 10))

    cols = ['COD', 'Vendedor', 'Meta_Fat', 'Real_Fat', 'Meta_Peso', 'Real_Peso',
            'Meta_Pos', 'Real_Pos', 'Meta_Cad', 'Real_Cad', 'Meta_PM', 'Real_PM',
            'P_Fat', 'P_Peso', 'P_PM', 'P_Pos', 'P_Cad']
    return df[cols]


# ============================================================
# BLOCO 2 — RECONSTRUÇÃO DOS DADOS DO QUADRIMESTRE 2 (4 meses somados)
# ============================================================
def montar_df_q2():
    txt_m = ["80001", "80002", "80003", "80005", "80006", "80007", "80010", "80011", "80012",
             "80021", "80022", "80039", "80048", "80052", "80053", "80055", "80058", "80060",
             "80061", "80062", "80063"]
    lista_codigos = list(map(int, txt_m))

    vendedores_lista = [
        'VENDEDOR PARA HOMOLOGAÇÃO', 'CARLOS EDUARDO PEREIRA DA CRUZ', 'VALDINEI LUIZ PAIVA',
        'LUIZ CARLOS SILVA NEVES', 'WESLEY FRANCIS DE JESUS LOPES', 'CELIO CLAUDIO OLIVEIRA',
        'HELIO ALMEIDA VIANA', 'RAIMUNDO ALEX BARBOSA', 'MAURICIO SIMÕES JORGE', 'Rota BH',
        'Rota BH - Interior de Minas', 'FREDERICO', 'FLAVIO CRISTIANO CARDOSO', 'WANDERSON DA SILVA LIMA',
        'DANIEL DE PAULA', 'MAURICIO MARQUES DA SILVA JUNIOR', 'NATALIA FATIMA', 'JANETE CIRILO',
        'RPA', 'Tallison Augusto de Oliveira', 'VENDEDOR 80063'
    ]

    matriz_meta_fat = np.array([[56400,75200,66000,4000],[324000,309700,321750,20000],[348500,359100,369800,22000],[292400,288750,306000,17500],[369800,350000,358750,21000],[441000,420900,430050,23000],[217000,208000,231000,14500],[274500,264600,291000,15500],[540000,522000,531000,30000],[672000,677600,696000,30000],[23500,23500,24000,1000],[54900,36800,36800,2500],[262500,230100,254800,15000],[255000,221000,232200,14000],[295200,310800,327600,20500],[82500,96000,99000,6500],[110400,131600,136500,7500],[92000,129500,133000,7500],[63000,126000,90000,5000],[36000,36000,63000,4000],[0,54000,63000,4000]], dtype=float)
    matriz_real_fat = np.array([[54797.9,74925.55,55718.05,62535.55],[272753.4,332596.55,295068.75,231934.56],[310243.5,359158.15,366127.85,280827.15],[240808.16,298921.9,274562.55,239176.87],[303155.06,355375.55,351301.05,296503.56],[390857.55,441361.9,449714.35,381824.9],[183655.7,246593.55,229787.6,192627.1],[241545.44,294028.09,248830.65,239371.61],[510365.9,567145.65,699003.45,500078.2],[623626,685743,694983,614048.5],[13736,16573,21504,17342.5],[16695.4,23287.9,22047.5,25650.8],[219409.08,291925.09,253083.73,198311.6],[181683.75,231502.1,234078.1,177473.3],[280912.75,348788.25,325428.65,297853.4],[138636.3,142088.41,125716.23,108419.92],[101987.2,124658.8,148081.96,148120.59],[114774.59,117299.95,125980.47,81573.78],[96810.7,67634.1,81582.9,128520.8],[8610.5,19112.5,13399.5,9184],[0,13035,13823.5,20098]], dtype=float)

    matriz_meta_pes = np.array([[3000,4000,4000,66.8],[20000,19000,19500,334],[20500,21000,21500,380.6],[17000,16500,17000,318.5],[21500,20000,20500,371.7],[24500,23000,23500,423.2],[14000,13000,14000,256.6],[15000,14000,15000,302.2],[30000,29000,29500,546],[28000,28000,29000,726],[1000,1000,1000,24.2],[3000,2000,2000,46.2],[15000,13000,14000,276],[15000,13000,13500,243.6],[18000,18500,19500,348.5],[5000,6000,6000,108.5],[6000,7000,7000,146.2],[5000,7000,7000,142.5],[3000,6000,4500,100],[2000,2000,3500,72.4],[0,3000,3500,72]], dtype=float)
    matriz_real_pes = np.array([[3445,4660,3540,4000],[17060,20517,17990,14113],[18759,21019,21025,16553],[13981,16779,15340,13893],[17932,20655,20348,17156],[21625,24304,24251,20452],[11940,15285,14310,12490],[13015,15292,12887,13323],[29167,31966,39592,30207],[26045,28955,29216,27375],[575,705,890,755],[927,1315,1160,1360],[12512,16205,14007,11168],[10990,13568,13575,10625],[16940,21785,19490,17836],[8891,8783,6808,5388],[5711,6457,7583,7937],[6362,6256,6489,4661],[4695,3510,3940,6350],[615,1130,855,690],[0,510,580,830]], dtype=float)

    matriz_meta_pme = np.array([[18.8,18.8,16.5,16.7],[16.2,16.3,16.5,16.7],[17,17.1,17.2,17.3],[17.2,17.5,18,18.2],[17.2,17.5,17.5,17.7],[18,18.3,18.3,18.4],[15.5,16,16.5,17.7],[18.3,18.9,19.4,19.5],[18,18,18,18.2],[24,24.2,24,24.2],[23.5,23.5,24,24.2],[18.3,18.4,18.4,18.5],[17.5,17.7,18.2,18.4],[17,17,17.2,17.4],[16.4,16.8,16.8,17],[16.5,16,16.5,16.7],[18.4,18.8,19.5,19.5],[18.4,18.5,19,19],[21,21,20,20],[18,18,18,18.1],[0,18,18,18]], dtype=float)
    matriz_real_pme = np.array([[15.91,16.08,15.74,15.63],[15.99,16.21,16.4,16.43],[16.54,17.09,17.41,16.97],[17.22,17.82,17.9,17.22],[16.91,17.21,17.26,17.28],[18.07,18.16,18.54,18.67],[15.38,16.13,16.06,15.42],[18.56,19.23,19.31,17.97],[17.5,17.74,17.66,16.56],[23.94,23.68,23.79,22.43],[23.89,23.51,24.16,22.97],[18.01,17.71,19.01,18.86],[17.54,18.01,18.07,17.76],[16.53,17.06,17.24,16.7],[16.58,16.01,16.7,16.7],[15.59,16.18,18.47,20.12],[17.86,19.31,19.53,18.66],[18.04,18.75,19.41,17.5],[20.62,19.27,20.71,20.24],[14,16.91,15.67,13.31],[0,25.56,23.83,24.21]], dtype=float)

    matriz_meta_pos = np.array([[4,4,4,4],[145,146,149,150],[149,150,150,151],[125,128,130,131],[153,154,154,155],[135,138,138,140],[116,117,122,125],[75,80,80,85],[8,8,8,8],[120,120,125,125],[4,4,4,4],[40,45,40,45],[150,152,155,153],[95,100,100,105],[95,100,100,105],[10,10,15,15],[55,60,60,65],[15,20,15,15],[35,45,45,50],[15,15,12,15],[0,5,12,15]], dtype=float)
    matriz_real_pos = np.array([[4,4,4,4],[143,151,135,142],[144,143,147,141],[122,126,124,121],[142,147,147,142],[128,127,128,128],[113,121,107,104],[69,75,71,73],[9,8,10,7],[117,123,122,130],[4,4,4,4],[20,18,18,18],[143,158,139,145],[89,92,89,82],[83,84,83,88],[14,15,15,15],[50,54,60,59],[12,11,16,15],[40,16,17,18],[9,9,9,8],[0,3,9,4]], dtype=float)

    matriz_meta_cad = np.array([[0,0,0,0],[3,4,4,4],[2,4,4,4],[4,4,4,4],[2,4,4,4],[4,4,4,4],[8,8,8,8],[8,8,8,8],[0,0,0,0],[0,0,2,2],[0,0,0,0],[10,10,10,10],[2,4,4,4],[8,8,8,8],[8,8,8,8],[0,0,2,2],[8,8,8,8],[5,8,6,6],[10,10,10,10],[10,10,10,10],[0,10,10,10]], dtype=float)
    matriz_real_cad = np.array([[0,0,0,0],[3,1,3,0],[3,3,1,2],[1,1,3,0],[2,3,3,3],[0,0,2,0],[3,5,2,0],[1,1,0,0],[1,0,1,0],[1,6,1,0],[0,0,0,0],[4,4,2,1],[3,4,1,0],[0,4,1,2],[1,1,2,0],[0,0,0,0],[8,8,5,1],[1,0,2,0],[13,1,0,0],[2,1,1,1],[0,2,2,0]], dtype=float)

    pontos_fat, pontos_pes, pontos_pme, pontos_pos, pontos_cad = [], [], [], [], []

    for i in range(4):
        af = (matriz_real_fat[:, i] / matriz_meta_fat[:, i]) * 100
        ap = (matriz_real_pes[:, i] / matriz_meta_pes[:, i]) * 100
        am = (matriz_real_pme[:, i] / matriz_meta_pme[:, i]) * 100
        ao = (matriz_real_pos[:, i] / matriz_meta_pos[:, i]) * 100
        ac = calcular_at_cad(matriz_meta_cad[:, i], matriz_real_cad[:, i])

        def fx(at, p1, p2, p3):
            return np.where(at < 90.0, 0.0, np.where(at < 100.0, float(p1), np.where(at < 110.0, float(p2), float(p3))))

        pontos_fat.append(fx(af, 5, 10, 15))
        pontos_pes.append(fx(ap, 5, 10, 15))
        pontos_pme.append(fx(am, 10, 15, 20))
        pontos_pos.append(fx(ao, 5, 7.5, 10))
        pontos_cad.append(fx(ac, 5, 7.5, 10))

    df_f = pd.DataFrame()
    df_f['COD'] = lista_codigos
    df_f['Vendedor'] = vendedores_lista

    df_f['Meta_Fat'] = np.sum(matriz_meta_fat, axis=1)
    df_f['Real_Fat'] = np.sum(matriz_real_fat, axis=1)
    df_f['Meta_Peso'] = np.sum(matriz_meta_pes, axis=1)
    df_f['Real_Peso'] = np.sum(matriz_real_pes, axis=1)
    df_f['Meta_Pos'] = np.sum(matriz_meta_pos, axis=1)
    df_f['Real_Pos'] = np.sum(matriz_real_pos, axis=1)
    df_f['Meta_Cad'] = np.sum(matriz_meta_cad, axis=1)
    df_f['Real_Cad'] = np.sum(matriz_real_cad, axis=1)

    df_f['Meta_PM'] = np.nanmean(np.where(matriz_meta_pme == 0, np.nan, matriz_meta_pme), axis=1)
    df_f['Real_PM'] = np.nanmean(np.where(matriz_real_pme == 0, np.nan, matriz_real_pme), axis=1)

    df_f['P_Fat'] = np.sum(np.array(pontos_fat), axis=0)
    df_f['P_Peso'] = np.sum(np.array(pontos_pes), axis=0)
    df_f['P_PM'] = np.sum(np.array(pontos_pme), axis=0)
    df_f['P_Pos'] = np.sum(np.array(pontos_pos), axis=0)
    df_f['P_Cad'] = np.sum(np.array(pontos_cad), axis=0)

    cols = ['COD', 'Vendedor', 'Meta_Fat', 'Real_Fat', 'Meta_Peso', 'Real_Peso',
            'Meta_Pos', 'Real_Pos', 'Meta_Cad', 'Real_Cad', 'Meta_PM', 'Real_PM',
            'P_Fat', 'P_Peso', 'P_PM', 'P_Pos', 'P_Cad']
    return df_f[cols]


# ============================================================
# BLOCO 3 — CONSOLIDAÇÃO ANUAL (SOMA ABSOLUTA DE KPIs E PONTOS)
# ============================================================
df1 = montar_df_q1()
df2 = montar_df_q2()

df = pd.merge(df1, df2, on='COD', how='outer', suffixes=('_q1', '_q2'))

# Nome: usa o do Q1, e se não existir (ex: 80063) usa o do Q2
df['Vendedor'] = df['Vendedor_q1'].fillna(df['Vendedor_q2'])

# 🎯 SOMA ABSOLUTA de volumes e pontos dos dois quadrimestres
volume_cols = ['Meta_Fat', 'Real_Fat', 'Meta_Peso', 'Real_Peso', 'Meta_Pos', 'Real_Pos',
               'Meta_Cad', 'Real_Cad', 'P_Fat', 'P_Peso', 'P_PM', 'P_Pos', 'P_Cad']
for col in volume_cols:
    df[col] = df[f'{col}_q1'].fillna(0) + df[f'{col}_q2'].fillna(0)

# Preço Médio: média entre os dois quadrimestres (só considera onde há valor)
df['Meta_PM'] = df[['Meta_PM_q1', 'Meta_PM_q2']].mean(axis=1, skipna=True)
df['Real_PM'] = df[['Real_PM_q1', 'Real_PM_q2']].mean(axis=1, skipna=True)

df['Pontuacao_Base'] = df['P_Fat'] + df['P_Peso'] + df['P_PM'] + df['P_Pos'] + df['P_Cad']

# ✂️ Primeiro nome
df['Vendedor'] = df['Vendedor'].apply(lambda x: str(x).split()[0] if str(x).strip() else "")

# União dos códigos "Especiais" dos dois quadrimestres
codigos_filtrados = sorted(set([80012, 80021, 80055, 80061, 80022, 80001, 80057, 80062]))
df['Categoria'] = np.where(df['COD'].isin(codigos_filtrados), 'Especiais', 'Padrao')

mostrar_especiais = st.sidebar.checkbox("Mostrar Todos Vendedores", value=False)
if not mostrar_especiais:
    df = df[df['Categoria'] == 'Padrao'].reset_index(drop=True)

# Percentuais de atingimento anuais (informativos)
df['At_Fat'] = (df['Real_Fat'] / df['Meta_Fat']) * 100
df['At_Peso'] = (df['Real_Peso'] / df['Meta_Peso']) * 100
df['At_PM'] = (df['Real_PM'] / df['Meta_PM']) * 100
df['At_Pos'] = (df['Real_Pos'] / df['Meta_Pos']) * 100
df['At_Cad'] = calcular_at_cad(df['Meta_Cad'].values, df['Real_Cad'].values)

# --- DESEMPATE POR MAIOR PREÇO MÉDIO REALIZADO (ANUAL) ---
df['Bonus_Desempate'] = 0.0
df['Marcacao'] = ""

pontuacoes_empatadas = df[df.duplicated(subset=['Pontuacao_Base'], keep=False)]['Pontuacao_Base'].unique()
for nota in pontuacoes_empatadas:
    if nota > 0:
        indices_grupo = df[df['Pontuacao_Base'] == nota].index
        maior_pm = df.loc[indices_grupo, 'Real_PM'].max()
        idx_vencedor = df[(df['Pontuacao_Base'] == nota) & (df['Real_PM'] == maior_pm)].index
        df.loc[idx_vencedor, 'Bonus_Desempate'] = 0.01
        df.loc[idx_vencedor, 'Marcacao'] = " 🎯"

df['Pontuacao_Ordenada'] = df['Pontuacao_Base'] + df['Bonus_Desempate']
df_ranking = df.sort_values(by='Pontuacao_Ordenada', ascending=False).reset_index(drop=True)
df_ranking['Vendedor'] = df_ranking['Vendedor'] + df_ranking['Marcacao']

# ============================================================
# BLOCO 4 — EXIBIÇÃO
# Pódio: somente os 5 primeiros | Tabelas: ranking completo
# ============================================================
top5 = df_ranking.head(5).reset_index(drop=True)

if len(top5) > 0:
    col_t1, col_t2, col_t3, col_t4, col_t5 = st.columns(5)
    col_t1.metric(label="🥇 1º LUGAR", value=top5.loc[0, 'Vendedor'], delta=f"{top5.loc[0, 'Pontuacao_Base']:.2f} pts")
    if len(top5) > 1:
        col_t2.metric(label="🥈 2º LUGAR", value=top5.loc[1, 'Vendedor'], delta=f"{top5.loc[1, 'Pontuacao_Base']:.2f} pts")
    if len(top5) > 2:
        col_t3.metric(label="🥉 3º LUGAR", value=top5.loc[2, 'Vendedor'], delta=f"{top5.loc[2, 'Pontuacao_Base']:.2f} pts")
    if len(top5) > 3:
        col_t4.metric(label="🏅 4º LUGAR", value=top5.loc[3, 'Vendedor'], delta=f"{top5.loc[3, 'Pontuacao_Base']:.2f} pts")
    if len(top5) > 4:
        col_t5.metric(label="🏅 5º LUGAR", value=top5.loc[4, 'Vendedor'], delta=f"{top5.loc[4, 'Pontuacao_Base']:.2f} pts")
    st.write("---")

df_ranking.index += 1
st.markdown("### 📋 TABELA DE PONTOS POR KPI (SOMA ANUAL: Q1 + Q2)")
st.dataframe(
    df_ranking[['COD', 'Vendedor', 'Pontuacao_Base', 'P_Fat', 'P_Peso', 'P_PM', 'P_Pos', 'P_Cad']]
    .rename(columns={'Pontuacao_Base': 'PONTUAÇÃO TOTAL'}),
    use_container_width=True
)
st.write("---")
st.markdown("### 📊 PERCENTUAIS DE ATINGIMENTO ANUAL (%)")
st.dataframe(
    df_ranking[['COD', 'Vendedor', 'At_Fat', 'At_Peso', 'At_PM', 'At_Pos', 'At_Cad']].style.format({
        'At_Fat': '{:.1f}%', 'At_Peso': '{:.1f}%', 'At_PM': '{:.1f}%', 'At_Pos': '{:.1f}%', 'At_Cad': '{:.1f}%'
    }),
    use_container_width=True
)
