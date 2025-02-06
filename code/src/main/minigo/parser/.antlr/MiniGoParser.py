# Generated from d:/HCMUT_Workspace/HK242/Principles-of-Programming-Languages/Assignment/Assignment-1/PPL-Assignment-1-MiniGo-Lexer-and-Recognizer/code/src/main/minigo/parser/MiniGo.g4 by ANTLR 4.13.1
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
        4,1,60,33,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,10,8,0,11,0,12,
        0,11,1,0,1,0,1,1,1,1,3,1,18,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,0,0,4,0,2,4,6,0,0,30,0,9,1,0,0,0,2,17,1,
        0,0,0,4,19,1,0,0,0,6,24,1,0,0,0,8,10,3,2,1,0,9,8,1,0,0,0,10,11,1,
        0,0,0,11,9,1,0,0,0,11,12,1,0,0,0,12,13,1,0,0,0,13,14,5,0,0,1,14,
        1,1,0,0,0,15,18,3,6,3,0,16,18,3,4,2,0,17,15,1,0,0,0,17,16,1,0,0,
        0,18,3,1,0,0,0,19,20,5,18,0,0,20,21,5,25,0,0,21,22,5,14,0,0,22,23,
        5,54,0,0,23,5,1,0,0,0,24,25,5,9,0,0,25,26,5,25,0,0,26,27,5,47,0,
        0,27,28,5,48,0,0,28,29,5,49,0,0,29,30,5,50,0,0,30,31,5,54,0,0,31,
        7,1,0,0,0,2,11,17
    ]

class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'if'", "'else'", "'for'", "'return'", 
                     "'func'", "'type'", "'struct'", "'interface'", "'string'", 
                     "'int'", "'float'", "'boolean'", "'const'", "'var'", 
                     "'continue'", "'break'", "'range'", "'nil'", "'true'", 
                     "'false'", "<INVALID>", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'&&'", "'||'", "'!'", "'='", "'+='", "'-='", "'*='", 
                     "'/='", "'%='", "'.'", "'('", "')'", "'{'", "'}'", 
                     "'['", "']'", "','", "';'" ]

    symbolicNames = [ "<INVALID>", "NL", "WS", "LINE_COMMENT", "MULTI_LINE_COMMENT", 
                      "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
                      "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", 
                      "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", 
                      "TRUE", "FALSE", "ID", "PLUS", "MINUS", "STAR", "SLASH", 
                      "MOD", "EQUALS", "NOT_EQUALS", "LESS_THAN", "LESS_THAN_OR_EQUAL", 
                      "GREATER_THAN", "GREATER_THAN_OR_EQUAL", "AND", "OR", 
                      "NOT", "ASSIGN", "PLUS_ASSIGN", "MINUS_ASSIGN", "STAR_ASSIGN", 
                      "SLASH_ASSIGN", "MOD_ASSIGN", "DOT", "L_PAREN", "R_PAREN", 
                      "L_BRACE", "R_BRACE", "L_BRACKET", "R_BRACKET", "COMMA", 
                      "SEMICOLON", "INT_LIT", "FLOAT_LIT", "STRING_LIT", 
                      "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_vardecl = 2
    RULE_funcdecl = 3

    ruleNames =  [ "program", "decl", "vardecl", "funcdecl" ]

    EOF = Token.EOF
    NL=1
    WS=2
    LINE_COMMENT=3
    MULTI_LINE_COMMENT=4
    IF=5
    ELSE=6
    FOR=7
    RETURN=8
    FUNC=9
    TYPE=10
    STRUCT=11
    INTERFACE=12
    STRING=13
    INT=14
    FLOAT=15
    BOOLEAN=16
    CONST=17
    VAR=18
    CONTINUE=19
    BREAK=20
    RANGE=21
    NIL=22
    TRUE=23
    FALSE=24
    ID=25
    PLUS=26
    MINUS=27
    STAR=28
    SLASH=29
    MOD=30
    EQUALS=31
    NOT_EQUALS=32
    LESS_THAN=33
    LESS_THAN_OR_EQUAL=34
    GREATER_THAN=35
    GREATER_THAN_OR_EQUAL=36
    AND=37
    OR=38
    NOT=39
    ASSIGN=40
    PLUS_ASSIGN=41
    MINUS_ASSIGN=42
    STAR_ASSIGN=43
    SLASH_ASSIGN=44
    MOD_ASSIGN=45
    DOT=46
    L_PAREN=47
    R_PAREN=48
    L_BRACE=49
    R_BRACE=50
    L_BRACKET=51
    R_BRACKET=52
    COMMA=53
    SEMICOLON=54
    INT_LIT=55
    FLOAT_LIT=56
    STRING_LIT=57
    ERROR_CHAR=58
    ILLEGAL_ESCAPE=59
    UNCLOSE_STRING=60

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DeclContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_program




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.decl()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==9 or _la==18):
                    break

            self.state = 13
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcdecl(self):
            return self.getTypedRuleContext(MiniGoParser.FuncdeclContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.state = 17
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.funcdecl()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.vardecl()
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


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_vardecl




    def vardecl(self):

        localctx = MiniGoParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(MiniGoParser.VAR)
            self.state = 20
            self.match(MiniGoParser.ID)
            self.state = 21
            self.match(MiniGoParser.INT)
            self.state = 22
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def L_PAREN(self):
            return self.getToken(MiniGoParser.L_PAREN, 0)

        def R_PAREN(self):
            return self.getToken(MiniGoParser.R_PAREN, 0)

        def L_BRACE(self):
            return self.getToken(MiniGoParser.L_BRACE, 0)

        def R_BRACE(self):
            return self.getToken(MiniGoParser.R_BRACE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_funcdecl




    def funcdecl(self):

        localctx = MiniGoParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(MiniGoParser.FUNC)
            self.state = 25
            self.match(MiniGoParser.ID)
            self.state = 26
            self.match(MiniGoParser.L_PAREN)
            self.state = 27
            self.match(MiniGoParser.R_PAREN)
            self.state = 28
            self.match(MiniGoParser.L_BRACE)
            self.state = 29
            self.match(MiniGoParser.R_BRACE)
            self.state = 30
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





