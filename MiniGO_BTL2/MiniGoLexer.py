# Generated from main/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


# 2210458
from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u01df\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\3\2\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3#\3")
        buf.write("$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3")
        buf.write("*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3")
        buf.write("\62\3\62\3\63\3\63\3\64\3\64\3\65\5\65\u0150\n\65\3\65")
        buf.write("\3\65\3\65\3\66\3\66\7\66\u0157\n\66\f\66\16\66\u015a")
        buf.write("\13\66\3\67\3\67\3\67\7\67\u015f\n\67\f\67\16\67\u0162")
        buf.write("\13\67\5\67\u0164\n\67\38\38\38\68\u0169\n8\r8\168\u016a")
        buf.write("\39\39\39\69\u0170\n9\r9\169\u0171\3:\3:\3:\6:\u0177\n")
        buf.write(":\r:\16:\u0178\3;\6;\u017c\n;\r;\16;\u017d\3<\3<\7<\u0182")
        buf.write("\n<\f<\16<\u0185\13<\3=\3=\5=\u0189\n=\3=\3=\3>\3>\3>")
        buf.write("\5>\u0190\n>\3?\3?\3?\5?\u0195\n?\3@\3@\7@\u0199\n@\f")
        buf.write("@\16@\u019c\13@\3@\3@\3A\6A\u01a1\nA\rA\16A\u01a2\3A\3")
        buf.write("A\3B\3B\3B\3B\7B\u01ab\nB\fB\16B\u01ae\13B\3B\3B\3C\3")
        buf.write("C\3C\3C\3C\3C\7C\u01b8\nC\fC\16C\u01bb\13C\3C\3C\3C\3")
        buf.write("C\3C\3D\3D\7D\u01c4\nD\fD\16D\u01c7\13D\3D\3D\3D\5D\u01cc")
        buf.write("\nD\3D\3D\3E\3E\7E\u01d2\nE\fE\16E\u01d5\13E\3E\3E\3E")
        buf.write("\3F\3F\3F\3G\3G\3G\3\u01b9\2H\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22")
        buf.write("#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\35")
        buf.write("9\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62")
        buf.write("c\63e\64g\65i\66k\67m8o9q:s;u\2w\2y\2{<}\2\177=\u0081")
        buf.write(">\u0083?\u0085@\u0087A\u0089B\u008b\2\u008dC\3\2\23\5")
        buf.write("\2C\\aac|\6\2\62;C\\aac|\3\2\63;\3\2\62;\4\2DDdd\3\2\62")
        buf.write("\63\4\2QQqq\3\2\629\4\2ZZzz\5\2\62;CHch\4\2GGgg\4\2--")
        buf.write("//\6\2\f\f\17\17$$^^\7\2$$^^ppttvv\5\2\13\13\16\17\"\"")
        buf.write("\4\2\f\f\17\17\3\3\f\f\2\u01ee\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2")
        buf.write("\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3")
        buf.write("\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2")
        buf.write("\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3")
        buf.write("\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E")
        buf.write("\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2")
        buf.write("O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2")
        buf.write("\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2")
        buf.write("\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2")
        buf.write("\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2{\3")
        buf.write("\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2")
        buf.write("\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\3\u008f\3\2\2\2\5\u0092\3\2\2\2\7\u0097\3\2\2")
        buf.write("\2\t\u009b\3\2\2\2\13\u00a2\3\2\2\2\r\u00a7\3\2\2\2\17")
        buf.write("\u00ac\3\2\2\2\21\u00b3\3\2\2\2\23\u00bd\3\2\2\2\25\u00c4")
        buf.write("\3\2\2\2\27\u00c8\3\2\2\2\31\u00ce\3\2\2\2\33\u00d6\3")
        buf.write("\2\2\2\35\u00dc\3\2\2\2\37\u00e0\3\2\2\2!\u00e9\3\2\2")
        buf.write("\2#\u00ef\3\2\2\2%\u00f5\3\2\2\2\'\u00f9\3\2\2\2)\u00fe")
        buf.write("\3\2\2\2+\u0104\3\2\2\2-\u0106\3\2\2\2/\u0108\3\2\2\2")
        buf.write("\61\u010a\3\2\2\2\63\u010c\3\2\2\2\65\u010e\3\2\2\2\67")
        buf.write("\u0111\3\2\2\29\u0114\3\2\2\2;\u0117\3\2\2\2=\u011a\3")
        buf.write("\2\2\2?\u011d\3\2\2\2A\u0120\3\2\2\2C\u0122\3\2\2\2E\u0125")
        buf.write("\3\2\2\2G\u0128\3\2\2\2I\u012a\3\2\2\2K\u012d\3\2\2\2")
        buf.write("M\u0130\3\2\2\2O\u0132\3\2\2\2Q\u0135\3\2\2\2S\u0137\3")
        buf.write("\2\2\2U\u013a\3\2\2\2W\u013c\3\2\2\2Y\u013e\3\2\2\2[\u0140")
        buf.write("\3\2\2\2]\u0142\3\2\2\2_\u0144\3\2\2\2a\u0146\3\2\2\2")
        buf.write("c\u0148\3\2\2\2e\u014a\3\2\2\2g\u014c\3\2\2\2i\u014f\3")
        buf.write("\2\2\2k\u0154\3\2\2\2m\u0163\3\2\2\2o\u0165\3\2\2\2q\u016c")
        buf.write("\3\2\2\2s\u0173\3\2\2\2u\u017b\3\2\2\2w\u017f\3\2\2\2")
        buf.write("y\u0186\3\2\2\2{\u018c\3\2\2\2}\u0194\3\2\2\2\177\u0196")
        buf.write("\3\2\2\2\u0081\u01a0\3\2\2\2\u0083\u01a6\3\2\2\2\u0085")
        buf.write("\u01b1\3\2\2\2\u0087\u01c1\3\2\2\2\u0089\u01cf\3\2\2\2")
        buf.write("\u008b\u01d9\3\2\2\2\u008d\u01dc\3\2\2\2\u008f\u0090\7")
        buf.write("k\2\2\u0090\u0091\7h\2\2\u0091\4\3\2\2\2\u0092\u0093\7")
        buf.write("g\2\2\u0093\u0094\7n\2\2\u0094\u0095\7u\2\2\u0095\u0096")
        buf.write("\7g\2\2\u0096\6\3\2\2\2\u0097\u0098\7h\2\2\u0098\u0099")
        buf.write("\7q\2\2\u0099\u009a\7t\2\2\u009a\b\3\2\2\2\u009b\u009c")
        buf.write("\7t\2\2\u009c\u009d\7g\2\2\u009d\u009e\7v\2\2\u009e\u009f")
        buf.write("\7w\2\2\u009f\u00a0\7t\2\2\u00a0\u00a1\7p\2\2\u00a1\n")
        buf.write("\3\2\2\2\u00a2\u00a3\7h\2\2\u00a3\u00a4\7w\2\2\u00a4\u00a5")
        buf.write("\7p\2\2\u00a5\u00a6\7e\2\2\u00a6\f\3\2\2\2\u00a7\u00a8")
        buf.write("\7v\2\2\u00a8\u00a9\7{\2\2\u00a9\u00aa\7r\2\2\u00aa\u00ab")
        buf.write("\7g\2\2\u00ab\16\3\2\2\2\u00ac\u00ad\7u\2\2\u00ad\u00ae")
        buf.write("\7v\2\2\u00ae\u00af\7t\2\2\u00af\u00b0\7w\2\2\u00b0\u00b1")
        buf.write("\7e\2\2\u00b1\u00b2\7v\2\2\u00b2\20\3\2\2\2\u00b3\u00b4")
        buf.write("\7k\2\2\u00b4\u00b5\7p\2\2\u00b5\u00b6\7v\2\2\u00b6\u00b7")
        buf.write("\7g\2\2\u00b7\u00b8\7t\2\2\u00b8\u00b9\7h\2\2\u00b9\u00ba")
        buf.write("\7c\2\2\u00ba\u00bb\7e\2\2\u00bb\u00bc\7g\2\2\u00bc\22")
        buf.write("\3\2\2\2\u00bd\u00be\7u\2\2\u00be\u00bf\7v\2\2\u00bf\u00c0")
        buf.write("\7t\2\2\u00c0\u00c1\7k\2\2\u00c1\u00c2\7p\2\2\u00c2\u00c3")
        buf.write("\7i\2\2\u00c3\24\3\2\2\2\u00c4\u00c5\7k\2\2\u00c5\u00c6")
        buf.write("\7p\2\2\u00c6\u00c7\7v\2\2\u00c7\26\3\2\2\2\u00c8\u00c9")
        buf.write("\7h\2\2\u00c9\u00ca\7n\2\2\u00ca\u00cb\7q\2\2\u00cb\u00cc")
        buf.write("\7c\2\2\u00cc\u00cd\7v\2\2\u00cd\30\3\2\2\2\u00ce\u00cf")
        buf.write("\7d\2\2\u00cf\u00d0\7q\2\2\u00d0\u00d1\7q\2\2\u00d1\u00d2")
        buf.write("\7n\2\2\u00d2\u00d3\7g\2\2\u00d3\u00d4\7c\2\2\u00d4\u00d5")
        buf.write("\7p\2\2\u00d5\32\3\2\2\2\u00d6\u00d7\7e\2\2\u00d7\u00d8")
        buf.write("\7q\2\2\u00d8\u00d9\7p\2\2\u00d9\u00da\7u\2\2\u00da\u00db")
        buf.write("\7v\2\2\u00db\34\3\2\2\2\u00dc\u00dd\7x\2\2\u00dd\u00de")
        buf.write("\7c\2\2\u00de\u00df\7t\2\2\u00df\36\3\2\2\2\u00e0\u00e1")
        buf.write("\7e\2\2\u00e1\u00e2\7q\2\2\u00e2\u00e3\7p\2\2\u00e3\u00e4")
        buf.write("\7v\2\2\u00e4\u00e5\7k\2\2\u00e5\u00e6\7p\2\2\u00e6\u00e7")
        buf.write("\7w\2\2\u00e7\u00e8\7g\2\2\u00e8 \3\2\2\2\u00e9\u00ea")
        buf.write("\7d\2\2\u00ea\u00eb\7t\2\2\u00eb\u00ec\7g\2\2\u00ec\u00ed")
        buf.write("\7c\2\2\u00ed\u00ee\7m\2\2\u00ee\"\3\2\2\2\u00ef\u00f0")
        buf.write("\7t\2\2\u00f0\u00f1\7c\2\2\u00f1\u00f2\7p\2\2\u00f2\u00f3")
        buf.write("\7i\2\2\u00f3\u00f4\7g\2\2\u00f4$\3\2\2\2\u00f5\u00f6")
        buf.write("\7p\2\2\u00f6\u00f7\7k\2\2\u00f7\u00f8\7n\2\2\u00f8&\3")
        buf.write("\2\2\2\u00f9\u00fa\7v\2\2\u00fa\u00fb\7t\2\2\u00fb\u00fc")
        buf.write("\7w\2\2\u00fc\u00fd\7g\2\2\u00fd(\3\2\2\2\u00fe\u00ff")
        buf.write("\7h\2\2\u00ff\u0100\7c\2\2\u0100\u0101\7n\2\2\u0101\u0102")
        buf.write("\7u\2\2\u0102\u0103\7g\2\2\u0103*\3\2\2\2\u0104\u0105")
        buf.write("\7-\2\2\u0105,\3\2\2\2\u0106\u0107\7/\2\2\u0107.\3\2\2")
        buf.write("\2\u0108\u0109\7,\2\2\u0109\60\3\2\2\2\u010a\u010b\7\61")
        buf.write("\2\2\u010b\62\3\2\2\2\u010c\u010d\7\'\2\2\u010d\64\3\2")
        buf.write("\2\2\u010e\u010f\7<\2\2\u010f\u0110\7?\2\2\u0110\66\3")
        buf.write("\2\2\2\u0111\u0112\7-\2\2\u0112\u0113\7?\2\2\u01138\3")
        buf.write("\2\2\2\u0114\u0115\7/\2\2\u0115\u0116\7?\2\2\u0116:\3")
        buf.write("\2\2\2\u0117\u0118\7,\2\2\u0118\u0119\7?\2\2\u0119<\3")
        buf.write("\2\2\2\u011a\u011b\7\61\2\2\u011b\u011c\7?\2\2\u011c>")
        buf.write("\3\2\2\2\u011d\u011e\7\'\2\2\u011e\u011f\7?\2\2\u011f")
        buf.write("@\3\2\2\2\u0120\u0121\7?\2\2\u0121B\3\2\2\2\u0122\u0123")
        buf.write("\7(\2\2\u0123\u0124\7(\2\2\u0124D\3\2\2\2\u0125\u0126")
        buf.write("\7~\2\2\u0126\u0127\7~\2\2\u0127F\3\2\2\2\u0128\u0129")
        buf.write("\7#\2\2\u0129H\3\2\2\2\u012a\u012b\7?\2\2\u012b\u012c")
        buf.write("\7?\2\2\u012cJ\3\2\2\2\u012d\u012e\7#\2\2\u012e\u012f")
        buf.write("\7?\2\2\u012fL\3\2\2\2\u0130\u0131\7>\2\2\u0131N\3\2\2")
        buf.write("\2\u0132\u0133\7>\2\2\u0133\u0134\7?\2\2\u0134P\3\2\2")
        buf.write("\2\u0135\u0136\7@\2\2\u0136R\3\2\2\2\u0137\u0138\7@\2")
        buf.write("\2\u0138\u0139\7?\2\2\u0139T\3\2\2\2\u013a\u013b\7\60")
        buf.write("\2\2\u013bV\3\2\2\2\u013c\u013d\7*\2\2\u013dX\3\2\2\2")
        buf.write("\u013e\u013f\7+\2\2\u013fZ\3\2\2\2\u0140\u0141\7}\2\2")
        buf.write("\u0141\\\3\2\2\2\u0142\u0143\7\177\2\2\u0143^\3\2\2\2")
        buf.write("\u0144\u0145\7]\2\2\u0145`\3\2\2\2\u0146\u0147\7_\2\2")
        buf.write("\u0147b\3\2\2\2\u0148\u0149\7.\2\2\u0149d\3\2\2\2\u014a")
        buf.write("\u014b\7=\2\2\u014bf\3\2\2\2\u014c\u014d\7<\2\2\u014d")
        buf.write("h\3\2\2\2\u014e\u0150\7\17\2\2\u014f\u014e\3\2\2\2\u014f")
        buf.write("\u0150\3\2\2\2\u0150\u0151\3\2\2\2\u0151\u0152\7\f\2\2")
        buf.write("\u0152\u0153\b\65\2\2\u0153j\3\2\2\2\u0154\u0158\t\2\2")
        buf.write("\2\u0155\u0157\t\3\2\2\u0156\u0155\3\2\2\2\u0157\u015a")
        buf.write("\3\2\2\2\u0158\u0156\3\2\2\2\u0158\u0159\3\2\2\2\u0159")
        buf.write("l\3\2\2\2\u015a\u0158\3\2\2\2\u015b\u0164\7\62\2\2\u015c")
        buf.write("\u0160\t\4\2\2\u015d\u015f\t\5\2\2\u015e\u015d\3\2\2\2")
        buf.write("\u015f\u0162\3\2\2\2\u0160\u015e\3\2\2\2\u0160\u0161\3")
        buf.write("\2\2\2\u0161\u0164\3\2\2\2\u0162\u0160\3\2\2\2\u0163\u015b")
        buf.write("\3\2\2\2\u0163\u015c\3\2\2\2\u0164n\3\2\2\2\u0165\u0166")
        buf.write("\7\62\2\2\u0166\u0168\t\6\2\2\u0167\u0169\t\7\2\2\u0168")
        buf.write("\u0167\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u0168\3\2\2\2")
        buf.write("\u016a\u016b\3\2\2\2\u016bp\3\2\2\2\u016c\u016d\7\62\2")
        buf.write("\2\u016d\u016f\t\b\2\2\u016e\u0170\t\t\2\2\u016f\u016e")
        buf.write("\3\2\2\2\u0170\u0171\3\2\2\2\u0171\u016f\3\2\2\2\u0171")
        buf.write("\u0172\3\2\2\2\u0172r\3\2\2\2\u0173\u0174\7\62\2\2\u0174")
        buf.write("\u0176\t\n\2\2\u0175\u0177\t\13\2\2\u0176\u0175\3\2\2")
        buf.write("\2\u0177\u0178\3\2\2\2\u0178\u0176\3\2\2\2\u0178\u0179")
        buf.write("\3\2\2\2\u0179t\3\2\2\2\u017a\u017c\t\5\2\2\u017b\u017a")
        buf.write("\3\2\2\2\u017c\u017d\3\2\2\2\u017d\u017b\3\2\2\2\u017d")
        buf.write("\u017e\3\2\2\2\u017ev\3\2\2\2\u017f\u0183\7\60\2\2\u0180")
        buf.write("\u0182\t\5\2\2\u0181\u0180\3\2\2\2\u0182\u0185\3\2\2\2")
        buf.write("\u0183\u0181\3\2\2\2\u0183\u0184\3\2\2\2\u0184x\3\2\2")
        buf.write("\2\u0185\u0183\3\2\2\2\u0186\u0188\t\f\2\2\u0187\u0189")
        buf.write("\t\r\2\2\u0188\u0187\3\2\2\2\u0188\u0189\3\2\2\2\u0189")
        buf.write("\u018a\3\2\2\2\u018a\u018b\5u;\2\u018bz\3\2\2\2\u018c")
        buf.write("\u018d\5u;\2\u018d\u018f\5w<\2\u018e\u0190\5y=\2\u018f")
        buf.write("\u018e\3\2\2\2\u018f\u0190\3\2\2\2\u0190|\3\2\2\2\u0191")
        buf.write("\u0195\n\16\2\2\u0192\u0193\7^\2\2\u0193\u0195\t\17\2")
        buf.write("\2\u0194\u0191\3\2\2\2\u0194\u0192\3\2\2\2\u0195~\3\2")
        buf.write("\2\2\u0196\u019a\7$\2\2\u0197\u0199\5}?\2\u0198\u0197")
        buf.write("\3\2\2\2\u0199\u019c\3\2\2\2\u019a\u0198\3\2\2\2\u019a")
        buf.write("\u019b\3\2\2\2\u019b\u019d\3\2\2\2\u019c\u019a\3\2\2\2")
        buf.write("\u019d\u019e\7$\2\2\u019e\u0080\3\2\2\2\u019f\u01a1\t")
        buf.write("\20\2\2\u01a0\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2")
        buf.write("\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a4\3\2\2\2")
        buf.write("\u01a4\u01a5\bA\3\2\u01a5\u0082\3\2\2\2\u01a6\u01a7\7")
        buf.write("\61\2\2\u01a7\u01a8\7\61\2\2\u01a8\u01ac\3\2\2\2\u01a9")
        buf.write("\u01ab\n\21\2\2\u01aa\u01a9\3\2\2\2\u01ab\u01ae\3\2\2")
        buf.write("\2\u01ac\u01aa\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad\u01af")
        buf.write("\3\2\2\2\u01ae\u01ac\3\2\2\2\u01af\u01b0\bB\3\2\u01b0")
        buf.write("\u0084\3\2\2\2\u01b1\u01b2\7\61\2\2\u01b2\u01b3\7,\2\2")
        buf.write("\u01b3\u01b9\3\2\2\2\u01b4\u01b8\5\u0085C\2\u01b5\u01b8")
        buf.write("\5\u0083B\2\u01b6\u01b8\13\2\2\2\u01b7\u01b4\3\2\2\2\u01b7")
        buf.write("\u01b5\3\2\2\2\u01b7\u01b6\3\2\2\2\u01b8\u01bb\3\2\2\2")
        buf.write("\u01b9\u01ba\3\2\2\2\u01b9\u01b7\3\2\2\2\u01ba\u01bc\3")
        buf.write("\2\2\2\u01bb\u01b9\3\2\2\2\u01bc\u01bd\7,\2\2\u01bd\u01be")
        buf.write("\7\61\2\2\u01be\u01bf\3\2\2\2\u01bf\u01c0\bC\3\2\u01c0")
        buf.write("\u0086\3\2\2\2\u01c1\u01c5\7$\2\2\u01c2\u01c4\5}?\2\u01c3")
        buf.write("\u01c2\3\2\2\2\u01c4\u01c7\3\2\2\2\u01c5\u01c3\3\2\2\2")
        buf.write("\u01c5\u01c6\3\2\2\2\u01c6\u01cb\3\2\2\2\u01c7\u01c5\3")
        buf.write("\2\2\2\u01c8\u01c9\7\17\2\2\u01c9\u01cc\7\f\2\2\u01ca")
        buf.write("\u01cc\t\22\2\2\u01cb\u01c8\3\2\2\2\u01cb\u01ca\3\2\2")
        buf.write("\2\u01cc\u01cd\3\2\2\2\u01cd\u01ce\bD\4\2\u01ce\u0088")
        buf.write("\3\2\2\2\u01cf\u01d3\7$\2\2\u01d0\u01d2\5}?\2\u01d1\u01d0")
        buf.write("\3\2\2\2\u01d2\u01d5\3\2\2\2\u01d3\u01d1\3\2\2\2\u01d3")
        buf.write("\u01d4\3\2\2\2\u01d4\u01d6\3\2\2\2\u01d5\u01d3\3\2\2\2")
        buf.write("\u01d6\u01d7\5\u008bF\2\u01d7\u01d8\bE\5\2\u01d8\u008a")
        buf.write("\3\2\2\2\u01d9\u01da\7^\2\2\u01da\u01db\n\17\2\2\u01db")
        buf.write("\u008c\3\2\2\2\u01dc\u01dd\13\2\2\2\u01dd\u01de\bG\6\2")
        buf.write("\u01de\u008e\3\2\2\2\27\2\u014f\u0158\u0160\u0163\u016a")
        buf.write("\u0171\u0178\u017d\u0183\u0188\u018f\u0194\u019a\u01a2")
        buf.write("\u01ac\u01b7\u01b9\u01c5\u01cb\u01d3\7\3\65\2\b\2\2\3")
        buf.write("D\3\3E\4\3G\5")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IF = 1
    ELSE = 2
    FOR = 3
    RETURN = 4
    FUNC = 5
    TYPE = 6
    STRUCT = 7
    INTERFACE = 8
    STRING = 9
    INT = 10
    FLOAT = 11
    BOOLEAN = 12
    CONST = 13
    VAR = 14
    CONTINUE = 15
    BREAK = 16
    RANGE = 17
    NIL = 18
    TRUE = 19
    FALSE = 20
    ADD = 21
    SUB = 22
    MUL = 23
    DIV = 24
    MOD = 25
    ASSIGN = 26
    ADD_ASSIGN = 27
    SUB_ASSIGN = 28
    MUL_ASSIGN = 29
    DIV_ASSIGN = 30
    MOD_ASSIGN = 31
    INIT = 32
    AND = 33
    OR = 34
    NOT = 35
    EQUAL = 36
    NOT_EQUAL = 37
    LESS = 38
    LESS_OR_EQUAL = 39
    GREATER = 40
    GREATER_OR_EQUAL = 41
    DOT = 42
    LPAREN = 43
    RPAREN = 44
    LBRACEBRACK = 45
    RBRACEBRACK = 46
    LSQUAREBRACK = 47
    RSQUAREBRACK = 48
    COMMA = 49
    SEMICOLON = 50
    COLON = 51
    NEW_LINE = 52
    ID = 53
    DECINT_LIT = 54
    BININT_LIT = 55
    OCTINT_LIT = 56
    HEXINT_LIT = 57
    FLOAT_LIT = 58
    STRING_LIT = 59
    SKIP_TOKENS = 60
    COMMENT_SINGLE_LINE = 61
    COMMENT_MULTI_LINE = 62
    UNCLOSE_STRING = 63
    ILLEGAL_ESCAPE = 64
    ERROR_CHAR = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", "'struct'", 
            "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'nil'", 
            "'true'", "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "':='", 
            "'+='", "'-='", "'*='", "'/='", "'%='", "'='", "'&&'", "'||'", 
            "'!'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'.'", 
            "'('", "')'", "'{'", "'}'", "'['", "']'", "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
            "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
            "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "ADD", "SUB", "MUL", 
            "DIV", "MOD", "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", 
            "DIV_ASSIGN", "MOD_ASSIGN", "INIT", "AND", "OR", "NOT", "EQUAL", 
            "NOT_EQUAL", "LESS", "LESS_OR_EQUAL", "GREATER", "GREATER_OR_EQUAL", 
            "DOT", "LPAREN", "RPAREN", "LBRACEBRACK", "RBRACEBRACK", "LSQUAREBRACK", 
            "RSQUAREBRACK", "COMMA", "SEMICOLON", "COLON", "NEW_LINE", "ID", 
            "DECINT_LIT", "BININT_LIT", "OCTINT_LIT", "HEXINT_LIT", "FLOAT_LIT", 
            "STRING_LIT", "SKIP_TOKENS", "COMMENT_SINGLE_LINE", "COMMENT_MULTI_LINE", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
                  "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", 
                  "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", "FALSE", 
                  "ADD", "SUB", "MUL", "DIV", "MOD", "ASSIGN", "ADD_ASSIGN", 
                  "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
                  "INIT", "AND", "OR", "NOT", "EQUAL", "NOT_EQUAL", "LESS", 
                  "LESS_OR_EQUAL", "GREATER", "GREATER_OR_EQUAL", "DOT", 
                  "LPAREN", "RPAREN", "LBRACEBRACK", "RBRACEBRACK", "LSQUAREBRACK", 
                  "RSQUAREBRACK", "COMMA", "SEMICOLON", "COLON", "NEW_LINE", 
                  "ID", "DECINT_LIT", "BININT_LIT", "OCTINT_LIT", "HEXINT_LIT", 
                  "FLOAT_INT_PART", "FLOAT_DEC_PART", "FLOAT_EXP_PART", 
                  "FLOAT_LIT", "INTERNAL_STRING_LIT", "STRING_LIT", "SKIP_TOKENS", 
                  "COMMENT_SINGLE_LINE", "COMMENT_MULTI_LINE", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ESC_ILLEGAL", "ERROR_CHAR" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None
        self.preType = None

    def emit(self):
        tk = self.type
        self.preType = tk;
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


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[51] = self.NEW_LINE_action 
            actions[66] = self.UNCLOSE_STRING_action 
            actions[67] = self.ILLEGAL_ESCAPE_action 
            actions[69] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NEW_LINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            statement_end_tokens = {MiniGoLexer.ID,
                                MiniGoLexer.DECINT_LIT,
                                MiniGoLexer.BININT_LIT,
                                MiniGoLexer.OCTINT_LIT,
                                MiniGoLexer.HEXINT_LIT,
                                MiniGoLexer.FLOAT_LIT,
                                MiniGoLexer.STRING_LIT,
                                MiniGoLexer.TRUE,
                                MiniGoLexer.FALSE,
                                MiniGoLexer.NIL,
                                MiniGoLexer.RPAREN,
                                MiniGoLexer.RBRACEBRACK,
                                MiniGoLexer.RSQUAREBRACK,
                                MiniGoLexer.RETURN,
                                MiniGoLexer.CONTINUE,
                                MiniGoLexer.BREAK}

            if self.preType in statement_end_tokens:  
                self.text = ';'  # Convert newline to semicolon
                self.preType = None
            else:
                self.skip()  # Ignore the newline     

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
             
                if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
                    raise UncloseString(self.text[:-2])
                elif (self.text[-1] == '\n'):
                    raise UncloseString(self.text[:-1])
                else:
                    raise UncloseString(self.text)

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                raise IllegalEscape(self.text)

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                raise ErrorToken(self.text)

     


