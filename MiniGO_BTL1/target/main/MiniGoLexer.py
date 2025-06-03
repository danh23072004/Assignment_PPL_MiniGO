# Generated from main/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\f")
        buf.write("9\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3")
        buf.write("\b\6\b+\n\b\r\b\16\b,\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\2\2\f\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\3\2\5\5\2C\\aac|\3\2\62;\5\2\13\f\16\17")
        buf.write("\"\"\29\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\3\27\3\2\2\2\5\36\3\2\2\2\7")
        buf.write("!\3\2\2\2\t#\3\2\2\2\13%\3\2\2\2\r\'\3\2\2\2\17*\3\2\2")
        buf.write("\2\21\60\3\2\2\2\23\63\3\2\2\2\25\66\3\2\2\2\27\30\7x")
        buf.write("\2\2\30\31\7q\2\2\31\32\7v\2\2\32\33\7k\2\2\33\34\7g\2")
        buf.write("\2\34\35\7p\2\2\35\4\3\2\2\2\36\37\7k\2\2\37 \7h\2\2 ")
        buf.write("\6\3\2\2\2!\"\7-\2\2\"\b\3\2\2\2#$\7*\2\2$\n\3\2\2\2%")
        buf.write("&\t\2\2\2&\f\3\2\2\2\'(\t\3\2\2(\16\3\2\2\2)+\t\4\2\2")
        buf.write("*)\3\2\2\2+,\3\2\2\2,*\3\2\2\2,-\3\2\2\2-.\3\2\2\2./\b")
        buf.write("\b\2\2/\20\3\2\2\2\60\61\13\2\2\2\61\62\b\t\3\2\62\22")
        buf.write("\3\2\2\2\63\64\7W\2\2\64\65\b\n\4\2\65\24\3\2\2\2\66\67")
        buf.write("\7K\2\2\678\b\13\5\28\26\3\2\2\2\4\2,\6\b\2\2\3\t\2\3")
        buf.write("\n\3\3\13\4")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    IF = 2
    ADD = 3
    LPAREN = 4
    ID = 5
    INT_LIT = 6
    WS = 7
    ERROR_CHAR = 8
    UNCLOSE_STRING = 9
    ILLEGAL_ESCAPE = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'votien'", "'if'", "'+'", "'('", "'U'", "'I'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ADD", "LPAREN", "ID", "INT_LIT", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "IF", "ADD", "LPAREN", "ID", "INT_LIT", "WS", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
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
            actions[7] = self.ERROR_CHAR_action 
            actions[8] = self.UNCLOSE_STRING_action 
            actions[9] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                raise UncloseString(self.text[1:-2])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                raise IllegalEscape(self.text[1:])

     


