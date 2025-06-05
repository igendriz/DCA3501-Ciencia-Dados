"""
Exemplo 5 - Filtros e Dados Reais

Este exemplo demonstra como implementar filtros interativos usando dados reais:
- Filtros por região
- Filtros por indicadores
- Filtros por faixa de valores
- Busca textual
- Atualização dinâmica de visualizações

O objetivo é mostrar como criar uma interface de análise de dados
interativa e funcional.

Autor: Victor Gomes
Data: Junho 2024
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configuração básica da página
st.set_page_config(page_title="Exemplo 5: Filtros e Dados Reais", page_icon="🔍")

# Título e introdução
st.title('Filtros e Análise de Dados Reais')
st.markdown('Este exemplo demonstra como implementar filtros interativos para análise dos dados socioeconômicos de Natal/RN.')

# Função para carregar os dados
@st.cache_data
def carregar_dados():
    # Carrega o dataset contendo informações socioeconômicas dos bairros de Natal/RN diretamente do GitHub
    df = pd.read_csv('https://raw.githubusercontent.com/igendriz/DCA3501-Ciencia-Dados/main/Dataset/Bairros_Natal_v01.csv')
    
    # Remove linhas com quaisquer valores ausentes (NaN)
    df = df.dropna()
    
    # Corrige nomes específicos de bairros para padronização (sem acentos ou espaços)
    df.loc[0, "bairro"] = 'ns_apresentacao'   # Nossa Senhora da Apresentação
    df.loc[34, "bairro"] = 'ns_nazare'        # Nossa Senhora de Nazaré
    df.loc[32, "bairro"] = 'c_esperanca'      # Cidade da Esperança
    
    # Remove a coluna 'Unnamed: 0', gerada automaticamente pelo salvamento anterior do CSV
    if 'Unnamed: 0' in df.columns:
        df = df.drop(columns='Unnamed: 0')
    
    return df

# Carrega os dados
df_natal = carregar_dados()

# Sidebar para filtros
st.sidebar.header("Filtros")

# Filtro por região
regioes = ["Todas"] + sorted(df_natal["regiao"].unique().tolist())
regiao_selecionada = st.sidebar.selectbox("Selecione a Região:", regioes)

# Filtro por indicador
indicadores = {
    "Renda Mensal por Pessoa (R$)": "renda_mensal_pessoa",
    "Rendimento Nominal Médio (sal. mín.)": "rendimento_nominal_medio",
    "População Total": "populacao"
}
indicador_selecionado = st.sidebar.selectbox("Selecione o Indicador:", list(indicadores.keys()))
coluna_indicador = indicadores[indicador_selecionado]

# Filtro por limiar
min_valor = float(df_natal[coluna_indicador].min())
max_valor = float(df_natal[coluna_indicador].max())
limiar = st.sidebar.slider(
    f"Limiar de {indicador_selecionado}:",
    min_valor, max_valor,
    (min_valor, max_valor)  # valor padrão (intervalo completo)
)

# Aplicar filtros
if regiao_selecionada != "Todas":
    df_filtrado = df_natal[df_natal["regiao"] == regiao_selecionada.lower()]
else:
    df_filtrado = df_natal.copy()

# Filtro por limiar
df_filtrado = df_filtrado[(df_filtrado[coluna_indicador] >= limiar[0]) & 
                          (df_filtrado[coluna_indicador] <= limiar[1])]

# Exibir dados filtrados
st.header("Dados Filtrados")
st.dataframe(df_filtrado)

# Visualizações
st.header("Visualizações")

# Layout com duas colunas
col1, col2 = st.columns(2)

with col1:
    # Gráfico de barras para o indicador selecionado
    st.subheader(f"{indicador_selecionado} por Bairro")
    
    fig_bar = px.bar(
        df_filtrado.sort_values(by=coluna_indicador, ascending=False),
        x="bairro",
        y=coluna_indicador,
        color="regiao",
        title=f"{indicador_selecionado} por Bairro",
        labels={"bairro": "Bairro", coluna_indicador: indicador_selecionado}
    )
    
    # Ajustar layout
    fig_bar.update_layout(
        xaxis_tickangle=-45,
        height=400
    )
    
    # Exibir o gráfico
    st.plotly_chart(fig_bar, use_container_width=True)

with col2:
    # Gráfico de dispersão relacionando dois indicadores
    st.subheader("Relação entre Indicadores")
    
    # Seletor para o segundo indicador
    segundo_indicador = st.selectbox(
        "Selecione outro indicador para comparação:",
        [k for k in indicadores.keys() if indicadores[k] != coluna_indicador]
    )
    coluna_segundo = indicadores[segundo_indicador]
    
    fig_scatter = px.scatter(
        df_filtrado,
        x=coluna_indicador,
        y=coluna_segundo,
        color="regiao",
        size="populacao",
        hover_name="bairro",
        title=f"{indicador_selecionado} vs {segundo_indicador}",
        labels={
            coluna_indicador: indicador_selecionado,
            coluna_segundo: segundo_indicador
        }
    )
    
    # Exibir o gráfico
    st.plotly_chart(fig_scatter, use_container_width=True)

# Estatísticas
st.header("Estatísticas Descritivas")

# Estatísticas por região
if regiao_selecionada != "Todas":
    st.write(f"Estatísticas para a região **{regiao_selecionada}**:")
else:
    st.write("Estatísticas por região:")

# Calcular estatísticas por região
stats_regiao = df_natal.groupby('regiao')[coluna_indicador].agg(['mean', 'min', 'max', 'count']).reset_index()
stats_regiao.columns = ['Região', 'Média', 'Mínimo', 'Máximo', 'Quantidade de Bairros']

# Formatar valores numéricos
if coluna_indicador != "populacao":
    stats_regiao['Média'] = stats_regiao['Média'].round(2)
    stats_regiao['Mínimo'] = stats_regiao['Mínimo'].round(2)
    stats_regiao['Máximo'] = stats_regiao['Máximo'].round(2)
else:
    stats_regiao['Média'] = stats_regiao['Média'].round(0).astype(int)
    stats_regiao['Mínimo'] = stats_regiao['Mínimo'].round(0).astype(int)
    stats_regiao['Máximo'] = stats_regiao['Máximo'].round(0).astype(int)

# Exibir tabela de estatísticas
st.dataframe(stats_regiao, use_container_width=True)

# Adicionar um gráfico de comparação entre regiões
st.subheader("Comparação entre Regiões")

fig_comparacao = px.bar(
    stats_regiao,
    x='Região',
    y='Média',
    color='Região',
    title=f"Média de {indicador_selecionado} por Região",
    labels={"Média": f"Média de {indicador_selecionado}"},
    text_auto=True
)

st.plotly_chart(fig_comparacao, use_container_width=True)

# Nota de rodapé
st.caption('Este exemplo demonstra como implementar filtros interativos para análise dos dados socioeconômicos de Natal/RN, permitindo exploração dinâmica e visualizações comparativas.')
