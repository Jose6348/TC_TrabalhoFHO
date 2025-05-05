from antlr4 import *
if "." in __name__:
    from .DataFlowParser import DataFlowParser
else:
    from DataFlowParser import DataFlowParser

class DataFlowVisitor(ParseTreeVisitor):
    def visitPrograma(self, ctx:DataFlowParser.ProgramaContext):
        return self.visitChildren(ctx)

    def visitComando(self, ctx:DataFlowParser.ComandoContext):
        return self.visitChildren(ctx)

    def visitComandoCarregar(self, ctx:DataFlowParser.ComandoCarregarContext):
        return self.visitChildren(ctx)

    def visitComandoFiltrar(self, ctx:DataFlowParser.ComandoFiltrarContext):
        return self.visitChildren(ctx)

    def visitComandoAgrupar(self, ctx:DataFlowParser.ComandoAgruparContext):
        return self.visitChildren(ctx)

    def visitComandoAgregar(self, ctx:DataFlowParser.ComandoAgregarContext):
        return self.visitChildren(ctx)

    def visitComandoOrdenar(self, ctx:DataFlowParser.ComandoOrdenarContext):
        return self.visitChildren(ctx)

    def visitComandoSelecionar(self, ctx:DataFlowParser.ComandoSelecionarContext):
        return self.visitChildren(ctx)

    def visitComandoTransformar(self, ctx:DataFlowParser.ComandoTransformarContext):
        return self.visitChildren(ctx)

    def visitComandoMostrar(self, ctx:DataFlowParser.ComandoMostrarContext):
        return self.visitChildren(ctx)

    def visitCondicao(self, ctx:DataFlowParser.CondicaoContext):
        return self.visitChildren(ctx)

    def visitOperador(self, ctx:DataFlowParser.OperadorContext):
        return self.visitChildren(ctx)

    def visitValor(self, ctx:DataFlowParser.ValorContext):
        return self.visitChildren(ctx)

    def visitFuncaoAgregacao(self, ctx:DataFlowParser.FuncaoAgregacaoContext):
        return self.visitChildren(ctx)

    def visitFormatoSaida(self, ctx:DataFlowParser.FormatoSaidaContext):
        return self.visitChildren(ctx)

    def visitDirecaoOrdenacao(self, ctx:DataFlowParser.DirecaoOrdenacaoContext):
        return self.visitChildren(ctx)

    def visitListaColunas(self, ctx:DataFlowParser.ListaColunasContext):
        return self.visitChildren(ctx)

    def visitExpressao(self, ctx:DataFlowParser.ExpressaoContext):
        return self.visitChildren(ctx)

    def visitOperadorAritmetico(self, ctx:DataFlowParser.OperadorAritmeticoContext):
        return self.visitChildren(ctx) 