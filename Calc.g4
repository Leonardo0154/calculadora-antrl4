grammar Calc;

// Parser rules
prog: stat+ ;
stat: expr NEWLINE ;

expr
    : INTEGRAL '(' expr ',' ID (',' expr ',' expr)? ')'      # ExprIntegral
    | DERIVADA '(' expr ',' ID ')'                           # ExprDerivada
    | SIN '(' expr ')'                                       # ExprSin
    | COS '(' expr ')'                                       # ExprCos
    | TAN '(' expr ')'                                       # ExprTan
    | EXP '(' expr ')'                                       # ExprExp
    | LOG '(' expr ')'                                       # ExprLog
    | expr POW expr                                          # ExprPow
    | expr (MUL | DIV) expr                                  # ExprMulDiv
    | expr (ADD | SUB) expr                                  # ExprAddSub
    | FLOAT                                                  # ExprFloat
    | INT                                                    # ExprInt
    | ID                                                     # ExprVar
    | '(' expr ')'                                           # ExprPar
    ;

// Lexer rules
INTEGRAL: 'integral';
DERIVADA: 'derivada';
SIN: 'sin';
COS: 'cos';
TAN: 'tan';
EXP: 'exp';
LOG: 'log';
POW: '**';
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
LPAREN: '(';
RPAREN: ')';
COMMA: ',';

ID: [a-zA-Z]+ ;
INT: [0-9]+ ;
FLOAT: [0-9]+ '.' [0-9]+ ;
NEWLINE: '\r'? '\n' ;
WS: [ \t]+ -> skip ;