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
ID: [A-Za-z_][A-Za-z0-9_]*;

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
program  : decl+ EOF ;

decl: funcdecl | vardecl  ;

vardecl: 'var' ID 'int' ';' ;

funcdecl: 'func' ID '(' ')' '{' '}' ';' ;