"""
 * Initial code for Assignment
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/profile.php?id=100056605580171
 * Link Group : https://www.facebook.com/groups/211867931379013
 * Date: 02.04.2024
"""
import unittest
from TestUtils import TestCodeGen
import inspect
from AST import *

"""
    (cd java_byte_code/test_001 && 
    java  -jar ../jasmin.jar MiniGoClass.j && 
    java -cp ../_io:. MiniGoClass)
"""
class CodeGenSuite(unittest.TestCase):

    def test_001(self):
        input = """
func fvoid() {putStringLn("VoTien");}

var global = fint()
func main() {
    fvoid();
    putFloatLn(global + 2.0)

    var local = "a";
    putBoolLn(local <= "b")
    local += "c"
    putStringLn(local)

};

func fint() int {return 1;}
"""
        self.assertTrue(TestCodeGen.test(input,"VoTien\n3.0\ntrue\nac\n",inspect.stack()[0].function))

    def test_002(self):
        input = """
func main() {putInt(5);};
"""
        self.assertTrue(TestCodeGen.test(input,"5",inspect.stack()[0].function))

    def test_010(self):
        input = """
func main() {
    var a float = 3.0;
    putFloat(1 + a)
}
"""
        self.assertTrue(TestCodeGen.test(input,"4.0",inspect.stack()[0].function))

    def test_016(self):
        input = """
func main() {
    putIntLn(5 % 2)
    putIntLn(2 % 5)
}
"""
        self.assertTrue(TestCodeGen.test(input,"1\n2\n",inspect.stack()[0].function))

    def test_019(self):
        input = """
func main() {
    putBoolLn(5.0 > 2.0)
    putBoolLn(5.0 < 2.0)
    putBoolLn(5.0 <= 5.0)
    putBoolLn(5.0 >= 5.0)
    putBoolLn(5.0 == 5.0)
    putBoolLn(5.0 != 5.0)
}
"""
        self.assertTrue(TestCodeGen.test(input,"true\nfalse\ntrue\ntrue\ntrue\nfalse\n",inspect.stack()[0].function))

    def test_020(self):
        input = """
func main() {
    putBoolLn("apple" > "banana")     // False
    putBoolLn("apple" < "banana")     // True
    putBoolLn("apple" <= "apple")     // True
    putBoolLn("banana" >= "apple")    // True
    putBoolLn("hello" == "hello")     // True
    putBoolLn("hello" != "hello")     // False
}
"""
        self.assertTrue(TestCodeGen.test(input,"false\ntrue\ntrue\ntrue\ntrue\nfalse\n",inspect.stack()[0].function))

    def test_049(self):
        input = """
var a float = 3;
func main() {
    putFloatLn(a)
    var a float = 4;
    putFloatLn(a)
    a := 2
    putFloat(a)
}
"""
        self.assertTrue(TestCodeGen.test(input,"3.0\n4.0\n2.0",inspect.stack()[0].function))

    def test_053(self):
        input = """
func main() {
    var a [2] int = [2] int {10, 20};
    putInt(a[0])
}
"""
        self.assertTrue(TestCodeGen.test(input,"10",inspect.stack()[0].function))

