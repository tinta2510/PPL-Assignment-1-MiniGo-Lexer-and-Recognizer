import unittest
from TestUtils import TestLexer
import inspect

class LexerSuite(unittest.TestCase): 
    # Test CHARACTER SET
    def test_char_newline(self):
        self.assertTrue(TestLexer.checkLexeme(""" // /* 
                                       */""", "\n,*,/,<EOF>", 101))
    
    
    # Test COMMENT
    def test_comment(self):
        """test comment"""
        self.assertTrue(TestLexer.checkLexeme("""/* abc */ var""","""var,<EOF>""",102))
        
    def test_multi_comment(self):
        """test multi comment"""
        self.assertTrue(TestLexer.checkLexeme("""/* comment */ func ()""","""func,(,),<EOF>""",103))
        
    def test_nested_comment(self):
        """test nested comment"""
        self.assertTrue(TestLexer.checkLexeme("""/* /* comment */ */ abc""","""abc,<EOF>""",104))
        
    def test_nested_comment2(self):
        """test nested comment"""
        self.assertTrue(TestLexer.checkLexeme("""/* /* comment */ */ abc /* comment2 */""","""abc,<EOF>""",105))
        
    def test_nested_comment3(self):
        """test nested comment"""
        self.assertTrue(TestLexer.checkLexeme("""/* /* comment */ comment_content /* comment2 */ */ abc""","""abc,<EOF>""",106))
        
    def test_nested_comment4(self):
        """test nested comment"""
        self.assertTrue(TestLexer.checkLexeme(
            """/* comment \n
                  comment2 \n
                  comment3 \n
                */  abc // comment3""","""abc,<EOF>""",107))
    
    def test_nested_comment5(self):
        """test nested comment"""
        self.assertTrue(TestLexer.checkLexeme(
            """/* a /* b /* c */ b */ a */	""","""<EOF>""",108))
        
    def test_nested_comment6(self):
        """test nested comment"""
        self.assertTrue(TestLexer.checkLexeme(
            """/* a //////* b /* c */ b */ a */	""","""<EOF>""",109))
    
    def test_nested_comment7(self):
        self.assertTrue(TestLexer.checkLexeme("""/*
        /* a */ /* b */ 
        // 321231
        */ if /* */ /* */""", "if,<EOF>", 110))
        
    def test_comments(self):
        self.assertTrue(TestLexer.checkLexeme("// TaTrungTin","<EOF>", 111))   
        
    def test_comments_2(self):
        self.assertTrue(TestLexer.checkLexeme("/* cmt /* /*cmt2*/ */ content","content,<EOF>", 112))
    
    # Test TOKEN SET
    ## Test IDENTIFIERS
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",113))
        
    def test_identifiers(self):
        self.assertTrue(TestLexer.checkLexeme("_TaTrungTin","_TaTrungTin,<EOF>", 114))
        
    ## Test KEYWORDS
    def test_keyword_var(self):
        """test keyword var"""
        self.assertTrue(TestLexer.checkLexeme("var abc int ;","var,abc,int,;,<EOF>",115))
        
    def test_keyword_func(self):
        """test keyword func"""
        self.assertTrue(TestLexer.checkLexeme("""func abc ( ) ""","""func,abc,(,),<EOF>""",116))
        
    def test_keyword_if_then_else(self):
        self.assertTrue(TestLexer.checkLexeme("if then else", "if,then,else,<EOF>", 117))
        
    ## Test OPERATORS
    def test_operator(self):
        self.assertTrue(TestLexer.checkLexeme("+","+,<EOF>", 118))
    
    ## Test SEPARATORS
    def test_separators(self):
        self.assertTrue(TestLexer.checkLexeme("[]","[,],<EOF>", 119))
        
    ## Test INT LITERALS
    def test_int_lit(self):
        self.assertTrue(TestLexer.checkLexeme("12","12,<EOF>", 120))
        
    def test_int_lit_2(self):
        self.assertTrue(TestLexer.checkLexeme("0x11","17,<EOF>", 121))
    
    def test_int_lit_3(self):
        self.assertTrue(TestLexer.checkLexeme("0452.", "0,452.,<EOF>", 122))
        
    def test_int_lit_4(self):
        self.assertTrue(TestLexer.checkLexeme("0X1234", "4660,<EOF>", 123))
    
    def test_int_lit_5(self):
        self.assertTrue(TestLexer.checkLexeme("0b1010", "10,<EOF>", 124))
    
    def test_int_lit_6(self):
        self.assertTrue(TestLexer.checkLexeme("0o1234", "668,<EOF>", 125))
    
    def test_int_lit_7(self):
        self.assertTrue(TestLexer.checkLexeme("0O1234", "668,<EOF>", 126))
    
    def test_int_lit_8(self):  
        self.assertTrue(TestLexer.checkLexeme("0B1001", "9,<EOF>", 127))
        
    def test_int_lit_9(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.test("-12", "-,12,<EOF>", inspect.stack()[0].function))
        
    ## Test FLOAT LITERALS
    def test_float_lit(self):
        self.assertTrue(TestLexer.checkLexeme("12.e-8","12.e-8,<EOF>", 128))
    
    def test_float_lit_2(self):
        self.assertTrue(TestLexer.checkLexeme("09.e-002","0,9.e-0,0,2,<EOF>", 129))
        
    ## Test STRING LITERALS
    def test_string_lit(self):
        """test string literal"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc" ""","""abc,<EOF>""",130))
    
    def test_string_lit_2(self):
        """test string literal"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\ndef" ""","""abc\\ndef,<EOF>""",131))
        
    def test_string_lit_3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "TaTrungTin \\r" ""","TaTrungTin \\r,<EOF>", 132))  
        
    ## Test BOOLEAN LITERALS
    
    ## Test NIL LITERALS
    
    # Test ERROR
    ## Test ERROR TOKEN
    def test_error_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?sVN","ab,ErrorToken ?",133))
        
    def test_error_token_2(self):
        self.assertTrue(TestLexer.checkLexeme("abc?xyz","abc,ErrorToken ?", 134))
        
    def test_error_token_3(self):
        self.assertTrue(TestLexer.checkLexeme("^","ErrorToken ^", 135))
        
    def test_error_token_4(self):
        self.assertTrue(TestLexer.checkLexeme("0b1234", "ErrorToken 2", 136))
        
    ## Test UNCLOSED STRING
    def test_unclosed_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\ndef" ""","Unclosed string: abc", 137))
        
    def test_unclosed_string_2(self):
        self.assertTrue(TestLexer.checkLexeme(
""""abc
""","Unclosed string: abc", 138))
        
    def test_unclose_string_3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "TaTrungTin\n" ""","Unclosed string: TaTrungTin", 139))
        
    ## Test ILLEGAL ESCAPE
    def test_illegal_escape(self):
        self.assertTrue(TestLexer.checkLexeme(""" "TaTrungTin\\f" ""","Illegal escape in string: TaTrungTin\\f", 140))
        
    def test_illegal_escape_2(self):
        self.assertTrue(TestLexer.checkLexeme(""" 
            const a = 2;
""","\n,const,a,=,2,;,\n,<EOF>", 141))
        
    def test_illegal_escape_3(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.checkLexeme(""" "abcd\ysafda" ""","Illegal escape in string: abcd\\y", 142))