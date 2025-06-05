"""
Exemplo 4 - Layout e Containers

Este exemplo demonstra as diferentes opções de layout do Streamlit:
- Colunas
- Containers
- Expanders
- Tabs
- Sidebar

O objetivo é mostrar como organizar a interface do usuário de forma
eficiente e responsiva.

Autor: Victor Gomes
Data: Junho 2024
"""

import streamlit as st
import pandas as pd
import numpy as np

# Configuração básica da página
st.set_page_config(page_title="Exemplo 4: Layout e Containers", page_icon="📑")

# Título e introdução
st.title('Layout e Containers no Streamlit')
st.markdown('Este exemplo demonstra como organizar sua aplicação usando diferentes opções de layout, utilizando dados de Natal/RN.')

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

# === Colunas ===
st.header('Colunas')
st.markdown('Você pode dividir a tela em colunas para melhor organização:')

# Criando três colunas
col1, col2, col3 = st.columns(3)

# Adicionando conteúdo em cada coluna
with col1:
    st.subheader("Região Norte")
    df_norte = df_natal[df_natal['regiao'] == 'norte']
    st.metric(label="Número de Bairros", value=len(df_norte))
    st.metric(label="Renda Média", value=f"R$ {df_norte['renda_mensal_pessoa'].mean():.2f}")

with col2:
    st.subheader("Região Sul")
    df_sul = df_natal[df_natal['regiao'] == 'sul']
    st.metric(label="Número de Bairros", value=len(df_sul))
    st.metric(label="Renda Média", value=f"R$ {df_sul['renda_mensal_pessoa'].mean():.2f}")

with col3:
    st.subheader("Região Leste")
    df_leste = df_natal[df_natal['regiao'] == 'leste']
    st.metric(label="Número de Bairros", value=len(df_leste))
    st.metric(label="Renda Média", value=f"R$ {df_leste['renda_mensal_pessoa'].mean():.2f}")

# === Containers ===
st.header('Containers')
st.markdown('Containers agrupam elementos relacionados:')

with st.container():
    st.write("Este container mostra a distribuição de população por região.")
    
    # Calculando a população total por região
    pop_por_regiao = df_natal.groupby('regiao')['populacao'].sum().reset_index()
    
    # Criando um gráfico de barras simples
    st.bar_chart(pop_por_regiao.set_index('regiao'))
    
    st.write("Podemos ver que a distribuição populacional varia significativamente entre as regiões.")

# === Expanders ===
st.header('Expanders')
st.markdown('Expanders podem ocultar conteúdo que não precisa ser mostrado o tempo todo:')

with st.expander("Clique para ver detalhes sobre rendimento nominal médio"):
    st.write("O rendimento nominal médio é medido em salários mínimos.")
    
    # Ordenando os bairros por rendimento nominal médio
    top_bairros = df_natal.sort_values('rendimento_nominal_medio', ascending=False).head(5)
    
    st.write("Top 5 bairros com maior rendimento nominal médio:")
    st.dataframe(top_bairros[['bairro', 'regiao', 'rendimento_nominal_medio']])
    
    st.write("Estatísticas de rendimento nominal médio por região:")
    st.dataframe(df_natal.groupby('regiao')['rendimento_nominal_medio'].agg(['mean', 'min', 'max']).round(2))

# === Tabs ===
st.header('Abas')
st.markdown('Abas permitem organizar conteúdo em diferentes seções:')

tab1, tab2, tab3 = st.tabs(["Gráfico", "Tabela", "Estatísticas"])

with tab1:
    st.header("Visualização em Gráfico")
    st.write("Renda mensal por pessoa em cada região:")
    
    # Calculando a média de renda por região
    renda_por_regiao = df_natal.groupby('regiao')['renda_mensal_pessoa'].mean().reset_index()
    
    # Criando um gráfico de barras
    st.bar_chart(renda_por_regiao.set_index('regiao'))

with tab2:
    st.header("Visualização em Tabela")
    st.write("Dados completos dos bairros:")
    st.dataframe(df_natal)

with tab3:
    st.header("Estatísticas")
    st.write("Estatísticas descritivas da população:")
    st.dataframe(df_natal['populacao'].describe().round(2))
    
    st.write("Estatísticas descritivas da renda mensal por pessoa:")
    st.dataframe(df_natal['renda_mensal_pessoa'].describe().round(2))

# === Sidebar ===
st.sidebar.header('Filtros na Sidebar')
st.sidebar.write('A sidebar é útil para controles e filtros.')

# Adicionando filtros na sidebar
regiao_filtro = st.sidebar.selectbox('Filtrar por região:', ['Todas'] + sorted(df_natal['regiao'].unique().tolist()))

if regiao_filtro != 'Todas':
    df_filtrado = df_natal[df_natal['regiao'] == regiao_filtro]
    st.sidebar.write(f"Mostrando {len(df_filtrado)} bairros da região {regiao_filtro}.")
else:
    df_filtrado = df_natal
    st.sidebar.write(f"Mostrando todos os {len(df_filtrado)} bairros.")

# Adicionando um slider para filtrar por população
pop_min, pop_max = st.sidebar.slider(
    'Filtrar por população:',
    min_value=int(df_natal['populacao'].min()),
    max_value=int(df_natal['populacao'].max()),
    value=(int(df_natal['populacao'].min()), int(df_natal['populacao'].max()))
)

df_filtrado = df_filtrado[(df_filtrado['populacao'] >= pop_min) & (df_filtrado['populacao'] <= pop_max)]
st.sidebar.write(f"Bairros selecionados: {len(df_filtrado)}")

# Exibindo os resultados filtrados
st.header('Resultados Filtrados')
st.dataframe(df_filtrado)

# Nota de rodapé
st.caption('Este exemplo demonstra as diferentes opções de layout disponíveis no Streamlit para organizar sua aplicação, utilizando dados reais de Natal/RN.')
