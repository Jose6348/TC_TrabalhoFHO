# Generated from grammar/DataFlow.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .DataFlowParser import DataFlowParser
else:
    from DataFlowParser import DataFlowParser

# This class defines a complete listener for a parse tree produced by DataFlowParser.
class DataFlowListener(ParseTreeListener):

    # Enter a parse tree produced by DataFlowParser#programa.
    def enterPrograma(self, ctx:DataFlowParser.ProgramaContext):
        pass

    # Exit a parse tree produced by DataFlowParser#programa.
    def exitPrograma(self, ctx:DataFlowParser.ProgramaContext):
        pass


    # Enter a parse tree produced by DataFlowParser#comando.
    def enterComando(self, ctx:DataFlowParser.ComandoContext):
        pass

    # Exit a parse tree produced by DataFlowParser#comando.
    def exitComando(self, ctx:DataFlowParser.ComandoContext):
        pass


    # Enter a parse tree produced by DataFlowParser#comandoCarregar.
    def enterComandoCarregar(self, ctx:DataFlowParser.ComandoCarregarContext):
        pass

    # Exit a parse tree produced by DataFlowParser#comandoCarregar.
    def exitComandoCarregar(self, ctx:DataFlowParser.ComandoCarregarContext):
        pass


    # Enter a parse tree produced by DataFlowParser#comandoFiltrar.
    def enterComandoFiltrar(self, ctx:DataFlowParser.ComandoFiltrarContext):
        pass

    # Exit a parse tree produced by DataFlowParser#comandoFiltrar.
    def exitComandoFiltrar(self, ctx:DataFlowParser.ComandoFiltrarContext):
        pass


    # Enter a parse tree produced by DataFlowParser#comandoAgrupar.
    def enterComandoAgrupar(self, ctx:DataFlowParser.ComandoAgruparContext):
        pass

    # Exit a parse tree produced by DataFlowParser#comandoAgrupar.
    def exitComandoAgrupar(self, ctx:DataFlowParser.ComandoAgruparContext):
        pass


    # Enter a parse tree produced by DataFlowParser#comandoAgregar.
    def enterComandoAgregar(self, ctx:DataFlowParser.ComandoAgregarContext):
        pass

    # Exit a parse tree produced by DataFlowParser#comandoAgregar.
    def exitComandoAgregar(self, ctx:DataFlowParser.ComandoAgregarContext):
        pass


    # Enter a parse tree produced by DataFlowParser#comandoOrdenar.
    def enterComandoOrdenar(self, ctx:DataFlowParser.ComandoOrdenarContext):
        pass

    # Exit a parse tree produced by DataFlowParser#comandoOrdenar.
    def exitComandoOrdenar(self, ctx:DataFlowParser.ComandoOrdenarContext):
        pass


    # Enter a parse tree produced by DataFlowParser#comandoSelecionar.
    def enterComandoSelecionar(self, ctx:DataFlowParser.ComandoSelecionarContext):
        pass

    # Exit a parse tree produced by DataFlowParser#comandoSelecionar.
    def exitComandoSelecionar(self, ctx:DataFlowParser.ComandoSelecionarContext):
        pass


    # Enter a parse tree produced by DataFlowParser#comandoTransformar.
    def enterComandoTransformar(self, ctx:DataFlowParser.ComandoTransformarContext):
        pass

    # Exit a parse tree produced by DataFlowParser#comandoTransformar.
    def exitComandoTransformar(self, ctx:DataFlowParser.ComandoTransformarContext):
        pass


    # Enter a parse tree produced by DataFlowParser#comandoMostrar.
    def enterComandoMostrar(self, ctx:DataFlowParser.ComandoMostrarContext):
        pass

    # Exit a parse tree produced by DataFlowParser#comandoMostrar.
    def exitComandoMostrar(self, ctx:DataFlowParser.ComandoMostrarContext):
        pass


    # Enter a parse tree produced by DataFlowParser#condicao.
    def enterCondicao(self, ctx:DataFlowParser.CondicaoContext):
        pass

    # Exit a parse tree produced by DataFlowParser#condicao.
    def exitCondicao(self, ctx:DataFlowParser.CondicaoContext):
        pass


    # Enter a parse tree produced by DataFlowParser#operador.
    def enterOperador(self, ctx:DataFlowParser.OperadorContext):
        pass

    # Exit a parse tree produced by DataFlowParser#operador.
    def exitOperador(self, ctx:DataFlowParser.OperadorContext):
        pass


    # Enter a parse tree produced by DataFlowParser#valor.
    def enterValor(self, ctx:DataFlowParser.ValorContext):
        pass

    # Exit a parse tree produced by DataFlowParser#valor.
    def exitValor(self, ctx:DataFlowParser.ValorContext):
        pass


    # Enter a parse tree produced by DataFlowParser#funcaoAgregacao.
    def enterFuncaoAgregacao(self, ctx:DataFlowParser.FuncaoAgregacaoContext):
        pass

    # Exit a parse tree produced by DataFlowParser#funcaoAgregacao.
    def exitFuncaoAgregacao(self, ctx:DataFlowParser.FuncaoAgregacaoContext):
        pass


    # Enter a parse tree produced by DataFlowParser#formatoSaida.
    def enterFormatoSaida(self, ctx:DataFlowParser.FormatoSaidaContext):
        pass

    # Exit a parse tree produced by DataFlowParser#formatoSaida.
    def exitFormatoSaida(self, ctx:DataFlowParser.FormatoSaidaContext):
        pass


    # Enter a parse tree produced by DataFlowParser#direcaoOrdenacao.
    def enterDirecaoOrdenacao(self, ctx:DataFlowParser.DirecaoOrdenacaoContext):
        pass

    # Exit a parse tree produced by DataFlowParser#direcaoOrdenacao.
    def exitDirecaoOrdenacao(self, ctx:DataFlowParser.DirecaoOrdenacaoContext):
        pass


    # Enter a parse tree produced by DataFlowParser#listaColunas.
    def enterListaColunas(self, ctx:DataFlowParser.ListaColunasContext):
        pass

    # Exit a parse tree produced by DataFlowParser#listaColunas.
    def exitListaColunas(self, ctx:DataFlowParser.ListaColunasContext):
        pass


    # Enter a parse tree produced by DataFlowParser#expressao.
    def enterExpressao(self, ctx:DataFlowParser.ExpressaoContext):
        pass

    # Exit a parse tree produced by DataFlowParser#expressao.
    def exitExpressao(self, ctx:DataFlowParser.ExpressaoContext):
        pass


    # Enter a parse tree produced by DataFlowParser#operadorAritmetico.
    def enterOperadorAritmetico(self, ctx:DataFlowParser.OperadorAritmeticoContext):
        pass

    # Exit a parse tree produced by DataFlowParser#operadorAritmetico.
    def exitOperadorAritmetico(self, ctx:DataFlowParser.OperadorAritmeticoContext):
        pass



del DataFlowParser