"""
Exemplo 2 - Widgets Interativos

Este exemplo explora os diferentes widgets interativos disponíveis no Streamlit:
- Botões e checkboxes
- Campos de entrada (texto e números)
- Seletores (dropdown, multi-select)
- Sliders
- Radio buttons
- Text areas

O objetivo é mostrar como criar interatividade na aplicação e
responder a ações do usuário.

Autor: Victor Gomes
Data: Junho 2024
"""

import streamlit as st
import pandas as pd
import numpy as np

# Configuração básica da página
st.set_page_config(page_title="Exemplo 2: Widgets Interativos", page_icon="🎛️")

# Título e introdução
st.title('Widgets Interativos do Streamlit')
st.markdown('Este exemplo demonstra os principais widgets interativos disponíveis no Streamlit usando dados de Natal/RN.')

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

# Sidebar para organizar os controles
st.sidebar.header('Controles')

# === Botões e Checkbox ===
st.header('Botões e Checkbox')
col1, col2 = st.columns(2)

with col1:
    if st.button('Mostrar estatísticas'):
        st.write('Estatísticas básicas da renda mensal por pessoa:')
        st.write(df_natal['renda_mensal_pessoa'].describe())
    else:
        st.write('Clique no botão para ver estatísticas.')
    
    mostrar_mapa = st.checkbox('Mostrar mapa de regiões')
    if mostrar_mapa:
        st.write('Quantidade de bairros por região:')
        st.write(df_natal['regiao'].value_counts())
    
st.divider()

# === Campos de entrada ===
st.header('Campos de Entrada')
col1, col2 = st.columns(2)

with col1:
    bairro_busca = st.text_input('Digite o nome de um bairro para buscar')
    if bairro_busca:
        resultados = df_natal[df_natal['bairro'].str.contains(bairro_busca.lower())]
        if not resultados.empty:
            st.write(f'Resultados para "{bairro_busca}":')
            st.dataframe(resultados)
        else:
            st.warning(f'Nenhum bairro encontrado com "{bairro_busca}"')
    
    limiar_renda = st.number_input('Limiar de renda mensal (R$)', 
                                  min_value=float(df_natal['renda_mensal_pessoa'].min()), 
                                  max_value=float(df_natal['renda_mensal_pessoa'].max()),
                                  value=1000.0,
                                  step=100.0)
    st.write(f'Bairros com renda acima de R$ {limiar_renda:.2f}: {len(df_natal[df_natal["renda_mensal_pessoa"] > limiar_renda])}')

with col2:
    notas = st.text_area('Anotações sobre a análise', height=100)
    if notas:
        st.info('Anotações salvas!')

st.divider()
# === Seletores ===
st.header('Seletores')
col1, col2 = st.columns(2)

with col1:
    regiao = st.selectbox(
        'Escolha uma região',
        ['Todas'] + sorted(df_natal['regiao'].unique().tolist())
    )
    
    if regiao != 'Todas':
        st.write(f'Dados da região {regiao}:')
        st.dataframe(df_natal[df_natal['regiao'] == regiao])
    else:
        st.write('Mostrando todas as regiões')
    
    colunas_selecionadas = st.multiselect(
        'Selecione as colunas para visualizar',
        df_natal.columns.tolist(),
        default=['bairro', 'regiao', 'populacao']
    )
    if colunas_selecionadas:
        st.dataframe(df_natal[colunas_selecionadas])

with col2:
    metrica = st.radio(
        'Escolha uma métrica para análise',
        ['Renda Mensal por Pessoa', 'Rendimento Nominal Médio', 'População']
    )
    
    if metrica == 'Renda Mensal por Pessoa':
        coluna = 'renda_mensal_pessoa'
        unidade = 'R$'
    elif metrica == 'Rendimento Nominal Médio':
        coluna = 'rendimento_nominal_medio'
        unidade = 'salários mínimos'
    else:
        coluna = 'populacao'
        unidade = 'habitantes'
    
    st.write(f'Estatísticas de {metrica}:')
    st.write(f'Média: {df_natal[coluna].mean():.2f} {unidade}')
    st.write(f'Máximo: {df_natal[coluna].max():.2f} {unidade}')
    st.write(f'Mínimo: {df_natal[coluna].min():.2f} {unidade}')

# === Sliders ===
st.header('Sliders')
col1, col2 = st.columns(2)

with col1:
    n_bairros = st.slider('Número de bairros para mostrar', 1, len(df_natal), 5)
    st.write(f'Top {n_bairros} bairros com maior renda:')
    st.dataframe(df_natal.sort_values('renda_mensal_pessoa', ascending=False).head(n_bairros))

with col2:
    faixa_populacao = st.slider(
        'Faixa de população',
        float(df_natal['populacao'].min()), 
        float(df_natal['populacao'].max()),
        (10000.0, 30000.0)
    )
    st.write(f'Bairros com população entre {faixa_populacao[0]:.0f} e {faixa_populacao[1]:.0f} habitantes:')
    filtro_pop = df_natal[(df_natal['populacao'] >= faixa_populacao[0]) & 
                          (df_natal['populacao'] <= faixa_populacao[1])]
    st.dataframe(filtro_pop)

# === Seletores de Data e Hora ===
st.header('Data e Hora')
col1, col2 = st.columns(2)

with col1:
    import datetime
    d = st.date_input('Data da análise', datetime.date.today())
    st.write(f'Análise realizada em: {d}')

with col2:
    t = st.time_input('Horário da análise', datetime.time(12, 0))
    st.write(f'Horário: {t}')

# === Upload de Arquivo ===
st.header('Upload de Arquivo')
st.write("Você pode fazer upload de um arquivo CSV com dados adicionais para complementar a análise:")
arquivo = st.file_uploader("Escolha um arquivo CSV")
if arquivo is not None:
    try:
        # Tenta ler como CSV
        df_upload = pd.read_csv(arquivo)
        st.write('Visualização dos dados enviados:')
        st.dataframe(df_upload.head())
    except Exception as e:
        st.error(f'Erro ao ler o arquivo: {e}')
        st.info('Tente fazer upload de um arquivo CSV válido.')

# Nota de rodapé
st.caption('Este exemplo demonstra os principais widgets interativos do Streamlit para entrada de dados e controle de interface, utilizando dados reais de Natal/RN.')
