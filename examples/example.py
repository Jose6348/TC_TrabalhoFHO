from src.dataflow import DataFlow

# Criar uma instância do DataFlow
df = DataFlow()

# Exemplo 1: Análise básica de vendas
pipeline1 = """
carregar "examples/sales.csv";
filtrar regiao = "Norte";
mostrar tabela;
"""

print("Exemplo 1: Vendas na região Norte")
df.executar(pipeline1)

# Exemplo 2: Análise de vendas por produto
pipeline2 = """
carregar "examples/sales.csv";
agrupar por produto;
agregar soma de vendas como total_vendas;
mostrar tabela;
"""

print("\nExemplo 2: Total de vendas por produto")
df.executar(pipeline2)

# Exemplo 3: Análise de vendas com filtro e agregação
pipeline3 = """
carregar "examples/sales.csv";
filtrar vendas > 1000;
agrupar por regiao;
agregar media de quantidade como media_quantidade;
mostrar tabela;
"""

print("\nExemplo 3: Quantidade média por região para vendas acima de 1000")
df.executar(pipeline3) 