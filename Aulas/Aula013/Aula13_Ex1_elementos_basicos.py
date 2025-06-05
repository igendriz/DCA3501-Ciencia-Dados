"""
Exemplo 1 - Elementos Básicos do Streamlit

Este exemplo demonstra os elementos fundamentais do Streamlit, incluindo:
- Texto e formatação com markdown
- Títulos e subtítulos
- Layouts básicos
- Exibição de dados
- Customização de página

O objetivo é fornecer uma introdução aos componentes básicos necessários
para criar uma aplicação Streamlit.

Autor: Victor Gomes
Data: Junho 2024
"""

import streamlit as st
import pandas as pd
import numpy as np

# Configuração básica da página
st.set_page_config(page_title="Exemplo 1: Elementos Básicos do Streamlit", page_icon="📝")

# Título e texto
st.title('Elementos Básicos do Streamlit')
st.header('Demonstração de componentes de texto e mídia')
st.subheader('Um exemplo simples para começar')

# Texto simples e markdown
st.text('Este é um texto simples sem formatação.')
st.markdown('**Markdown** permite _formatação_ de texto.')

# Exibindo informações
st.write('O comando st.write() é versátil e aceita diferentes tipos de dados:')
st.write(
    "- Texto simples",
    {"chave": "valor"},
    pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
)

# Exibindo código
st.code('''
def hello():
    print("Olá, Streamlit!")
''', language='python')

# Exibindo métricas
st.metric(label="Temperatura", value="28°C", delta="1.2°C")

# Separador
st.divider()

# Mensagens de status
st.success('Este é um exemplo de mensagem de sucesso')
st.info('Este é um exemplo de mensagem informativa')
st.warning('Este é um exemplo de aviso')
st.error('Este é um exemplo de erro')

# Nota de rodapé
st.caption('Este exemplo demonstra os elementos básicos de texto e formatação do Streamlit.')
