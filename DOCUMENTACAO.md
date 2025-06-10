# DataFlow DSL — Documentação do Sistema

## 1. Elaboração da Linguagem e Gramática
- **DSL**: DataFlow
- **Gramática**: Definida em `grammar/DataFlow.g4` usando ANTLR 4
- **Cobertura da gramática**:
  - Tokens: IDENTIFICADOR, STRING, NUMERO, BOOLEANO, etc.
  - Regras sintáticas para comandos: carregar, filtrar, agrupar, etc.
  - Expressões e operadores

## 2. Aplicação da Linguagem/Gramática
- **Contexto**: Análise de dados tabulares
- **DSL**: Específica para manipulação e análise de dados
- **Backend**: Pandas para processamento eficiente

## 3. Implementação de Lexer/Parser/Analisador Semântico/Máquina Virtual

### Camadas e Ferramentas
| Camada | Ferramenta | Arquivos Gerados/Classes |
|--------|------------|-------------------------|
| Lexer | ANTLR4 | DataFlow.tokens, DataFlowLexer.tokens |
| Parser | ANTLR4 | DataFlow.interp, DataFlowLexer.interp |
| Semântico | Visitor Pattern | DataFlowVisitorImpl |
| Máquina Virtual | Python + pandas | Classe DataFlow |

## 4. Operações Suportadas

### Comandos e Suas Finalidades
| Comando | Finalidade |
|---------|------------|
| carregar | Carregamento de dados |
| filtrar | Filtragem |
| agrupar por | Agrupamento |
| agregar | Agregação |
| ordenar por | Ordenação |
| selecionar | Seleção de colunas |
| transformar | Transformação de dados |
| mostrar | Visualização |

## 4.1 Criação e Localização dos Pipelines

### Localização dos Pipelines
Os pipelines são definidos em dois lugares principais:

1. **Aplicação Web (`web/app.py`)**:
```python
pipelines = {
    1: """
    carregar "sales.csv";
    ordenar por vendas desc;
    selecionar regiao, produto, vendas;
    mostrar tabela;
    """,
    2: """
    carregar "sales.csv";
    transformar valor_total = vendas * quantidade;
    agrupar por regiao;
    agregar soma de valor_total como total_regiao;
    ordenar por total_regiao desc;
    mostrar tabela;
    """,
    3: """
    carregar "sales.csv";
    filtrar vendas > 1000;
    transformar margem_lucro = vendas * 0.3;
    agrupar por produto;
    agregar media de margem_lucro como media_lucro;
    ordenar por media_lucro desc;
    selecionar produto, media_lucro;
    mostrar tabela;
    """
}
```

2. **Exemplos (`examples/advanced_example.py`)**:
```python
# Exemplo 1: Ordenação e seleção de colunas
pipeline1 = """
carregar "sales.csv";
ordenar por vendas desc;
selecionar regiao, produto, vendas;
mostrar tabela;
"""

# Exemplo 2: Transformação de dados
pipeline2 = """
carregar "sales.csv";
transformar valor_total = vendas * quantidade;
agrupar por regiao;
agregar soma de valor_total como total_regiao;
ordenar por total_regiao desc;
mostrar tabela;
"""

# Exemplo 3: Análise combinada
pipeline3 = """
carregar "sales.csv";
filtrar vendas > 1000;
transformar margem_lucro = vendas * 0.3;
agrupar por produto;
agregar media de margem_lucro como media_lucro;
ordenar por media_lucro desc;
selecionar produto, media_lucro;
mostrar tabela;
"""
```

### Como Criar um Pipeline

1. **Estrutura Básica**:
   - Cada pipeline é uma string contendo comandos
   - Comandos são separados por ponto e vírgula (;)
   - Cada comando segue a sintaxe definida na gramática

2. **Ordem dos Comandos**:
   - Primeiro: carregar os dados
   - Depois: aplicar transformações
   - Por fim: mostrar resultados

