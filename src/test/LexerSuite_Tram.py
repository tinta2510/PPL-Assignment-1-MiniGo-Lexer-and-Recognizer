import unittest
from TestUtils import TestLexer
import inspect

class LexerSuite(unittest.TestCase): 
    # Test CHARACTER SET
    def test_single_line_comment_with_code(self):
        """Test single-line comment followed by code"""
        input = """// This is a comment
                x := 10;"""
        expect = "x,:=,10,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 201))
        
    def test_nested_multiline_comment(self):
        """Test multi-line comment with nested comments"""
        input = """/* Outer comment /* Inner comment */ Still outer */ x := 5;"""
        expect = "x,:=,5,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 202))
    
    def test_id(self):
        """test comment"""
        self.assertTrue(TestLexer.checkLexeme("""var abc
                                              ""","""var,abc,;,<EOF>""",103))
        
    def test_multi_line_comment(self):
        self.assertTrue(TestLexer.checkLexeme("""/* A multiple-line comment */ foo()""","""foo,(,),<EOF>""",104))
        
    def test_nested_multiline_comment_2(self):
        """Single-line inside multiple line comment"""
        self.assertTrue(TestLexer.checkLexeme("""/* A multiple-line /* // A single-line comment */ comment */ abc""","""abc,<EOF>""",105))
        
    def test_nested_multiline_comment_3(self):
        self.assertTrue(TestLexer.checkLexeme("""/* outer comment /* comment1 */ /* comment2 */ still outer; */  abc // single-line comment""","""abc,<EOF>""",106))
        
    def test_single_line_comment(self):
        self.assertTrue(TestLexer.checkLexeme("""// a single-line comment;
                                              
                                              // another single-line comment""","""<EOF>""",107))
        
    def test_multi_line_comment_2(self):
        self.assertTrue(TestLexer.checkLexeme(
            """// a single-line comment
            const abc = 10; // another single-line comment
            /* comment \n
                comment2 \t
                comment3 \\n
            */""", """const,abc,=,10,;,<EOF>""",108))
    
    def test_nested_multiline_comment_4(self):
        """test nested comment"""
        self.assertTrue(TestLexer.checkLexeme(
            """/* a /* b /* c */ b */ a */\t""","""<EOF>""",109))
        
    def test_id_2(self):
        self.assertTrue(TestLexer.checkLexeme("_abc123","_abc123,<EOF>", 110))
        
    def test_id_3(self):
        """test keyword var"""
        self.assertTrue(TestLexer.checkLexeme("var 123abc;","var,123,abc,;,<EOF>",111))
        
    def test_func(self):
        self.assertTrue(TestLexer.checkLexeme("""func foo(a, b, c) ""","""func,foo,(,a,,,b,,,c,),<EOF>""",112))
        
    def test_if_else(self):
        self.assertTrue(TestLexer.checkLexeme("if (a == 10) {} else {}", "if,(,a,==,10,),{,},else,{,},<EOF>", 113))
        
    def test_operators(self):
        self.assertTrue(TestLexer.checkLexeme("+ - / % *","+,-,/,%,*,<EOF>", 114))
    
    def test_brackets(self):
        self.assertTrue(TestLexer.checkLexeme("[] {} ()","[,],{,},(,),<EOF>", 115))
        
    def test_dec(self):
        self.assertTrue(TestLexer.checkLexeme("12","12,<EOF>", 116))
        
    def test_bin(self):
        self.assertTrue(TestLexer.checkLexeme("0x11","0x11,<EOF>", 117))
    
    def test_float(self):
        """integer part has no constraints"""
        self.assertTrue(TestLexer.checkLexeme("0452.", "0452.,<EOF>", 118))
        
    def test_hex(self):
        self.assertTrue(TestLexer.checkLexeme("0X123ABC", "0X123ABC,<EOF>", 119))
    
    def test_hex_2(self):
        self.assertTrue(TestLexer.checkLexeme("0X456DEF", "0X456DEF,<EOF>", 120))
        
    def test_invalid_hex(self):
        self.assertTrue(TestLexer.checkLexeme("0x123G", "0x123,G,<EOF>", 121))
        
    def test_bin_2(self):
        self.assertTrue(TestLexer.checkLexeme("0B1010", "0B1010,<EOF>", 122))
        
    def test_invalid_bin(self):
        self.assertTrue(TestLexer.checkLexeme("0b101023", "0b1010,23,<EOF>", 123))
    
    def test_oct(self):
        self.assertTrue(TestLexer.checkLexeme("0o1234", "0o1234,<EOF>", 124))
        
    def test_oct_2(self):
        self.assertTrue(TestLexer.checkLexeme("0O567", "0O567,<EOF>", 125))
        
    def test_invalid_oct(self):
        self.assertTrue(TestLexer.checkLexeme("0o1238A", "0o123,8,A,<EOF>", 126))
        
    def test_negative_int(self):
        self.assertTrue(TestLexer.checkLexeme("-12", "-,12,<EOF>", 127))
        
    def test_invalid_oct_2(self):
        self.assertTrue(TestLexer.checkLexeme("0o", "0,o,<EOF>", 128))
        
    def test_float_2(self):
        self.assertTrue(TestLexer.checkLexeme("12.e-8","12.e-8,<EOF>", 129))
    
    def test_float_3(self):
        self.assertTrue(TestLexer.checkLexeme("09.e-002","09.e-002,<EOF>", 130))

    def test_float_4(self):
        self.assertTrue(TestLexer.checkLexeme("010.010e-020.2", "010.010e-020,.,2,<EOF>", 131))
        
    def test_string(self):
        """test string literal"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc" """,""""abc",<EOF>""",132))
    
    def test_string_w_newline(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\ndef" """,""""abc\\ndef",<EOF>""",133))
        
    def test_string_w_escaped_sequence(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\ndef\\tghi\\\haha\\r" """,""""abc\\ndef\\tghi\\\haha\\r",<EOF>""",134))
        
    ## Test BOOLEAN LITERALS
    def test_boolean(self):
        self.assertTrue(TestLexer.checkLexeme("true false", "true,false,<EOF>", 135))
    
    ## Test NIL LITERALS
    def test_nil(self):
        self.assertTrue(TestLexer.checkLexeme("nil", "nil,<EOF>", 136))
    
    # Test ERROR
    ## Test ERROR TOKEN
    def test_error_token(self):
        self.assertTrue(TestLexer.checkLexeme("valid?TOKEN","valid,ErrorToken ?",137))
        
    def test_error_token_2(self):
        self.assertTrue(TestLexer.checkLexeme("valid&TOKENN","valid,ErrorToken &", 138))
        
    def test_error_token_3(self):
        self.assertTrue(TestLexer.checkLexeme("(^)","(,ErrorToken ^", 139))
        
    ## Test UNCLOSED STRING
    def test_unclosed_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "string_w_newline\ndef" ""","Unclosed string: \"string_w_newline", 140))
        
    def test_unclosed_string_2(self):
        self.assertTrue(TestLexer.checkLexeme(""""unclosed_string
        ""","Unclosed string: \"unclosed_string", 141))
        
    ## Test ILLEGAL ESCAPE
    def test_illegal_escape(self):
        self.assertTrue(TestLexer.checkLexeme(""" "string_w_illegal_escape\\f" ""","Illegal escape in string: \"string_w_illegal_escape\\f", 142))
        
    def test_illegal_escape_2(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.checkLexeme(""" "string_w_\y_illegal_escape" ""","Illegal escape in string: \"string_w_\\y", 143))
        
    # Additional random test cases
    def test_hex_3(self):
        """Test hexadecimal integer literals"""
        self.assertTrue(TestLexer.checkLexeme("0x89A 0XFFXYZ 0x010o110", "0x89A,0XFF,XYZ,0x010,o110,<EOF>", 144))

    def test_float_5(self):
        """Test floating literals missing integer part"""
        self.assertTrue(TestLexer.checkLexeme(".1e-9", ".,1,e,-,9,<EOF>", 145))

    def test_id_4(self):
        """Test identifier containing a keyword"""
        self.assertTrue(TestLexer.checkLexeme("return_value", "return_value,<EOF>", 146))

    def test_relational_ops(self):
        self.assertTrue(TestLexer.checkLexeme("== != < <= > >=", "==,!=,<,<=,>,>=,<EOF>", 147))

    def test_logical_ops(self):
        self.assertTrue(TestLexer.checkLexeme("! && ||", "!,&&,||,<EOF>", 148))

    def test_assignment_ops(self):
        self.assertTrue(TestLexer.checkLexeme(":= = += -= %= *= /=", ":=,=,+=,-=,%=,*=,/=,<EOF>", 149))

    def test_id_5(self):
        self.assertTrue(TestLexer.checkLexeme("var x$ = 5;", "var,x,ErrorToken $", 150))

    def test_invalid_multiple_line_comment(self):
        """invalid multi-line comment"""
        self.assertTrue(TestLexer.checkLexeme("/* A multiple-line comment", "/,*,A,multiple,-,line,comment,<EOF>", 151))

    def test_invalid_float(self):
        """Test floating-point number with invalid exponent"""
        self.assertTrue(TestLexer.checkLexeme("9.87e", "9.87,e,<EOF>", 152))

    def test_func_call(self):
        """Test a function call with arguments"""
        self.assertTrue(TestLexer.checkLexeme("println(123, \"hello world\")", "println,(,123,,,\"hello world\",),<EOF>", 153))

    def test_mix_ops(self):
        """Test mixed arithmetic and relational operators"""
        self.assertTrue(TestLexer.checkLexeme("a == b + c || d * e % f >= g", "a,==,b,+,c,||,d,*,e,%,f,>=,g,<EOF>", 154))

    def test_struct_dec(self):
        self.assertTrue(TestLexer.checkLexeme("type Greeting struct { name string; message string; }", 
                                            "type,Greeting,struct,{,name,string,;,message,string,;,},<EOF>", 155))
        
    def test_func_newline(self):
        self.assertTrue(TestLexer.checkLexeme("func foo() \n { \n \n return; }", "func,foo,(,),;,{,return,;,},<EOF>", 156))
        
    def test_var_dec(self):
        self.assertTrue(TestLexer.checkLexeme("var x int", "var,x,int,<EOF>", 157))
        
    def test_const_dec(self):
        self.assertTrue(TestLexer.checkLexeme("const x = 10", "const,x,=,10,<EOF>", 158))
    
    def test_arr_dec(self):
        self.assertTrue(TestLexer.checkLexeme("var array [id]float;", "var,array,[,id,],float,;,<EOF>", 159))
        
    def test_arr_dec2(self):
        self.assertTrue(TestLexer.checkLexeme("var array = [2][2]float{{1,2},{3,4}};", "var,array,=,[,2,],[,2,],float,{,{,1,,,2,},,,{,3,,,4,},},;,<EOF>", 160))
        
    def test_if_else_2(self):
        self.assertTrue(TestLexer.checkLexeme("""if (a == 10) 
                                              { return a; } 
                                              else { return ; }""", "if,(,a,==,10,),;,{,return,a,;,},;,else,{,return,;,},<EOF>", 161))
        
    def test_update_for_loop(self):
        self.assertTrue(TestLexer.checkLexeme("for i := 0; i < 10; i++ { println(i); }", "for,i,:=,0,;,i,<,10,;,i,+,+,{,println,(,i,),;,},<EOF>", 162))
    
    def test_basic_for_loop(self):
        self.assertTrue(TestLexer.checkLexeme("for i < 10 { println(1); }", "for,i,<,10,{,println,(,1,),;,},<EOF>", 163))
        
    def test_range_for_loop(self):
        self.assertTrue(TestLexer.checkLexeme("for i := range arr { println(i); }", "for,i,:=,range,arr,{,println,(,i,),;,},<EOF>", 164))
        
    def test_for_w_newline(self):
        self.assertTrue(TestLexer.checkLexeme("""for i := 0
                                              i < 10
                                              i++ { 
                                              
                                              println(i); 
                                              
                                              }""", "for,i,:=,0,;,i,<,10,;,i,+,+,{,println,(,i,),;,},<EOF>", 165))
        
    def test_for_w_newline_2(self):
        self.assertTrue(TestLexer.checkLexeme("""for i < 5 { \n \n println(i); }""", "for,i,<,5,{,println,(,i,),;,},<EOF>", 166))
        
    def test_method_call(self):
        self.assertTrue(TestLexer.checkLexeme("obj.method()", "obj,.,method,(,),<EOF>", 167))
        
    def test_method_decl(self):
        self.assertTrue(TestLexer.checkLexeme("func (obj Object) method() { return a; }", "func,(,obj,Object,),method,(,),{,return,a,;,},<EOF>", 168))
        
    def test_method_decl_2(self):
        self.assertTrue(TestLexer.checkLexeme("func (obj Object) method(a, b int) string { return \"hello\\n\"; }", "func,(,obj,Object,),method,(,a,,,b,int,),string,{,return,\"hello\\n\",;,},<EOF>", 169))
        
    def test_method_call_2(self):
        self.assertTrue(TestLexer.checkLexeme("arr[1][2].obj.method(1, 2)", "arr,[,1,],[,2,],.,obj,.,method,(,1,,,2,),<EOF>", 170))
        
    def test_continue_break_return(self):
        self.assertTrue(TestLexer.checkLexeme("continue break return", "continue,break,return,<EOF>", 171))
    
    def test_complex_func_call(self):
        self.assertTrue(TestLexer.checkLexeme("func(obj.foo(bar(1, 2), 3))", "func,(,obj,.,foo,(,bar,(,1,,,2,),,,3,),),<EOF>", 172))
        
    def test_struct_w_newline(self):
        self.assertTrue(TestLexer.checkLexeme(
            """type Greeting struct {
            name string
            message string
            
            }""", 
            "type,Greeting,struct,{,name,string,;,message,string,;,},<EOF>", 173))
        
    def test_assignment(self):
        self.assertTrue(TestLexer.checkLexeme("x := 10", "x,:=,10,<EOF>", 174))
        
    def test_assignment_2(self):
        self.assertTrue(TestLexer.checkLexeme("x := Greeting{name: \"John\", message: \"Hello\"}", "x,:=,Greeting,{,name,:,\"John\",,,message,:,\"Hello\",},<EOF>", 175))
        
    def test_assignment_3(self):
        self.assertTrue(TestLexer.checkLexeme("x := arr[1][2]", "x,:=,arr,[,1,],[,2,],<EOF>", 176))
        
    def test_assignment_4(self):
        self.assertTrue(TestLexer.checkLexeme("x := obj.method(1, 2)", "x,:=,obj,.,method,(,1,,,2,),<EOF>", 177))
        
    def test_complex_assignment(self):
        self.assertTrue(TestLexer.checkLexeme("x := obj.method(1, 2) + 10 / id[1][2])", "x,:=,obj,.,method,(,1,,,2,),+,10,/,id,[,1,],[,2,],),<EOF>", 178))
    
    def test_struct_w_invalid_field(self):
        self.assertTrue(TestLexer.checkLexeme("type Special struct { name_with_underscore string; name-with-dash int; }", 
                                            "type,Special,struct,{,name_with_underscore,string,;,name,-,with,-,dash,int,;,},<EOF>", 179))
        
    def test_string_double_quotes(self):
        self.assertTrue(TestLexer.checkLexeme(""" 
                    "Hello \\"World\\"" 
            ""","""\"Hello \\"World\\"\",;,<EOF>""", 180))
        
    def test_invalid_single_quote(self):
        self.assertTrue(TestLexer.checkLexeme("'abc'", "ErrorToken '", 181))
        
    def test_string_with_double_backlash(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Hello \\\\ World" """,""""Hello \\\\ World",<EOF>""",182))
        
    def test_data_type(self):
        self.assertTrue(TestLexer.checkLexeme("int float string bool", "int,float,string,bool,<EOF>", 183))
        
    def test_interface_decl(self):
        self.assertTrue(TestLexer.checkLexeme("type MyInterface interface { func1(); func2(); }", 
                                            "type,MyInterface,interface,{,func1,(,),;,func2,(,),;,},<EOF>", 184))
        
    def test_interface_decl_2(self):
        """test interface with newline"""
        self.assertTrue(TestLexer.checkLexeme("""type MyInterface interface { 
                                              func1() \n func2() 
                                              }""", 
                                            """type,MyInterface,interface,{,func1,(,),;,func2,(,),;,},<EOF>""", 185))
        
    def test_interface_decl_3(self):
        """test interface with parameters"""
        self.assertTrue(TestLexer.checkLexeme("""type MyInterface interface { 
                                              func1(a int) \n func2(b [2]int) 
                                              }""", 
                                            """type,MyInterface,interface,{,func1,(,a,int,),;,func2,(,b,[,2,],int,),;,},<EOF>""", 186))
        
    
    def test_complete_program(self):
        input = """int main() {
            int a = 10;
            float b = 3.14;
            string message = "Hello, World!";
            bool flag = true;
            return 0;
        }"""
        expect = "int,main,(,),{,int,a,=,10,;,float,b,=,3.14,;,string,message,=,\"Hello, World!\",;,bool,flag,=,true,;,return,0,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 187))
        
    def test_complete_program_2(self):
        input = """type Greeting struct {
            name string;
            message string;
        }
        
        func (g Greeting) greet() {
            println(g.name + " says " + g.message);
        }"""
        expect = "type,Greeting,struct,{,name,string,;,message,string,;,},;,func,(,g,Greeting,),greet,(,),{,println,(,g,.,name,+,\" says \",+,g,.,message,),;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 188))
        
    def test_complete_program_3(self):
        input = """type Greeting struct {
            name string;
            message string;
        }
        
        func (g Greeting) greet() {
            println(g.name + " says " + g.message);
        }
        
        func main() {
            Greeting g = Greeting{name: "John", message: "Hello"};
            g.greet();
        }"""
        expect = "type,Greeting,struct,{,name,string,;,message,string,;,},;,func,(,g,Greeting,),greet,(,),{,println,(,g,.,name,+,\" says \",+,g,.,message,),;,},;,func,main,(,),{,Greeting,g,=,Greeting,{,name,:,\"John\",,,message,:,\"Hello\",},;,g,.,greet,(,),;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 189))
        
    def test_complete_program_4(self):
        input = """int main() {
            int x = 10;
            if (x > 5) {
                x = x - 1;
            } else {
                x = x + 1;
            }
            return 0;
        }"""
        expect = "int,main,(,),{,int,x,=,10,;,if,(,x,>,5,),{,x,=,x,-,1,;,},else,{,x,=,x,+,1,;,},;,return,0,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 190))
        
    def test_complete_program_5(self):
        input = """int add(a int, b int) {
            return a + b;
        }

        int main() {
            int result = add(5, 10);
            return 0
        }"""
        expect = "int,add,(,a,int,,,b,int,),{,return,a,+,b,;,},;,int,main,(,),{,int,result,=,add,(,5,,,10,),;,return,0,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 191))
        
    def test_complete_program_6(self):
        input = """int main() {
            int arr[5] = {1, 2, 3, 4, 5};
            int sum = arr[0] + arr[1];
            return 0;
        }"""
        output = "int,main,(,),{,int,arr,[,5,],=,{,1,,,2,,,3,,,4,,,5,},;,int,sum,=,arr,[,0,],+,arr,[,1,],;,return,0,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, output, 192))
        
    def test_complete_program_7(self):
        input = """const c bool = false;
        int main() {
            bool a = true;
            bool b = false;
            bool result = a && b || !a && !c;
            return 0;
        }"""
        expect = "const,c,bool,=,false,;,int,main,(,),{,bool,a,=,true,;,bool,b,=,false,;,bool,result,=,a,&&,b,||,!,a,&&,!,c,;,return,0,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 193))
        
    def test_complete_program_8(self):
        input="""
        type Circle struct {
            radius float;
        }
        func (c Circle) area() float {
            return 3.14 * c.radius * c.radius;
        }
        type Rectangle struct {
            width float;
            height float;
        }
        func (r Rectangle) area() float {
            return r.width * r.height;
        }
        func main() {
            Circle c = Circle{radius: 5};
            Rectangle r = Rectangle{width: 10, height: 5};
            println(c.area());
            println(r.area());
        }"""
        expect = "type,Circle,struct,{,radius,float,;,},;,func,(,c,Circle,),area,(,),float,{,return,3.14,*,c,.,radius,*,c,.,radius,;,},;,type,Rectangle,struct,{,width,float,;,height,float,;,},;,func,(,r,Rectangle,),area,(,),float,{,return,r,.,width,*,r,.,height,;,},;,func,main,(,),{,Circle,c,=,Circle,{,radius,:,5,},;,Rectangle,r,=,Rectangle,{,width,:,10,,,height,:,5,},;,println,(,c,.,area,(,),),;,println,(,r,.,area,(,),),;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 194))
        
    def test_complete_program_9(self):
        input = """int main() {
            string s1 = "Hello";
            string s2 = "World";
            string result = s1 + " " + s2;
            return 0;
        }"""
        expect = "int,main,(,),{,string,s1,=,\"Hello\",;,string,s2,=,\"World\",;,string,result,=,s1,+,\" \",+,s2,;,return,0,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 195))
        
    def test_complete_program_10(self):
        input = """int main() {
            string s = "Hello, World;
            return 0;
        }"""
        expect = "int,main,(,),{,string,s,=,Unclosed string: \"Hello, World;"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 196))
        
    def test_complete_program_11(self):
        input = """int main() {
            string s = "Hello, World!";
            println(s);
            return 0;
        }"""
        expect = "int,main,(,),{,string,s,=,\"Hello, World!\",;,println,(,s,),;,return,0,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 197))
        
    def test_complete_program_12(self):
        input = """const a int = 10
        var b int = 5
        int main() {
            
            return a + b
            
        }"""
        expect = "const,a,int,=,10,;,var,b,int,=,5,;,int,main,(,),{,return,a,+,b,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 198))
        
    def test_complete_program_13(self):
        input = """int main() {
            var a [2]int = [2]int{1, 2};
            var b = [2][1]int{{3}, {"string"}};
            c := 10
            c += 2
            return c;
        }"""
        expect = "int,main,(,),{,var,a,[,2,],int,=,[,2,],int,{,1,,,2,},;,var,b,=,[,2,],[,1,],int,{,{,3,},,,{,\"string\",},},;,c,:=,10,;,c,+=,2,;,return,c,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 199))
        
    def test_complete_program_14(self):
        input = """int add(int a, int b) {
            return a + b;
        }

        int main() {
            int result = add(add(5, 10), add(20, 30));
            return 0;
        }"""
        expect = "int,add,(,int,a,,,int,b,),{,return,a,+,b,;,},;,int,main,(,),{,int,result,=,add,(,add,(,5,,,10,),,,add,(,20,,,30,),),;,return,0,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 200))
        