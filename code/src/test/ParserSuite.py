import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_201(self):
        """Literal int"""
        input = "const Dk = 1;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 201))

    def test_202(self):
        """Literal boolean true"""
        input = "const Dk = true;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser( input,expect, 202))
    
    def test_203(self):
        """Literal boolean false"""
        input = "const Dk = false;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser( input,expect, 203))
        
    def test_204(self):
        """Literal nil"""
        input = "const Dk = foo(1+1);"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 204))
        
    def test_205(self):
        """Literal float"""
        input = "const Dk = 10.12;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 205))
        
    def test_206(self):
        """Literal array"""
        input = "const Dk = [5][0]string{1, \"string\"};"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input , expect, 206))

    def test_207(self):
        """Literal array with nest element"""
        input = "const Dk = [5][5]string{1, \"string\", {1.21, \"khang\"}, {3}};"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input , expect, 207))
        
    def test_208(self):
        """Literal array with index is constant"""
        input = """ const Dk = [ID1][ID2]int{{1, \"string\", {21}}, {1.21, \"khang\"}}; """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input , expect, 208))
        
    def test_209(self):
        """Literal array with element type is composit"""
        input = "const Dk = [ID1][ID2]ID3{1, \"string\", {1.21, \"khang\"}};"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input , expect, 209))
        
    def test_210(self):
        """Literal array index is not int_lit"""
        input = "const Dk = [10.]ID{2, 3};"
        expect = "Error on line 1 col 13: 10."
        self.assertTrue(TestParser.checkParser(input, expect, 210))
        
    def test_211(self):
        """Literal array index is not int_lit"""
        input = "const Dk = [true]ID{2, 3};"
        expect = "Error on line 1 col 13: true"
        self.assertTrue(TestParser.checkParser(input, expect, 211))
        
    def test_212(self):
        input = """const a = [1]int{1+1}"""
        expect = "Error on line 1 col 19: +"
        self.assertTrue(TestParser.checkParser(input , expect, 212))
        
    def test_213(self):
        """Literal array index is expression"""
        input = "const Dk = [1+2+3]ID3{1, \"string\", {1.21, \"khang\"}};"
        expect = "Error on line 1 col 14: +"
        self.assertTrue(TestParser.checkParser(input , expect, 213))
        
    def test_214(self):
        """Literal array empty element"""
        input = "const Dk = [14]float{};"
        expect = "Error on line 1 col 22: }"
        self.assertTrue(TestParser.checkParser(input, expect, 214))
        
    def test_215(self):
        """Literal array not comma separator"""
        input = "const Dk = [5][0]string{1 \"string\" 3};"
        expect = "Error on line 1 col 27: \"string\""
        self.assertTrue(TestParser.checkParser(input , expect, 215))
        
    def test_216(self):
        """Literal array not in curly braces"""
        input = "const Dk = [5][0]string(1, \"string\", 3);"
        expect = "Error on line 1 col 24: ("
        self.assertTrue(TestParser.checkParser(input , expect, 216))
        
    def test_217(self):
        """Literal array not type element"""
        input = "const Dk = [5][0]{1, \"string\", 3};"
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.checkParser(input , expect, 217))
    
    def test_218(self):
        """Literal array omit curly braces"""
        input = "const Dk = [5][0]{1, \"string\", 3;"
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.checkParser(input , expect, 218))
        
    def test_219(self):
        """Literal struct"""
        input = "const Dk = Person{name: \"Alice\", age: 30};"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 219))
    
    def test_220(self):
        """Literal struct not comma-separator"""
        input = "const Dk = DUYKHANG{name: \"khang\" age: 21};"
        expect = "Error on line 1 col 35: age"
        self.assertTrue(TestParser.checkParser(input, expect, 220))
             
    def test_221(self):
        """Literal struct comma-separator at tail"""
        input = "const Dk = DUYKHANG{name: \"khang\", age: 21, school: \"hcmut\",};"
        expect = "Error on line 1 col 61: }"
        self.assertTrue(TestParser.checkParser(input, expect, 221))
    
    def test_222(self):
        """Literal struct not colon between field name and expression"""
        input = "const Dk = DUYKHANG{name \"khang\"};"
        expect = "Error on line 1 col 26: khang"
        self.assertTrue(TestParser.checkParser(input, expect, 222))
        
    def test_223(self):
        """Literal struct omit curly braces"""
        input = "const Dk = DUYKHANG{name: \"khang\";"
        expect = "Error on line 1 col 34: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 223))
    
    def test_224(self):
        """Literal struct empty element"""
        input = "const Dk = DUYKHANG{};"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 224))
    
    def test_225(self):
        """Literal struct not in curly braces"""
        input = "const Dk = DUYKHANG(name: , age: 21);"
        expect = "Error on line 1 col 25: :"
        self.assertTrue(TestParser.checkParser(input, expect, 225))
    
    def test_226(self):
        """Literal struct not expression"""
        input = "const Dk = DUYKHANG{name: };"
        expect = "Error on line 1 col 27: }"
        self.assertTrue(TestParser.checkParser(input, expect, 226))
        
    def test_227(self):
        """Literal struct not field name"""
        input = "const Dk = DUYKHANG{\"khang\"};"
        expect = "Error on line 1 col 21: khang"
        self.assertTrue(TestParser.checkParser(input, expect, 227))
        
    def test_228(self):
        """Literal array not dimension"""
        input = "const Dk = int{\"khang\"};"
        expect = "Error on line 1 col 12: int"
        self.assertTrue(TestParser.checkParser(input, expect, 228))
            
    def test_229(self):
        """expression Arithmetic operator"""
        input = "const Dk = 2 + 2 - 2 * 2 / 2 % 2;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 229))
        
    def test_229(self):
        """expression contain not a Arithmetic operator"""
        input = "const Dk = 2 + 2 - 2 ** 2 // 2 % 2;"
        expect = "Error on line 1 col 23: *"
        self.assertTrue(TestParser.checkParser(input,expect, 229))
        
    def test_230(self):
        """expression Relational operator"""
        input = "const Dk = 2 == 2 != 2 > 2 < 2 >= 2 <= 2;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 230))
        
    def test_231(self):
        """expression Boolean operators"""
        input = "const Dk = !3 && 3 || 3 && !!3 ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 231))
        
    def test_232(self):
        """expression access array"""
        input = "const Dk = a[3];"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 232))
        
    def test_233(self):
        """expression access array multi dimension"""
        input = "const Dk = a[3][2];"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 233))
        
    def test_234(self):
        """Expressions access array, index is a expression"""
        input = "var z khang = a[2][3][a + 2 / d && true];"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 201))
        
    def test_235(self):
        """Expressions access array fail"""
        input = "var z khang = a[2, 3]; "
        expect = "Error on line 1 col 18: ,"
        self.assertTrue(TestParser.checkParser(input,expect, 235))
        
    def test_236(self):
        """Expressions access struct field"""
        input = " var z DK = khang.name;" 
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 236))
        
    def test_237(self):
        """Expressions access multi struct field"""
        input = " var z DK = khang.name.first_name;" 
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 237))
        
    def test_238(self):
        """Expressions access struct field fail"""
        input = " var z DK = khang..name;" 
        expect = "Error on line 1 col 19: ."
        self.assertTrue(TestParser.checkParser(input,expect, 238))
        
    def test_239(self):
        """Expressions access struct field fail"""
        input = " var z DK = khang.1;" 
        expect = "Error on line 1 col 19: 1"
        self.assertTrue(TestParser.checkParser(input,expect, 239))
           
    def test_240(self):
        """Expressions function call with no argument"""
        input = " var z DK = add();" 
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 240))
        
    def test_241(self):
        """Expressions function call with expression argument"""
        input = " var z DK = add(1+3, 2/4, a[3][2]);" 
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 241))
        
    def test_242(self):
        """Expressions function call with not comma-separator argument"""
        input = " var z DK = add(3 a);" 
        expect = "Error on line 1 col 19: a"
        self.assertTrue(TestParser.checkParser(input,expect, 242))
        
    def test_243(self):
        """Expressions function call with argument"""
        input = " var z DK = add(a, c, 2);" 
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 243))
        
    def test_244(self):
        """Expressions method call"""
        input = " var z DK = add(3, a);" 
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 244))
    
    def test_245(self):
        """Expressions method call"""
        input = " var z DK = add();" 
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 245))
         
    def test_246(self):
        """expression"""
        input = "const Dk = 1 || 2 && c + 3 / 2 - -1;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 246))

    def test_247(self):
        """expression"""
        input = "const Dk = 1[2] + foo()[2] + ID[2].b.b;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))

    def test_248(self):
        """expression"""
        input = "const Dk = ca.foo(132) + b.c[2];"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,"successful", 248))

    def test_249(self):
        """expression"""
        input = "const Dk = a.a.foo();"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 249))
        
    def test_250(self):
        """Expressions"""
        input = "var z TDK = ID {a: 2, b: 2 + 2 + ID {a: 2}};"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 250))
        
        
    def test_251(self):
        """Expressions"""
        input = "var z khang = a >= 2 <= \"string\" > a[2][3] < ID{A: 2} >= [2]S{2};"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 251))
        
        
    def test_252(self):
        """Expressions"""
        input = "var z khang = a.a.a[2].foo();"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 252))
    
    
    def test_253(self):
        """Expressions"""
        input = "var z khang = a.a.a[2].c[2].foo(1,);"
        expect = "Error on line 1 col 35: )"
        self.assertTrue(TestParser.checkParser(input, expect, 253))
        
    def test_254(self):
        """Expressions"""
        input = "var z khang = !a.a.a[2].c[2].foo(1, ID{A: 2});"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 254))
        
    def test_255(self):
        """Expressions"""
        input = "var z khang = KHANG {name: NAME{firt_name: \"duy\", last_name: \"khang\"}, age: a[2][3]};"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 255))
    

    def test_256(self):
        """declared variables"""
        input = """
            var x int = foo() + 3 / 4;
            var y = "Hello" / 4
            var z str;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input ,expect, 256))

    def test_257(self):
        """declared constants"""
        input = "const khang = a.b() + 2;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 257))
        
    def test_258(self):
        input = """
            func (c c) Add(x, c int) {return ;}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input ,expect, 258))
    
    def test_259(self):
        """declared constants miss ;"""
        input = "const khang = a.b() + 2"
        expect = "Error on line 1 col 24: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 259))
        
    def test_260(self):
        """declared variables fail"""
        input = "var y;"
        expect = "Error on line 1 col 6: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 260))
    
    def test_261(self):
        """declared variables fail"""
        input = "var float;"
        expect = "Error on line 1 col 5: float"
        self.assertTrue(TestParser.checkParser(input, expect, 261))
        
