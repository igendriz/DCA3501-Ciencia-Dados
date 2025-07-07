<h1 align="center">DCA3501 – Ciência de Dados</h1>


<p align="center">
  <em>"Os números têm uma história importante para contar.<br>
  Cabe a você apresentar essa história de forma clara e convincente."</em><br>
  — <strong>Stephen Few</strong>
</p>

---

## 🧭 Visão Geral da Disciplina

A disciplina **DCA3501 – Ciência de Dados** apresenta os fundamentos essenciais da área, incluindo conceitos introdutórios de **Aprendizado de Máquina (Machine Learning – ML)**, com foco em aplicações práticas. O conteúdo combina teoria, notebooks interativos e estudos de caso. As aulas são estruturadas para conduzir o estudante de forma gradual dos conceitos básicos até tópicos mais avançados, sempre com ênfase no uso de ferramentas computacionais modernas e na resolução de problemas do mundo real.

---

## 🎯 Objetivos da Disciplina

- Introduzir os conceitos fundamentais de Ciência de Dados e ML;
- Desenvolver habilidades práticas em Python para análise e modelagem de dados;
- Aplicar técnicas de visualização, pré-processamento e classificação em dados reais;
- Estimular o pensamento crítico para avaliação de modelos e resultados.

---

## 🧪 Metodologia

