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
