import unittest
from TestUtils import TestParser
import inspect
class ParserSuite(unittest.TestCase):
    def test_001(self):
        """Literal"""
        self.assertTrue(TestParser.checkParser("const Votien = 1;","successful", inspect.stack()[0].function))

    def test_002(self):
        """Literal"""
        self.assertTrue(TestParser.checkParser("const Votien = true;","successful", inspect.stack()[0].function))

    def test_003(self):
        """Literal"""
        self.assertTrue(TestParser.checkParser("const Votien = [5][0]string{1, \"string\"};","successful", inspect.stack()[0].function))

    def test_004(self):
        """Literal"""
        self.assertTrue(TestParser.checkParser("const Votien = [1.]ID{1, 3};","Error on line 1 col 17: 1.", inspect.stack()[0].function))

    def test_005(self):
        """Literal"""
        self.assertTrue(TestParser.checkParser("const Votien = Person{name: \"Alice\", age: 30};","successful", inspect.stack()[0].function))

    def test_006(self):
        """expression"""
        self.assertTrue(TestParser.checkParser("const Votien = 1 || 2 && c + 3 / 2 - -1;","successful", inspect.stack()[0].function))

    def test_007(self):
        """expression"""
        self.assertTrue(TestParser.checkParser("const Votien = 1[2] + foo()[2] + ID[2].b.b;","successful", inspect.stack()[0].function))

    def test_008(self):
        """expression"""
        self.assertTrue(TestParser.checkParser("const Votien = ca.foo(132) + b.c[2];","successful", inspect.stack()[0].function))

    def test_009(self):
        """expression"""
        self.assertTrue(TestParser.checkParser("const Votien = a.a.foo();","successful", inspect.stack()[0].function))

    def test_010(self):
        """declared variables"""
        self.assertTrue(TestParser.checkParser("""
            var x int = foo() + 3 / 4;
            var y = "Hello" / 4;   
            var z str;
        ""","successful", inspect.stack()[0].function))

    def test_011(self):
        """declared constants"""
        self.assertTrue(TestParser.checkParser("""
            const VoTien = a.b() + 2;
        ""","successful", inspect.stack()[0].function))

    def test_012(self):
        """declared function"""
        self.assertTrue(TestParser.checkParser("""
            func VoTien(x int, y int) int {return;}
            func VoTien1() [2][3] ID {return;};        
            func VoTien2() {return;}                                       
        ""","successful", inspect.stack()[0].function))

    def test_013(self):
        """declared method"""
        self.assertTrue(TestParser.checkParser("""
            func (c Calculator) VoTien(x int) int {return;};  
            func (c Calculator) VoTien() ID {return;}      
            func (c Calculator) VoTien(x int, y [2]VoTien) {return;}                                                      
        ""","successful", inspect.stack()[0].function))

    def test_014(self):
        """declared struct"""
        self.assertTrue(TestParser.checkParser("""
            type VoTien struct {
                VoTien string ;
                VoTien [1][3]VoTien ;                     
            }                                                                     
        ""","successful", inspect.stack()[0].function))

    def test_015(self):
        """declared Interface"""
        self.assertTrue(TestParser.checkParser("""
            type VoTien struct {}                                                                       
        ""","successful", inspect.stack()[0].function))

    def test_016(self):
        """declared Interface"""
        self.assertTrue(TestParser.checkParser("""
            type Calculator interface {
                                        
                Add(x, y int) int;
                Subtract(a, b float, c int) [3]ID;
                Reset()
                                        
                SayHello(name string);
                                        
            }
            type VoTien interface {}                                                                       
        ""","successful", inspect.stack()[0].function))

    def test_017(self):
        """declared_statement"""
        self.assertTrue(TestParser.checkParser("""    
            func VoTien() {
                var x int = foo() + 3 / 4;
                var y = "Hello" / 4;   
                var z str;
                                        
                const VoTien = a.b() + 2;
            }                                       
        ""","successful", inspect.stack()[0].function))


    def test_018(self):
        """assign_statement"""
        self.assertTrue(TestParser.checkParser("""    
            func VoTien() {
                x  := foo() + 3 / 4;
                x.c[2][4] := 1 + 2;                       
            }                                       
        ""","successful", inspect.stack()[0].function))

    def test_019(self):
        """for_statement"""
        self.assertTrue(TestParser.checkParser("""    
            func VoTien() {
                if (x > 10) {return; } 
                if (x > 10) {
                  return; 
                } else if (x == 10) {
                    var z str;
                } else {
                    var z ID;
                }
            }
        ""","successful", inspect.stack()[0].function))

    def test_020(self):
        """if_statement"""
        self.assertTrue(TestParser.checkParser("""    
            func VoTien() {
                for i < 10 {return; }
                for i := 0; i < 10; i += 1 {return; }
                for index, value := range array {return; }
            }
        ""","successful", inspect.stack()[0].function))


    def test_021(self):
        """break and continue, return, Call  statement"""
        self.assertTrue(TestParser.checkParser("""    
            func VoTien() {                           
                for i < 10 {break;}
                break;
                continue;
                return 1;
                return
                foo(2 + x, 4 / y); m.goo();                        
             }
                                        
        ""","successful", inspect.stack()[0].function))
       
    def test_021(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            const a = 0b11;                         
        ""","successful", inspect.stack()[0].function))

    def test_025(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = [true]int{1};                         
        ""","Error on line 2 col 29: true", inspect.stack()[0].function))

    def test_031(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = ID {};                         
        ""","successful", inspect.stack()[0].function))

    def test_032(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = ID {a: 2, b: 2 + 2 + ID {a: 1}};                         
        ""","successful", inspect.stack()[0].function))

    def test_036(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = 1 && 2 && 3 || 1 || 1;                         
        ""","successful", inspect.stack()[0].function))
    
    def test_037(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a >= 2 <= "string" > a[2][3] < ID{A: 2} >= [2]S{2};                         
        ""","successful", inspect.stack()[0].function))

    def test_040(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a.b.a.c.e.g;                         
        ""","successful", inspect.stack()[0].function))

    def test_041(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a[2][3][a + 2];                         
        ""","successful", inspect.stack()[0].function))

    def test_045(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a.a.a[2].foo(1);                         
        ""","successful", inspect.stack()[0].function))

    def test_050(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = foo().a[2].goo();                         
        ""","successful", inspect.stack()[0].function))

    def test_053(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            const k = -a + -!-!c - ---[2]int{2};                         
        ""","successful", inspect.stack()[0].function))

    def test_064(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            var c [2][3]ID
        ""","successful", inspect.stack()[0].function))

    def test_067(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            const a =;
        ""","Error on line 2 col 22: ;", inspect.stack()[0].function))
        
    def test_069(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            func Add(x int, y [2]int) [2]id {return ;}
""","successful", inspect.stack()[0].function))
        
    def test_073(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            func Add() {return ;}
""","successful", inspect.stack()[0].function))
        
    def test_077(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator struct {
                                        
                value int;
                a [2]int; a [2]ID;
                c Calculator                    
            }
""","successful", inspect.stack()[0].function))
        
    def test_079(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator struct {
                a int = 2;       
            }
""","Error on line 3 col 23: =", inspect.stack()[0].function))
        
    def test_080(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator interface {
                Add(x, y [2]ID) [2]int;
                Subtract(a, b float, c, e int);
                Reset()
                SayHello(name string)
            }
""","successful", inspect.stack()[0].function))
        
    def test_081(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator interface {Reset()}
""","Error on line 2 col 47: }", inspect.stack()[0].function))
        
    def test_084(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator interface {
                Add(x int,c,d ID); Add()
        }
""","successful", inspect.stack()[0].function))
        
    def test_088(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            func Add(x int, y int) int  {return ;};
""","successful", inspect.stack()[0].function))
        
    def test_089(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
            func (c int) Add(x int) int {return ;}
""","Error on line 2 col 21: int", inspect.stack()[0].function))
        
    def test_099(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""

""","Error on line 3 col 1: <EOF>", inspect.stack()[0].function))

    def test_102(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                         var a int;      
                                    };""","successful", inspect.stack()[0].function))
        
    def test_103(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                         var a = a[2].b;      
                                    };""","successful", inspect.stack()[0].function))

    def test_107(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        a += 2;
                                        a -= a[2].b();
                                        a /= 2
                                        a *= 2
                                        a %= 2;       
                                    };""","successful", inspect.stack()[0].function))

    def test_109(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        a.c[2].e[3].k += 2;       
                                    };""","successful", inspect.stack()[0].function))

    def test_110(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        a.foo() += 2;       
                                    };""","Error on line 3 col 49: +=", inspect.stack()[0].function))

    def test_113(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                       a[2+3&&2] += foo().b[2];       
                                    };""","successful", inspect.stack()[0].function))
        
    def test_114(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        if (x.foo().b[2]) {
                                            a := 2;
                                        } else if (a && b) {
                                            return; 
                                        } else {
                                            a := 2;
                                        }   
                                    };""","successful", inspect.stack()[0].function))

    def test_120(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for true + 2 + foo().b {return; }
                                    };""","successful", inspect.stack()[0].function))
   
    def test_123(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for i := 0; i < 10; i += 1 {
                                           return; 
                                        }
                                    };""","successful", inspect.stack()[0].function))
    
    def test_134(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for index, value := range 23 {return; 
                                        }
                                    };""","successful", inspect.stack()[0].function))
        
    def test_136(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        break;
                                        continue
                                        break; continue; break
                                    };""","successful", inspect.stack()[0].function))
        
    def test_137(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        return
                                        return 2 + a[2].b()
                                        return; return a
                                    };""","successful", inspect.stack()[0].function))
        
    def test_141(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        a.foo(2 + 3, a {a:2})
                                        foo(2 + 3, a {a:2});
                                    };""","successful", inspect.stack()[0].function))
        
    def test_143(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        a[2][3].foo(2 + 3, a {a:2})
                                    };""","successful", inspect.stack()[0].function))
        
    def test_152(self):
        """array_literal"""
        self.assertTrue(TestParser.checkParser("""const a = [1]int{{1, 0x1}, ID{}, {{ID{}}}}                    
""","successful", inspect.stack()[0].function))
        
    def test_179(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for var b [2]ID = 1 + 2 / 4; foo().a.b(); i := 1 {
                                            return; 
                                        }
                                    };""","successful", inspect.stack()[0].function))

    def test_180(self):
        self.assertTrue(TestParser.checkParser("""
                                            const a = [ID][2][VT]int{{{1}}}                              
                                        ""","successful", inspect.stack()[0].function))

    def test_181(self):
        self.assertTrue(TestParser.checkParser("""
                                            var a;
                                        ""","Error on line 2 col 50: ;", inspect.stack()[0].function))
    def test_182(self):
        self.assertTrue(TestParser.checkParser("""
                                            var a = {1, 2};
                                        ""","Error on line 2 col 53: {", inspect.stack()[0].function))