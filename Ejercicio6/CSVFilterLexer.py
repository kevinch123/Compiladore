# Generated from CSVFilter.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\f")
        buf.write("`\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\bB\n\b\3\t")
        buf.write("\3\t\7\tF\n\t\f\t\16\tI\13\t\3\t\3\t\3\n\6\nN\n\n\r\n")
        buf.write("\16\nO\3\n\3\n\6\nT\n\n\r\n\16\nU\5\nX\n\n\3\13\6\13[")
        buf.write("\n\13\r\13\16\13\\\3\13\3\13\2\2\f\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\3\2\6\4\2>>@@\5\2\f\f\17\17")
        buf.write("$$\3\2\62;\5\2\13\f\17\17\"\"\2h\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\3\27")
        buf.write("\3\2\2\2\5\34\3\2\2\2\7\36\3\2\2\2\t%\3\2\2\2\13,\3\2")
        buf.write("\2\2\r\62\3\2\2\2\17A\3\2\2\2\21C\3\2\2\2\23M\3\2\2\2")
        buf.write("\25Z\3\2\2\2\27\30\7n\2\2\30\31\7q\2\2\31\32\7c\2\2\32")
        buf.write("\33\7f\2\2\33\4\3\2\2\2\34\35\7=\2\2\35\6\3\2\2\2\36\37")
        buf.write("\7h\2\2\37 \7k\2\2 !\7n\2\2!\"\7v\2\2\"#\7g\2\2#$\7t\2")
        buf.write("\2$\b\3\2\2\2%&\7e\2\2&\'\7q\2\2\'(\7n\2\2()\7w\2\2)*")
        buf.write("\7o\2\2*+\7p\2\2+\n\3\2\2\2,-\7e\2\2-.\7q\2\2./\7w\2\2")
        buf.write("/\60\7p\2\2\60\61\7v\2\2\61\f\3\2\2\2\62\63\7r\2\2\63")
        buf.write("\64\7t\2\2\64\65\7k\2\2\65\66\7p\2\2\66\67\7v\2\2\67\16")
        buf.write("\3\2\2\28B\t\2\2\29:\7@\2\2:B\7?\2\2;<\7>\2\2<B\7?\2\2")
        buf.write("=>\7?\2\2>B\7?\2\2?@\7#\2\2@B\7?\2\2A8\3\2\2\2A9\3\2\2")
        buf.write("\2A;\3\2\2\2A=\3\2\2\2A?\3\2\2\2B\20\3\2\2\2CG\7$\2\2")
        buf.write("DF\n\3\2\2ED\3\2\2\2FI\3\2\2\2GE\3\2\2\2GH\3\2\2\2HJ\3")
        buf.write("\2\2\2IG\3\2\2\2JK\7$\2\2K\22\3\2\2\2LN\t\4\2\2ML\3\2")
        buf.write("\2\2NO\3\2\2\2OM\3\2\2\2OP\3\2\2\2PW\3\2\2\2QS\7\60\2")
        buf.write("\2RT\t\4\2\2SR\3\2\2\2TU\3\2\2\2US\3\2\2\2UV\3\2\2\2V")
        buf.write("X\3\2\2\2WQ\3\2\2\2WX\3\2\2\2X\24\3\2\2\2Y[\t\5\2\2ZY")
        buf.write("\3\2\2\2[\\\3\2\2\2\\Z\3\2\2\2\\]\3\2\2\2]^\3\2\2\2^_")
        buf.write("\b\13\2\2_\26\3\2\2\2\t\2AGOUW\\\3\b\2\2")
        return buf.getvalue()


class CSVFilterLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    OPERATOR = 7
    STRING = 8
    NUMBER = 9
    WS = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'load'", "';'", "'filter'", "'column'", "'count'", "'print'" ]

    symbolicNames = [ "<INVALID>",
            "OPERATOR", "STRING", "NUMBER", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "OPERATOR", 
                  "STRING", "NUMBER", "WS" ]

    grammarFileName = "CSVFilter.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


