# Generated from grammar/DataFlow.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,40,141,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,4,0,40,8,0,
        11,0,12,0,41,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,54,8,1,
        1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,3,6,81,8,6,1,6,1,6,1,7,1,7,1,
        7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,
        1,11,1,11,1,12,1,12,1,13,1,13,1,14,1,14,1,15,1,15,1,16,1,16,1,16,
        5,16,116,8,16,10,16,12,16,119,9,16,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,3,17,128,8,17,1,17,1,17,1,17,1,17,5,17,134,8,17,10,17,12,17,
        137,9,17,1,18,1,18,1,18,0,1,34,19,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,34,36,0,6,2,0,11,11,13,17,1,0,35,37,1,0,18,22,1,0,
        23,24,1,0,25,26,1,0,30,33,134,0,39,1,0,0,0,2,53,1,0,0,0,4,55,1,0,
        0,0,6,59,1,0,0,0,8,63,1,0,0,0,10,68,1,0,0,0,12,76,1,0,0,0,14,84,
        1,0,0,0,16,88,1,0,0,0,18,94,1,0,0,0,20,98,1,0,0,0,22,102,1,0,0,0,
        24,104,1,0,0,0,26,106,1,0,0,0,28,108,1,0,0,0,30,110,1,0,0,0,32,112,
        1,0,0,0,34,127,1,0,0,0,36,138,1,0,0,0,38,40,3,2,1,0,39,38,1,0,0,
        0,40,41,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,43,1,0,0,0,43,44,
        5,0,0,1,44,1,1,0,0,0,45,54,3,4,2,0,46,54,3,6,3,0,47,54,3,8,4,0,48,
        54,3,10,5,0,49,54,3,12,6,0,50,54,3,14,7,0,51,54,3,16,8,0,52,54,3,
        18,9,0,53,45,1,0,0,0,53,46,1,0,0,0,53,47,1,0,0,0,53,48,1,0,0,0,53,
        49,1,0,0,0,53,50,1,0,0,0,53,51,1,0,0,0,53,52,1,0,0,0,54,3,1,0,0,
        0,55,56,5,1,0,0,56,57,5,35,0,0,57,58,5,38,0,0,58,5,1,0,0,0,59,60,
        5,2,0,0,60,61,3,20,10,0,61,62,5,38,0,0,62,7,1,0,0,0,63,64,5,3,0,
        0,64,65,5,4,0,0,65,66,5,34,0,0,66,67,5,38,0,0,67,9,1,0,0,0,68,69,
        5,5,0,0,69,70,3,26,13,0,70,71,5,6,0,0,71,72,5,34,0,0,72,73,5,7,0,
        0,73,74,5,34,0,0,74,75,5,38,0,0,75,11,1,0,0,0,76,77,5,8,0,0,77,78,
        5,4,0,0,78,80,5,34,0,0,79,81,3,30,15,0,80,79,1,0,0,0,80,81,1,0,0,
        0,81,82,1,0,0,0,82,83,5,38,0,0,83,13,1,0,0,0,84,85,5,9,0,0,85,86,
        3,32,16,0,86,87,5,38,0,0,87,15,1,0,0,0,88,89,5,10,0,0,89,90,5,34,
        0,0,90,91,5,11,0,0,91,92,3,34,17,0,92,93,5,38,0,0,93,17,1,0,0,0,
        94,95,5,12,0,0,95,96,3,28,14,0,96,97,5,38,0,0,97,19,1,0,0,0,98,99,
        5,34,0,0,99,100,3,22,11,0,100,101,3,24,12,0,101,21,1,0,0,0,102,103,
        7,0,0,0,103,23,1,0,0,0,104,105,7,1,0,0,105,25,1,0,0,0,106,107,7,
        2,0,0,107,27,1,0,0,0,108,109,7,3,0,0,109,29,1,0,0,0,110,111,7,4,
        0,0,111,31,1,0,0,0,112,117,5,34,0,0,113,114,5,27,0,0,114,116,5,34,
        0,0,115,113,1,0,0,0,116,119,1,0,0,0,117,115,1,0,0,0,117,118,1,0,
        0,0,118,33,1,0,0,0,119,117,1,0,0,0,120,121,6,17,-1,0,121,128,3,24,
        12,0,122,128,5,34,0,0,123,124,5,28,0,0,124,125,3,34,17,0,125,126,
        5,29,0,0,126,128,1,0,0,0,127,120,1,0,0,0,127,122,1,0,0,0,127,123,
        1,0,0,0,128,135,1,0,0,0,129,130,10,2,0,0,130,131,3,36,18,0,131,132,
        3,34,17,3,132,134,1,0,0,0,133,129,1,0,0,0,134,137,1,0,0,0,135,133,
        1,0,0,0,135,136,1,0,0,0,136,35,1,0,0,0,137,135,1,0,0,0,138,139,7,
        5,0,0,139,37,1,0,0,0,6,41,53,80,117,127,135
    ]

