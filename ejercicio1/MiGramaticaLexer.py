# Generated from MiGramatica.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r")
        buf.write("<\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\3")
        buf.write("\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3")
        buf.write("\n\3\n\7\n,\n\n\f\n\16\n/\13\n\3\13\6\13\62\n\13\r\13")
        buf.write("\16\13\63\3\f\6\f\67\n\f\r\f\16\f8\3\f\3\f\2\2\r\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\3\2\6\5")
        buf.write("\2C\\aac|\6\2\62;C\\aac|\3\2\62;\5\2\13\f\17\17\"\"\2")
        buf.write(">\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\3\31\3\2\2\2\5\33\3\2")
        buf.write("\2\2\7\35\3\2\2\2\t\37\3\2\2\2\13!\3\2\2\2\r#\3\2\2\2")
        buf.write("\17%\3\2\2\2\21\'\3\2\2\2\23)\3\2\2\2\25\61\3\2\2\2\27")
        buf.write("\66\3\2\2\2\31\32\7=\2\2\32\4\3\2\2\2\33\34\7?\2\2\34")
        buf.write("\6\3\2\2\2\35\36\7,\2\2\36\b\3\2\2\2\37 \7\61\2\2 \n\3")
        buf.write("\2\2\2!\"\7-\2\2\"\f\3\2\2\2#$\7/\2\2$\16\3\2\2\2%&\7")
        buf.write("*\2\2&\20\3\2\2\2\'(\7+\2\2(\22\3\2\2\2)-\t\2\2\2*,\t")
        buf.write("\3\2\2+*\3\2\2\2,/\3\2\2\2-+\3\2\2\2-.\3\2\2\2.\24\3\2")
        buf.write("\2\2/-\3\2\2\2\60\62\t\4\2\2\61\60\3\2\2\2\62\63\3\2\2")
        buf.write("\2\63\61\3\2\2\2\63\64\3\2\2\2\64\26\3\2\2\2\65\67\t\5")
        buf.write("\2\2\66\65\3\2\2\2\678\3\2\2\28\66\3\2\2\289\3\2\2\29")
        buf.write(":\3\2\2\2:;\b\f\2\2;\30\3\2\2\2\6\2-\638\3\b\2\2")
        return buf.getvalue()


class MiGramaticaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    ID = 9
    INT = 10
    WS = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'='", "'*'", "'/'", "'+'", "'-'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "INT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "ID", "INT", "WS" ]

    grammarFileName = "MiGramatica.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