#     def test_262(self):
#         input = """
#         type Person struct {
#             func (p Person) Greet() string {
#                 return "Hello, " + p.name
#             }; c c;
#             func (p Person) Greet() string {
#                 return "Hello, " + p.name
#             } c c;                                                    
#         }      
# """
#         expect = "Error on line 8 col 15: c"
#         self.assertTrue(TestParser.checkParser(input,expect,262))

    def test_263(self):
        input = """func foo () {
        };"""
        expect = "Error on line 2 col 9: }"
        self.assertTrue(TestParser.checkParser(input,expect,263))
    
    def test_264(self):
        """Miss ) void main( {}"""
        input = """func main({};"""
        expect = "Error on line 1 col 11: {"
        self.assertTrue(TestParser.checkParser(input,expect,264))
        
    
    def test_265(self):
        """declared function"""
        input = """
            func khang(x int, y int) int {}
            func khang1() [2][3] ID {}
            func khang2() {}                                       
        """
        expect = "Error on line 2 col 43: }"
        self.assertTrue(TestParser.checkParser(input,expect, 265))

    def test_266(self):
        """declared method"""
        input = """
            func (c Calculator) khang(x int) int {return;}  
            func (c Calculator) khang() ID {return;};
            func (c Calculator) khang(x int, y [2]khang) {return;}                                                      
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 266))

    def test_267(self):
        """declared struct"""
        input = """
            type khang struct {
                khang string ;
                khang [1][3]khang ;                     
            }                                                                     
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 267))

    def test_268(self):
        """assign_statement"""
        input = """    
            func khang() {
                x  := foo() + 3 / 4;
                x.c[2][4] := 1 + 2;                       
            }                                       
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 268))
        

    def test_269(self):
        """declared Interface"""
        input = """
            type Calculator interface {
                                        
                Add(x, y int) int;
                Subtract(a, b float, c int) [3]ID;
                Reset()
                                        
                SayHello(name string);
                                        
            }
            type khang interface {}                                                                       
        """
        expect = "Error on line 11 col 35: }"
        self.assertTrue(TestParser.checkParser(input, expect, 269))


    def test_270(self):
        """declared_statement"""
        input = """    
            func khang() {
                var x int = foo() + 3 / 4;
                var y = "Hello" / 4;   
                var z str;
                                        
                const khang = a.b() + 2;
            }                                       
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 270))

    
    def test_271(self):
        """if_statement"""
        input = """    
            func khang() {
                if (x > 10) {return;} 
                if (x > 10) {
                  return;
                } else if (x == 10) {
                    var z str;
                } else {
                    var z ID;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 271))

    def test_272(self):
        """for_statement"""
        input = """    
            func khang() {
                for i < 10 {return;}
                for i := 0; i < 10; i += 1 {return;}
                for index, value := range array {return;}
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input ,expect, 272))


    def test_273(self):
        """break and continue, return, Call  statement"""
        input = """    
            func khang() {                           
                for i < 10 {break;}
                break;
                continue;
                return 1;
                return
                foo(2 + x, 4 / y); m.goo();                        
             }
                                        
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser( input, expect, 273))
    
         
    def test_274(self):
        """Declared"""
        input = """    
            func Add(a) [2]id {}
        """
        expect = "Error on line 2 col 23: )"
        self.assertTrue(TestParser.checkParser( input, expect, 274))     

    def test_275(self):
        """Declared"""
        input = """    
            type Calculator interface {
                Add(x, y [2]ID) [2]int;
                Subtract(a, b float, c, e int);
                Reset()
                SayHello(name string)
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser( input, expect, 275))
        
    def test_276(self):
        """Declared"""
        input = """
            type Calculator interface { Subtract(a int); }
            type Person struct {a int;}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 276))
        
    def test_277(self):
        """Declared"""
        input = """
                                        
            func (c c) Add(x int)  {return;}
            
            func Add(x int, y int) {return;}; var c int;
            
            var c int; type Calculator struct{a int;} type Calculator struct {} var c int;
        """
        expect = "Error on line 7 col 55: type"
        self.assertTrue(TestParser.checkParser(input, expect, 277))
        
    def test_278(self):
        """Declared"""
        input = """
            func Add(x int, y int) int  {return;};
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser( input, expect, 278))
    
    def test_279(self):
        """Declared"""
        input = """
            func (c int) Add(x int) int {}
        """
        expect = "Error on line 2 col 21: int"
        self.assertTrue(TestParser.checkParser( input, expect, 279))
    
    def test_280(self):
        """Declared"""
        input = """    
            func (c c) Add(x, c int) {}
        """
        expect = "Error on line 2 col 39: }"
        self.assertTrue(TestParser.checkParser( input, expect, 280))
        
    def test_281(self):
        """Declared"""
        input = """    
            const a = 2 func (c c) Add(x int) {}
        """
        expect = "Error on line 2 col 25: func"
        self.assertTrue(TestParser.checkParser( input, expect, 281))
        
    def test_282(self):
        """Statement"""
        input = """
                func Add() {
                    const a = a[2].b
                    var a = a[2].b; var a = "s";           
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 282))
        
    def test_283(self):
        """Statement"""
        input ="""
                func Add() {
                    a += 2;
                    a -= a[2].b();
                    a /= 2
                    a *= 2
                    a %= 2;         
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input ,expect, 283))
        
    def test_284(self):
        """Statement"""
        input = """
                                    func Add() {
                                        a[2].b := 2;          
                                    };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 284))
        
    def test_285(self):
        """Statement"""
        input = """
                                    func Add() {
                                        a.foo() += 2;
                                    }"""
        expect = "Error on line 3 col 49: +="
        self.assertTrue(TestParser.checkParser(input,expect, 285))
    
    def test_286(self):
        """Statement !!!(maybe I am true)"""
        input = """
                                    func Add() {
                                        2[1] + 2 += 2;     
                                    }"""
        expect = "Error on line 3 col 41: 2"
        self.assertTrue(TestParser.checkParser(input,expect, 286))
    
    
    def test_287(self):
        """Statement"""
        input = """
                                    func Add() {
                                       a[2+3&&2] += foo().b[2];       
                                    };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 287))
        
    def test_288(self):
        """Statement"""
        input = """
                                    func Add() {
                                        if (x.foo().b[2]) {
                                            if (){}
                                        }
                                    };"""
        expect = "Error on line 4 col 49: )"
        self.assertTrue(TestParser.checkParser(input, expect, 288))
        
    def test_289(self):
        """Statement"""
        input = """
                                    func Add() {
                                        for var i = 0; i < 10; i += 1 {
                                            // loop body
                                            break;
                                        }
                                    };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 289))
        
    def test_290(self):
        """Statement"""
        input = """
                                    func Add() {
                                        for var i [2]int = 0; foo().a.b(); i[3] := 1 {
                                            // loop body
                                            break;
                                        }
                                    };"""
        expect = "Error on line 3 col 77: ["
        self.assertTrue(TestParser.checkParser(input,expect, 290))
        
    def test_291(self):
        """Statement"""
        input = """
                                    func Add() {
                                        for index[2], value := range arr {
                                        // index: 0, 1, 2
                                        // value: 10, 20, 30
                                        }
                                    }"""
        expect = "Error on line 3 col 53: ,"
        self.assertTrue(TestParser.checkParser(input, expect, 291))
    
    def test_292(self):
        """Statement"""
        input = """
                                    func Add() {
                                        for index, value := range arr[2] {
                                            break;
                                        }
                                    };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 292))
    
    def test_293(self):
        """Statement"""
        input = """
                                    func Add() {
                                        for index, value := range 23 {
                                            break;
                                        }
                                    };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 293))
    
    def test_294(self):
        """Statement"""
        input ="""
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
"""
        expect = "Error on line 10 col 29: ;"
        self.assertTrue(TestParser.checkParser(input,expect, 294)) 
    
    def test_295(self):
        """Statement"""
        input = """
                                    func Add() {
                                        a[2][3].foo(2 + 3, a {a:2})
                                    };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 295))
    
    def test_296(self):
        """Statement"""
        input = """
                                    func Add() {
                                        return (2 + 3).b
                                        return -1.c
                                    }"""
        expect = "Error on line 4 col 51: c"
        self.assertTrue(TestParser.checkParser(input, expect, 296))
        
    def test_297(self):
        """Statement"""
        input = """
                                    func Add() {
                                        if (1) {return;}
                                        else if(2) {return string}
                                        else if(3) {reutrn int;}
                                    }"""
        expect = "Error on line 4 col 41: else"
        self.assertTrue(TestParser.checkParser(input,expect, 297))
        
        
    def test_298(self):
        """Expression"""
        input = """const a = (-1).c;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 298))
    
    def test_299(self):
        """Statement"""
        input = """
                                    func Add() {
                                        if (x.foo().b[2]) {
                                            if (1){return; } else {return; }

                                        } else if(2) {return; 
                                        }
                                    };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 299))
        
    def test_300(self):
        """Statement"""
        input = """
            func (p Person) Greet() string {
                if (1) {return;}
                else if (1)
                {}
            };  
"""
        expect = "Error on line 4 col 17: else"
        self.assertTrue(TestParser.checkParser( input,expect, 300))

       
    