- Aulas expositivas com exemplos práticos;
- Notebooks interativos em Python com execução via [Google Colab](https://colab.research.google.com);
- Estudos de caso baseados em dados reais;
- Avaliação baseada em participação, exercícios práticos e projeto final.

## 📝 Avaliações
A avaliação da disciplina será baseada principalmente em três projetos práticos, que envolvem o desenvolvimento de soluções de Ciência de Dados aplicadas a problemas reais. Além desses projetos, poderão ser propostas atividades complementares ao longo do semestre para reforçar o aprendizado.

---

## 🎓 Público-alvo

Estudantes de graduação em cursos de **Engenharia** ou de outras áreas que tenham interesse em **Ciência de Dados**, **Aprendizado de Máquina** e suas **aplicações práticas em contextos reais**.

---

## 📘 Aula 00 – Apresentação e Organização da Disciplina

### Conteúdo:
- Apresentação geral da disciplina;
- O que é Ciência de Dados? Por que estudar?
- Exemplos de aplicações em engenharia e outras áreas de atuação.

### Materiais:

📄 [`aula00.pdf`](Aulas/Aula00/aula00.pdf)

---

## 📘 Aula 01 – Repositório da Disciplina e Introdução ao Python

### Conteúdo:
- Estrutura do repositório e como utilizar os notebooks no Google Colab;
- Breve introdução ao ambiente de desenvolvimento (Colab, GitHub, Python).

### Materiais:

💻 [`notebook_aula01.ipynb`](Aulas/Aula01/Aula01-Introducao_ao_Python.ipynb)  

---

## 📘 Aula 02 – Computação Científica com o Pacote NumPy

### Objetivo:
- Apresentar o pacote **NumPy** para computação científica em Python.
- Demonstrar o uso do tipo **array**, que, apesar de sintaticamente semelhante a listas, é significativamente mais eficiente em termos computacionais.
- Explicar que os elementos de uma variável do tipo **array** em NumPy são do mesmo tipo, o que garante maior eficiência em comparação com listas.

### Contextualização:
- **NumPy** é o pacote fundamental para computação científica com Python, fornecendo suporte para operações com vetores multidimensionais e funções de álgebra linear.
- Muitos outros pacotes Python utilizam as representações de **array** do NumPy como uma estrutura de dados básica e eficiente.
- O pacote **SciPy** amplia as funcionalidades do NumPy, oferecendo uma coleção de algoritmos numéricos e ferramentas específicas para áreas como processamento de sinais, otimização e estatísticas.
- **Matplotlib**, um dos pacotes mais populares para visualização de dados em Python, utiliza arrays do NumPy como base para criar gráficos.

### Materiais:

💻 [`notebook_aula02.ipynb`](Aulas/Aula02/Aula02-Pacote_Numpy.ipynb)  

---

## 📘 Aula 03 – Pacote de Gráficos Matplotlib

### Conteúdo:
- Introdução ao pacote **Matplotlib** para visualização de dados em Python.
- Principais comandos para criação de gráficos básicos e personalização.
- Uso da interface **pyplot** para traçado de gráficos.

### Contextualização:
O **Matplotlib** é uma das bibliotecas mais populares para visualização de dados em Python, sendo amplamente utilizada por sua flexibilidade e integração com o pacote **NumPy**. É uma biblioteca multiplataforma projetada para funcionar em conjunto com outras ferramentas científicas, como o **SciPy**.

#### Principais Características:
- Permite a criação de diversos tipos de gráficos, desde gráficos de linha básicos até visualizações mais complexas.
- A interface **pyplot** é amplamente utilizada para gerar gráficos interativos e estáticos de forma simples.

#### Exemplos de Uso:
- Para importar o pacote Matplotlib:
  ```python
  import matplotlib as mpl
  import matplotlib.pyplot as plt
  ```
- Para traçar um gráfico de linha básico:
  ```python
  plt.plot(x, y)
  plt.show()
  ```
  
#### Mais Informações:
- Site oficial do Matplotlib: [https://matplotlib.org/index.html](https://matplotlib.org/index.html)

### Materiais:

💻 [`notebook_aula03.ipynb`](Aulas/Aula03/Aula03-Pacote_MatPlotlib.ipynb)  

---

## 📘 Aula 04 – Pacote Pandas – Parte I

### Conteúdo:
- Introdução ao pacote **Pandas** para manipulação e análise de dados em Python.
- Principais estruturas de dados: **DataFrame** e **Series**.
- Diferenças entre os tipos de dados do Pandas e os arrays do **NumPy**.

### Contextualização:
O pacote **Pandas** é amplamente utilizado para análise de dados e é construído sobre os pacotes **NumPy** e **Matplotlib**. Diferentemente dos arrays do NumPy, as variáveis manipuladas pelo Pandas podem conter elementos de tipos diversos (não homogêneos), proporcionando maior flexibilidade na manipulação de dados estruturados.

#### Principais Estruturas de Dados:
- **DataFrames:**  
  Estruturas de dados retangulares que representam informações em formato de tabela, semelhante a planilhas. As colunas possuem o mesmo comprimento, e cada coluna contém elementos de um mesmo tipo de dado.  

- **Series:**  
  Objetos unidimensionais que contêm um array de dados, semelhante a um array NumPy, mas com um conjunto associado de rótulos (índices). Quando não especificados, os índices seguem o padrão NumPy (de zero a n-1).  

#### Principais Vantagens:
Com essas estruturas de dados, o Pandas implementa uma série de operações de alto nível, especialmente úteis para usuários que trabalham com **bancos de dados** e **planilhas**.

### Materiais:

💻 [`notebook_aula04.ipynb`](Aulas/Aula04/Aula04_Pacote_Pandas_ParteI.ipynb)  

## 📘 Aula 05 – Pacote Pandas – Parte II (Prática Individual)

### Conteúdo:
- Atividade prática para reforçar os conceitos apresentados na aula anterior.
- Exercícios envolvendo leitura de arquivos e visualização de dados com Pandas e Matplotlib.
- Exploração de diferentes bases de dados para aplicar operações básicas de análise.

### Contextualização:
O objetivo desta aula é permitir que os(as) estudantes pratiquem, de forma individual, o uso de comandos essenciais do Pandas. A aula foca na consolidação dos conhecimentos por meio da experimentação prática com importação de dados, criação de gráficos e manipulação básica de tabelas.

### Materiais:

💻 [`notebook_aula05.ipynb`](Aulas/Aula05/Aula05-Pacote_Pandas_ParteII.ipynb)  

---

## 📘 Aula 06 – Pacote Pandas – Parte III

### Conteúdo:
- Manipulação avançada de DataFrames com **GroupBy**, **Merge**, **Join** e **Concatenação**.
- Aplicações práticas de operações condicionais e agregações estruturadas.

### Contextualização:
Nesta aula, abordamos funcionalidades avançadas do Pandas voltadas à integração, filtragem e agregação de dados em múltiplas tabelas. São ferramentas fundamentais para a análise exploratória de dados mais complexos e estruturados, comumente encontradas em contextos profissionais e científicos.

#### Funcionalidades Avançadas:
- **GroupBy:** Técnica inspirada no comando SQL `GROUP BY`, que realiza uma sequência de operações:
  - **Split:** Agrupamento do DataFrame com base em uma ou mais chaves.
  - **Apply:** Aplicação de funções de agregação, transformação ou filtragem sobre os grupos.
  - **Combine:** Combinação dos resultados em um único objeto de saída.

- **Merge e Join:** Técnicas para combinar tabelas com base em chaves comuns, semelhantes às operações de junção em bancos de dados relacionais.

- **Concatenação:** Empilhamento de DataFrames horizontal ou verticalmente, útil para reorganizar e unir tabelas.

### Materiais:

💻 [`notebook_aula06.ipynb`](Aulas/Aula06/Aula06-Pacote_Pandas_ParteIII.ipynb)  

---
## 📘 Aula 07 – Pandas – Parte IV: Análise Exploratória de Dados (EDA)

### Conteúdo:
- Introdução à **Análise Exploratória de Dados (EDA)**.
- Uso de dados reais para estudo comparativo entre bairros de Natal/RN.
- Geração de gráficos de barras, dispersão e observações estatísticas com `pandas` e `matplotlib`.

### Contextualização:
A Análise Exploratória de Dados (AED ou EDA – *Exploratory Data Analysis*) é uma etapa fundamental na **Ciência de Dados**, utilizada para compreender padrões, detectar anomalias e formular hipóteses com base em dados. Neste estudo, são analisados dados socioeconômicos de 36 bairros da cidade de **Natal/RN**, agrupados em quatro regiões administrativas: **Norte**, **Sul**, **Leste** e **Oeste**.

#### Objetivos:
- Aplicar técnicas de EDA em um conjunto de dados reais.
- Compreender desigualdades regionais por meio de indicadores como população e renda.
- Explorar visualizações como gráficos de dispersão e gráficos de barras.

#### Materiais e Métodos:
- **Dados**: Extraídos do **IBGE** (com fins exclusivamente didáticos).  
- **Ferramentas**: Python 3.12.4 com `pandas`, `numpy` e `matplotlib` (usando os conteúdos estudados em aulas anteriores).
- **Abordagem**: Visualização e separação simples por regiões administrativas.

#### Resultados:
A análise revelou contrastes socioeconômicos entre os bairros das regiões:
- **Norte** e **Oeste**: maior densidade populacional e menor renda média.
- **Leste** e **Sul**: bairros menos populosos e com maior rendimento médio per capita.

#### Conclusão:
A aula demonstra o potencial das ferramentas de Ciência de Dados na análise de dados públicos, promovendo o desenvolvimento de análises quantitativas com relevância social e apoio à tomada de decisão.

### Materiais:

💻 [`notebook_aula07.ipynb`](Aulas/Aula07/Aula07_PandasIV-EDA.ipynb)  
📄 [`aula07.pdf`](Aulas/Aula07/Aula07_PandasIV-EDA.pdf)

## 📘 Aula 08 – Fundamentos de Estatística

### Conteúdo:
- Conceitos fundamentais de estatística: média, mediana, variância, desvio padrão e outras medidas de tendência central e dispersão.
- Utilização de funções estatísticas nos pacotes **NumPy**, **Pandas** e **SciPy**.
- Introdução prática às distribuições estatísticas usando o módulo `stats` da biblioteca **SciPy**.

### Contextualização:
A estatística é uma base essencial da **Ciência de Dados**, fornecendo ferramentas para descrever, interpretar e modelar dados. Nesta aula, são apresentados conceitos fundamentais da estatística descritiva, bem como a aplicação de distribuições de probabilidade para modelar variáveis aleatórias.

#### Tópicos abordados:
- Como calcular medidas estatísticas com funções prontas das bibliotecas NumPy, Pandas e SciPy.
- Geração de números aleatórios para simulações.
- Uso do módulo `scipy.stats` para trabalhar com distribuições discretas e contínuas.
- Comandos iniciais:
  ```python
  from scipy import stats
  ```

#### Exemplos de aplicação:
- Simulação de variáveis aleatórias.
- Visualização de distribuições.
- Análise de características estatísticas de conjuntos de dados.

### Materiais:

💻 [`notebook_aula08.ipynb`](Aulas/Aula08/Aula08_Fundamentos-Estatistica.ipynb)  
📄 [`aula08.pdf`](Aulas/Aula08/Aula08_Fundamentos-Estatistica.pdf)

## 📘 Aula 09 – Modelos Estatísticos

### Conteúdo:
- Aplicação prática de **modelos estatísticos** por meio do uso de distribuições de probabilidade no pacote `scipy.stats`.
- Extração de medidas estatísticas a partir de distribuições paramétricas.
- Geração e visualização de distribuições para análise e simulação.

### Contextualização:
Nesta aula, aprofundamos o estudo das distribuições estatísticas, focando em sua implementação prática com a biblioteca **SciPy**, por meio do submódulo `stats`. As distribuições estatísticas permitem representar matematicamente variáveis aleatórias e modelar fenômenos reais em diversos contextos científicos e aplicados.

#### Distribuições abordadas:
- **Distribuição Uniforme:**  
  Modelo de distribuição onde todos os valores de um intervalo possuem a mesma probabilidade de ocorrência.
  
- **Distribuição Normal:**  
  Uma das distribuições mais utilizadas em estatística e ciência de dados. Usada para modelar fenômenos naturais com comportamento simétrico em torno da média.

#### Exemplos de aplicação:
- Simulação de dados a partir de distribuições conhecidas.
- Cálculo de estatísticas como média, variância, desvio padrão, quantis e funções de densidade.
- Visualização e comparação entre distribuições.

### Materiais:

💻 [`notebook_aula09.ipynb`](Aulas/Aula09/Aula09_Modelos-Estatisticos.ipynb)  
📄 [`aula09.pdf`](Aulas/Aula09/Aula09_Modelos-Estatisticos.pdf)

## 📘 Aula 10 – Análise Exploratória de Dados (EDA) com Pandas e Seaborn

### Conteúdo:

* Uso do pacote **Seaborn** para visualização estatística durante o processo de EDA.
* Aplicação de ferramentas baseadas no **Pandas** para agilizar e/ou automatizar o processo de análise exploratória.

### Contextualização:

A **Análise Exploratória de Dados (EDA)** é uma etapa essencial no fluxo de trabalho da Ciência de Dados, permitindo a identificação de padrões, tendências e anomalias. Nesta aula, exploraremos as capacidades do **Seaborn**, uma biblioteca de visualização de dados construída sobre o **Matplotlib**, com integração direta com o **Pandas**.

#### Pacote Seaborn:

O **Seaborn** fornece uma API de alto nível para a criação de gráficos estatísticos, permitindo gerar visualizações ricas e esteticamente atraentes com poucas linhas de código. Ele facilita a criação de gráficos como:

* Gráficos de dispersão (scatter plots)
* Gráficos de regressão
* Gráficos de densidade (kdeplots)
* Mapas de calor (heatmaps)

📌 **Links de Referência para Seaborn:**

* [Seaborn – Documentação Oficial](https://seaborn.pydata.org/)
* [Python Data Science Handbook – Seaborn](https://jakevdp.github.io/PythonDataScienceHandbook/04.14-visualization-with-seaborn.html)
* [Minerando Dados – Seaborn Tutorial](https://minerandodados.com.br/tutorial-completo-de-como-trabalhar-com-a-biblioteca-seaborn/)

---

### Pacotes para Automatização do Processo de EDA:

Além do Seaborn, há ferramentas desenvolvidas sobre o **Pandas** para automatizar o processo de EDA, permitindo gerar relatórios rápidos e gráficos detalhados de forma automática:

* **Pandas Profiling:** Gera um relatório exploratório detalhado a partir de um DataFrame.

  * [Documentação](https://pandas-profiling.github.io/pandas-profiling/docs/master/index.html)

* **Sweetviz:** Cria relatórios interativos e visualizações de comparação entre conjuntos de dados.

  * [Sweetviz no PyPI](https://pypi.org/project/sweetviz/)

* **AutoViz:** Automatiza a criação de gráficos exploratórios a partir de um único comando.

  * [AutoViz – Site Oficial](https://autoviz.io/)

* **QuickDA:** Uma abordagem simplificada para EDA e limpeza de dados.

  * [QuickDA – Tutorial](https://analyticsindiamag.com/hands-on-tutorial-on-quickda-for-data-analysis-and-cleaning/)

### Materiais:

💻 [`notebook_aula10.ipynb`](Aulas/Aula10/Aula10_EDA-Pandas&Seaborn.ipynb)
📄 [`aula10.pdf`](Aulas/Aula10/Aula10_EDA.pdf)

---

## 📘 Aula 12 – Gráficos Interativos com o Pacote Plotly

### Conteúdo:

* Introdução ao pacote **Plotly** para criação de gráficos interativos em Python.
* Diferenças entre os módulos `plotly.express` e `plotly.graph_objects`.
* Exemplos de visualização interativa para dados geográficos, séries temporais e categorias.

### Contextualização:

O **Plotly** é uma biblioteca open-source voltada à **visualização interativa de dados**, compatível com Python, R e JavaScript. Sua versão para Python (`plotly.py`) é construída sobre a biblioteca JavaScript `plotly.js` e permite incorporar visualizações interativas em **notebooks Jupyter/Colab** e **páginas HTML estáticas**.

Com suporte a mais de 40 tipos de gráficos (como gráficos de linhas, barras, dispersão, mapas e candlesticks), o Plotly é uma ferramenta poderosa e versátil para a construção de dashboards e relatórios interativos em ciência de dados.

#### Estrutura de Uso:

O Plotly possui dois módulos principais com abordagens distintas:

* **Plotly Express (`plotly.express` ou `px`)**
  Interface de alto nível, mais simples e concisa.

  ```python
  import plotly.express as px
  fig = px.tipo_grafico(dados, parametros)
  fig.show()
  ```

* **Plotly Graph Objects (`plotly.graph_objects` ou `go`)**
  Interface mais detalhada e flexível, ideal para customizações avançadas.

  ```python
  import plotly.graph_objects as go
  trace = go.TipoGrafico(x=x, y=y, ...)
  fig = go.Figure(data=[trace])
  fig.show()
  ```

#### Links de Referência:

* [Documentação Oficial do Plotly](https://plotly.com/)
* [Galeria de Gráficos](https://plotly.com/graphing-libraries/)
* [Blog – Plotly com Geomaps](https://medium.com/analytics-vidhya/plotly-for-geomaps-bb75d1de189f)
* [Tutorial Sigmoidal (em português)](https://sigmoidal.ai/como-criar-graficos-interativos-usando-plotly-e-python/)
* [YouTube: Introdução ao Plotly (vídeo 1)](https://www.youtube.com/watch?v=Xk0zHZBa7LM)
* [YouTube: Gráficos com Plotly (vídeo 2)](https://www.youtube.com/watch?v=CVSd0WKy5cs)

### Materiais:

💻 [`notebook_aula12.ipynb`](Aulas/Aula12/Aula12_Pacote-Plotly.ipynb)
📄 [`aula12.pdf`](Aulas/Aula12/Aula12_Graficos-Interativos.pdf)

---

## 📘 Aula 13 – Aplicações Interativas com Streamlit

### Conteúdo:

* Introdução ao uso do **Streamlit** para construção de aplicações web interativas voltadas à visualização e análise de dados.
* Exploração de componentes essenciais: `st.write()`, `st.dataframe()`, `st.plotly_chart()`, `st.slider()`, `st.button()`, entre outros.
* Integração com **Plotly** para visualizações interativas.
* Construção de uma aplicação baseada em dados socioeconômicos reais de Natal/RN.

### Contextualização:

O **Streamlit** é uma biblioteca de código aberto para Python que permite criar aplicações web de forma rápida e simples, com foco em **ciência de dados**. Sua integração nativa com bibliotecas como **Pandas**, **Matplotlib** e **Plotly** facilita a criação de dashboards interativos com poucas linhas de código.

Durante esta aula, os alunos exploram o Streamlit através de exemplos práticos e constroem uma aplicação interativa para visualizar e filtrar dados reais, aplicando técnicas de EDA em um ambiente web dinâmico.

### Materiais:

💻 Exemplos práticos:

* [`Aula13_Ex1_elementos_basicos.py`](Aulas/Aula13/Aula13_Ex1_elementos_basicos.py)
* [`Aula13_Ex2_widgets_interativos.py`](Aulas/Aula13/Aula13_Ex2_widgets_interativos.py)
* [`Aula13_Ex3_plotly_visualizacao.py`](Aulas/Aula13/Aula13_Ex3_plotly_visualizacao.py)
* [`Aula13_Ex4_layout_containers.py`](Aulas/Aula13/Aula13_Ex4_layout_containers.py)
* [`Aula13_Ex5_filtros_dados_reais.py`](Aulas/Aula13/Aula13_Ex5_filtros_dados_reais.py)

📄 Slides: [`aula13.pdf`](Aulas/Aula13/Aula13_Streamlit-para-Ciencia-de-Dados.pdf)

🔗 **Créditos:**
Os exemplos práticos utilizados nesta aula foram baseados e adaptados a partir do material criado por **Victor Gomes**, disponível em:
[https://github.com/VictorNGomes/Streamlit-Introduction](https://github.com/VictorNGomes/Streamlit-Introduction)

---

## 📘 Aula 14 – Aprendizagem Supervisionada com o Pacote Scikit-learn

### Conteúdo:

* Introdução ao pacote **Scikit-learn (sklearn)** para tarefas de **aprendizado supervisionado**.
* Aplicação prática do algoritmo de classificação **K-Nearest Neighbors (KNN)**.
* Execução completa de um pipeline de modelagem: do carregamento de dados à avaliação do modelo.

### Contextualização:

O **Scikit-learn** é uma das bibliotecas mais importantes da linguagem Python para tarefas de aprendizado de máquina. Nesta aula, exploramos sua aplicação em problemas de **classificação supervisionada**, com foco no modelo **KNN**, percorrendo todas as etapas essenciais do fluxo de trabalho em machine learning.

#### Etapas do Processo:

* Importação dos pacotes e definição do modelo (ex: `KNeighborsClassifier`).
* Carregamento e preparação dos dados (features e alvo como arrays do NumPy).
* Separação em **dados de treinamento e teste**.
* **Binarização** de dados, se necessário.
* **Treinamento** do modelo com `modelo.fit(...)`.****
* **Predição** com `modelo.predict(...)`.
* Avaliação dos resultados por meio de métricas adequadas.

### Materiais:

💻 [`notebook_aula14.ipynb`](Aulas/Aula14/Aula_14_Pacote_Sklearn_Classificacao.ipynb)

---
## 📘 Aula 16 – Aprendizagem Não Supervisionada com o Pacote Scikit-learn

### Conteúdo:

* Introdução aos principais **algoritmos de agrupamento (clustering)** disponíveis no pacote **Scikit-learn**.
* Aplicações práticas com os métodos **K-Means** e **Hierárquico Aglomerativo**.
* Análise preliminar de dados e avaliação de agrupamentos com métricas específicas.

### Contextualização:

A aprendizagem **não supervisionada** é uma abordagem em que os modelos aprendem padrões a partir de dados **sem rótulos definidos**. Nesta aula, exploramos técnicas de **agrupamento de dados (clustering)** com o uso do Scikit-learn, destacando a aplicação dos algoritmos **K-Means** e **Hierárquico**, amplamente utilizados para segmentação de dados em diversas áreas.

#### Tópicos abordados:

* Exemplos práticos com conjuntos de dados sintéticos e reais.
* Análise exploratória para identificar estruturas ou tendências nos dados.
* Algoritmos de agrupamento offline:

  * **K-Means**
  * **Hierárquico Aglomerativo**
* Avaliação da qualidade dos agrupamentos por meio de métricas como **inércia**, **silhouette score**, entre outras.

### Referências:

* Jake VanderPlas – *Python Data Science Handbook*, O’Reilly (2017)
* Andreas C. Müller & Sarah Guido – *Introduction to Machine Learning with Python*, O’Reilly (2017)
* [Documentação oficial – Scikit-learn Clustering](https://scikit-learn.org/stable/modules/clustering.html)
* [Artigo – Towards Data Science: 5 clustering algorithms](https://towardsdatascience.com/the-5-clustering-algorithms-data-scientists-need-to-know-a36d136ef68)

### Materiais:

💻 [`notebook_aula16.ipynb`](Aulas/Aula16/Aula_16_Agrupamento_de_Dados.ipynb)

---

## 📁 Estrutura do Repositório

```plaintext
DCA3501-Ciencia-de-Dados/
│
├── README.md                  ← Este arquivo
├── requirements.txt           ← Dependências dos notebooks (opcional)
│
├── Images/                    ← Imagens usadas no README ou nas apresentações
│   └── ...
│
├── Dataset/                   ← Conjuntos de dados usados nos notebooks
│   └── exemplo_dataset.csv    ← Acessível via URL direta do GitHub para uso no Colab
│
├── Aulas/                     ← Pastas com os materiais de cada aula
│   ├── Aula00/                
│   │   └── aula00.pdf        ← Apresentações em PDF ou outro formato
│   │   └── notebook_aula00.ipynb
│   │
│   ├── Aula01/
│   ├── Aula02/
│   └── ...
```

> 💡 Todos os notebooks serão preparados para execução no [Google Colab](https://colab.research.google.com).  
> Os datasets são carregados diretamente usando links brutos do GitHub.

---

## 📚 Recursos de Apoio

- [Livro1](https://jakevdp.github.io/PythonDataScienceHandbook/) - Python Data Science Handbook.
- [Livro2](https://wesmckinney.com/book/) - Python for Data Analysis
- [Kaggle – Curso de Python](https://www.kaggle.com/learn/python) – Curso introdutório com exercícios práticos.  
- [AI Python for Beginners – Andrew Ng](https://www.deeplearning.ai/short-courses/ai-python-for-beginners/) – Curso curto sobre Python voltado para IA.  
- [Python para Data Science](https://github.com/codenation-dev/Data-Science-Online) – Conteúdo aberto voltado para ciência de dados em português.

---

## 👨‍🏫 Docentes Responsáveis

- **Prof. Luis Affonso Guedes¹**  
  Ciência de Dados, Aprendizado de Máquina e Monitoramento Inteligente em Ambientes Industriais  

- **Prof. Colaborador Ignacio Sánchez-Gendriz**  
  Aprendizado de Máquina e Processamento de Sinais aplicados às Ciências da Vida  

¹ Departamento de Engenharia de Computação e Automação – Universidade Federal do Rio Grande do Norte (DCA/UFRN)
