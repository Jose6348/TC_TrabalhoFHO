from src.dataflow import DataFlow

# Criar uma instância do DataFlow
df = DataFlow()

# Exemplo 1: Ordenação e seleção de colunas
pipeline1 = """
carregar "examples/sales.csv";
ordenar por vendas desc;
selecionar regiao, produto, vendas;
mostrar tabela;
"""

print("Exemplo 1: Vendas ordenadas por valor (maior para menor)")
df.executar(pipeline1)

# Exemplo 2: Transformação de dados
pipeline2 = """
carregar "examples/sales.csv";
transformar valor_total = vendas * quantidade;
agrupar por regiao;
agregar soma de valor_total como total_regiao;
ordenar por total_regiao desc;
mostrar tabela;
"""

print("\nExemplo 2: Valor total por região (preço * quantidade)")
df.executar(pipeline2)

# Exemplo 3: Análise combinada
pipeline3 = """
carregar "examples/sales.csv";
filtrar vendas > 1000;
transformar margem_lucro = vendas * 0.3;
agrupar por produto;
agregar media de margem_lucro como media_lucro;
ordenar por media_lucro desc;
selecionar produto, media_lucro;
mostrar tabela;
"""

print("\nExemplo 3: Margem de lucro média por produto (para vendas acima de 1000)")
df.executar(pipeline3) 