// Student ID: 2213506
grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}

// Lexer rules
NL: '\n'; // NOT skip newlines

WS : [ \t\r\f]+ -> skip ; // skip spaces, tabs

LINE_COMMENT: '//' ~[\r\n]* -> skip;

MULTI_LINE_COMMENT: '/*' ( MULTI_LINE_COMMENT | .)*? '*/' -> skip;

// Keywords
IF: 'if';
ELSE: 'else';
FOR: 'for';
RETURN: 'return';
FUNC: 'func';
TYPE: 'type';
STRUCT: 'struct';
INTERFACE: 'interface';
STRING: 'string';
INT: 'int';
FLOAT: 'float';
BOOLEAN: 'boolean';
CONST: 'const';
VAR: 'var';
CONTINUE: 'continue';
BREAK: 'break';
RANGE: 'range';
NIL: 'nil';
TRUE: 'true';
FALSE: 'false';


// Operators
PLUS: '+';
MINUS: '-';
STAR: '*';
SLASH: '/';
MOD: '%';
EQUALS: '==';
NOT_EQUALS: '!=';
LESS_THAN: '<';
LESS_THAN_OR_EQUAL: '<=';
GREATER_THAN: '>';
GREATER_THAN_OR_EQUAL: '>=';
AND: '&&';
OR: '||';
NOT: '!';
ASSIGN: '=';
COLON_ASSIGN: ':=';
PLUS_ASSIGN: '+=';
MINUS_ASSIGN: '-=';
STAR_ASSIGN: '*=';
SLASH_ASSIGN: '/=';
MOD_ASSIGN: '%=';
DOT: '.';
COLON: ':';

// Separators
L_PAREN: '(';
R_PAREN: ')';
L_BRACE: '{';
R_BRACE: '}';
L_BRACKET: '[';
R_BRACKET: ']';
COMMA: ',';
SEMICOLON: ';';

// Identifiers (go after keywords)
IDENTIFIER: [A-Za-z_][A-Za-z0-9_]*;

// INT Literals
DECIMAL_INT: [1-9]DIGIT* | '0'; 
fragment DIGIT: [0-9];
BINARY_INT: '0'[Bb][01]+ { self.text = str(int(self.text, 2)) };
OCTAL_INT: '0'[Oo][0-7]+ { self.text = str(int(self.text, 8)) };
HEX_INT: '0'[Xx][0-9A-Fa-f]+ { self.text = str(int(self.text, 16)) };

FLOAT_LIT: DECIMAL_INT '.' DIGIT* EXPONENT?;
        // | DECIMAL_INT EXPONENT ; //???
fragment EXPONENT: [eE][+-]?DECIMAL_INT;

STRING_LIT: '"' STRING_CHAR* '"' {self.text = self.text[1:-1];}; //???
fragment STRING_CHAR: (~[\n"\\] | '\\' [ntr"\\]);

ERROR_CHAR: . ;
ILLEGAL_ESCAPE: '"' STRING_CHAR* '\\' ~[ntr"\\] { self.text = self.text[1:]; } ;
UNCLOSE_STRING: '"' STRING_CHAR* ('\r'? '\n' | EOF) {
    if (self.text[-1] == '\n' and self.text[-2] == '\r'):
        self.text = self.text[1:-2];
    elif (self.text[-1] == '\n'):
        self.text = self.text[1:-1];
    else:
        self.text = self.text[1:]
}; 

// Parser rules
program  : declList EOF ;

declList: decl | declList decl ;

decl: funcdecl | vardecl  ;

vardecl: 'var' IDENTIFIER 'int' ';' ;

funcdecl: 'func' IDENTIFIER '(' ')' '{' '}' ';' ;

type_: IDENTIFIER | arrayType ;

literal: basicLit | compositeLit ;

basicLit: integerLit | FLOAT_LIT | STRING_LIT | TRUE | FALSE | NIL ;

integerLit: DECIMAL_INT | BINARY_INT | OCTAL_INT | HEX_INT ;

compositeLit: arrayLit | structLit ;

arrayLit: arrayType arrayValue ;

arrayType: L_BRACKET integerLit R_BRACKET elementType ; //???: or constant

elementType: type_ ;

arrayValue
    : L_BRACE elementList COMMA R_BRACE 
    | L_BRACE elementList R_BRACE
    | L_BRACE R_BRACE ;

structLit: structType structValue ;

structType: IDENTIFIER ;

structValue
    : L_BRACE keyedElementList COMMA R_BRACE 
    | L_BRACE keyedElementList R_BRACE
    | L_BRACE R_BRACE ; 

elementList: element COMMA elementList | element ;

keyedElementList: keyedElement COMMA keyedElementList | keyedElement ;

keyedElement: key COLON element | element ;

key: expression | structValue ;

element: expression | structValue ;

expression: expression OR logAndExpr |  logAndExpr ;

logAndExpr: logAndExpr AND relExpr | relExpr ;

relExpr: relExpr relOp = ( EQUALS | NOT_EQUALS | LESS_THAN | LESS_THAN_OR_EQUAL 
    | GREATER_THAN | GREATER_THAN_OR_EQUAL ) addExpr | addExpr ;

addExpr: addExpr addOp = (PLUS | MINUS) mulExpr | mulExpr ;

mulExpr: mulExpr mulOp = (STAR | SLASH | MOD) unaryExpr | unaryExpr ;

unaryExpr: unaryOp = (PLUS | MINUS | NOT) primaryExpr | primaryExpr ;

primaryExpr
    : primaryExpr DOT IDENTIFIER
    | primaryExpr index
    | operand; //??? function call

index: L_BRACKET expression R_BRACKET ;

operand: literal | IDENTIFIER | L_PAREN expression R_PAREN ; //


