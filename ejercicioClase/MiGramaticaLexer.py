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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\24")
        buf.write("d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20")
        buf.write("\3\20\3\21\3\21\7\21P\n\21\f\21\16\21S\13\21\3\22\6\22")
        buf.write("V\n\22\r\22\16\22W\3\23\6\23[\n\23\r\23\16\23\\\3\23\3")
        buf.write("\23\3\24\3\24\3\25\3\25\2\2\26\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!")
        buf.write("\22#\23%\24\'\2)\2\3\2\6\5\2C\\aac|\6\2\62;C\\aac|\3\2")
        buf.write("\62;\6\2\13\f\17\17\"\"\u00a2\u00a2\2d\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\3+\3\2")
        buf.write("\2\2\5-\3\2\2\2\7\61\3\2\2\2\t\63\3\2\2\2\13\65\3\2\2")
        buf.write("\2\r\67\3\2\2\2\179\3\2\2\2\21;\3\2\2\2\23=\3\2\2\2\25")
        buf.write("?\3\2\2\2\27B\3\2\2\2\31E\3\2\2\2\33G\3\2\2\2\35I\3\2")
        buf.write("\2\2\37K\3\2\2\2!M\3\2\2\2#U\3\2\2\2%Z\3\2\2\2\'`\3\2")
        buf.write("\2\2)b\3\2\2\2+,\7=\2\2,\4\3\2\2\2-.\7h\2\2./\7q\2\2/")
        buf.write("\60\7t\2\2\60\6\3\2\2\2\61\62\7*\2\2\62\b\3\2\2\2\63\64")
        buf.write("\7+\2\2\64\n\3\2\2\2\65\66\7}\2\2\66\f\3\2\2\2\678\7\177")
        buf.write("\2\28\16\3\2\2\29:\7?\2\2:\20\3\2\2\2;<\7@\2\2<\22\3\2")
        buf.write("\2\2=>\7>\2\2>\24\3\2\2\2?@\7?\2\2@A\7?\2\2A\26\3\2\2")
        buf.write("\2BC\7#\2\2CD\7?\2\2D\30\3\2\2\2EF\7,\2\2F\32\3\2\2\2")
        buf.write("GH\7\61\2\2H\34\3\2\2\2IJ\7-\2\2J\36\3\2\2\2KL\7/\2\2")
        buf.write("L \3\2\2\2MQ\t\2\2\2NP\t\3\2\2ON\3\2\2\2PS\3\2\2\2QO\3")
        buf.write("\2\2\2QR\3\2\2\2R\"\3\2\2\2SQ\3\2\2\2TV\t\4\2\2UT\3\2")
        buf.write("\2\2VW\3\2\2\2WU\3\2\2\2WX\3\2\2\2X$\3\2\2\2Y[\t\5\2\2")
        buf.write("ZY\3\2\2\2[\\\3\2\2\2\\Z\3\2\2\2\\]\3\2\2\2]^\3\2\2\2")
        buf.write("^_\b\23\2\2_&\3\2\2\2`a\t\4\2\2a(\3\2\2\2bc\t\2\2\2c*")
        buf.write("\3\2\2\2\6\2QW\\\3\b\2\2")
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
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    ID = 16
    INT = 17
    WS = 18

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'for'", "'('", "')'", "'{'", "'}'", "'='", "'>'", "'<'", 
            "'=='", "'!='", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "INT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "ID", "INT", "WS", "DIGIT", "LETTER" ]

    grammarFileName = "MiGramatica.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


