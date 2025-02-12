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
        result = super().emit();
        self.preceding_token = result;
        return result;
}

options{
	language=Python3;
}

// Lexer rules
NL: ('\r'?'\n') {
    accepted_tokens_before_newline_char = [
        self.IDENTIFIER, self.INT_LIT, self.FLOAT_LIT, self.TRUE, self.FALSE, 
        self.STRING_LIT, self.INT, self.FLOAT, self.BOOLEAN, self.STRING, self.RETURN, 
        self.CONTINUE, self.BREAK, self.R_PAREN, self.R_BRACKET, self.R_BRACE
    ]
    if hasattr(self, 'preceding_token') and self.preceding_token and self.preceding_token.type in accepted_tokens_before_newline_char:
        self.type = self.SEMICOLON;
    else:
        self.skip();
}; 

WS : [ \t\r\f]+ -> skip ; // skip spaces, tabs

LINE_COMMENT: '//' ~[\r\n]* -> skip;

MULTI_LINE_COMMENT: '/*' ( MULTI_LINE_COMMENT | .)*? '*/' -> skip;

EOS: SEMICOLON ;

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
INT_LIT //???
    : DECIMAL_INT 
    | BINARY_INT { self.text = str(int(self.text, 2)) }
    | OCTAL_INT { self.text = str(int(self.text, 8)) }
    | HEX_INT { self.text = str(int(self.text, 16)) }
    ;
fragment DECIMAL_INT: [1-9]DIGIT* | '0'; 
fragment DIGIT: [0-9];
fragment BINARY_INT: '0'[Bb][01]+ ;
fragment OCTAL_INT: '0'[Oo][0-7]+ ;
fragment HEX_INT: '0'[Xx][0-9A-Fa-f]+ ;

FLOAT_LIT: DECIMAL_INT '.' DIGIT* EXPONENT?;

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

// Declaration
declList: decl | declList decl ;

decl: varDecl | constDecl | funcDecl | methodDefine | structDecl | interfaceDecl ;

varDecl
    : varDeclWithInit //???: Identifier list
    | VAR IDENTIFIER type_ EOS
    ;

varDeclWithInit
    : VAR IDENTIFIER type_ initilization EOS 
    | VAR IDENTIFIER initilization EOS
    ;

type_: IDENTIFIER | STRING | INT | FLOAT | BOOLEAN | arrayType ;

initilization: ASSIGN expression ;

constDecl: CONST IDENTIFIER initilization EOS ;

funcDecl: FUNC IDENTIFIER signature block ;

signature
    : parameterList returnType
    | parameterList ;

parameterList: L_PAREN parameterDeclList R_PAREN ;

returnType: type_;

parameterDeclList: nonNullParameterDeclList | ;

nonNullParameterDeclList: parameterDecl COMMA nonNullParameterDeclList | typedParameterDecl ;

parameterDecl: IDENTIFIER type_ | IDENTIFIER ;

typedParameterDecl: IDENTIFIER type_ ;

block: L_BRACE stmtList R_BRACE ;

stmtList: stmt | stmtList stmt ;

methodDefine: FUNC receiver IDENTIFIER signature block ;

receiver: L_PAREN IDENTIFIER type_ R_PAREN ;

structDecl: TYPE IDENTIFIER STRUCT structBody ;

structBody: L_BRACE fieldDeclList R_BRACE ;

fieldDeclList: fieldDecl | fieldDeclList fieldDecl ;

fieldDecl: IDENTIFIER type_ EOS ;

interfaceDecl: TYPE IDENTIFIER INTERFACE interfaceBody ;

interfaceBody: L_BRACE methodDeclList R_BRACE ;

methodDeclList: methodDecl | methodDeclList methodDecl ;

methodDecl: IDENTIFIER signature EOS;

// Statement
stmt
    : varDecl | constDecl | assignStmt | ifStmt | forStmt | breakStmt 
    | continueStmt | callStmt | returnStmt ;

assignStmt: lhs assignOp rhs EOS ;

lhs: IDENTIFIER | lhs fieldAccess | lhs arrayAccess ; //???

assignOp: COLON_ASSIGN | PLUS_ASSIGN | MINUS_ASSIGN | STAR_ASSIGN | SLASH_ASSIGN | MOD_ASSIGN ;

rhs: expression ;

ifStmt: IF ifCondition block elseStmt ;

ifCondition: L_PAREN expression R_PAREN ;

elseStmt: ELSE block | ELSE ifStmt | ;

forStmt: FOR forClause block ;

forClause: forCondition | forLoop | forRange ;

forCondition: expression ;

forLoop: forLoopInit SEMICOLON forCondition SEMICOLON forLoopUpdate ;

forLoopInit: assignStmt | varDeclWithInit ;

forLoopUpdate: assignStmt ;

forRange: forIndex COMMA forValue COLON_ASSIGN rangeExpr ;

forIndex: IDENTIFIER ;

forValue: IDENTIFIER ;

rangeExpr: RANGE IDENTIFIER ;

breakStmt: BREAK EOS ;

continueStmt: CONTINUE EOS ;

callStmt: primaryExpr arguments EOS ; //???

returnStmt: RETURN expression EOS | RETURN EOS ;

// Expression
literal: basicLit | compositeLit ;

basicLit: INT_LIT | FLOAT_LIT | STRING_LIT | TRUE | FALSE | NIL ;

compositeLit: arrayLit | structLit ;

arrayLit: arrayType arrayValue ;

arrayType: L_BRACKET arrayTypeIndex R_BRACKET elementType ; //???: or constant

arrayTypeIndex: INT_LIT | IDENTIFIER ;

elementType: type_ ;

arrayValue
    : L_BRACE elementList R_BRACE
    | L_BRACE R_BRACE ;

structLit: structType structValue ;

structType: INT_LIT | IDENTIFIER ;

structValue
    : L_BRACE keyedElementList R_BRACE
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
    : operand
    | primaryExpr fieldAccess   // field access
    | primaryExpr arrayAccess         // array access
    | primaryExpr arguments     // function/method call
    ; 

fieldAccess: DOT IDENTIFIER ;

arrayAccess: L_BRACKET expression R_BRACKET ;

arguments: L_PAREN argumentList R_PAREN ;

argumentList: nonNullArgumentList | ;

nonNullArgumentList: expression COMMA nonNullArgumentList | expression ;

operand: literal | IDENTIFIER | L_PAREN expression R_PAREN ; 