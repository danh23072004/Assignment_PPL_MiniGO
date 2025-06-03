# Generated from main/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C")
        buf.write("\u0277\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\3\2\6\2\u008c\n\2\r\2\16\2\u008d\3\2\3\2\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\u009b\n\4\3\5\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\7\6\u00a7\n\6\f\6\16\6")
        buf.write("\u00aa\13\6\3\7\3\7\3\7\3\7\3\7\3\7\7\7\u00b2\n\7\f\7")
        buf.write("\16\7\u00b5\13\7\3\b\3\b\3\b\3\b\3\b\3\b\7\b\u00bd\n\b")
        buf.write("\f\b\16\b\u00c0\13\b\3\t\3\t\3\t\3\t\3\t\3\t\7\t\u00c8")
        buf.write("\n\t\f\t\16\t\u00cb\13\t\3\n\3\n\3\n\3\n\3\n\3\n\7\n\u00d3")
        buf.write("\n\n\f\n\16\n\u00d6\13\n\3\13\3\13\3\13\5\13\u00db\n\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00e4\n\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\7\f\u00f5")
        buf.write("\n\f\f\f\16\f\u00f8\13\f\3\r\3\r\3\r\5\r\u00fd\n\r\3\16")
        buf.write("\3\16\5\16\u0101\n\16\3\17\3\17\3\17\3\17\3\17\5\17\u0108")
        buf.write("\n\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u0111\n")
        buf.write("\20\3\21\3\21\3\21\3\21\3\21\5\21\u0118\n\21\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\5\23\u0122\n\23\3\24\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\5\24\u0130\n\24\3\24\3\24\3\24\7\24\u0135\n\24\f\24\16")
        buf.write("\24\u0138\13\24\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\5\30\u014d\n\30\3\31\3\31\5\31\u0151\n\31\3\32\3\32\3")
        buf.write("\32\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\5\34\u0160\n\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\5\35\u016d\n\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\5\36\u0175\n\36\3\37\3\37\3\37\3\37\3\37\3")
        buf.write(" \3 \3 \3!\3!\3!\3!\3!\3!\5!\u0185\n!\3\"\3\"\5\"\u0189")
        buf.write("\n\"\3#\3#\3#\3$\3$\5$\u0190\n$\3%\3%\3%\3%\3%\3%\3%\3")
        buf.write("%\3%\3%\5%\u019c\n%\3&\3&\3&\5&\u01a1\n&\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3\'\5\'\u01aa\n\'\3(\3(\3(\3(\3(\3(\3(\3(\5")
        buf.write("(\u01b4\n(\3)\3)\3)\3)\5)\u01ba\n)\3*\3*\3*\5*\u01bf\n")
        buf.write("*\3+\3+\3,\3,\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\7-\u01d0")
        buf.write("\n-\f-\16-\u01d3\13-\3.\3.\3/\3/\3/\3/\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\5\62\u01f2")
        buf.write("\n\62\3\63\3\63\3\63\3\63\3\63\3\63\5\63\u01fa\n\63\3")
        buf.write("\64\3\64\3\64\5\64\u01ff\n\64\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\38")
        buf.write("\38\38\58\u0213\n8\38\38\38\38\38\38\38\38\39\39\39\3")
        buf.write("9\39\39\39\39\39\39\39\3:\3:\5:\u022a\n:\3;\3;\3;\3;\3")
        buf.write(";\3<\3<\3<\3<\3<\3<\3<\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3")
        buf.write(">\3>\3>\3>\3>\3>\3>\3>\3>\3>\3>\3?\3?\3?\3?\3?\3@\3@\3")
        buf.write("@\3@\3@\3@\3@\3A\3A\3A\3A\5A\u025d\nA\3B\3B\3B\3B\3C\3")
        buf.write("C\3C\3C\3C\3C\3C\3D\3D\3D\3D\5D\u026e\nD\3E\3E\3E\3E\3")
        buf.write("E\3E\3E\3E\2\n\n\f\16\20\22\26&XF\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR")
        buf.write("TVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088")
        buf.write("\2\13\3\28<\3\2&+\3\2\27\30\3\2\31\33\4\2\30\30%%\3\2")
        buf.write("\678\4\2\13\16\67\67\4\2\64\64\66\66\3\2\34!\2\u027a\2")
        buf.write("\u008b\3\2\2\2\4\u0091\3\2\2\2\6\u009a\3\2\2\2\b\u009c")
        buf.write("\3\2\2\2\n\u00a0\3\2\2\2\f\u00ab\3\2\2\2\16\u00b6\3\2")
        buf.write("\2\2\20\u00c1\3\2\2\2\22\u00cc\3\2\2\2\24\u00da\3\2\2")
        buf.write("\2\26\u00e3\3\2\2\2\30\u00fc\3\2\2\2\32\u0100\3\2\2\2")
        buf.write("\34\u0107\3\2\2\2\36\u0110\3\2\2\2 \u0117\3\2\2\2\"\u0119")
        buf.write("\3\2\2\2$\u0121\3\2\2\2&\u012f\3\2\2\2(\u0139\3\2\2\2")
        buf.write("*\u013b\3\2\2\2,\u013f\3\2\2\2.\u014c\3\2\2\2\60\u0150")
        buf.write("\3\2\2\2\62\u0152\3\2\2\2\64\u0157\3\2\2\2\66\u015f\3")
        buf.write("\2\2\28\u016c\3\2\2\2:\u0174\3\2\2\2<\u0176\3\2\2\2>\u017b")
        buf.write("\3\2\2\2@\u0184\3\2\2\2B\u0188\3\2\2\2D\u018a\3\2\2\2")
        buf.write("F\u018f\3\2\2\2H\u019b\3\2\2\2J\u01a0\3\2\2\2L\u01a9\3")
        buf.write("\2\2\2N\u01b3\3\2\2\2P\u01b9\3\2\2\2R\u01be\3\2\2\2T\u01c0")
        buf.write("\3\2\2\2V\u01c2\3\2\2\2X\u01c4\3\2\2\2Z\u01d4\3\2\2\2")
        buf.write("\\\u01d6\3\2\2\2^\u01da\3\2\2\2`\u01e4\3\2\2\2b\u01f1")
        buf.write("\3\2\2\2d\u01f9\3\2\2\2f\u01fe\3\2\2\2h\u0200\3\2\2\2")
        buf.write("j\u0206\3\2\2\2l\u020a\3\2\2\2n\u020f\3\2\2\2p\u021c\3")
        buf.write("\2\2\2r\u0229\3\2\2\2t\u022b\3\2\2\2v\u0230\3\2\2\2x\u0237")
        buf.write("\3\2\2\2z\u0241\3\2\2\2|\u024c\3\2\2\2~\u0251\3\2\2\2")
        buf.write("\u0080\u025c\3\2\2\2\u0082\u025e\3\2\2\2\u0084\u0262\3")
        buf.write("\2\2\2\u0086\u026d\3\2\2\2\u0088\u026f\3\2\2\2\u008a\u008c")
        buf.write("\5\66\34\2\u008b\u008a\3\2\2\2\u008c\u008d\3\2\2\2\u008d")
        buf.write("\u008b\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u008f\3\2\2\2")
        buf.write("\u008f\u0090\7\2\2\3\u0090\3\3\2\2\2\u0091\u0092\t\2\2")
        buf.write("\2\u0092\5\3\2\2\2\u0093\u009b\5\4\3\2\u0094\u009b\7=")
        buf.write("\2\2\u0095\u009b\7\25\2\2\u0096\u009b\7\26\2\2\u0097\u009b")
        buf.write("\7\24\2\2\u0098\u009b\5,\27\2\u0099\u009b\5\62\32\2\u009a")
        buf.write("\u0093\3\2\2\2\u009a\u0094\3\2\2\2\u009a\u0095\3\2\2\2")
        buf.write("\u009a\u0096\3\2\2\2\u009a\u0097\3\2\2\2\u009a\u0098\3")
        buf.write("\2\2\2\u009a\u0099\3\2\2\2\u009b\7\3\2\2\2\u009c\u009d")
        buf.write("\7-\2\2\u009d\u009e\5\n\6\2\u009e\u009f\7.\2\2\u009f\t")
        buf.write("\3\2\2\2\u00a0\u00a1\b\6\1\2\u00a1\u00a2\5\f\7\2\u00a2")
        buf.write("\u00a8\3\2\2\2\u00a3\u00a4\f\4\2\2\u00a4\u00a5\7$\2\2")
        buf.write("\u00a5\u00a7\5\f\7\2\u00a6\u00a3\3\2\2\2\u00a7\u00aa\3")
        buf.write("\2\2\2\u00a8\u00a6\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\13")
        buf.write("\3\2\2\2\u00aa\u00a8\3\2\2\2\u00ab\u00ac\b\7\1\2\u00ac")
        buf.write("\u00ad\5\16\b\2\u00ad\u00b3\3\2\2\2\u00ae\u00af\f\4\2")
        buf.write("\2\u00af\u00b0\7#\2\2\u00b0\u00b2\5\16\b\2\u00b1\u00ae")
        buf.write("\3\2\2\2\u00b2\u00b5\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b3")
        buf.write("\u00b4\3\2\2\2\u00b4\r\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b6")
        buf.write("\u00b7\b\b\1\2\u00b7\u00b8\5\20\t\2\u00b8\u00be\3\2\2")
        buf.write("\2\u00b9\u00ba\f\4\2\2\u00ba\u00bb\t\3\2\2\u00bb\u00bd")
        buf.write("\5\20\t\2\u00bc\u00b9\3\2\2\2\u00bd\u00c0\3\2\2\2\u00be")
        buf.write("\u00bc\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\17\3\2\2\2\u00c0")
        buf.write("\u00be\3\2\2\2\u00c1\u00c2\b\t\1\2\u00c2\u00c3\5\22\n")
        buf.write("\2\u00c3\u00c9\3\2\2\2\u00c4\u00c5\f\4\2\2\u00c5\u00c6")
        buf.write("\t\4\2\2\u00c6\u00c8\5\22\n\2\u00c7\u00c4\3\2\2\2\u00c8")
        buf.write("\u00cb\3\2\2\2\u00c9\u00c7\3\2\2\2\u00c9\u00ca\3\2\2\2")
        buf.write("\u00ca\21\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cc\u00cd\b\n")
        buf.write("\1\2\u00cd\u00ce\5\24\13\2\u00ce\u00d4\3\2\2\2\u00cf\u00d0")
        buf.write("\f\4\2\2\u00d0\u00d1\t\5\2\2\u00d1\u00d3\5\24\13\2\u00d2")
        buf.write("\u00cf\3\2\2\2\u00d3\u00d6\3\2\2\2\u00d4\u00d2\3\2\2\2")
        buf.write("\u00d4\u00d5\3\2\2\2\u00d5\23\3\2\2\2\u00d6\u00d4\3\2")
        buf.write("\2\2\u00d7\u00d8\t\6\2\2\u00d8\u00db\5\24\13\2\u00d9\u00db")
        buf.write("\5\26\f\2\u00da\u00d7\3\2\2\2\u00da\u00d9\3\2\2\2\u00db")
        buf.write("\25\3\2\2\2\u00dc\u00dd\b\f\1\2\u00dd\u00de\7\67\2\2\u00de")
        buf.write("\u00df\7-\2\2\u00df\u00e0\5\32\16\2\u00e0\u00e1\7.\2\2")
        buf.write("\u00e1\u00e4\3\2\2\2\u00e2\u00e4\5\30\r\2\u00e3\u00dc")
        buf.write("\3\2\2\2\u00e3\u00e2\3\2\2\2\u00e4\u00f6\3\2\2\2\u00e5")
        buf.write("\u00e6\f\7\2\2\u00e6\u00e7\7\61\2\2\u00e7\u00e8\5\n\6")
        buf.write("\2\u00e8\u00e9\7\62\2\2\u00e9\u00f5\3\2\2\2\u00ea\u00eb")
        buf.write("\f\6\2\2\u00eb\u00ec\7,\2\2\u00ec\u00ed\7\67\2\2\u00ed")
        buf.write("\u00ee\7-\2\2\u00ee\u00ef\5\32\16\2\u00ef\u00f0\7.\2\2")
        buf.write("\u00f0\u00f5\3\2\2\2\u00f1\u00f2\f\5\2\2\u00f2\u00f3\7")
        buf.write(",\2\2\u00f3\u00f5\7\67\2\2\u00f4\u00e5\3\2\2\2\u00f4\u00ea")
        buf.write("\3\2\2\2\u00f4\u00f1\3\2\2\2\u00f5\u00f8\3\2\2\2\u00f6")
        buf.write("\u00f4\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\27\3\2\2\2\u00f8")
        buf.write("\u00f6\3\2\2\2\u00f9\u00fd\5\6\4\2\u00fa\u00fd\7\67\2")
        buf.write("\2\u00fb\u00fd\5\b\5\2\u00fc\u00f9\3\2\2\2\u00fc\u00fa")
        buf.write("\3\2\2\2\u00fc\u00fb\3\2\2\2\u00fd\31\3\2\2\2\u00fe\u0101")
        buf.write("\5\34\17\2\u00ff\u0101\3\2\2\2\u0100\u00fe\3\2\2\2\u0100")
        buf.write("\u00ff\3\2\2\2\u0101\33\3\2\2\2\u0102\u0103\5\n\6\2\u0103")
        buf.write("\u0104\7\63\2\2\u0104\u0105\5\34\17\2\u0105\u0108\3\2")
        buf.write("\2\2\u0106\u0108\5\n\6\2\u0107\u0102\3\2\2\2\u0107\u0106")
        buf.write("\3\2\2\2\u0108\35\3\2\2\2\u0109\u0111\7\67\2\2\u010a\u0111")
        buf.write("\5\62\32\2\u010b\u0111\7=\2\2\u010c\u0111\7\25\2\2\u010d")
        buf.write("\u0111\7\26\2\2\u010e\u0111\7\24\2\2\u010f\u0111\5\4\3")
        buf.write("\2\u0110\u0109\3\2\2\2\u0110\u010a\3\2\2\2\u0110\u010b")
        buf.write("\3\2\2\2\u0110\u010c\3\2\2\2\u0110\u010d\3\2\2\2\u0110")
        buf.write("\u010e\3\2\2\2\u0110\u010f\3\2\2\2\u0111\37\3\2\2\2\u0112")
        buf.write("\u0113\5\36\20\2\u0113\u0114\7\63\2\2\u0114\u0115\5 \21")
        buf.write("\2\u0115\u0118\3\2\2\2\u0116\u0118\5\36\20\2\u0117\u0112")
        buf.write("\3\2\2\2\u0117\u0116\3\2\2\2\u0118!\3\2\2\2\u0119\u011a")
        buf.write("\7\61\2\2\u011a\u011b\t\7\2\2\u011b\u011c\7\62\2\2\u011c")
        buf.write("#\3\2\2\2\u011d\u011e\5\"\22\2\u011e\u011f\5$\23\2\u011f")
        buf.write("\u0122\3\2\2\2\u0120\u0122\5\"\22\2\u0121\u011d\3\2\2")
        buf.write("\2\u0121\u0120\3\2\2\2\u0122%\3\2\2\2\u0123\u0124\b\24")
        buf.write("\1\2\u0124\u0130\5 \21\2\u0125\u0126\7/\2\2\u0126\u0127")
        buf.write("\5&\24\2\u0127\u0128\7\60\2\2\u0128\u0129\7\63\2\2\u0129")
        buf.write("\u012a\5&\24\4\u012a\u0130\3\2\2\2\u012b\u012c\7/\2\2")
        buf.write("\u012c\u012d\5&\24\2\u012d\u012e\7\60\2\2\u012e\u0130")
        buf.write("\3\2\2\2\u012f\u0123\3\2\2\2\u012f\u0125\3\2\2\2\u012f")
        buf.write("\u012b\3\2\2\2\u0130\u0136\3\2\2\2\u0131\u0132\f\5\2\2")
        buf.write("\u0132\u0133\7\63\2\2\u0133\u0135\5&\24\6\u0134\u0131")
        buf.write("\3\2\2\2\u0135\u0138\3\2\2\2\u0136\u0134\3\2\2\2\u0136")
        buf.write("\u0137\3\2\2\2\u0137\'\3\2\2\2\u0138\u0136\3\2\2\2\u0139")
        buf.write("\u013a\5&\24\2\u013a)\3\2\2\2\u013b\u013c\7/\2\2\u013c")
        buf.write("\u013d\5(\25\2\u013d\u013e\7\60\2\2\u013e+\3\2\2\2\u013f")
        buf.write("\u0140\5$\23\2\u0140\u0141\t\b\2\2\u0141\u0142\5*\26\2")
        buf.write("\u0142-\3\2\2\2\u0143\u0144\7\67\2\2\u0144\u0145\7\65")
        buf.write("\2\2\u0145\u0146\5\n\6\2\u0146\u0147\7\63\2\2\u0147\u0148")
        buf.write("\5.\30\2\u0148\u014d\3\2\2\2\u0149\u014a\7\67\2\2\u014a")
        buf.write("\u014b\7\65\2\2\u014b\u014d\5\n\6\2\u014c\u0143\3\2\2")
        buf.write("\2\u014c\u0149\3\2\2\2\u014d/\3\2\2\2\u014e\u0151\5.\30")
        buf.write("\2\u014f\u0151\3\2\2\2\u0150\u014e\3\2\2\2\u0150\u014f")
        buf.write("\3\2\2\2\u0151\61\3\2\2\2\u0152\u0153\7\67\2\2\u0153\u0154")
        buf.write("\7/\2\2\u0154\u0155\5\60\31\2\u0155\u0156\7\60\2\2\u0156")
        buf.write("\63\3\2\2\2\u0157\u0158\t\t\2\2\u0158\65\3\2\2\2\u0159")
        buf.write("\u0160\5<\37\2\u015a\u0160\5H%\2\u015b\u0160\5x=\2\u015c")
        buf.write("\u0160\5z>\2\u015d\u0160\5~@\2\u015e\u0160\5\u0088E\2")
        buf.write("\u015f\u0159\3\2\2\2\u015f\u015a\3\2\2\2\u015f\u015b\3")
        buf.write("\2\2\2\u015f\u015c\3\2\2\2\u015f\u015d\3\2\2\2\u015f\u015e")
        buf.write("\3\2\2\2\u0160\u0161\3\2\2\2\u0161\u0162\5\64\33\2\u0162")
        buf.write("\67\3\2\2\2\u0163\u016d\5<\37\2\u0164\u016d\5H%\2\u0165")
        buf.write("\u016d\5\\/\2\u0166\u016d\5f\64\2\u0167\u016d\5R*\2\u0168")
        buf.write("\u016d\5^\60\2\u0169\u016d\5T+\2\u016a\u016d\5V,\2\u016b")
        buf.write("\u016d\5r:\2\u016c\u0163\3\2\2\2\u016c\u0164\3\2\2\2\u016c")
        buf.write("\u0165\3\2\2\2\u016c\u0166\3\2\2\2\u016c\u0167\3\2\2\2")
        buf.write("\u016c\u0168\3\2\2\2\u016c\u0169\3\2\2\2\u016c\u016a\3")
        buf.write("\2\2\2\u016c\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016e\u016f")
        buf.write("\5\64\33\2\u016f9\3\2\2\2\u0170\u0171\58\35\2\u0171\u0172")
        buf.write("\5:\36\2\u0172\u0175\3\2\2\2\u0173\u0175\3\2\2\2\u0174")
        buf.write("\u0170\3\2\2\2\u0174\u0173\3\2\2\2\u0175;\3\2\2\2\u0176")
        buf.write("\u0177\7\17\2\2\u0177\u0178\7\67\2\2\u0178\u0179\7\"\2")
        buf.write("\2\u0179\u017a\5\n\6\2\u017a=\3\2\2\2\u017b\u017c\5$\23")
        buf.write("\2\u017c\u017d\5@!\2\u017d?\3\2\2\2\u017e\u0185\7\f\2")
        buf.write("\2\u017f\u0185\7\r\2\2\u0180\u0185\7\13\2\2\u0181\u0185")
        buf.write("\7\16\2\2\u0182\u0185\7\67\2\2\u0183\u0185\5> \2\u0184")
        buf.write("\u017e\3\2\2\2\u0184\u017f\3\2\2\2\u0184\u0180\3\2\2\2")
        buf.write("\u0184\u0181\3\2\2\2\u0184\u0182\3\2\2\2\u0184\u0183\3")
        buf.write("\2\2\2\u0185A\3\2\2\2\u0186\u0189\5@!\2\u0187\u0189\3")
        buf.write("\2\2\2\u0188\u0186\3\2\2\2\u0188\u0187\3\2\2\2\u0189C")
        buf.write("\3\2\2\2\u018a\u018b\7\"\2\2\u018b\u018c\5\n\6\2\u018c")
        buf.write("E\3\2\2\2\u018d\u0190\5D#\2\u018e\u0190\3\2\2\2\u018f")
        buf.write("\u018d\3\2\2\2\u018f\u018e\3\2\2\2\u0190G\3\2\2\2\u0191")
        buf.write("\u0192\7\20\2\2\u0192\u0193\7\67\2\2\u0193\u0194\5@!\2")
        buf.write("\u0194\u0195\5F$\2\u0195\u019c\3\2\2\2\u0196\u0197\7\20")
        buf.write("\2\2\u0197\u0198\7\67\2\2\u0198\u0199\5B\"\2\u0199\u019a")
        buf.write("\5D#\2\u019a\u019c\3\2\2\2\u019b\u0191\3\2\2\2\u019b\u0196")
        buf.write("\3\2\2\2\u019cI\3\2\2\2\u019d\u01a1\5L\'\2\u019e\u01a1")
        buf.write("\5N(\2\u019f\u01a1\3\2\2\2\u01a0\u019d\3\2\2\2\u01a0\u019e")
        buf.write("\3\2\2\2\u01a0\u019f\3\2\2\2\u01a1K\3\2\2\2\u01a2\u01a3")
        buf.write("\7\67\2\2\u01a3\u01a4\5@!\2\u01a4\u01a5\7\63\2\2\u01a5")
        buf.write("\u01a6\5L\'\2\u01a6\u01aa\3\2\2\2\u01a7\u01a8\7\67\2\2")
        buf.write("\u01a8\u01aa\5@!\2\u01a9\u01a2\3\2\2\2\u01a9\u01a7\3\2")
        buf.write("\2\2\u01aaM\3\2\2\2\u01ab\u01ac\5P)\2\u01ac\u01ad\5@!")
        buf.write("\2\u01ad\u01ae\7\63\2\2\u01ae\u01af\5N(\2\u01af\u01b4")
        buf.write("\3\2\2\2\u01b0\u01b1\5P)\2\u01b1\u01b2\5@!\2\u01b2\u01b4")
        buf.write("\3\2\2\2\u01b3\u01ab\3\2\2\2\u01b3\u01b0\3\2\2\2\u01b4")
        buf.write("O\3\2\2\2\u01b5\u01b6\7\67\2\2\u01b6\u01b7\7\63\2\2\u01b7")
        buf.write("\u01ba\5P)\2\u01b8\u01ba\7\67\2\2\u01b9\u01b5\3\2\2\2")
        buf.write("\u01b9\u01b8\3\2\2\2\u01baQ\3\2\2\2\u01bb\u01bc\7\6\2")
        buf.write("\2\u01bc\u01bf\5\n\6\2\u01bd\u01bf\7\6\2\2\u01be\u01bb")
        buf.write("\3\2\2\2\u01be\u01bd\3\2\2\2\u01bfS\3\2\2\2\u01c0\u01c1")
        buf.write("\7\22\2\2\u01c1U\3\2\2\2\u01c2\u01c3\7\21\2\2\u01c3W\3")
        buf.write("\2\2\2\u01c4\u01c5\b-\1\2\u01c5\u01c6\7\67\2\2\u01c6\u01d1")
        buf.write("\3\2\2\2\u01c7\u01c8\f\5\2\2\u01c8\u01c9\7,\2\2\u01c9")
        buf.write("\u01d0\7\67\2\2\u01ca\u01cb\f\4\2\2\u01cb\u01cc\7\61\2")
        buf.write("\2\u01cc\u01cd\5\n\6\2\u01cd\u01ce\7\62\2\2\u01ce\u01d0")
        buf.write("\3\2\2\2\u01cf\u01c7\3\2\2\2\u01cf\u01ca\3\2\2\2\u01d0")
        buf.write("\u01d3\3\2\2\2\u01d1\u01cf\3\2\2\2\u01d1\u01d2\3\2\2\2")
        buf.write("\u01d2Y\3\2\2\2\u01d3\u01d1\3\2\2\2\u01d4\u01d5\t\n\2")
        buf.write("\2\u01d5[\3\2\2\2\u01d6\u01d7\5X-\2\u01d7\u01d8\5Z.\2")
        buf.write("\u01d8\u01d9\5\n\6\2\u01d9]\3\2\2\2\u01da\u01db\7\3\2")
        buf.write("\2\u01db\u01dc\7-\2\2\u01dc\u01dd\5\n\6\2\u01dd\u01de")
        buf.write("\7.\2\2\u01de\u01df\7/\2\2\u01df\u01e0\5:\36\2\u01e0\u01e1")
        buf.write("\7\60\2\2\u01e1\u01e2\5b\62\2\u01e2\u01e3\5d\63\2\u01e3")
        buf.write("_\3\2\2\2\u01e4\u01e5\7\3\2\2\u01e5\u01e6\7-\2\2\u01e6")
        buf.write("\u01e7\5\n\6\2\u01e7\u01e8\7.\2\2\u01e8\u01e9\7/\2\2\u01e9")
        buf.write("\u01ea\5:\36\2\u01ea\u01eb\7\60\2\2\u01eba\3\2\2\2\u01ec")
        buf.write("\u01ed\7\4\2\2\u01ed\u01ee\5`\61\2\u01ee\u01ef\5b\62\2")
        buf.write("\u01ef\u01f2\3\2\2\2\u01f0\u01f2\3\2\2\2\u01f1\u01ec\3")
        buf.write("\2\2\2\u01f1\u01f0\3\2\2\2\u01f2c\3\2\2\2\u01f3\u01f4")
        buf.write("\7\4\2\2\u01f4\u01f5\7/\2\2\u01f5\u01f6\5:\36\2\u01f6")
        buf.write("\u01f7\7\60\2\2\u01f7\u01fa\3\2\2\2\u01f8\u01fa\3\2\2")
        buf.write("\2\u01f9\u01f3\3\2\2\2\u01f9\u01f8\3\2\2\2\u01fae\3\2")
        buf.write("\2\2\u01fb\u01ff\5h\65\2\u01fc\u01ff\5n8\2\u01fd\u01ff")
        buf.write("\5p9\2\u01fe\u01fb\3\2\2\2\u01fe\u01fc\3\2\2\2\u01fe\u01fd")
        buf.write("\3\2\2\2\u01ffg\3\2\2\2\u0200\u0201\7\5\2\2\u0201\u0202")
        buf.write("\5\n\6\2\u0202\u0203\7/\2\2\u0203\u0204\5:\36\2\u0204")
        buf.write("\u0205\7\60\2\2\u0205i\3\2\2\2\u0206\u0207\7\67\2\2\u0207")
        buf.write("\u0208\5Z.\2\u0208\u0209\5\n\6\2\u0209k\3\2\2\2\u020a")
        buf.write("\u020b\7\20\2\2\u020b\u020c\7\67\2\2\u020c\u020d\5B\"")
        buf.write("\2\u020d\u020e\5D#\2\u020em\3\2\2\2\u020f\u0212\7\5\2")
        buf.write("\2\u0210\u0213\5j\66\2\u0211\u0213\5l\67\2\u0212\u0210")
        buf.write("\3\2\2\2\u0212\u0211\3\2\2\2\u0213\u0214\3\2\2\2\u0214")
        buf.write("\u0215\5\64\33\2\u0215\u0216\5\n\6\2\u0216\u0217\5\64")
        buf.write("\33\2\u0217\u0218\5j\66\2\u0218\u0219\7/\2\2\u0219\u021a")
        buf.write("\5:\36\2\u021a\u021b\7\60\2\2\u021bo\3\2\2\2\u021c\u021d")
        buf.write("\7\5\2\2\u021d\u021e\7\67\2\2\u021e\u021f\7\63\2\2\u021f")
        buf.write("\u0220\7\67\2\2\u0220\u0221\5Z.\2\u0221\u0222\7\23\2\2")
        buf.write("\u0222\u0223\5\n\6\2\u0223\u0224\7/\2\2\u0224\u0225\5")
        buf.write(":\36\2\u0225\u0226\7\60\2\2\u0226q\3\2\2\2\u0227\u022a")
        buf.write("\5t;\2\u0228\u022a\5v<\2\u0229\u0227\3\2\2\2\u0229\u0228")
        buf.write("\3\2\2\2\u022as\3\2\2\2\u022b\u022c\7\67\2\2\u022c\u022d")
        buf.write("\7-\2\2\u022d\u022e\5\32\16\2\u022e\u022f\7.\2\2\u022f")
        buf.write("u\3\2\2\2\u0230\u0231\5X-\2\u0231\u0232\7,\2\2\u0232\u0233")
        buf.write("\7\67\2\2\u0233\u0234\7-\2\2\u0234\u0235\5\32\16\2\u0235")
        buf.write("\u0236\7.\2\2\u0236w\3\2\2\2\u0237\u0238\7\7\2\2\u0238")
        buf.write("\u0239\7\67\2\2\u0239\u023a\7-\2\2\u023a\u023b\5J&\2\u023b")
        buf.write("\u023c\7.\2\2\u023c\u023d\5B\"\2\u023d\u023e\7/\2\2\u023e")
        buf.write("\u023f\5:\36\2\u023f\u0240\7\60\2\2\u0240y\3\2\2\2\u0241")
        buf.write("\u0242\7\7\2\2\u0242\u0243\5|?\2\u0243\u0244\7\67\2\2")
        buf.write("\u0244\u0245\7-\2\2\u0245\u0246\5J&\2\u0246\u0247\7.\2")
        buf.write("\2\u0247\u0248\5B\"\2\u0248\u0249\7/\2\2\u0249\u024a\5")
        buf.write(":\36\2\u024a\u024b\7\60\2\2\u024b{\3\2\2\2\u024c\u024d")
        buf.write("\7-\2\2\u024d\u024e\7\67\2\2\u024e\u024f\7\67\2\2\u024f")
        buf.write("\u0250\7.\2\2\u0250}\3\2\2\2\u0251\u0252\7\b\2\2\u0252")
        buf.write("\u0253\7\67\2\2\u0253\u0254\7\t\2\2\u0254\u0255\7/\2\2")
        buf.write("\u0255\u0256\5\u0080A\2\u0256\u0257\7\60\2\2\u0257\177")
        buf.write("\3\2\2\2\u0258\u0259\5\u0082B\2\u0259\u025a\5\u0080A\2")
        buf.write("\u025a\u025d\3\2\2\2\u025b\u025d\5\u0082B\2\u025c\u0258")
        buf.write("\3\2\2\2\u025c\u025b\3\2\2\2\u025d\u0081\3\2\2\2\u025e")
        buf.write("\u025f\7\67\2\2\u025f\u0260\5@!\2\u0260\u0261\5\64\33")
        buf.write("\2\u0261\u0083\3\2\2\2\u0262\u0263\7\67\2\2\u0263\u0264")
        buf.write("\7-\2\2\u0264\u0265\5J&\2\u0265\u0266\7.\2\2\u0266\u0267")
        buf.write("\5B\"\2\u0267\u0268\5\64\33\2\u0268\u0085\3\2\2\2\u0269")
        buf.write("\u026a\5\u0084C\2\u026a\u026b\5\u0086D\2\u026b\u026e\3")
        buf.write("\2\2\2\u026c\u026e\5\u0084C\2\u026d\u0269\3\2\2\2\u026d")
        buf.write("\u026c\3\2\2\2\u026e\u0087\3\2\2\2\u026f\u0270\7\b\2\2")
        buf.write("\u0270\u0271\7\67\2\2\u0271\u0272\7\n\2\2\u0272\u0273")
        buf.write("\7/\2\2\u0273\u0274\5\u0086D\2\u0274\u0275\7\60\2\2\u0275")
        buf.write("\u0089\3\2\2\2,\u008d\u009a\u00a8\u00b3\u00be\u00c9\u00d4")
        buf.write("\u00da\u00e3\u00f4\u00f6\u00fc\u0100\u0107\u0110\u0117")
        buf.write("\u0121\u012f\u0136\u014c\u0150\u015f\u016c\u0174\u0184")
        buf.write("\u0188\u018f\u019b\u01a0\u01a9\u01b3\u01b9\u01be\u01cf")
        buf.write("\u01d1\u01f1\u01f9\u01fe\u0212\u0229\u025c\u026d")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'for'", "'return'", 
                     "'func'", "'type'", "'struct'", "'interface'", "'string'", 
                     "'int'", "'float'", "'boolean'", "'const'", "'var'", 
                     "'continue'", "'break'", "'range'", "'nil'", "'true'", 
                     "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "':='", 
                     "'+='", "'-='", "'*='", "'/='", "'%='", "'='", "'&&'", 
                     "'||'", "'!'", "'=='", "'!='", "'<'", "'<='", "'>'", 
                     "'>='", "'.'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
                      "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", 
                      "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", 
                      "NIL", "TRUE", "FALSE", "ADD", "SUB", "MUL", "DIV", 
                      "MOD", "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", 
                      "DIV_ASSIGN", "MOD_ASSIGN", "INIT", "AND", "OR", "NOT", 
                      "EQUAL", "NOT_EQUAL", "LESS", "LESS_OR_EQUAL", "GREATER", 
                      "GREATER_OR_EQUAL", "DOT", "LPAREN", "RPAREN", "LBRACEBRACK", 
                      "RBRACEBRACK", "LSQUAREBRACK", "RSQUAREBRACK", "COMMA", 
                      "SEMICOLON", "COLON", "NEW_LINE", "ID", "DECINT_LIT", 
                      "BININT_LIT", "OCTINT_LIT", "HEXINT_LIT", "FLOAT_LIT", 
                      "STRING_LIT", "SKIP_TOKENS", "COMMENT_SINGLE_LINE", 
                      "COMMENT_MULTI_LINE", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_number = 1
    RULE_literal = 2
    RULE_grouped_expression = 3
    RULE_expression1 = 4
    RULE_expression2 = 5
    RULE_expression3 = 6
    RULE_expression4 = 7
    RULE_expression5 = 8
    RULE_expression6 = 9
    RULE_expression7 = 10
    RULE_final_expression = 11
    RULE_expression_list = 12
    RULE_expression_part = 13
    RULE_literal_inside_array = 14
    RULE_list_literal = 15
    RULE_dimension_part = 16
    RULE_dimension_list = 17
    RULE_nested_array_element_list = 18
    RULE_list_nested_array_element_list = 19
    RULE_array_element_list = 20
    RULE_array_literal = 21
    RULE_field_element = 22
    RULE_field_list = 23
    RULE_struct_literal = 24
    RULE_end_statement = 25
    RULE_declared = 26
    RULE_statement = 27
    RULE_statement_list = 28
    RULE_const_declared_statement = 29
    RULE_array_type = 30
    RULE_required_type = 31
    RULE_optional_type = 32
    RULE_required_initial_expression = 33
    RULE_optional_initial_expression = 34
    RULE_variable_declared_statement = 35
    RULE_optional_parameter_list = 36
    RULE_separated_parameter_list = 37
    RULE_grouped_parameter_list = 38
    RULE_variable_list = 39
    RULE_return_statement = 40
    RULE_break_statement = 41
    RULE_continue_statement = 42
    RULE_lhs = 43
    RULE_assign_operator = 44
    RULE_assignment_statement = 45
    RULE_if_statement = 46
    RULE_if_in_else_if_statement = 47
    RULE_else_if_statement_list = 48
    RULE_else_statement = 49
    RULE_for_statement = 50
    RULE_for_condition = 51
    RULE_for_assignment_statement = 52
    RULE_for_variable_declared_statement = 53
    RULE_for_initialization_declaration = 54
    RULE_for_range = 55
    RULE_call_statement = 56
    RULE_function_call_statement = 57
    RULE_method_call_statement = 58
    RULE_function_declared_statement = 59
    RULE_method_declared_statement = 60
    RULE_method_receiver = 61
    RULE_struct_declared_statement = 62
    RULE_list_field_declared_statement = 63
    RULE_field_declared_statement = 64
    RULE_function_interface_declared_statement = 65
    RULE_list_function_declared_interface = 66
    RULE_interface_declared_statement = 67

    ruleNames =  [ "program", "number", "literal", "grouped_expression", 
                   "expression1", "expression2", "expression3", "expression4", 
                   "expression5", "expression6", "expression7", "final_expression", 
                   "expression_list", "expression_part", "literal_inside_array", 
                   "list_literal", "dimension_part", "dimension_list", "nested_array_element_list", 
                   "list_nested_array_element_list", "array_element_list", 
                   "array_literal", "field_element", "field_list", "struct_literal", 
                   "end_statement", "declared", "statement", "statement_list", 
                   "const_declared_statement", "array_type", "required_type", 
                   "optional_type", "required_initial_expression", "optional_initial_expression", 
                   "variable_declared_statement", "optional_parameter_list", 
                   "separated_parameter_list", "grouped_parameter_list", 
                   "variable_list", "return_statement", "break_statement", 
                   "continue_statement", "lhs", "assign_operator", "assignment_statement", 
                   "if_statement", "if_in_else_if_statement", "else_if_statement_list", 
                   "else_statement", "for_statement", "for_condition", "for_assignment_statement", 
                   "for_variable_declared_statement", "for_initialization_declaration", 
                   "for_range", "call_statement", "function_call_statement", 
                   "method_call_statement", "function_declared_statement", 
                   "method_declared_statement", "method_receiver", "struct_declared_statement", 
                   "list_field_declared_statement", "field_declared_statement", 
                   "function_interface_declared_statement", "list_function_declared_interface", 
                   "interface_declared_statement" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    FOR=3
    RETURN=4
    FUNC=5
    TYPE=6
    STRUCT=7
    INTERFACE=8
    STRING=9
    INT=10
    FLOAT=11
    BOOLEAN=12
    CONST=13
    VAR=14
    CONTINUE=15
    BREAK=16
    RANGE=17
    NIL=18
    TRUE=19
    FALSE=20
    ADD=21
    SUB=22
    MUL=23
    DIV=24
    MOD=25
    ASSIGN=26
    ADD_ASSIGN=27
    SUB_ASSIGN=28
    MUL_ASSIGN=29
    DIV_ASSIGN=30
    MOD_ASSIGN=31
    INIT=32
    AND=33
    OR=34
    NOT=35
    EQUAL=36
    NOT_EQUAL=37
    LESS=38
    LESS_OR_EQUAL=39
    GREATER=40
    GREATER_OR_EQUAL=41
    DOT=42
    LPAREN=43
    RPAREN=44
    LBRACEBRACK=45
    RBRACEBRACK=46
    LSQUAREBRACK=47
    RSQUAREBRACK=48
    COMMA=49
    SEMICOLON=50
    COLON=51
    NEW_LINE=52
    ID=53
    DECINT_LIT=54
    BININT_LIT=55
    OCTINT_LIT=56
    HEXINT_LIT=57
    FLOAT_LIT=58
    STRING_LIT=59
    SKIP_TOKENS=60
    COMMENT_SINGLE_LINE=61
    COMMENT_MULTI_LINE=62
    UNCLOSE_STRING=63
    ILLEGAL_ESCAPE=64
    ERROR_CHAR=65

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def declared(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DeclaredContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DeclaredContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 136
                self.declared()
                self.state = 139 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR))) != 0)):
                    break

            self.state = 141
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECINT_LIT(self):
            return self.getToken(MiniGoParser.DECINT_LIT, 0)

        def OCTINT_LIT(self):
            return self.getToken(MiniGoParser.OCTINT_LIT, 0)

        def HEXINT_LIT(self):
            return self.getToken(MiniGoParser.HEXINT_LIT, 0)

        def BININT_LIT(self):
            return self.getToken(MiniGoParser.BININT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_number

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = MiniGoParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.DECINT_LIT) | (1 << MiniGoParser.BININT_LIT) | (1 << MiniGoParser.OCTINT_LIT) | (1 << MiniGoParser.HEXINT_LIT) | (1 << MiniGoParser.FLOAT_LIT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(MiniGoParser.NumberContext,0)


        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literalContext,0)


        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_literal)
        try:
            self.state = 152
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.DECINT_LIT, MiniGoParser.BININT_LIT, MiniGoParser.OCTINT_LIT, MiniGoParser.HEXINT_LIT, MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.number()
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [MiniGoParser.TRUE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 147
                self.match(MiniGoParser.TRUE)
                pass
            elif token in [MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 148
                self.match(MiniGoParser.FALSE)
                pass
            elif token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 149
                self.match(MiniGoParser.NIL)
                pass
            elif token in [MiniGoParser.LSQUAREBRACK]:
                self.enterOuterAlt(localctx, 6)
                self.state = 150
                self.array_literal()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 7)
                self.state = 151
                self.struct_literal()
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


    class Grouped_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_grouped_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGrouped_expression" ):
                return visitor.visitGrouped_expression(self)
            else:
                return visitor.visitChildren(self)




    def grouped_expression(self):

        localctx = MiniGoParser.Grouped_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_grouped_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(MiniGoParser.LPAREN)
            self.state = 155
            self.expression1(0)
            self.state = 156
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self):
            return self.getTypedRuleContext(MiniGoParser.Expression2Context,0)


        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression1" ):
                return visitor.visitExpression1(self)
            else:
                return visitor.visitChildren(self)



    def expression1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expression1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.expression2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 166
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression1)
                    self.state = 161
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 162
                    self.match(MiniGoParser.OR)
                    self.state = 163
                    self.expression2(0) 
                self.state = 168
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression3(self):
            return self.getTypedRuleContext(MiniGoParser.Expression3Context,0)


        def expression2(self):
            return self.getTypedRuleContext(MiniGoParser.Expression2Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression2" ):
                return visitor.visitExpression2(self)
            else:
                return visitor.visitChildren(self)



    def expression2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expression2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 177
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 172
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 173
                    self.match(MiniGoParser.AND)
                    self.state = 174
                    self.expression3(0) 
                self.state = 179
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression4(self):
            return self.getTypedRuleContext(MiniGoParser.Expression4Context,0)


        def expression3(self):
            return self.getTypedRuleContext(MiniGoParser.Expression3Context,0)


        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(MiniGoParser.NOT_EQUAL, 0)

        def LESS(self):
            return self.getToken(MiniGoParser.LESS, 0)

        def LESS_OR_EQUAL(self):
            return self.getToken(MiniGoParser.LESS_OR_EQUAL, 0)

        def GREATER(self):
            return self.getToken(MiniGoParser.GREATER, 0)

        def GREATER_OR_EQUAL(self):
            return self.getToken(MiniGoParser.GREATER_OR_EQUAL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression3" ):
                return visitor.visitExpression3(self)
            else:
                return visitor.visitChildren(self)



    def expression3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 188
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 183
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 184
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQUAL) | (1 << MiniGoParser.NOT_EQUAL) | (1 << MiniGoParser.LESS) | (1 << MiniGoParser.LESS_OR_EQUAL) | (1 << MiniGoParser.GREATER) | (1 << MiniGoParser.GREATER_OR_EQUAL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 185
                    self.expression4(0) 
                self.state = 190
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(MiniGoParser.Expression5Context,0)


        def expression4(self):
            return self.getTypedRuleContext(MiniGoParser.Expression4Context,0)


        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression4" ):
                return visitor.visitExpression4(self)
            else:
                return visitor.visitChildren(self)



    def expression4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.expression5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 199
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 194
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 195
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 196
                    self.expression5(0) 
                self.state = 201
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def expression5(self):
            return self.getTypedRuleContext(MiniGoParser.Expression5Context,0)


        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression5" ):
                return visitor.visitExpression5(self)
            else:
                return visitor.visitChildren(self)



    def expression5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expression5, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.expression6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 210
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression5)
                    self.state = 205
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 206
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 207
                    self.expression6() 
                self.state = 212
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def expression7(self):
            return self.getTypedRuleContext(MiniGoParser.Expression7Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression6" ):
                return visitor.visitExpression6(self)
            else:
                return visitor.visitChildren(self)




    def expression6(self):

        localctx = MiniGoParser.Expression6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expression6)
        self._la = 0 # Token type
        try:
            self.state = 216
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SUB, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SUB or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 214
                self.expression6()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LPAREN, MiniGoParser.LSQUAREBRACK, MiniGoParser.ID, MiniGoParser.DECINT_LIT, MiniGoParser.BININT_LIT, MiniGoParser.OCTINT_LIT, MiniGoParser.HEXINT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.expression7(0)
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


    class Expression7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression_list(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_listContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def final_expression(self):
            return self.getTypedRuleContext(MiniGoParser.Final_expressionContext,0)


        def expression7(self):
            return self.getTypedRuleContext(MiniGoParser.Expression7Context,0)


        def LSQUAREBRACK(self):
            return self.getToken(MiniGoParser.LSQUAREBRACK, 0)

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def RSQUAREBRACK(self):
            return self.getToken(MiniGoParser.RSQUAREBRACK, 0)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression7" ):
                return visitor.visitExpression7(self)
            else:
                return visitor.visitChildren(self)



    def expression7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expression7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 219
                self.match(MiniGoParser.ID)
                self.state = 220
                self.match(MiniGoParser.LPAREN)
                self.state = 221
                self.expression_list()
                self.state = 222
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 2:
                self.state = 224
                self.final_expression()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 244
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 242
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expression7Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression7)
                        self.state = 227
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 228
                        self.match(MiniGoParser.LSQUAREBRACK)
                        self.state = 229
                        self.expression1(0)
                        self.state = 230
                        self.match(MiniGoParser.RSQUAREBRACK)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expression7Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression7)
                        self.state = 232
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 233
                        self.match(MiniGoParser.DOT)
                        self.state = 234
                        self.match(MiniGoParser.ID)
                        self.state = 235
                        self.match(MiniGoParser.LPAREN)
                        self.state = 236
                        self.expression_list()
                        self.state = 237
                        self.match(MiniGoParser.RPAREN)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expression7Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression7)
                        self.state = 239
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 240
                        self.match(MiniGoParser.DOT)
                        self.state = 241
                        self.match(MiniGoParser.ID)
                        pass

             
                self.state = 246
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Final_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def grouped_expression(self):
            return self.getTypedRuleContext(MiniGoParser.Grouped_expressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_final_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFinal_expression" ):
                return visitor.visitFinal_expression(self)
            else:
                return visitor.visitChildren(self)




    def final_expression(self):

        localctx = MiniGoParser.Final_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_final_expression)
        try:
            self.state = 250
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 249
                self.grouped_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_part(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_partContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_list" ):
                return visitor.visitExpression_list(self)
            else:
                return visitor.visitChildren(self)




    def expression_list(self):

        localctx = MiniGoParser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expression_list)
        try:
            self.state = 254
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB, MiniGoParser.NOT, MiniGoParser.LPAREN, MiniGoParser.LSQUAREBRACK, MiniGoParser.ID, MiniGoParser.DECINT_LIT, MiniGoParser.BININT_LIT, MiniGoParser.OCTINT_LIT, MiniGoParser.HEXINT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                self.expression_part()
                pass
            elif token in [MiniGoParser.RPAREN]:
                self.enterOuterAlt(localctx, 2)

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


    class Expression_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def expression_part(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_partContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_part" ):
                return visitor.visitExpression_part(self)
            else:
                return visitor.visitChildren(self)




    def expression_part(self):

        localctx = MiniGoParser.Expression_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expression_part)
        try:
            self.state = 261
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.expression1(0)
                self.state = 257
                self.match(MiniGoParser.COMMA)
                self.state = 258
                self.expression_part()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 260
                self.expression1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_inside_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def number(self):
            return self.getTypedRuleContext(MiniGoParser.NumberContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literal_inside_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral_inside_array" ):
                return visitor.visitLiteral_inside_array(self)
            else:
                return visitor.visitChildren(self)




    def literal_inside_array(self):

        localctx = MiniGoParser.Literal_inside_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_literal_inside_array)
        try:
            self.state = 270
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
                self.struct_literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 265
                self.match(MiniGoParser.STRING_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 266
                self.match(MiniGoParser.TRUE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 267
                self.match(MiniGoParser.FALSE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 268
                self.match(MiniGoParser.NIL)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 269
                self.number()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal_inside_array(self):
            return self.getTypedRuleContext(MiniGoParser.Literal_inside_arrayContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_literal(self):
            return self.getTypedRuleContext(MiniGoParser.List_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_literal" ):
                return visitor.visitList_literal(self)
            else:
                return visitor.visitChildren(self)




    def list_literal(self):

        localctx = MiniGoParser.List_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_list_literal)
        try:
            self.state = 277
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 272
                self.literal_inside_array()
                self.state = 273
                self.match(MiniGoParser.COMMA)
                self.state = 274
                self.list_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
                self.literal_inside_array()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dimension_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSQUAREBRACK(self):
            return self.getToken(MiniGoParser.LSQUAREBRACK, 0)

        def RSQUAREBRACK(self):
            return self.getToken(MiniGoParser.RSQUAREBRACK, 0)

        def DECINT_LIT(self):
            return self.getToken(MiniGoParser.DECINT_LIT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_dimension_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimension_part" ):
                return visitor.visitDimension_part(self)
            else:
                return visitor.visitChildren(self)




    def dimension_part(self):

        localctx = MiniGoParser.Dimension_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_dimension_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(MiniGoParser.LSQUAREBRACK)
            self.state = 280
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.ID or _la==MiniGoParser.DECINT_LIT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 281
            self.match(MiniGoParser.RSQUAREBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dimension_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimension_part(self):
            return self.getTypedRuleContext(MiniGoParser.Dimension_partContext,0)


        def dimension_list(self):
            return self.getTypedRuleContext(MiniGoParser.Dimension_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_dimension_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimension_list" ):
                return visitor.visitDimension_list(self)
            else:
                return visitor.visitChildren(self)




    def dimension_list(self):

        localctx = MiniGoParser.Dimension_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_dimension_list)
        try:
            self.state = 287
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                self.dimension_part()
                self.state = 284
                self.dimension_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 286
                self.dimension_part()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Nested_array_element_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_literal(self):
            return self.getTypedRuleContext(MiniGoParser.List_literalContext,0)


        def LBRACEBRACK(self):
            return self.getToken(MiniGoParser.LBRACEBRACK, 0)

        def nested_array_element_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Nested_array_element_listContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Nested_array_element_listContext,i)


        def RBRACEBRACK(self):
            return self.getToken(MiniGoParser.RBRACEBRACK, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_nested_array_element_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNested_array_element_list" ):
                return visitor.visitNested_array_element_list(self)
            else:
                return visitor.visitChildren(self)



    def nested_array_element_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Nested_array_element_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_nested_array_element_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 290
                self.list_literal()
                pass

            elif la_ == 2:
                self.state = 291
                self.match(MiniGoParser.LBRACEBRACK)
                self.state = 292
                self.nested_array_element_list(0)
                self.state = 293
                self.match(MiniGoParser.RBRACEBRACK)
                self.state = 294
                self.match(MiniGoParser.COMMA)
                self.state = 295
                self.nested_array_element_list(2)
                pass

            elif la_ == 3:
                self.state = 297
                self.match(MiniGoParser.LBRACEBRACK)
                self.state = 298
                self.nested_array_element_list(0)
                self.state = 299
                self.match(MiniGoParser.RBRACEBRACK)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 308
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Nested_array_element_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_nested_array_element_list)
                    self.state = 303
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 304
                    self.match(MiniGoParser.COMMA)
                    self.state = 305
                    self.nested_array_element_list(4) 
                self.state = 310
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class List_nested_array_element_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nested_array_element_list(self):
            return self.getTypedRuleContext(MiniGoParser.Nested_array_element_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_nested_array_element_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_nested_array_element_list" ):
                return visitor.visitList_nested_array_element_list(self)
            else:
                return visitor.visitChildren(self)




    def list_nested_array_element_list(self):

        localctx = MiniGoParser.List_nested_array_element_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_list_nested_array_element_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.nested_array_element_list(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_element_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACEBRACK(self):
            return self.getToken(MiniGoParser.LBRACEBRACK, 0)

        def list_nested_array_element_list(self):
            return self.getTypedRuleContext(MiniGoParser.List_nested_array_element_listContext,0)


        def RBRACEBRACK(self):
            return self.getToken(MiniGoParser.RBRACEBRACK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_element_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_element_list" ):
                return visitor.visitArray_element_list(self)
            else:
                return visitor.visitChildren(self)




    def array_element_list(self):

        localctx = MiniGoParser.Array_element_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_array_element_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.match(MiniGoParser.LBRACEBRACK)
            self.state = 314
            self.list_nested_array_element_list()
            self.state = 315
            self.match(MiniGoParser.RBRACEBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimension_list(self):
            return self.getTypedRuleContext(MiniGoParser.Dimension_listContext,0)


        def array_element_list(self):
            return self.getTypedRuleContext(MiniGoParser.Array_element_listContext,0)


        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = MiniGoParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_array_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.dimension_list()
            self.state = 318
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 319
            self.array_element_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def field_element(self):
            return self.getTypedRuleContext(MiniGoParser.Field_elementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_field_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField_element" ):
                return visitor.visitField_element(self)
            else:
                return visitor.visitChildren(self)




    def field_element(self):

        localctx = MiniGoParser.Field_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_field_element)
        try:
            self.state = 330
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 321
                self.match(MiniGoParser.ID)
                self.state = 322
                self.match(MiniGoParser.COLON)
                self.state = 323
                self.expression1(0)
                self.state = 324
                self.match(MiniGoParser.COMMA)
                self.state = 325
                self.field_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 327
                self.match(MiniGoParser.ID)
                self.state = 328
                self.match(MiniGoParser.COLON)
                self.state = 329
                self.expression1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_element(self):
            return self.getTypedRuleContext(MiniGoParser.Field_elementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_field_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField_list" ):
                return visitor.visitField_list(self)
            else:
                return visitor.visitChildren(self)




    def field_list(self):

        localctx = MiniGoParser.Field_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_field_list)
        try:
            self.state = 334
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self.field_element()
                pass
            elif token in [MiniGoParser.RBRACEBRACK]:
                self.enterOuterAlt(localctx, 2)

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


    class Struct_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LBRACEBRACK(self):
            return self.getToken(MiniGoParser.LBRACEBRACK, 0)

        def field_list(self):
            return self.getTypedRuleContext(MiniGoParser.Field_listContext,0)


        def RBRACEBRACK(self):
            return self.getToken(MiniGoParser.RBRACEBRACK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_literal" ):
                return visitor.visitStruct_literal(self)
            else:
                return visitor.visitChildren(self)




    def struct_literal(self):

        localctx = MiniGoParser.Struct_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_struct_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(MiniGoParser.ID)
            self.state = 337
            self.match(MiniGoParser.LBRACEBRACK)
            self.state = 338
            self.field_list()
            self.state = 339
            self.match(MiniGoParser.RBRACEBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class End_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def NEW_LINE(self):
            return self.getToken(MiniGoParser.NEW_LINE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_end_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnd_statement" ):
                return visitor.visitEnd_statement(self)
            else:
                return visitor.visitChildren(self)




    def end_statement(self):

        localctx = MiniGoParser.End_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_end_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NEW_LINE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def end_statement(self):
            return self.getTypedRuleContext(MiniGoParser.End_statementContext,0)


        def const_declared_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declared_statementContext,0)


        def variable_declared_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Variable_declared_statementContext,0)


        def function_declared_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Function_declared_statementContext,0)


        def method_declared_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Method_declared_statementContext,0)


        def struct_declared_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declared_statementContext,0)


        def interface_declared_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_declared_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclared" ):
                return visitor.visitDeclared(self)
            else:
                return visitor.visitChildren(self)




    def declared(self):

        localctx = MiniGoParser.DeclaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_declared)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 343
                self.const_declared_statement()
                pass

            elif la_ == 2:
                self.state = 344
                self.variable_declared_statement()
                pass

            elif la_ == 3:
                self.state = 345
                self.function_declared_statement()
                pass

            elif la_ == 4:
                self.state = 346
                self.method_declared_statement()
                pass

            elif la_ == 5:
                self.state = 347
                self.struct_declared_statement()
                pass

            elif la_ == 6:
                self.state = 348
                self.interface_declared_statement()
                pass


            self.state = 351
            self.end_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def end_statement(self):
            return self.getTypedRuleContext(MiniGoParser.End_statementContext,0)


        def const_declared_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declared_statementContext,0)


        def variable_declared_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Variable_declared_statementContext,0)


        def assignment_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(MiniGoParser.For_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Return_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(MiniGoParser.If_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_statementContext,0)


        def call_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Call_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 353
                self.const_declared_statement()
                pass

            elif la_ == 2:
                self.state = 354
                self.variable_declared_statement()
                pass

            elif la_ == 3:
                self.state = 355
                self.assignment_statement()
                pass

            elif la_ == 4:
                self.state = 356
                self.for_statement()
                pass

            elif la_ == 5:
                self.state = 357
                self.return_statement()
                pass

            elif la_ == 6:
                self.state = 358
                self.if_statement()
                pass

            elif la_ == 7:
                self.state = 359
                self.break_statement()
                pass

            elif la_ == 8:
                self.state = 360
                self.continue_statement()
                pass

            elif la_ == 9:
                self.state = 361
                self.call_statement()
                pass


            self.state = 364
            self.end_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(MiniGoParser.Statement_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_list" ):
                return visitor.visitStatement_list(self)
            else:
                return visitor.visitChildren(self)




    def statement_list(self):

        localctx = MiniGoParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_statement_list)
        try:
            self.state = 370
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 366
                self.statement()
                self.state = 367
                self.statement_list()
                pass
            elif token in [MiniGoParser.RBRACEBRACK]:
                self.enterOuterAlt(localctx, 2)

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


    class Const_declared_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INIT(self):
            return self.getToken(MiniGoParser.INIT, 0)

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_const_declared_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_declared_statement" ):
                return visitor.visitConst_declared_statement(self)
            else:
                return visitor.visitChildren(self)




    def const_declared_statement(self):

        localctx = MiniGoParser.Const_declared_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_const_declared_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.match(MiniGoParser.CONST)
            self.state = 373
            self.match(MiniGoParser.ID)
            self.state = 374
            self.match(MiniGoParser.INIT)
            self.state = 375
            self.expression1(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimension_list(self):
            return self.getTypedRuleContext(MiniGoParser.Dimension_listContext,0)


        def required_type(self):
            return self.getTypedRuleContext(MiniGoParser.Required_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = MiniGoParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.dimension_list()
            self.state = 378
            self.required_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Required_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_required_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRequired_type" ):
                return visitor.visitRequired_type(self)
            else:
                return visitor.visitChildren(self)




    def required_type(self):

        localctx = MiniGoParser.Required_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_required_type)
        try:
            self.state = 386
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 380
                self.match(MiniGoParser.INT)
                pass
            elif token in [MiniGoParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 381
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [MiniGoParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 382
                self.match(MiniGoParser.STRING)
                pass
            elif token in [MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 383
                self.match(MiniGoParser.BOOLEAN)
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 384
                self.match(MiniGoParser.ID)
                pass
            elif token in [MiniGoParser.LSQUAREBRACK]:
                self.enterOuterAlt(localctx, 6)
                self.state = 385
                self.array_type()
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


    class Optional_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def required_type(self):
            return self.getTypedRuleContext(MiniGoParser.Required_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_optional_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptional_type" ):
                return visitor.visitOptional_type(self)
            else:
                return visitor.visitChildren(self)




    def optional_type(self):

        localctx = MiniGoParser.Optional_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_optional_type)
        try:
            self.state = 390
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LSQUAREBRACK, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 388
                self.required_type()
                pass
            elif token in [MiniGoParser.INIT, MiniGoParser.LBRACEBRACK, MiniGoParser.SEMICOLON, MiniGoParser.NEW_LINE]:
                self.enterOuterAlt(localctx, 2)

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


    class Required_initial_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INIT(self):
            return self.getToken(MiniGoParser.INIT, 0)

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_required_initial_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRequired_initial_expression" ):
                return visitor.visitRequired_initial_expression(self)
            else:
                return visitor.visitChildren(self)




    def required_initial_expression(self):

        localctx = MiniGoParser.Required_initial_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_required_initial_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.match(MiniGoParser.INIT)
            self.state = 393
            self.expression1(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Optional_initial_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def required_initial_expression(self):
            return self.getTypedRuleContext(MiniGoParser.Required_initial_expressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_optional_initial_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptional_initial_expression" ):
                return visitor.visitOptional_initial_expression(self)
            else:
                return visitor.visitChildren(self)




    def optional_initial_expression(self):

        localctx = MiniGoParser.Optional_initial_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_optional_initial_expression)
        try:
            self.state = 397
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 395
                self.required_initial_expression()
                pass
            elif token in [MiniGoParser.SEMICOLON, MiniGoParser.NEW_LINE]:
                self.enterOuterAlt(localctx, 2)

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


    class Variable_declared_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def required_type(self):
            return self.getTypedRuleContext(MiniGoParser.Required_typeContext,0)


        def optional_initial_expression(self):
            return self.getTypedRuleContext(MiniGoParser.Optional_initial_expressionContext,0)


        def optional_type(self):
            return self.getTypedRuleContext(MiniGoParser.Optional_typeContext,0)


        def required_initial_expression(self):
            return self.getTypedRuleContext(MiniGoParser.Required_initial_expressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_variable_declared_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_declared_statement" ):
                return visitor.visitVariable_declared_statement(self)
            else:
                return visitor.visitChildren(self)




    def variable_declared_statement(self):

        localctx = MiniGoParser.Variable_declared_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_variable_declared_statement)
        try:
            self.state = 409
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 399
                self.match(MiniGoParser.VAR)
                self.state = 400
                self.match(MiniGoParser.ID)
                self.state = 401
                self.required_type()
                self.state = 402
                self.optional_initial_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 404
                self.match(MiniGoParser.VAR)
                self.state = 405
                self.match(MiniGoParser.ID)
                self.state = 406
                self.optional_type()
                self.state = 407
                self.required_initial_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Optional_parameter_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def separated_parameter_list(self):
            return self.getTypedRuleContext(MiniGoParser.Separated_parameter_listContext,0)


        def grouped_parameter_list(self):
            return self.getTypedRuleContext(MiniGoParser.Grouped_parameter_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_optional_parameter_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptional_parameter_list" ):
                return visitor.visitOptional_parameter_list(self)
            else:
                return visitor.visitChildren(self)




    def optional_parameter_list(self):

        localctx = MiniGoParser.Optional_parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_optional_parameter_list)
        try:
            self.state = 414
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 411
                self.separated_parameter_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 412
                self.grouped_parameter_list()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Separated_parameter_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def required_type(self):
            return self.getTypedRuleContext(MiniGoParser.Required_typeContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def separated_parameter_list(self):
            return self.getTypedRuleContext(MiniGoParser.Separated_parameter_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_separated_parameter_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeparated_parameter_list" ):
                return visitor.visitSeparated_parameter_list(self)
            else:
                return visitor.visitChildren(self)




    def separated_parameter_list(self):

        localctx = MiniGoParser.Separated_parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_separated_parameter_list)
        try:
            self.state = 423
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 416
                self.match(MiniGoParser.ID)
                self.state = 417
                self.required_type()
                self.state = 418
                self.match(MiniGoParser.COMMA)
                self.state = 419
                self.separated_parameter_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 421
                self.match(MiniGoParser.ID)
                self.state = 422
                self.required_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Grouped_parameter_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_list(self):
            return self.getTypedRuleContext(MiniGoParser.Variable_listContext,0)


        def required_type(self):
            return self.getTypedRuleContext(MiniGoParser.Required_typeContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def grouped_parameter_list(self):
            return self.getTypedRuleContext(MiniGoParser.Grouped_parameter_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_grouped_parameter_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGrouped_parameter_list" ):
                return visitor.visitGrouped_parameter_list(self)
            else:
                return visitor.visitChildren(self)




    def grouped_parameter_list(self):

        localctx = MiniGoParser.Grouped_parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_grouped_parameter_list)
        try:
            self.state = 433
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 425
                self.variable_list()
                self.state = 426
                self.required_type()
                self.state = 427
                self.match(MiniGoParser.COMMA)
                self.state = 428
                self.grouped_parameter_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 430
                self.variable_list()
                self.state = 431
                self.required_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def variable_list(self):
            return self.getTypedRuleContext(MiniGoParser.Variable_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_variable_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_list" ):
                return visitor.visitVariable_list(self)
            else:
                return visitor.visitChildren(self)




    def variable_list(self):

        localctx = MiniGoParser.Variable_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_variable_list)
        try:
            self.state = 439
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 435
                self.match(MiniGoParser.ID)
                self.state = 436
                self.match(MiniGoParser.COMMA)
                self.state = 437
                self.variable_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 438
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = MiniGoParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_return_statement)
        try:
            self.state = 444
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 441
                self.match(MiniGoParser.RETURN)
                self.state = 442
                self.expression1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 443
                self.match(MiniGoParser.RETURN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = MiniGoParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 446
            self.match(MiniGoParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = MiniGoParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448
            self.match(MiniGoParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def LSQUAREBRACK(self):
            return self.getToken(MiniGoParser.LSQUAREBRACK, 0)

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def RSQUAREBRACK(self):
            return self.getToken(MiniGoParser.RSQUAREBRACK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)



    def lhs(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.LhsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_lhs, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.match(MiniGoParser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 463
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 461
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.LhsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                        self.state = 453
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 454
                        self.match(MiniGoParser.DOT)
                        self.state = 455
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.LhsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                        self.state = 456
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 457
                        self.match(MiniGoParser.LSQUAREBRACK)
                        self.state = 458
                        self.expression1(0)
                        self.state = 459
                        self.match(MiniGoParser.RSQUAREBRACK)
                        pass

             
                self.state = 465
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Assign_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def ADD_ASSIGN(self):
            return self.getToken(MiniGoParser.ADD_ASSIGN, 0)

        def SUB_ASSIGN(self):
            return self.getToken(MiniGoParser.SUB_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(MiniGoParser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(MiniGoParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(MiniGoParser.MOD_ASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_operator" ):
                return visitor.visitAssign_operator(self)
            else:
                return visitor.visitChildren(self)




    def assign_operator(self):

        localctx = MiniGoParser.Assign_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_assign_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASSIGN) | (1 << MiniGoParser.ADD_ASSIGN) | (1 << MiniGoParser.SUB_ASSIGN) | (1 << MiniGoParser.MUL_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def assign_operator(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_operatorContext,0)


        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_statement" ):
                return visitor.visitAssignment_statement(self)
            else:
                return visitor.visitChildren(self)




    def assignment_statement(self):

        localctx = MiniGoParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.lhs(0)
            self.state = 469
            self.assign_operator()
            self.state = 470
            self.expression1(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def LBRACEBRACK(self):
            return self.getToken(MiniGoParser.LBRACEBRACK, 0)

        def statement_list(self):
            return self.getTypedRuleContext(MiniGoParser.Statement_listContext,0)


        def RBRACEBRACK(self):
            return self.getToken(MiniGoParser.RBRACEBRACK, 0)

        def else_if_statement_list(self):
            return self.getTypedRuleContext(MiniGoParser.Else_if_statement_listContext,0)


        def else_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Else_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = MiniGoParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            self.match(MiniGoParser.IF)
            self.state = 473
            self.match(MiniGoParser.LPAREN)
            self.state = 474
            self.expression1(0)
            self.state = 475
            self.match(MiniGoParser.RPAREN)
            self.state = 476
            self.match(MiniGoParser.LBRACEBRACK)
            self.state = 477
            self.statement_list()
            self.state = 478
            self.match(MiniGoParser.RBRACEBRACK)
            self.state = 479
            self.else_if_statement_list()
            self.state = 480
            self.else_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_in_else_if_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def LBRACEBRACK(self):
            return self.getToken(MiniGoParser.LBRACEBRACK, 0)

        def statement_list(self):
            return self.getTypedRuleContext(MiniGoParser.Statement_listContext,0)


        def RBRACEBRACK(self):
            return self.getToken(MiniGoParser.RBRACEBRACK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_if_in_else_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_in_else_if_statement" ):
                return visitor.visitIf_in_else_if_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_in_else_if_statement(self):

        localctx = MiniGoParser.If_in_else_if_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_if_in_else_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 482
            self.match(MiniGoParser.IF)
            self.state = 483
            self.match(MiniGoParser.LPAREN)
            self.state = 484
            self.expression1(0)
            self.state = 485
            self.match(MiniGoParser.RPAREN)
            self.state = 486
            self.match(MiniGoParser.LBRACEBRACK)
            self.state = 487
            self.statement_list()
            self.state = 488
            self.match(MiniGoParser.RBRACEBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_if_statement_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def if_in_else_if_statement(self):
            return self.getTypedRuleContext(MiniGoParser.If_in_else_if_statementContext,0)


        def else_if_statement_list(self):
            return self.getTypedRuleContext(MiniGoParser.Else_if_statement_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_if_statement_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_if_statement_list" ):
                return visitor.visitElse_if_statement_list(self)
            else:
                return visitor.visitChildren(self)




    def else_if_statement_list(self):

        localctx = MiniGoParser.Else_if_statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_else_if_statement_list)
        try:
            self.state = 495
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 490
                self.match(MiniGoParser.ELSE)
                self.state = 491
                self.if_in_else_if_statement()
                self.state = 492
                self.else_if_statement_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def LBRACEBRACK(self):
            return self.getToken(MiniGoParser.LBRACEBRACK, 0)

        def statement_list(self):
            return self.getTypedRuleContext(MiniGoParser.Statement_listContext,0)


        def RBRACEBRACK(self):
            return self.getToken(MiniGoParser.RBRACEBRACK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_else_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_statement" ):
                return visitor.visitElse_statement(self)
            else:
                return visitor.visitChildren(self)




    def else_statement(self):

        localctx = MiniGoParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_else_statement)
        try:
            self.state = 503
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ELSE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 497
                self.match(MiniGoParser.ELSE)
                self.state = 498
                self.match(MiniGoParser.LBRACEBRACK)
                self.state = 499
                self.statement_list()
                self.state = 500
                self.match(MiniGoParser.RBRACEBRACK)
                pass
            elif token in [MiniGoParser.SEMICOLON, MiniGoParser.NEW_LINE]:
                self.enterOuterAlt(localctx, 2)

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


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def for_condition(self):
            return self.getTypedRuleContext(MiniGoParser.For_conditionContext,0)


        def for_initialization_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.For_initialization_declarationContext,0)


        def for_range(self):
            return self.getTypedRuleContext(MiniGoParser.For_rangeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = MiniGoParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_for_statement)
        try:
            self.state = 508
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 505
                self.for_condition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 506
                self.for_initialization_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 507
                self.for_range()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def LBRACEBRACK(self):
            return self.getToken(MiniGoParser.LBRACEBRACK, 0)

        def statement_list(self):
            return self.getTypedRuleContext(MiniGoParser.Statement_listContext,0)


        def RBRACEBRACK(self):
            return self.getToken(MiniGoParser.RBRACEBRACK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_for_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_condition" ):
                return visitor.visitFor_condition(self)
            else:
                return visitor.visitChildren(self)




    def for_condition(self):

        localctx = MiniGoParser.For_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_for_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 510
            self.match(MiniGoParser.FOR)
            self.state = 511
            self.expression1(0)
            self.state = 512
            self.match(MiniGoParser.LBRACEBRACK)
            self.state = 513
            self.statement_list()
            self.state = 514
            self.match(MiniGoParser.RBRACEBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_assignment_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def assign_operator(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_operatorContext,0)


        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_assignment_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_assignment_statement" ):
                return visitor.visitFor_assignment_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_assignment_statement(self):

        localctx = MiniGoParser.For_assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_for_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 516
            self.match(MiniGoParser.ID)
            self.state = 517
            self.assign_operator()
            self.state = 518
            self.expression1(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_variable_declared_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def optional_type(self):
            return self.getTypedRuleContext(MiniGoParser.Optional_typeContext,0)


        def required_initial_expression(self):
            return self.getTypedRuleContext(MiniGoParser.Required_initial_expressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_variable_declared_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_variable_declared_statement" ):
                return visitor.visitFor_variable_declared_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_variable_declared_statement(self):

        localctx = MiniGoParser.For_variable_declared_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_for_variable_declared_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 520
            self.match(MiniGoParser.VAR)
            self.state = 521
            self.match(MiniGoParser.ID)
            self.state = 522
            self.optional_type()
            self.state = 523
            self.required_initial_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_initialization_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def end_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.End_statementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.End_statementContext,i)


        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def for_assignment_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.For_assignment_statementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.For_assignment_statementContext,i)


        def LBRACEBRACK(self):
            return self.getToken(MiniGoParser.LBRACEBRACK, 0)

        def statement_list(self):
            return self.getTypedRuleContext(MiniGoParser.Statement_listContext,0)


        def RBRACEBRACK(self):
            return self.getToken(MiniGoParser.RBRACEBRACK, 0)

        def for_variable_declared_statement(self):
            return self.getTypedRuleContext(MiniGoParser.For_variable_declared_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_initialization_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_initialization_declaration" ):
                return visitor.visitFor_initialization_declaration(self)
            else:
                return visitor.visitChildren(self)




    def for_initialization_declaration(self):

        localctx = MiniGoParser.For_initialization_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_for_initialization_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 525
            self.match(MiniGoParser.FOR)
            self.state = 528
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 526
                self.for_assignment_statement()
                pass
            elif token in [MiniGoParser.VAR]:
                self.state = 527
                self.for_variable_declared_statement()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 530
            self.end_statement()
            self.state = 531
            self.expression1(0)
            self.state = 532
            self.end_statement()
            self.state = 533
            self.for_assignment_statement()
            self.state = 534
            self.match(MiniGoParser.LBRACEBRACK)
            self.state = 535
            self.statement_list()
            self.state = 536
            self.match(MiniGoParser.RBRACEBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_rangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def assign_operator(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_operatorContext,0)


        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def LBRACEBRACK(self):
            return self.getToken(MiniGoParser.LBRACEBRACK, 0)

        def statement_list(self):
            return self.getTypedRuleContext(MiniGoParser.Statement_listContext,0)


        def RBRACEBRACK(self):
            return self.getToken(MiniGoParser.RBRACEBRACK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_for_range

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_range" ):
                return visitor.visitFor_range(self)
            else:
                return visitor.visitChildren(self)




    def for_range(self):

        localctx = MiniGoParser.For_rangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_for_range)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 538
            self.match(MiniGoParser.FOR)
            self.state = 539
            self.match(MiniGoParser.ID)
            self.state = 540
            self.match(MiniGoParser.COMMA)
            self.state = 541
            self.match(MiniGoParser.ID)
            self.state = 542
            self.assign_operator()
            self.state = 543
            self.match(MiniGoParser.RANGE)
            self.state = 544
            self.expression1(0)
            self.state = 545
            self.match(MiniGoParser.LBRACEBRACK)
            self.state = 546
            self.statement_list()
            self.state = 547
            self.match(MiniGoParser.RBRACEBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_call_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Function_call_statementContext,0)


        def method_call_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Method_call_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_statement" ):
                return visitor.visitCall_statement(self)
            else:
                return visitor.visitChildren(self)




    def call_statement(self):

        localctx = MiniGoParser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_call_statement)
        try:
            self.state = 551
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 549
                self.function_call_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 550
                self.method_call_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression_list(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_listContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_function_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call_statement" ):
                return visitor.visitFunction_call_statement(self)
            else:
                return visitor.visitChildren(self)




    def function_call_statement(self):

        localctx = MiniGoParser.Function_call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_function_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 553
            self.match(MiniGoParser.ID)
            self.state = 554
            self.match(MiniGoParser.LPAREN)
            self.state = 555
            self.expression_list()
            self.state = 556
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression_list(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_listContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_method_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_call_statement" ):
                return visitor.visitMethod_call_statement(self)
            else:
                return visitor.visitChildren(self)




    def method_call_statement(self):

        localctx = MiniGoParser.Method_call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_method_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 558
            self.lhs(0)
            self.state = 559
            self.match(MiniGoParser.DOT)
            self.state = 560
            self.match(MiniGoParser.ID)
            self.state = 561
            self.match(MiniGoParser.LPAREN)
            self.state = 562
            self.expression_list()
            self.state = 563
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declared_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def optional_parameter_list(self):
            return self.getTypedRuleContext(MiniGoParser.Optional_parameter_listContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def optional_type(self):
            return self.getTypedRuleContext(MiniGoParser.Optional_typeContext,0)


        def LBRACEBRACK(self):
            return self.getToken(MiniGoParser.LBRACEBRACK, 0)

        def statement_list(self):
            return self.getTypedRuleContext(MiniGoParser.Statement_listContext,0)


        def RBRACEBRACK(self):
            return self.getToken(MiniGoParser.RBRACEBRACK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_function_declared_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_declared_statement" ):
                return visitor.visitFunction_declared_statement(self)
            else:
                return visitor.visitChildren(self)




    def function_declared_statement(self):

        localctx = MiniGoParser.Function_declared_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_function_declared_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 565
            self.match(MiniGoParser.FUNC)
            self.state = 566
            self.match(MiniGoParser.ID)
            self.state = 567
            self.match(MiniGoParser.LPAREN)
            self.state = 568
            self.optional_parameter_list()
            self.state = 569
            self.match(MiniGoParser.RPAREN)
            self.state = 570
            self.optional_type()
            self.state = 571
            self.match(MiniGoParser.LBRACEBRACK)
            self.state = 572
            self.statement_list()
            self.state = 573
            self.match(MiniGoParser.RBRACEBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declared_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def method_receiver(self):
            return self.getTypedRuleContext(MiniGoParser.Method_receiverContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def optional_parameter_list(self):
            return self.getTypedRuleContext(MiniGoParser.Optional_parameter_listContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def optional_type(self):
            return self.getTypedRuleContext(MiniGoParser.Optional_typeContext,0)


        def LBRACEBRACK(self):
            return self.getToken(MiniGoParser.LBRACEBRACK, 0)

        def statement_list(self):
            return self.getTypedRuleContext(MiniGoParser.Statement_listContext,0)


        def RBRACEBRACK(self):
            return self.getToken(MiniGoParser.RBRACEBRACK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_method_declared_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_declared_statement" ):
                return visitor.visitMethod_declared_statement(self)
            else:
                return visitor.visitChildren(self)




    def method_declared_statement(self):

        localctx = MiniGoParser.Method_declared_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_method_declared_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 575
            self.match(MiniGoParser.FUNC)
            self.state = 576
            self.method_receiver()
            self.state = 577
            self.match(MiniGoParser.ID)
            self.state = 578
            self.match(MiniGoParser.LPAREN)
            self.state = 579
            self.optional_parameter_list()
            self.state = 580
            self.match(MiniGoParser.RPAREN)
            self.state = 581
            self.optional_type()
            self.state = 582
            self.match(MiniGoParser.LBRACEBRACK)
            self.state = 583
            self.statement_list()
            self.state = 584
            self.match(MiniGoParser.RBRACEBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_receiverContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_method_receiver

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_receiver" ):
                return visitor.visitMethod_receiver(self)
            else:
                return visitor.visitChildren(self)




    def method_receiver(self):

        localctx = MiniGoParser.Method_receiverContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_method_receiver)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 586
            self.match(MiniGoParser.LPAREN)
            self.state = 587
            self.match(MiniGoParser.ID)
            self.state = 588
            self.match(MiniGoParser.ID)
            self.state = 589
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_declared_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def LBRACEBRACK(self):
            return self.getToken(MiniGoParser.LBRACEBRACK, 0)

        def list_field_declared_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_field_declared_statementContext,0)


        def RBRACEBRACK(self):
            return self.getToken(MiniGoParser.RBRACEBRACK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_declared_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_declared_statement" ):
                return visitor.visitStruct_declared_statement(self)
            else:
                return visitor.visitChildren(self)




    def struct_declared_statement(self):

        localctx = MiniGoParser.Struct_declared_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_struct_declared_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 591
            self.match(MiniGoParser.TYPE)
            self.state = 592
            self.match(MiniGoParser.ID)
            self.state = 593
            self.match(MiniGoParser.STRUCT)
            self.state = 594
            self.match(MiniGoParser.LBRACEBRACK)
            self.state = 595
            self.list_field_declared_statement()
            self.state = 596
            self.match(MiniGoParser.RBRACEBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_field_declared_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_declared_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Field_declared_statementContext,0)


        def list_field_declared_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_field_declared_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_field_declared_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_field_declared_statement" ):
                return visitor.visitList_field_declared_statement(self)
            else:
                return visitor.visitChildren(self)




    def list_field_declared_statement(self):

        localctx = MiniGoParser.List_field_declared_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_list_field_declared_statement)
        try:
            self.state = 602
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 598
                self.field_declared_statement()
                self.state = 599
                self.list_field_declared_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 601
                self.field_declared_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_declared_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def required_type(self):
            return self.getTypedRuleContext(MiniGoParser.Required_typeContext,0)


        def end_statement(self):
            return self.getTypedRuleContext(MiniGoParser.End_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_field_declared_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField_declared_statement" ):
                return visitor.visitField_declared_statement(self)
            else:
                return visitor.visitChildren(self)




    def field_declared_statement(self):

        localctx = MiniGoParser.Field_declared_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_field_declared_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 604
            self.match(MiniGoParser.ID)
            self.state = 605
            self.required_type()
            self.state = 606
            self.end_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_interface_declared_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def optional_parameter_list(self):
            return self.getTypedRuleContext(MiniGoParser.Optional_parameter_listContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def optional_type(self):
            return self.getTypedRuleContext(MiniGoParser.Optional_typeContext,0)


        def end_statement(self):
            return self.getTypedRuleContext(MiniGoParser.End_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_function_interface_declared_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_interface_declared_statement" ):
                return visitor.visitFunction_interface_declared_statement(self)
            else:
                return visitor.visitChildren(self)




    def function_interface_declared_statement(self):

        localctx = MiniGoParser.Function_interface_declared_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_function_interface_declared_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 608
            self.match(MiniGoParser.ID)
            self.state = 609
            self.match(MiniGoParser.LPAREN)
            self.state = 610
            self.optional_parameter_list()
            self.state = 611
            self.match(MiniGoParser.RPAREN)
            self.state = 612
            self.optional_type()
            self.state = 613
            self.end_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_function_declared_interfaceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_interface_declared_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Function_interface_declared_statementContext,0)


        def list_function_declared_interface(self):
            return self.getTypedRuleContext(MiniGoParser.List_function_declared_interfaceContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_function_declared_interface

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_function_declared_interface" ):
                return visitor.visitList_function_declared_interface(self)
            else:
                return visitor.visitChildren(self)




    def list_function_declared_interface(self):

        localctx = MiniGoParser.List_function_declared_interfaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_list_function_declared_interface)
        try:
            self.state = 619
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 615
                self.function_interface_declared_statement()
                self.state = 616
                self.list_function_declared_interface()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 618
                self.function_interface_declared_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_declared_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def LBRACEBRACK(self):
            return self.getToken(MiniGoParser.LBRACEBRACK, 0)

        def list_function_declared_interface(self):
            return self.getTypedRuleContext(MiniGoParser.List_function_declared_interfaceContext,0)


        def RBRACEBRACK(self):
            return self.getToken(MiniGoParser.RBRACEBRACK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_declared_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_declared_statement" ):
                return visitor.visitInterface_declared_statement(self)
            else:
                return visitor.visitChildren(self)




    def interface_declared_statement(self):

        localctx = MiniGoParser.Interface_declared_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_interface_declared_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 621
            self.match(MiniGoParser.TYPE)
            self.state = 622
            self.match(MiniGoParser.ID)
            self.state = 623
            self.match(MiniGoParser.INTERFACE)
            self.state = 624
            self.match(MiniGoParser.LBRACEBRACK)
            self.state = 625
            self.list_function_declared_interface()
            self.state = 626
            self.match(MiniGoParser.RBRACEBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.expression1_sempred
        self._predicates[5] = self.expression2_sempred
        self._predicates[6] = self.expression3_sempred
        self._predicates[7] = self.expression4_sempred
        self._predicates[8] = self.expression5_sempred
        self._predicates[10] = self.expression7_sempred
        self._predicates[18] = self.nested_array_element_list_sempred
        self._predicates[43] = self.lhs_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression1_sempred(self, localctx:Expression1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression2_sempred(self, localctx:Expression2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression3_sempred(self, localctx:Expression3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expression4_sempred(self, localctx:Expression4Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expression5_sempred(self, localctx:Expression5Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expression7_sempred(self, localctx:Expression7Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 3)
         

    def nested_array_element_list_sempred(self, localctx:Nested_array_element_listContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 3)
         

    def lhs_sempred(self, localctx:LhsContext, predIndex:int):
            if predIndex == 9:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 2)
         