class DataFlowParser ( Parser ):

    grammarFileName = "DataFlow.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'carregar'", "'filtrar'", "'agrupar'", 
                     "'por'", "'agregar'", "'de'", "'como'", "'ordenar'", 
                     "'selecionar'", "'transformar'", "'='", "'mostrar'", 
                     "'!='", "'>'", "'<'", "'>='", "'<='", "'soma'", "'media'", 
                     "'contagem'", "'minimo'", "'maximo'", "'tabela'", "'grafico'", 
                     "'asc'", "'desc'", "','", "'('", "')'", "'+'", "'-'", 
                     "'*'", "'/'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "IDENTIFICADOR", "STRING", 
                      "NUMERO", "BOOLEANO", "PONTO_VIRGULA", "ESPACO", "COMENTARIO" ]

    RULE_programa = 0
    RULE_comando = 1
    RULE_comandoCarregar = 2
    RULE_comandoFiltrar = 3
    RULE_comandoAgrupar = 4
    RULE_comandoAgregar = 5
    RULE_comandoOrdenar = 6
    RULE_comandoSelecionar = 7
    RULE_comandoTransformar = 8
    RULE_comandoMostrar = 9
    RULE_condicao = 10
    RULE_operador = 11
    RULE_valor = 12
    RULE_funcaoAgregacao = 13
    RULE_formatoSaida = 14
    RULE_direcaoOrdenacao = 15
    RULE_listaColunas = 16
    RULE_expressao = 17
    RULE_operadorAritmetico = 18

    ruleNames =  [ "programa", "comando", "comandoCarregar", "comandoFiltrar", 
                   "comandoAgrupar", "comandoAgregar", "comandoOrdenar", 
                   "comandoSelecionar", "comandoTransformar", "comandoMostrar", 
                   "condicao", "operador", "valor", "funcaoAgregacao", "formatoSaida", 
                   "direcaoOrdenacao", "listaColunas", "expressao", "operadorAritmetico" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    IDENTIFICADOR=34
    STRING=35
    NUMERO=36
    BOOLEANO=37
    PONTO_VIRGULA=38
    ESPACO=39
    COMENTARIO=40

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(DataFlowParser.EOF, 0)

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DataFlowParser.ComandoContext)
            else:
                return self.getTypedRuleContext(DataFlowParser.ComandoContext,i)


        def getRuleIndex(self):
            return DataFlowParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = DataFlowParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 38
                self.comando()
                self.state = 41 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 5934) != 0)):
                    break

            self.state = 43
            self.match(DataFlowParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comandoCarregar(self):
            return self.getTypedRuleContext(DataFlowParser.ComandoCarregarContext,0)


        def comandoFiltrar(self):
            return self.getTypedRuleContext(DataFlowParser.ComandoFiltrarContext,0)


        def comandoAgrupar(self):
            return self.getTypedRuleContext(DataFlowParser.ComandoAgruparContext,0)


        def comandoAgregar(self):
            return self.getTypedRuleContext(DataFlowParser.ComandoAgregarContext,0)


        def comandoOrdenar(self):
            return self.getTypedRuleContext(DataFlowParser.ComandoOrdenarContext,0)


        def comandoSelecionar(self):
            return self.getTypedRuleContext(DataFlowParser.ComandoSelecionarContext,0)


        def comandoTransformar(self):
            return self.getTypedRuleContext(DataFlowParser.ComandoTransformarContext,0)


        def comandoMostrar(self):
            return self.getTypedRuleContext(DataFlowParser.ComandoMostrarContext,0)


        def getRuleIndex(self):
            return DataFlowParser.RULE_comando

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando" ):
                listener.enterComando(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando" ):
                listener.exitComando(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComando" ):
                return visitor.visitComando(self)
            else:
                return visitor.visitChildren(self)




    def comando(self):

        localctx = DataFlowParser.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_comando)
        try:
            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.comandoCarregar()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.comandoFiltrar()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 47
                self.comandoAgrupar()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 48
                self.comandoAgregar()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 5)
                self.state = 49
                self.comandoOrdenar()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 6)
                self.state = 50
                self.comandoSelecionar()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 7)
                self.state = 51
                self.comandoTransformar()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 8)
                self.state = 52
                self.comandoMostrar()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoCarregarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(DataFlowParser.STRING, 0)

        def PONTO_VIRGULA(self):
            return self.getToken(DataFlowParser.PONTO_VIRGULA, 0)

        def getRuleIndex(self):
            return DataFlowParser.RULE_comandoCarregar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandoCarregar" ):
                listener.enterComandoCarregar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandoCarregar" ):
                listener.exitComandoCarregar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComandoCarregar" ):
                return visitor.visitComandoCarregar(self)
            else:
                return visitor.visitChildren(self)




    def comandoCarregar(self):

        localctx = DataFlowParser.ComandoCarregarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_comandoCarregar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(DataFlowParser.T__0)
            self.state = 56
            self.match(DataFlowParser.STRING)
            self.state = 57
            self.match(DataFlowParser.PONTO_VIRGULA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoFiltrarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condicao(self):
            return self.getTypedRuleContext(DataFlowParser.CondicaoContext,0)


        def PONTO_VIRGULA(self):
            return self.getToken(DataFlowParser.PONTO_VIRGULA, 0)

        def getRuleIndex(self):
            return DataFlowParser.RULE_comandoFiltrar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandoFiltrar" ):
                listener.enterComandoFiltrar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandoFiltrar" ):
                listener.exitComandoFiltrar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComandoFiltrar" ):
                return visitor.visitComandoFiltrar(self)
            else:
                return visitor.visitChildren(self)




    def comandoFiltrar(self):

        localctx = DataFlowParser.ComandoFiltrarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_comandoFiltrar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(DataFlowParser.T__1)
            self.state = 60
            self.condicao()
            self.state = 61
            self.match(DataFlowParser.PONTO_VIRGULA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoAgruparContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICADOR(self):
            return self.getToken(DataFlowParser.IDENTIFICADOR, 0)

        def PONTO_VIRGULA(self):
            return self.getToken(DataFlowParser.PONTO_VIRGULA, 0)

        def getRuleIndex(self):
            return DataFlowParser.RULE_comandoAgrupar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandoAgrupar" ):
                listener.enterComandoAgrupar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandoAgrupar" ):
                listener.exitComandoAgrupar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComandoAgrupar" ):
                return visitor.visitComandoAgrupar(self)
            else:
                return visitor.visitChildren(self)




    def comandoAgrupar(self):

        localctx = DataFlowParser.ComandoAgruparContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_comandoAgrupar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(DataFlowParser.T__2)
            self.state = 64
            self.match(DataFlowParser.T__3)
            self.state = 65
            self.match(DataFlowParser.IDENTIFICADOR)
            self.state = 66
            self.match(DataFlowParser.PONTO_VIRGULA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoAgregarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcaoAgregacao(self):
            return self.getTypedRuleContext(DataFlowParser.FuncaoAgregacaoContext,0)


        def IDENTIFICADOR(self, i:int=None):
            if i is None:
                return self.getTokens(DataFlowParser.IDENTIFICADOR)
            else:
                return self.getToken(DataFlowParser.IDENTIFICADOR, i)

        def PONTO_VIRGULA(self):
            return self.getToken(DataFlowParser.PONTO_VIRGULA, 0)

        def getRuleIndex(self):
            return DataFlowParser.RULE_comandoAgregar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandoAgregar" ):
                listener.enterComandoAgregar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandoAgregar" ):
                listener.exitComandoAgregar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComandoAgregar" ):
                return visitor.visitComandoAgregar(self)
            else:
                return visitor.visitChildren(self)




    def comandoAgregar(self):

        localctx = DataFlowParser.ComandoAgregarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_comandoAgregar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(DataFlowParser.T__4)
            self.state = 69
            self.funcaoAgregacao()
            self.state = 70
            self.match(DataFlowParser.T__5)
            self.state = 71
            self.match(DataFlowParser.IDENTIFICADOR)
            self.state = 72
            self.match(DataFlowParser.T__6)
            self.state = 73
            self.match(DataFlowParser.IDENTIFICADOR)
            self.state = 74
            self.match(DataFlowParser.PONTO_VIRGULA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoOrdenarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICADOR(self):
            return self.getToken(DataFlowParser.IDENTIFICADOR, 0)

        def PONTO_VIRGULA(self):
            return self.getToken(DataFlowParser.PONTO_VIRGULA, 0)

        def direcaoOrdenacao(self):
            return self.getTypedRuleContext(DataFlowParser.DirecaoOrdenacaoContext,0)


        def getRuleIndex(self):
            return DataFlowParser.RULE_comandoOrdenar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandoOrdenar" ):
                listener.enterComandoOrdenar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandoOrdenar" ):
                listener.exitComandoOrdenar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComandoOrdenar" ):
                return visitor.visitComandoOrdenar(self)
            else:
                return visitor.visitChildren(self)




    def comandoOrdenar(self):

        localctx = DataFlowParser.ComandoOrdenarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_comandoOrdenar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(DataFlowParser.T__7)
            self.state = 77
            self.match(DataFlowParser.T__3)
            self.state = 78
            self.match(DataFlowParser.IDENTIFICADOR)
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25 or _la==26:
                self.state = 79
                self.direcaoOrdenacao()


            self.state = 82
            self.match(DataFlowParser.PONTO_VIRGULA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoSelecionarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listaColunas(self):
            return self.getTypedRuleContext(DataFlowParser.ListaColunasContext,0)


        def PONTO_VIRGULA(self):
            return self.getToken(DataFlowParser.PONTO_VIRGULA, 0)

        def getRuleIndex(self):
            return DataFlowParser.RULE_comandoSelecionar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandoSelecionar" ):
                listener.enterComandoSelecionar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandoSelecionar" ):
                listener.exitComandoSelecionar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComandoSelecionar" ):
                return visitor.visitComandoSelecionar(self)
            else:
                return visitor.visitChildren(self)




    def comandoSelecionar(self):

        localctx = DataFlowParser.ComandoSelecionarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_comandoSelecionar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(DataFlowParser.T__8)
            self.state = 85
            self.listaColunas()
            self.state = 86
            self.match(DataFlowParser.PONTO_VIRGULA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoTransformarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICADOR(self):
            return self.getToken(DataFlowParser.IDENTIFICADOR, 0)

        def expressao(self):
            return self.getTypedRuleContext(DataFlowParser.ExpressaoContext,0)


        def PONTO_VIRGULA(self):
            return self.getToken(DataFlowParser.PONTO_VIRGULA, 0)

        def getRuleIndex(self):
            return DataFlowParser.RULE_comandoTransformar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandoTransformar" ):
                listener.enterComandoTransformar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandoTransformar" ):
                listener.exitComandoTransformar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComandoTransformar" ):
                return visitor.visitComandoTransformar(self)
            else:
                return visitor.visitChildren(self)




    def comandoTransformar(self):

        localctx = DataFlowParser.ComandoTransformarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_comandoTransformar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(DataFlowParser.T__9)
            self.state = 89
            self.match(DataFlowParser.IDENTIFICADOR)
            self.state = 90
            self.match(DataFlowParser.T__10)
            self.state = 91
            self.expressao(0)
            self.state = 92
            self.match(DataFlowParser.PONTO_VIRGULA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoMostrarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def formatoSaida(self):
            return self.getTypedRuleContext(DataFlowParser.FormatoSaidaContext,0)


        def PONTO_VIRGULA(self):
            return self.getToken(DataFlowParser.PONTO_VIRGULA, 0)

        def getRuleIndex(self):
            return DataFlowParser.RULE_comandoMostrar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandoMostrar" ):
                listener.enterComandoMostrar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandoMostrar" ):
                listener.exitComandoMostrar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComandoMostrar" ):
                return visitor.visitComandoMostrar(self)
            else:
                return visitor.visitChildren(self)




    def comandoMostrar(self):

        localctx = DataFlowParser.ComandoMostrarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_comandoMostrar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(DataFlowParser.T__11)
            self.state = 95
            self.formatoSaida()
            self.state = 96
            self.match(DataFlowParser.PONTO_VIRGULA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICADOR(self):
            return self.getToken(DataFlowParser.IDENTIFICADOR, 0)

        def operador(self):
            return self.getTypedRuleContext(DataFlowParser.OperadorContext,0)


        def valor(self):
            return self.getTypedRuleContext(DataFlowParser.ValorContext,0)


        def getRuleIndex(self):
            return DataFlowParser.RULE_condicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicao" ):
                listener.enterCondicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicao" ):
                listener.exitCondicao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicao" ):
                return visitor.visitCondicao(self)
            else:
                return visitor.visitChildren(self)




    def condicao(self):

        localctx = DataFlowParser.CondicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_condicao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(DataFlowParser.IDENTIFICADOR)
            self.state = 99
            self.operador()
            self.state = 100
            self.valor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperadorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DataFlowParser.RULE_operador

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperador" ):
                listener.enterOperador(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperador" ):
                listener.exitOperador(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperador" ):
                return visitor.visitOperador(self)
            else:
                return visitor.visitChildren(self)




    def operador(self):

        localctx = DataFlowParser.OperadorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_operador)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 256000) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(DataFlowParser.STRING, 0)

        def NUMERO(self):
            return self.getToken(DataFlowParser.NUMERO, 0)

        def BOOLEANO(self):
            return self.getToken(DataFlowParser.BOOLEANO, 0)

        def getRuleIndex(self):
            return DataFlowParser.RULE_valor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValor" ):
                listener.enterValor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValor" ):
                listener.exitValor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValor" ):
                return visitor.visitValor(self)
            else:
                return visitor.visitChildren(self)




    def valor(self):

        localctx = DataFlowParser.ValorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_valor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 240518168576) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncaoAgregacaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DataFlowParser.RULE_funcaoAgregacao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncaoAgregacao" ):
                listener.enterFuncaoAgregacao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncaoAgregacao" ):
                listener.exitFuncaoAgregacao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncaoAgregacao" ):
                return visitor.visitFuncaoAgregacao(self)
            else:
                return visitor.visitChildren(self)




    def funcaoAgregacao(self):

        localctx = DataFlowParser.FuncaoAgregacaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_funcaoAgregacao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8126464) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormatoSaidaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DataFlowParser.RULE_formatoSaida

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormatoSaida" ):
                listener.enterFormatoSaida(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormatoSaida" ):
                listener.exitFormatoSaida(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormatoSaida" ):
                return visitor.visitFormatoSaida(self)
            else:
                return visitor.visitChildren(self)




    def formatoSaida(self):

        localctx = DataFlowParser.FormatoSaidaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_formatoSaida)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            _la = self._input.LA(1)
            if not(_la==23 or _la==24):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DirecaoOrdenacaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DataFlowParser.RULE_direcaoOrdenacao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDirecaoOrdenacao" ):
                listener.enterDirecaoOrdenacao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDirecaoOrdenacao" ):
                listener.exitDirecaoOrdenacao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDirecaoOrdenacao" ):
                return visitor.visitDirecaoOrdenacao(self)
            else:
                return visitor.visitChildren(self)




    def direcaoOrdenacao(self):

        localctx = DataFlowParser.DirecaoOrdenacaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_direcaoOrdenacao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            _la = self._input.LA(1)
            if not(_la==25 or _la==26):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaColunasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICADOR(self, i:int=None):
            if i is None:
                return self.getTokens(DataFlowParser.IDENTIFICADOR)
            else:
                return self.getToken(DataFlowParser.IDENTIFICADOR, i)

        def getRuleIndex(self):
            return DataFlowParser.RULE_listaColunas

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaColunas" ):
                listener.enterListaColunas(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaColunas" ):
                listener.exitListaColunas(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaColunas" ):
                return visitor.visitListaColunas(self)
            else:
                return visitor.visitChildren(self)




    def listaColunas(self):

        localctx = DataFlowParser.ListaColunasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_listaColunas)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(DataFlowParser.IDENTIFICADOR)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 113
                self.match(DataFlowParser.T__26)
                self.state = 114
                self.match(DataFlowParser.IDENTIFICADOR)
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def valor(self):
            return self.getTypedRuleContext(DataFlowParser.ValorContext,0)


        def IDENTIFICADOR(self):
            return self.getToken(DataFlowParser.IDENTIFICADOR, 0)

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DataFlowParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(DataFlowParser.ExpressaoContext,i)


        def operadorAritmetico(self):
            return self.getTypedRuleContext(DataFlowParser.OperadorAritmeticoContext,0)


        def getRuleIndex(self):
            return DataFlowParser.RULE_expressao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressao" ):
                listener.enterExpressao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressao" ):
                listener.exitExpressao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressao" ):
                return visitor.visitExpressao(self)
            else:
                return visitor.visitChildren(self)



    def expressao(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = DataFlowParser.ExpressaoContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expressao, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [35, 36, 37]:
                self.state = 121
                self.valor()
                pass
            elif token in [34]:
                self.state = 122
                self.match(DataFlowParser.IDENTIFICADOR)
                pass
            elif token in [28]:
                self.state = 123
                self.match(DataFlowParser.T__27)
                self.state = 124
                self.expressao(0)
                self.state = 125
                self.match(DataFlowParser.T__28)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 135
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = DataFlowParser.ExpressaoContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expressao)
                    self.state = 129
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 130
                    self.operadorAritmetico()
                    self.state = 131
                    self.expressao(3) 
                self.state = 137
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OperadorAritmeticoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DataFlowParser.RULE_operadorAritmetico

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperadorAritmetico" ):
                listener.enterOperadorAritmetico(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperadorAritmetico" ):
                listener.exitOperadorAritmetico(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperadorAritmetico" ):
                return visitor.visitOperadorAritmetico(self)
            else:
                return visitor.visitChildren(self)




    def operadorAritmetico(self):

        localctx = DataFlowParser.OperadorAritmeticoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_operadorAritmetico)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16106127360) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[17] = self.expressao_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expressao_sempred(self, localctx:ExpressaoContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