3. **Exemplo de Criação**:
```python
# 1. Criar uma string com os comandos
pipeline = """
carregar "dados.csv";
filtrar valor > 1000;
agrupar por categoria;
agregar soma de valor como total;
mostrar tabela;
"""

# 2. Executar o pipeline
df = DataFlow()
resultado = df.executar(pipeline)
```

4. **Boas Práticas**:
   - Sempre comece com o comando `carregar`
   - Use indentação para melhor legibilidade
   - Termine com o comando `mostrar`
   - Documente o propósito do pipeline

5. **Execução na Interface Web**:
   - Pipelines são executados via requisição AJAX
   - Resultados são exibidos em tabelas formatadas
   - Erros são tratados e exibidos na interface

## 5. Estrutura de Diretórios
```
DataFlow/
├── src/           # Código-fonte principal
├── grammar/       # Definição da gramática
├── examples/      # Exemplos de uso
├── tests/         # Testes
└── requirements.txt # Dependências
```

## 6. Características de Implementação
- Suporte a diferentes tipos de dados (strings, números, booleanos)
- Operadores aritméticos e de comparação
- Funções de agregação (soma, média, contagem, etc.)
- Sistema de tipos para validação semântica
- Tratamento de erros

## 7. Estrutura de Arquivos e Suas Funções

### a) Arquivos de Gramática
- `grammar/DataFlow.g4` — Define a gramática da linguagem
- `DataFlow.tokens` & `DataFlowLexer.tokens` — Definições dos tokens (gerados)
- `DataFlow.interp` & `DataFlowLexer.interp` — Arquivos intermediários (gerados)

### b) Arquivos de Implementação
- `src/dataflow.py` — Implementação principal
- `src/__init__.py` — Torna o diretório um pacote Python
- `requirements.txt` — Dependências do projeto

## 8. Fluxo de Execução

### a) Inicialização
```python
from dataflow import DataFlow
df = DataFlow()
pipeline = """
carregar "dados.csv";
filtrar vendas > 1000;
mostrar tabela;
"""
```

### b) Processamento
1. **Análise Léxica (Lexer)** — texto ➜ tokens (DataFlowLexer)
   - Exemplo: carregar → COMANDO_CARREGAR, "dados.csv" → STRING

2. **Análise Sintática (Parser)** — tokens ➜ árvore sintática (DataFlowParser)

3. **Análise Semântica & Execução (Visitor)** — DataFlowVisitorImpl percorre a árvore, executa comandos usando pandas e mantém o estado do DataFrame

## 9. Componentes Principais

### DataFlowErrorListener
- Captura e formata erros de sintaxe

### DataFlowVisitorImpl
- Implementa a lógica dos comandos
- Mantém self.df (DataFrame atual)

### Métodos de Visitação
- `visitComandoCarregar` — Carrega arquivo CSV
- `visitComandoFiltrar` — Aplica filtros
- `visitComandoAgrupar` — Agrupa dados
- `visitComandoAgregar` — Realiza agregações
- `visitComandoOrdenar` — Ordena dados
- `visitComandoSelecionar` — Seleciona colunas
- `visitComandoTransformar` — Cria novas colunas
- `visitComandoMostrar` — Exibe resultados

### DataFlow
- Classe principal que coordena o processo:
  1. Cria o lexer
  2. Cria o parser
  3. Gera a árvore sintática
  4. Executa o visitor

## 10. Exemplo Completo
```python
# 1. Criação do objeto DataFlow
df = DataFlow()

# 2. Definição do pipeline
pipeline = """
carregar "vendas.csv";
filtrar valor > 1000;
agrupar por regiao;
agregar soma de valor como total;
mostrar tabela;
"""

# 3. Execução
resultado = df.executar(pipeline)
```

## 11. Ordem de Processamento
1. Texto ➜ tokens
2. Tokens ➜ árvore sintática
3. Visitor executa cada comando
4. Comandos modificam o DataFrame
5. Resultado final retornado

## 12. Tratamento de Erros
- **Erros de Sintaxe**: capturados pelo DataFlowErrorListener
- **Erros de Execução**: tratados com try/except e mensagens formatadas 