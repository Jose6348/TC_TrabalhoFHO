grammar DataFlow;

programa: comando+ EOF;

comando
    : comandoCarregar
    | comandoFiltrar
    | comandoAgrupar
    | comandoAgregar
    | comandoOrdenar
    | comandoSelecionar
    | comandoTransformar
    | comandoMostrar
    ;

comandoCarregar: 'carregar' STRING PONTO_VIRGULA;
comandoFiltrar: 'filtrar' condicao PONTO_VIRGULA;
comandoAgrupar: 'agrupar' 'por' IDENTIFICADOR PONTO_VIRGULA;
comandoAgregar: 'agregar' funcaoAgregacao 'de' IDENTIFICADOR 'como' IDENTIFICADOR PONTO_VIRGULA;
comandoOrdenar: 'ordenar' 'por' IDENTIFICADOR direcaoOrdenacao? PONTO_VIRGULA;
comandoSelecionar: 'selecionar' listaColunas PONTO_VIRGULA;
comandoTransformar: 'transformar' IDENTIFICADOR '=' expressao PONTO_VIRGULA;
comandoMostrar: 'mostrar' formatoSaida PONTO_VIRGULA;

condicao: IDENTIFICADOR operador valor;
operador: '=' | '!=' | '>' | '<' | '>=' | '<=';
valor: STRING | NUMERO | BOOLEANO;
funcaoAgregacao: 'soma' | 'media' | 'contagem' | 'minimo' | 'maximo';
formatoSaida: 'tabela' | 'grafico';
direcaoOrdenacao: 'asc' | 'desc';
listaColunas: IDENTIFICADOR (',' IDENTIFICADOR)*;
expressao
    : valor
    | IDENTIFICADOR
    | expressao operadorAritmetico expressao
    | '(' expressao ')'
    ;

operadorAritmetico: '+' | '-' | '*' | '/';

IDENTIFICADOR: [a-zA-Z_][a-zA-Z0-9_]*;
STRING: '"' (~["\r\n] | '\\"')* '"';
NUMERO: [0-9]+ ('.' [0-9]+)?;
BOOLEANO: 'verdadeiro' | 'falso';
PONTO_VIRGULA: ';';

ESPACO: [ \t\r\n]+ -> skip;
COMENTARIO: '//' ~[\r\n]* -> skip; 