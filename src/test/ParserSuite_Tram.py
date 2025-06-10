import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: void main() {} """
        input = """func main() {
            sing("Good morning!")
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_more_complex_program(self):
        """More complex program"""
        input = """func sum(a int, b float) float {
                return a + b;
            };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    
    def test_wrong_miss_close(self):
        """Miss ) void main( {}"""
        input = """func main({};"""
        expect = "Error on line 1 col 11: {"
        self.assertTrue(TestParser.checkParser(input,expect,203))
        
    def test_wrong_variable(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,204))
        
    def test_wrong_index(self):
        input = """var i ;"""
        expect = "Error on line 1 col 7: ;"
        self.assertTrue(TestParser.checkParser(input,expect,205))
        
    # --------------LIT DECLARATION----------------
    def test_int_lit(self):
        """Literal"""
        self.assertTrue(TestParser.checkParser("const lit_const = 1;","successful", 206))

    def test_bool_lit(self):
        """Literal"""
        self.assertTrue(TestParser.checkParser("const bool_const = true;","successful", 207))

    def test_array_lit(self):
        """Literal"""
        self.assertTrue(TestParser.checkParser("const string_arr = [5][0]string{1, \"string\"};","successful", 208))

    def test_array_w_float_type(self):
        """Literal"""
        self.assertTrue(TestParser.checkParser("const float_type_arr = [1.]ID{1, 3};","Error on line 1 col 25: 1.", 209))

    def test_struct(self):
        """Literal"""
        self.assertTrue(TestParser.checkParser("var struct_var = Person{name: \"Alice\", age: 30};","successful", 210))
        
    def test_var_declaration_1(self):
        input = """
            var a int;
            var b float;
            var c string;
            var d bool;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 211))
        
    def test_var_declaration_2(self):
        input = """
            var a int = 1;
            var b float = 2.0;
            var c string = "string";
            var d bool = true;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 212))
        
    def test_var_declaration_3(self):
        """no type and initial value"""
        input = """
            var a, b int;
        """
        expect = "Error on line 2 col 18: ,"
        self.assertTrue(TestParser.checkParser(input, expect, 213))
    
    def test_var_declaration_4(self):
        #???
        input = """func main() {
            a := 0;
            a = 1;
            }
        """
        expect = "Error on line 3 col 15: ="
        self.assertTrue(TestParser.checkParser(input, expect, 214))   
    
    def test_var_declaration_5(self):
        """absence of rhs expression"""
        input = """
            var i int = ;
        """
        expect = "Error on line 2 col 25: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 215))
        
    #---------------FUNCTION DECLARATION----------------
        
    def test_method_declaration_1(self):
        """valid program with struct declaration and method"""
        input = """type Person struct {
                    name string;
                    age int;
                };
                func (p Person) greet() {
                    print("Hello, " + p.name);
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 216))
        
    def test_invalid_function_declaration(self):
        """invalid method declaration"""
        input = """func () {};"""
        expect = "Error on line 1 col 7: )"
        self.assertTrue(TestParser.checkParser(input, expect, 217))
        
    def test_invalid_function_declaration_2(self):
        """invalid nested function declaration"""
        input = """func main() {
                    func foo() {};
                };"""
        expect = "Error on line 2 col 21: func"
        self.assertTrue(TestParser.checkParser(input, expect, 218))
    
    def test_invalid_function_declaration_3(self):
        """Iinvalid function declaration without body"""
        input = """func main();"""
        expect = "Error on line 1 col 12: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 219))
        
    def test_invalid_function_declaration_4(self):
        """function declaration without body statement"""
        input = """func main() {};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 220))
        
    #----------------METHOD DECLARATION----------------
        
    def test_invalid_method_declaration(self):
        """invalid nested method declaration"""
        input = """func (p Person) main() {
                    func foo() {};
                };"""
        expect = "Error on line 2 col 21: func"
        self.assertTrue(TestParser.checkParser(input, expect, 221))
        
    def test_invalid_method_declaration_2(self):
        """method declaration without body statement"""
        #???
        input = """func (p Person) main() {};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 222))
        
    #----------------STRUCT DECLARATION----------------
    def test_struct_declaration(self):
        """struct declaration with methods"""
        input = """type Greeting struct {
                    name string;
                    message string;
                };
                func (p Person) greet() {
                    print("Hello, " + p.name);
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 223))
        
    def test_invalid_struct_declaration(self):
        """invalid struct declaration without identifier"""
        input = """type struct {};"""
        expect = "Error on line 1 col 6: struct"
        self.assertTrue(TestParser.checkParser(input, expect, 224))
        
    #----------------INTERFACE DECLARATION----------------
    def test_interface_declaration(self):
        """interface declaration with methods"""
        input = """type Greeting interface {
                    greet();
                    getName() string;
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 225))
        
    def test_invalid_interface_declaration(self):
        """Invalid interface declaration without identifier"""
        input = """type interface {};"""
        expect = "Error on line 1 col 6: interface"
        self.assertTrue(TestParser.checkParser(input, expect, 226))
        
    def test_invalid_interface_declaration_2(self):
        """Invalid interface declaration without body"""
        input = """type Greeting interface;"""
        expect = "Error on line 1 col 24: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 227))
        
    #----------------PROGRAM------------------
    def test_program_structure(self):
        """program with many declarations"""
        input = """
        var a float;
        const b = 1;
        var c int = 1;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 228))
        
    def test_program_structure_2(self):
        """func decl with return type"""
        input = """
        var a float;
        const b = 1;
        func Greeting() string {
            return "Hello";
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 229))
    
    def test_program_w_stm_1(self):
        """program with a statement"""
        input = """for a := 1 to 10 do {}"""
        expect = "Error on line 1 col 1: for"
        self.assertTrue(TestParser.checkParser(input, expect, 230))
        
    def test_program_w_stm_2(self):
        input = """
            var a int;
            for a := 1 to 5 do {}
        """
        expect = "Error on line 3 col 13: for"
        self.assertTrue(TestParser.checkParser(input, expect, 231))
        
    def test_program_w_stm_3(self):
        """Invalid program with if statement"""
        input = """if a == 1 then {}"""
        expect = "Error on line 1 col 1: if"
        self.assertTrue(TestParser.checkParser(input, expect, 232))
        
    def test_program_w_struct(self):
        input = """type a struct {
            message string;
            error_code int;
            };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 233))
        
    def test_program_w_struct_func(self):
        input = """type Greeting struct {
                    name string;
                    message string
                };
                func (p Person) greet() {
                    print(p.message + p.name + "!");
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 234))
        
    #----------------ARRAY-----------------
    def test_array_literal(self):
        """Array literal"""
        input = """const a = [2]int{1, "string"};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 235))
        
    def test_array_literal_2(self):
        """Multi-dimensional array literal"""
        input = """const a = [2][3]int{{1, "string", {2, 3}}, {4, 5, 6.5}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 236))
    
    #-----------------NIL LITERAL----------------
        
    def test_nil_literal(self):
        input = """const a = nil;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 237))
        
    #-----------------ARRAY ACCESS, METHOD CALL, STRUCT ACCESS----------------
    def test_array_access(self):
        """multi-dimensional array element expression"""
        input = """const a = b[0][1+2];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 238))
        
    def test_struct_access(self):
        input = """const a = b.name;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 239))
        
    def test_method_call(self):
        input = """const a = b.foo();"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 240))
        
    def test_method_call_2(self):
        """Array element expression with nested function call"""
        input = """const a = b[0].c();"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 241))

    def test_method_call_struct_access(self):
        input = """const a = d(b.c.foo());"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 242))
    
    # --------------EXPRESSION----------------
    def test_large_expression(self):
        input = """const a = b - c % d * e / f - g;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 243))
        
    def test_relational_logical_expression(self):
        input = """const a = b <= c > d && e || f;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 244))
        
    def test_expression_missing_rp(self):
        """Missing parentheses"""
        input = """const a = ((b - c) % d;"""
        expect = "Error on line 1 col 23: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 245))
    
    # -----------------ASSIGN STATEMENT----------------
    def test_assignment_statement(self):
        """Assignment with +=, -=, *=, /=, %= operator"""
        input = """func foo() {z:=a; z += b; z -= c; z *= d; z /= e; z %= f;};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 246))
    
    # ---------------- IF STATEMENT ----------------
    def test_if_statement_basic(self):
        """basic if statement"""
        input = """func main() {
            if (x > 10) {
                x := x - 1;
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 247))
        
    def test_if_statement_with_else(self):
        input = """func main() {
            if (x < 10) {
                x := x + 1;
            } else {
                x := x - 1;
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 248))
        
    def test_if_statement_with_else_if(self):
        """If statement with multiple else if"""
        input = """func main() {
            if (x == 10) {
                x := 0;
            } else if (x > 10) {
                x := 1;
            } else if (x < 10) {
                x := -1;
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 249))
        
    def test_if_statement_nested(self):
        input = """func main() {
            if (x > 10) {
                if (y < 5) {
                    y := y + 1;
                }
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 250))
    
    def test_if_statement_missing_condition(self):
        input = """func main() {
            if () {
                x := 10;
            }
        };"""
        expect = "Error on line 2 col 17: )"
        self.assertTrue(TestParser.checkParser(input, expect, 251))
        
    def test_if_statement_complex_condition(self):
        """if statement with complex condition"""
        input = """func main() {
            if (x > 10 && y < 5 || z == 0) {
                x := x + y;
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 252))
        
    def test_if_statement_wo_paren(self):
        """if statement with incorrect syntax"""
        input = """func main() {
            if x > 10 {
                x := x - 1;
            }
        };"""
        expect = "Error on line 2 col 16: x"
        self.assertTrue(TestParser.checkParser(input, expect, 253))
        
    def test_if_statement_incorrect_operator(self):
        """if statement with incorrect operator"""
        input = """func main() {
            if (x = 10) {
                x := x - 1;
            }
        };"""
        expect = "Error on line 2 col 19: ="
        self.assertTrue(TestParser.checkParser(input, expect, 254))
        
    # ---------------- FOR STATEMENT ----------------
    def test_for_statement_basic(self):
        input = """func main() {
            for i := 0; i < 10; i += 1 {
                print(i);
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 255))
        
    def test_for_statement_missing_init(self):
        """For statement with missing initialization"""
        input = """func main() {
            for ; i < 10; i += 1 {
                print(i);
            }
        };"""
        expect = "Error on line 2 col 17: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 256))
        
    def test_for_statement_missing_init_2(self):
        """For statement with missing initialization"""
        input = """func main() {
            for i < 10; i += 1 {
                print(i);
            }
        };"""
        expect = "Error on line 2 col 23: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 257))
        
    def test_for_statement_missing_update(self):
        input = """func main() {
            for i := 0; i < 10 {
                print(i);
            }
        };"""
        expect = "Error on line 2 col 32: {"
        self.assertTrue(TestParser.checkParser(input, expect, 258))
        
    def test_for_statement_complex_update(self):
        """For statement with complex update"""
        #???
        input = """func main() {
            for i := 0; i < 10; i = i * 2 + 1 {
                print(i);
            }
        };"""
        expect = "Error on line 2 col 35: ="
        self.assertTrue(TestParser.checkParser(input, expect, 259))
        
    def test_for_statement_range(self):
        """For statement with range"""
        input = """func main() {
            for i, value := range array {
                print(value);
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 260))
        
    def test_for_statement_underscore_range(self):
        """For statement with underscore in range"""
        input = """func main() {
            for _, value := range array {
                print(value);
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 261))
        
    def test_for_statement_invalid_condition(self):
        """For statement with invalid condition"""
        input = """func main() {
            for i := 0; i:=1; i += 1 {
                print(i);
            }
        };"""
        expect = "Error on line 2 col 26: :="
        self.assertTrue(TestParser.checkParser(input, expect, 262))
        
    def test_for_statement_missing_semicolon(self):
        """For statement with missing semicolon"""
        input = """func main() {
            for i := 0 i < 10; i += 1 {
                print(i);
            }
        };"""
        expect = "Error on line 2 col 24: i"
        self.assertTrue(TestParser.checkParser(input, expect, 263))
        
    def test_for_statement_with_break(self):
        """For statement with break"""
        input = """func main() {
            for i < 10 {
                if (i == 5) {
                    break;
                }
                print(i);
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 264))
        
    def test_for_statement_with_continue(self):
        """For statement with continue"""
        input = """func main() {
            for i, value := range array {
                if (i % 2 == 0) {
                    continue;
                }
                print(i);
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 265))
    
    def test_for_statement_invalid_range(self):
        """For statement with invalid range"""
        input = """func main() {
            for i, value := range {
                print(value);
            }
        };"""
        expect = "Error on line 2 col 35: {"
        self.assertTrue(TestParser.checkParser(input, expect, 266))
        
    #-----------------CONTINUE, BREAK, RETURN----------------------
        
    def test_continue(self):
        input = """func main() {
                for i < 10 {
                    a := continue;
                }
            };"""
        expect = "Error on line 3 col 26: continue"
        self.assertTrue(TestParser.checkParser(input, expect, 267))
        
    def test_break_2(self):
        input = """
                func Add() {
                    break a;
                }"""
        expect = "Error on line 3 col 27: a"
        self.assertTrue(TestParser.checkParser(input,expect, 295))
        
    def test_continue_2(self):
        input = """
                func Add() {
                    continue a;
                }"""
        expect = "Error on line 3 col 30: a"
        self.assertTrue(TestParser.checkParser(input,expect, 296))
        
    def test_return(self):
        #???
        input = """
                func foo() {
                    return a.b().e.f();
                }"""
        expect = "Error on line 4 col 18: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect, 297))
        
    #-----------------CALL STATEMET-----------------
    def test_call_statement(self):
        input = """func main() {
            a.foo().bar(b, c, d);
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 268))
        
    def test_call_statement_missing_rp(self):
        input = """func main() {
            a.foo().bar(b, c, d;
        };"""
        expect = "Error on line 2 col 32: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 269))
        
    def test_call_statement_missing_param(self):
        input = """func main() {
            a.foo().bar(b, c,);
        };"""
        expect = "Error on line 2 col 30: )"
        self.assertTrue(TestParser.checkParser(input, expect, 270))
        
    def test_call_statement_missing_param_2(self):
        input = """func main() {
            a.foo(,);
        };"""
        expect = "Error on line 2 col 19: ,"
        self.assertTrue(TestParser.checkParser(input, expect, 271))
        
    #-----------------BLOCK_STATEMENT-----------------
    def test_block_statement(self):
        """Block statement"""
        input = """func main() {
            if (a == 1) {
                a := 1;
                var b float = 2.0;
                const c = "string";
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 272))
        
    # ----------------- COMMENT ----------------
    def test_comment_4(self):
        """Single line of single line comment with newline"""
        input = """// This is a comment
        // This is another comment

        func main() {
            a := 1
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 273))
    
    # --------------MORE TESTCASES----------------
    def test_struct_assign(self):
        input = """
            var z Info = Info{name: "Alice", age: 20};
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 274))
        
    def test_for_statement_with_scalar(self):
        """For statement with non-scalar initialization"""
        input = """func main() {
            for b[ID] := 1; x < 10; x+=1 {
                x += 1;
            }
        };"""
        expect = "Error on line 2 col 23: :="
        self.assertTrue(TestParser.checkParser(input, expect, 275))
        
    def test_159(self):
        self.assertTrue(TestParser.checkParser("""
            func (p Person) Greet() string {
                for i := 0
                    i < 10
                    i += 1 {
                    return
                }
                for i := 0
                    i < 10
                    i += 1 
                {
                    return
                }
            };  
    ""","Error on line 10 col 29: ;", 276))
        
    def test_158(self):
        self.assertTrue(TestParser.checkParser("""
        type Person struct {
            func (p Person) Greet() string {
                return "Hello, " + p.name
            }; c c;
            func (p Person) Greet() string {
                return "Hello, " + p.name
            } c c;                                                    
        }      
        ""","Error on line 3 col 13: func", 277))
        
    def test_160(self):
        self.assertTrue(TestParser.checkParser("""
            func (p Person) Greet() string {
                if (1) {return;}
                else if (1)
                {}
            };  
        ""","Error on line 4 col 17: else", 278))
        
    def test_116(self):
        self.assertTrue(TestParser.checkParser("""
                                    func main() {
                                        if (x.foo().b[2]) {
                                            if (1){return; } else {return; }

                                        } else if(2) {return; 
                                        }
                                    };""","successful", 279))
        
    def test_100(self):
        #???
        self.assertTrue(TestParser.checkParser("""
            func Add() {
                                        }
        ""","successful", 280))
        
    def test_016(self):
        #???
        """interface with empty body"""
        self.assertTrue(TestParser.checkParser("""
            type Calculator interface {
                                        
                Add(x, y int) int;
                Subtract(a, b float, c int) [3]ID;
                Reset()
                                        
                SayHello(name string);
                                        
            }
            type MyInterface interface {}                                                                       
        ""","successful", 281))
        
    def test_143(self):
        self.assertTrue(TestParser.checkParser("""
                                    func main() {
                                        a[3][1].foo(5 + c, a {b:2})
                                    }""","Error on line 4 col 38: <EOF>", 282))
        
    def test_134(self):
        """only need exp as range array"""
        #???
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for index, value := range 23 {
                                        }
                                    };""","successful", 283))
        
    def test_missing_type_array(self):
        input = """var arr [] = {1,2,3};"""
        expect = "Error on line 1 col 10: ]"
        self.assertTrue(TestParser.checkParser(input,expect,284))
        
    def test_wrong_operator(self):
        """Using an invalid operator in expression"""
        input = """
        var x = 5 & 3;
        """
        expect = "&"
        self.assertTrue(TestParser.checkParser(input, expect, 285))
        
    def test_268(self):
        """assign_statement"""
        input = """    
            func khang() {
                x  := foo() + 3 / 4;
                x.c[2][4] := 1 + 2;                       
            }                                       
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 286))
        
    def test_for_statement_with_scalar_3(self):
        """For statement with non-scalar update"""
        input = """func main() {
            for i := 0; a[1]; i[1]+=1 {
                a := i;
            }
        };"""
        expect = "Error on line 2 col 32: ["
        self.assertTrue(TestParser.checkParser(input, expect, 287))
        
    def test_newline(self):
        input = """
                                        
            func (c c) Add(x int)  {return;}
            
            func Add(x int, y int) {return;}; var c int;
            
            var c int; type Calculator struct{a int;} type Calculator struct {} var c int;
        """
        expect = "Error on line 7 col 55: type"
        self.assertTrue(TestParser.checkParser(input, expect, 288))
        
        
    def test_for_statement_with_scalar_4(self):
        """For statement with non-scalar update: attribute assignment"""
        input = """func main() {
            for i := 0; i < 10; a.b += 1 {
                    a := i;
                }
            }"""
        expect = "Error on line 2 col 34: ."
        self.assertTrue(TestParser.checkParser(input, expect, 289))

    def test_for_statement_with_scalar_5(self):
        """For range statement with non-scalar index"""
        input = """func main() {
            for a[1], value := range a {
                a := value;
            }
        };"""
        expect = "Error on line 2 col 21: ,"
        self.assertTrue(TestParser.checkParser(input, expect, 290))
        
    def test_279(self):
        input = """
            func (c int) Add(x int) int {}
        """
        expect = "Error on line 2 col 21: int"
        self.assertTrue(TestParser.checkParser( input, expect, 291))
        
    def test_invalid_expression_9(self):
        """missing parameter after comma"""
        input = """const a = foo(a,);"""
        expect = "Error on line 1 col 17: )"
        self.assertTrue(TestParser.checkParser(input, expect, 292))
        
    def test_invalid_expression_7(self):
        """missing field"""
        input = """const a = b.;"""
        expect = "Error on line 1 col 13: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 293))
        
    def test_assignment(self):
        input = """
                func Add() {
                    a.foo() += 2;
                }"""
        expect = "Error on line 3 col 29: +="
        self.assertTrue(TestParser.checkParser(input,expect, 294))
        
    def test_complete_program(self):
        input = """
            func main() {
                var a int;
                a := 1;
                if (a > 0) {
                    print("a is positive");
                } else {
                    print("a is non-positive");
                }
                
                for i := 0; i < 10; i += 1 {
                    print(i);
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 298))
        
    def test_invalid_expression(self):
        """missing field - complex"""
        input = """const a = b.c[d].e().f.;"""
        expect = "Error on line 1 col 24: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 299))
        
    def test_comment_2(self):
        """multiple-line comment with newline"""
        input = """/* A multiple-line comment */

        func main() {
            /* Another multiple-line comment */
            var x = 2;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 300))
        
    def test_comment_3(self):
        """nested multiple-line comment"""
        input = """/* This is /* a nested */ comment*/
        func main() {
            /* This is /* a nested */ comment*/
            const a = "hello"
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 301))
        
    def test_negated_negative_num(self):
        input = """func main() {
            x := !-a == a.foo();
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 302))

    def test_negative_num_division(self):
        input = """func main() {
            x := -2 / -1;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 303))