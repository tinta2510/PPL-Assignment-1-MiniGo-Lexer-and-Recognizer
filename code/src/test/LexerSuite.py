import unittest
from TestUtils import TestLexer
import inspect

class LexerSuite(unittest.TestCase): 
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
        
    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?sVN","ab,ErrorToken ?",102))
        
    def test_keyword_var(self):
        """test keyword var"""
        self.assertTrue(TestLexer.checkLexeme("var abc int ;","var,abc,int,;,<EOF>",103))
        
    def test_keyword_func(self):
        """test keyword func"""
        self.assertTrue(TestLexer.checkLexeme("""func abc ( ) ""","""func,abc,(,),<EOF>""",104))
        
    def test_string_lit(self):
        """test string literal"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc" """,""""abc",<EOF>""",105))
    
    def test_comment(self):
        """test comment"""
        self.assertTrue(TestLexer.checkLexeme("""/* abc */ var""","""var,<EOF>""",106))
        
    def test_multi_comment(self):
        """test multi comment"""
        self.assertTrue(TestLexer.checkLexeme("""/* comment */ func ()""","""func,(,),<EOF>""",107))
        
    def test_nested_comment(self):
        """test nested comment"""
        self.assertTrue(TestLexer.checkLexeme("""/* /* comment */ */ abc""","""abc,<EOF>""",108))
        
    def test_nested_comment2(self):
        """test nested comment"""
        self.assertTrue(TestLexer.checkLexeme("""/* /* comment */ */ abc /* comment2 */""","""abc,<EOF>""",109))
        
    def test_nested_comment3(self):
        """test nested comment"""
        self.assertTrue(TestLexer.checkLexeme("""/* /* comment */ comment_content /* comment2 */ */ abc""","""abc,<EOF>""",110))
        
    def test_nested_comment4(self):
        """test nested comment"""
        self.assertTrue(TestLexer.checkLexeme(
            """/* comment \n
                  comment2 \n
                  comment3 \n
                */  abc // comment3""","""abc,<EOF>""",111))
    
    def test_nested_comment5(self):
        """test nested comment"""
        self.assertTrue(TestLexer.checkLexeme(
            """/* a /* b /* c */ b */ a */	""","""<EOF>""",112))
        
    def test_nested_comment6(self):
        """test nested comment"""
        self.assertTrue(TestLexer.checkLexeme(
            """/* a //////* b /* c */ b */ a */	""","""<EOF>""",113))
        
    def test_string_lit_2(self):
        """test string literal"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\ndef" """,""""abc\\ndef",<EOF>""",114))
        
    def test_illegal_escape(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.checkLexeme(""" "abcd\ysafda" ""","Illegal escape in string: abcd\\y", 115))
        
    def test_error_token(self):
        self.assertTrue(TestLexer.checkLexeme("abc?xyz","abc,ErrorToken ?", 116))
        
    def test_unclosed_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\ndef" ""","Unclosed string: abc", 117))
        
    def test_unclosed_string_2(self):
        self.assertTrue(TestLexer.checkLexeme(
""""abc
""","Unclosed string: abc", 118))
        
    def test_nested_comment7(self):
        self.assertTrue(TestLexer.checkLexeme("""/*
        /* a */ /* b */ 
        // 321231
        */ if /* */ /* */""", "if,<EOF>", 119))