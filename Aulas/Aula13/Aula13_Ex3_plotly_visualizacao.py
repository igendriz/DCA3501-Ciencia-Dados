"""
Exemplo 3 - Visualizações com Plotly

Este exemplo demonstra diferentes tipos de visualizações usando Plotly:
- Gráficos de barras
- Gráficos de dispersão

O objetivo é mostrar como criar visualizações interativas e
personalizáveis usando Plotly com Streamlit.

Autor: Victor Gomes
Data: Junho 2024
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configuração básica da página
st.set_page_config(page_title="Exemplo 3: Visualização com Plotly", page_icon="📊")

# Título e introdução
st.title('Visualizações com Plotly no Streamlit')
st.markdown('Este exemplo demonstra como integrar gráficos interativos do Plotly em aplicações Streamlit usando os dados de Natal/RN.')

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

# Exibindo os dados
st.header('Dados dos Bairros de Natal/RN')
st.dataframe(df_natal)

# Gráfico de barras com Plotly Express
st.header('Gráfico de Barras')
st.markdown('Usando `px.bar()` para criar um gráfico de barras interativo:')

fig_bar = px.bar(
    df_natal, 
    x='bairro', 
    y='rendimento_nominal_medio',
    color='regiao',
    title='Rendimento Nominal Médio por Bairro (em salários mínimos)',
    labels={'rendimento_nominal_medio': 'Rendimento Nominal Médio (sal. mín.)', 'bairro': 'Bairro'}
)

# Ajustando layout para melhor visualização
fig_bar.update_layout(
    xaxis_tickangle=-45,
    height=500
)

# Exibindo o gráfico
st.plotly_chart(fig_bar, use_container_width=True)

# Gráfico de dispersão
st.header('Gráfico de Dispersão')
st.markdown('Usando `px.scatter()` para criar um gráfico de dispersão interativo:')

fig_scatter = px.scatter(
    df_natal, 
    x='renda_mensal_pessoa', 
    y='populacao',
    color='regiao',
    size='rendimento_nominal_medio',
    hover_name='bairro',
    title='Renda Mensal por Pessoa vs População',
    labels={
        'renda_mensal_pessoa': 'Renda Mensal por Pessoa (R$)',
        'populacao': 'População',
        'rendimento_nominal_medio': 'Rendimento Nominal Médio'
    }
)

# Exibindo o gráfico
st.plotly_chart(fig_scatter, use_container_width=True)

# Visualização espacial com Plotly
st.header('Visualização Espacial')
st.markdown('Usando `go.Scatter` para criar uma visualização espacial dos bairros:')

# Dicionário com cores atribuídas para cada região
cores_regiao = {
    'norte': 'blue',
    'sul': 'green',
    'leste': 'orange',
    'oeste': 'red'
}

# Criar figura Plotly para visualização espacial
fig_espacial = go.Figure()

# Adicionar pontos para cada região
for regiao, grupo in df_natal.groupby('regiao'):
    fig_espacial.add_trace(go.Scatter(
        x=grupo['x'] / 1e3,  # Converter para km
        y=grupo['y'] / 1e3,  # Converter para km
        mode='markers+text',
        marker=dict(
            size=grupo['rendimento_nominal_medio'] * 10,  # Tamanho proporcional ao rendimento
            color=cores_regiao.get(regiao, 'gray'),
            opacity=0.8,
            line=dict(width=1, color='black')
        ),
        text=grupo['bairro'],
        textposition="top center",
        name=regiao.capitalize(),
        hovertemplate=(
            "<b>%{text}</b><br>" +
            f"Região: {regiao.capitalize()}<br>" +
            "Rendimento: %{marker.size:.1f} sal. mín.<br>" +
            "Coordenada X: %{x:.2f} km<br>" +
            "Coordenada Y: %{y:.2f} km"
        )
    ))

# Configurações do layout
fig_espacial.update_layout(
    title="Distribuição Espacial dos Bairros por Rendimento",
    xaxis_title="Coordenada X (km)",
    yaxis_title="Coordenada Y (km)",
    legend_title="Região",
    height=600,
    hovermode='closest'
)

# Exibir o gráfico
st.plotly_chart(fig_espacial, use_container_width=True)

# Adicionando interatividade com widgets
st.header('Interatividade com Widgets')

# Seletor para escolher a variável Y
y_var = st.selectbox(
    'Selecione a variável para análise:',
    ['rendimento_nominal_medio', 'renda_mensal_pessoa', 'populacao']
)

# Mapeamento de rótulos para exibição
rotulos = {
    'rendimento_nominal_medio': 'Rendimento Nominal Médio (sal. mín.)',
    'renda_mensal_pessoa': 'Renda Mensal por Pessoa (R$)',
    'populacao': 'População'
}

# Checkbox para mostrar valores nos gráficos
show_values = st.checkbox('Mostrar valores no gráfico', value=True)

# Criando gráfico baseado na seleção
fig_interactive = px.bar(
    df_natal.sort_values(by=y_var, ascending=False), 
    x='bairro', 
    y=y_var,
    color='regiao',
    title=f'{rotulos[y_var]} por Bairro',
    text=y_var if show_values else None,
    labels={'bairro': 'Bairro', y_var: rotulos[y_var]}
)

if show_values:
    fig_interactive.update_traces(texttemplate='%{text:.2s}', textposition='outside')

# Ajustando layout para melhor visualização
fig_interactive.update_layout(
    xaxis_tickangle=-45,
    height=500
)

# Exibindo o gráfico interativo
st.plotly_chart(fig_interactive, use_container_width=True)

# Nota de rodapé
st.caption('Este exemplo demonstra como integrar gráficos interativos do Plotly em aplicações Streamlit usando dados reais de Natal/RN.')
