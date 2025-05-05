# DataFlow DSL

DataFlow é uma Linguagem de Domínio Específico (DSL) para análise de dados, desenvolvida em Python usando ANTLR4. A DSL permite realizar operações comuns de análise de dados de forma simples e intuitiva.

## Requisitos

- Python 3.13 ou superior
- ANTLR4 Tools
- Dependências Python listadas em `requirements.txt`

## Instalação

1. Clone o repositório:
```bash
git clone <repository-url>
cd DataFlow
```

2. Instale o ANTLR4 Tools:
```bash
pip install antlr4-tools
```

3. Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```

4. Instale o projeto em modo de desenvolvimento:
```bash
pip install -e .
```

## Estrutura do Projeto

```
DataFlow/
├── src/
│   ├── grammar/
│   │   ├── DataFlow.g4        # Gramática ANTLR4
│   │   └── ...               # Arquivos gerados pelo ANTLR4
│   ├── __init__.py
│   └── dataflow.py           # Implementação principal
├── examples/
│   ├── sales.csv             # Dados de exemplo
│   ├── example.py            # Exemplos básicos
│   └── advanced_example.py   # Exemplos avançados
├── requirements.txt
└── setup.py
```

## Funcionalidades

A DSL suporta as seguintes operações:

1. **Carregamento de Dados**
   ```
   load "arquivo.csv";
   ```

2. **Filtragem**
   ```
   filter coluna > valor;
   filter regiao = "Norte";
   ```

3. **Agrupamento**
   ```
   group by coluna;
   ```

4. **Agregação**
   ```
   aggregate sum of vendas as total_vendas;
   ```
   Funções suportadas: sum, avg, count, min, max

5. **Ordenação**
   ```
   sort by coluna desc;
   sort by coluna asc;
   ```

6. **Seleção de Colunas**
   ```
   select coluna1, coluna2, coluna3;
   ```

7. **Transformação de Dados**
   ```
   transform nova_coluna = coluna1 * coluna2;
   ```
   Operadores suportados: +, -, *, /

8. **Visualização**
   ```
   show table;
   ```

## Exemplos

### Exemplo Básico
```python
from src.dataflow import DataFlow

df = DataFlow()

pipeline = """
load "data.csv";
filter vendas > 1000;
group by regiao;
aggregate sum of vendas as total;
show table;
"""

df.execute(pipeline)
```

### Exemplo Avançado
```python
pipeline = """
load "sales.csv";
transform total_value = sales * quantity;
group by region;
aggregate sum of total_value as region_total;
sort by region_total desc;
select region, region_total;
show table;
"""
```

## Como Funciona

O projeto utiliza o ANTLR4 para processar a DSL em três etapas principais:

1. **Análise Léxica**: O código da DSL é dividido em tokens (palavras-chave, identificadores, operadores, etc.)

2. **Análise Sintática**: Os tokens são organizados em uma árvore de análise sintática de acordo com as regras da gramática

3. **Visitante**: A classe `DataFlowVisitorImpl` percorre a árvore e executa as operações correspondentes usando o pandas

A implementação usa o pandas para realizar as operações de dados de forma eficiente, permitindo:
- Manipulação de dados tabulares
- Filtragem e agregação
- Transformações e cálculos
- Ordenação e seleção de colunas

## Regenerando os Arquivos do ANTLR

Se você modificar a gramática (`DataFlow.g4`), será necessário regenerar os arquivos do ANTLR:

```bash
antlr4 -Dlanguage=Python3 -visitor grammar/DataFlow.g4
```

## Limitações Atuais

- Suporta apenas arquivos CSV como fonte de dados
- Visualização limitada ao formato tabular
- Não suporta joins entre diferentes fontes de dados
- Operações matemáticas limitadas às quatro operações básicas 