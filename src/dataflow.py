import pandas as pd
import os
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from src.grammar.DataFlowLexer import DataFlowLexer
from src.grammar.DataFlowParser import DataFlowParser
from src.grammar.DataFlowVisitor import DataFlowVisitor

class DataFlowErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"Erro de sintaxe na linha {line}, coluna {column}: {msg}")

class DataFlowVisitorImpl(DataFlowVisitor):
    def __init__(self):
        self.df = None
        self.grupo_atual = None

    def visitPrograma(self, ctx):
        resultado = None
        for comando in ctx.comando():
            resultado = self.visit(comando)
        return resultado

    def visitComando(self, ctx):
        if ctx.comandoCarregar():
            return self.visit(ctx.comandoCarregar())
        elif ctx.comandoFiltrar():
            return self.visit(ctx.comandoFiltrar())
        elif ctx.comandoAgrupar():
            return self.visit(ctx.comandoAgrupar())
        elif ctx.comandoAgregar():
            return self.visit(ctx.comandoAgregar())
        elif ctx.comandoOrdenar():
            return self.visit(ctx.comandoOrdenar())
        elif ctx.comandoSelecionar():
            return self.visit(ctx.comandoSelecionar())
        elif ctx.comandoTransformar():
            return self.visit(ctx.comandoTransformar())
        elif ctx.comandoMostrar():
            return self.visit(ctx.comandoMostrar())

    def visitComandoCarregar(self, ctx):
        caminho_arquivo = ctx.STRING().getText().strip('"')
        print(f"Tentando carregar arquivo: {caminho_arquivo}")
        print(f"Diretório atual: {os.getcwd()}")
        print(f"O arquivo existe? {os.path.exists(caminho_arquivo)}")
        try:
            self.df = pd.read_csv(caminho_arquivo)
            print("Arquivo carregado com sucesso!")
            print(self.df.head())
        except Exception as e:
            print(f"Erro ao carregar arquivo: {str(e)}")
            raise
        return self.df

    def visitComandoFiltrar(self, ctx):
        if self.df is None:
            raise ValueError("Nenhum DataFrame carregado. Use o comando 'carregar' primeiro.")
        
        condicao = self.visit(ctx.condicao())
        print(f"Aplicando filtro: {condicao}")
        try:
            df_filtrado = self.df.query(condicao)
            print("Filtro aplicado com sucesso!")
            print(df_filtrado.head())
            self.df = df_filtrado
        except Exception as e:
            print(f"Erro ao aplicar filtro: {str(e)}")
            raise
        return self.df

    def visitComandoAgrupar(self, ctx):
        if self.df is None:
            raise ValueError("Nenhum DataFrame carregado. Use o comando 'carregar' primeiro.")
        
        agrupar_por = ctx.IDENTIFICADOR().getText()
        print(f"Agrupando por: {agrupar_por}")
        self.grupo_atual = agrupar_por
        return self.df

    def visitComandoAgregar(self, ctx):
        if self.df is None:
            raise ValueError("Nenhum DataFrame carregado. Use o comando 'carregar' primeiro.")
        
        funcao_agregacao = self.visit(ctx.funcaoAgregacao())
        coluna = ctx.IDENTIFICADOR(0).getText()
        alias = ctx.IDENTIFICADOR(1).getText()
        print(f"Agregando: {funcao_agregacao}({coluna}) como {alias}")
        
        try:
            if self.grupo_atual:
                dicionario_agregacao = {coluna: funcao_agregacao}
                df_agrupado = self.df.groupby(self.grupo_atual).agg(dicionario_agregacao).reset_index()
                self.df = df_agrupado.rename(columns={coluna: alias})
            else:
                valor = getattr(self.df[coluna], funcao_agregacao)()
                self.df = pd.DataFrame({alias: [valor]})
            
            print("Agregação aplicada com sucesso!")
            print(self.df.head())
        except Exception as e:
            print(f"Erro ao aplicar agregação: {str(e)}")
            raise
        
        return self.df

    def visitComandoMostrar(self, ctx):
        if self.df is None:
            raise ValueError("Nenhum DataFrame carregado. Use o comando 'carregar' primeiro.")
        
        tipo_formato = self.visit(ctx.formatoSaida())
        print(f"\nMostrando resultado como: {tipo_formato}")
        if tipo_formato == 'tabela':
            print("\nResultado:")
            print("-" * 80)
            print(self.df)
            print("-" * 80)
        elif tipo_formato == 'grafico':
            print("Visualização em gráfico ainda não implementada")
        return self.df

    def visitCondicao(self, ctx):
        coluna = ctx.IDENTIFICADOR().getText()
        operador = self.visit(ctx.operador())
        valor = self.visit(ctx.valor())
        
        if isinstance(valor, str):
            valor = f"'{valor}'"
        
        return f"{coluna} {operador} {valor}"

    def visitOperador(self, ctx):
        op = ctx.getText()
        if op == '=':
            return '=='
        return op

    def visitValor(self, ctx):
        if ctx.STRING():
            return ctx.STRING().getText().strip('"')
        elif ctx.NUMERO():
            return float(ctx.NUMERO().getText())
        elif ctx.BOOLEANO():
            return ctx.BOOLEANO().getText().lower() == 'verdadeiro'

    def visitFuncaoAgregacao(self, ctx):
        funcao = ctx.getText()
        mapeamento = {
            'soma': 'sum',
            'media': 'mean',
            'contagem': 'count',
            'minimo': 'min',
            'maximo': 'max'
        }
        return mapeamento.get(funcao, funcao)

    def visitFormatoSaida(self, ctx):
        return ctx.getText()

    def visitComandoOrdenar(self, ctx):
        if self.df is None:
            raise ValueError("Nenhum DataFrame carregado. Use o comando 'carregar' primeiro.")
        
        coluna = ctx.IDENTIFICADOR().getText()
        direcao = 'ascending' if not ctx.direcaoOrdenacao() else 'ascending' if ctx.direcaoOrdenacao().getText() == 'asc' else 'descending'
        
        print(f"Ordenando por {coluna} em ordem {direcao}")
        try:
            self.df = self.df.sort_values(by=coluna, ascending=(direcao == 'ascending'))
            print("Ordenação aplicada com sucesso!")
            print(self.df.head())
        except Exception as e:
            print(f"Erro ao ordenar: {str(e)}")
            raise
        return self.df

    def visitComandoSelecionar(self, ctx):
        if self.df is None:
            raise ValueError("Nenhum DataFrame carregado. Use o comando 'carregar' primeiro.")
        
        colunas = [col.getText() for col in ctx.listaColunas().IDENTIFICADOR()]
        print(f"Selecionando colunas: {', '.join(colunas)}")
        
        try:
            self.df = self.df[colunas]
            print("Seleção de colunas aplicada com sucesso!")
            print(self.df.head())
        except Exception as e:
            print(f"Erro ao selecionar colunas: {str(e)}")
            raise
        return self.df

    def visitComandoTransformar(self, ctx):
        if self.df is None:
            raise ValueError("Nenhum DataFrame carregado. Use o comando 'carregar' primeiro.")
        
        nova_coluna = ctx.IDENTIFICADOR().getText()
        expressao = self.visit(ctx.expressao())
        
        print(f"Transformando coluna {nova_coluna} com expressão: {expressao}")
        try:
            if isinstance(expressao, str):
                self.df[nova_coluna] = self.df.eval(expressao)
            else:
                self.df[nova_coluna] = expressao
            print("Transformação aplicada com sucesso!")
            print(self.df.head())
        except Exception as e:
            print(f"Erro ao transformar coluna: {str(e)}")
            raise
        return self.df

    def visitExpressao(self, ctx):
        if ctx.valor():
            return self.visit(ctx.valor())
        elif ctx.IDENTIFICADOR():
            return ctx.IDENTIFICADOR().getText()
        else:
            esquerda = self.visit(ctx.expressao(0))
            operador = ctx.operadorAritmetico().getText()
            direita = self.visit(ctx.expressao(1))
            return f"{esquerda} {operador} {direita}"

class DataFlow:
    def __init__(self):
        self.visitor = DataFlowVisitorImpl()

    def executar(self, pipeline):
        try:
            input_stream = InputStream(pipeline)
            lexer = DataFlowLexer(input_stream)
            lexer.removeErrorListeners()
            lexer.addErrorListener(DataFlowErrorListener())
            
            token_stream = CommonTokenStream(lexer)
            parser = DataFlowParser(token_stream)
            parser.removeErrorListeners()
            parser.addErrorListener(DataFlowErrorListener())
            
            tree = parser.programa()
            return self.visitor.visit(tree)
        except Exception as e:
            print(f"Erro ao executar pipeline: {str(e)}")
            raise 