# Generated from D:/git/contextFreeLanguage/var_num/calculator\gcalculator.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\35")
        buf.write("`\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2\3\2")
        buf.write("\3\2\3\2\5\2\37\n\2\3\3\3\3\3\3\7\3$\n\3\f\3\16\3\'\13")
        buf.write("\3\3\4\3\4\3\4\7\4,\n\4\f\4\16\4/\13\4\3\5\3\5\3\5\7\5")
        buf.write("\64\n\5\f\5\16\5\67\13\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6?")
        buf.write("\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7H\n\7\3\b\3\b\3\t")
        buf.write("\3\t\3\n\3\n\3\13\3\13\3\13\3\13\3\13\7\13U\n\13\f\13")
        buf.write("\16\13X\13\13\3\13\3\13\3\f\3\f\3\r\3\r\3\r\2\2\16\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\30\2\7\3\2\16\17\3\2\20\21\3\2")
        buf.write("\30\32\3\2\3\13\3\2\22\24\2^\2\32\3\2\2\2\4 \3\2\2\2\6")
        buf.write("(\3\2\2\2\b\60\3\2\2\2\n>\3\2\2\2\fG\3\2\2\2\16I\3\2\2")
        buf.write("\2\20K\3\2\2\2\22M\3\2\2\2\24O\3\2\2\2\26[\3\2\2\2\30")
        buf.write("]\3\2\2\2\32\36\5\4\3\2\33\34\5\30\r\2\34\35\5\4\3\2\35")
        buf.write("\37\3\2\2\2\36\33\3\2\2\2\36\37\3\2\2\2\37\3\3\2\2\2 ")
        buf.write("%\5\6\4\2!\"\t\2\2\2\"$\5\6\4\2#!\3\2\2\2$\'\3\2\2\2%")
        buf.write("#\3\2\2\2%&\3\2\2\2&\5\3\2\2\2\'%\3\2\2\2(-\5\b\5\2)*")
        buf.write("\t\3\2\2*,\5\b\5\2+)\3\2\2\2,/\3\2\2\2-+\3\2\2\2-.\3\2")
        buf.write("\2\2.\7\3\2\2\2/-\3\2\2\2\60\65\5\n\6\2\61\62\7\27\2\2")
        buf.write("\62\64\5\n\6\2\63\61\3\2\2\2\64\67\3\2\2\2\65\63\3\2\2")
        buf.write("\2\65\66\3\2\2\2\66\t\3\2\2\2\67\65\3\2\2\289\7\16\2\2")
        buf.write("9?\5\n\6\2:;\7\17\2\2;?\5\n\6\2<?\5\24\13\2=?\5\f\7\2")
        buf.write(">8\3\2\2\2>:\3\2\2\2><\3\2\2\2>=\3\2\2\2?\13\3\2\2\2@")
        buf.write("H\5\16\b\2AH\5\22\n\2BH\5\20\t\2CD\7\f\2\2DE\5\4\3\2E")
        buf.write("F\7\r\2\2FH\3\2\2\2G@\3\2\2\2GA\3\2\2\2GB\3\2\2\2GC\3")
        buf.write("\2\2\2H\r\3\2\2\2IJ\7\34\2\2J\17\3\2\2\2KL\t\4\2\2L\21")
        buf.write("\3\2\2\2MN\7\33\2\2N\23\3\2\2\2OP\5\26\f\2PQ\7\f\2\2Q")
        buf.write("V\5\4\3\2RS\7\25\2\2SU\5\4\3\2TR\3\2\2\2UX\3\2\2\2VT\3")
        buf.write("\2\2\2VW\3\2\2\2WY\3\2\2\2XV\3\2\2\2YZ\7\r\2\2Z\25\3\2")
        buf.write("\2\2[\\\t\5\2\2\\\27\3\2\2\2]^\t\6\2\2^\31\3\2\2\2\t\36")
        buf.write("%-\65>GV")
        return buf.getvalue()


class gcalculatorParser ( Parser ):

    grammarFileName = "gcalculator.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'cos'", "'sin'", "'tan'", "'acos'", "'asin'", 
                     "'atan'", "'ln'", "'log'", "'sqrt'", "'('", "')'", 
                     "'+'", "'-'", "'*'", "'/'", "'>'", "'<'", "'='", "','", 
                     "'.'", "'^'", "'pi'", "<INVALID>", "'i'" ]

    symbolicNames = [ "<INVALID>", "COS", "SIN", "TAN", "ACOS", "ASIN", 
                      "ATAN", "LN", "LOG", "SQRT", "LPAREN", "RPAREN", "PLUS", 
                      "MINUS", "TIMES", "DIV", "GT", "LT", "EQ", "COMMA", 
                      "POINT", "POW", "PI", "EULER", "I", "VARIABLE", "SCIENTIFIC_NUMBER", 
                      "WS" ]

    RULE_equation = 0
    RULE_expression = 1
    RULE_multiplyingExpression = 2
    RULE_powExpression = 3
    RULE_signedAtom = 4
    RULE_atom = 5
    RULE_scientific = 6
    RULE_constant = 7
    RULE_variable = 8
    RULE_func = 9
    RULE_funcname = 10
    RULE_relop = 11

    ruleNames =  [ "equation", "expression", "multiplyingExpression", "powExpression", 
                   "signedAtom", "atom", "scientific", "constant", "variable", 
                   "func", "funcname", "relop" ]

    EOF = Token.EOF
    COS=1
    SIN=2
    TAN=3
    ACOS=4
    ASIN=5
    ATAN=6
    LN=7
    LOG=8
    SQRT=9
    LPAREN=10
    RPAREN=11
    PLUS=12
    MINUS=13
    TIMES=14
    DIV=15
    GT=16
    LT=17
    EQ=18
    COMMA=19
    POINT=20
    POW=21
    PI=22
    EULER=23
    I=24
    VARIABLE=25
    SCIENTIFIC_NUMBER=26
    WS=27

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class EquationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gcalculatorParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(gcalculatorParser.ExpressionContext,i)


        def relop(self):
            return self.getTypedRuleContext(gcalculatorParser.RelopContext,0)


        def getRuleIndex(self):
            return gcalculatorParser.RULE_equation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquation" ):
                listener.enterEquation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquation" ):
                listener.exitEquation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquation" ):
                return visitor.visitEquation(self)
            else:
                return visitor.visitChildren(self)




    def equation(self):

        localctx = gcalculatorParser.EquationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_equation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.expression()
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << gcalculatorParser.GT) | (1 << gcalculatorParser.LT) | (1 << gcalculatorParser.EQ))) != 0):
                self.state = 25
                self.relop()
                self.state = 26
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplyingExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gcalculatorParser.MultiplyingExpressionContext)
            else:
                return self.getTypedRuleContext(gcalculatorParser.MultiplyingExpressionContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(gcalculatorParser.PLUS)
            else:
                return self.getToken(gcalculatorParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(gcalculatorParser.MINUS)
            else:
                return self.getToken(gcalculatorParser.MINUS, i)

        def getRuleIndex(self):
            return gcalculatorParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = gcalculatorParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.multiplyingExpression()
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==gcalculatorParser.PLUS or _la==gcalculatorParser.MINUS:
                self.state = 31
                _la = self._input.LA(1)
                if not(_la==gcalculatorParser.PLUS or _la==gcalculatorParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 32
                self.multiplyingExpression()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplyingExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def powExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gcalculatorParser.PowExpressionContext)
            else:
                return self.getTypedRuleContext(gcalculatorParser.PowExpressionContext,i)


        def TIMES(self, i:int=None):
            if i is None:
                return self.getTokens(gcalculatorParser.TIMES)
            else:
                return self.getToken(gcalculatorParser.TIMES, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(gcalculatorParser.DIV)
            else:
                return self.getToken(gcalculatorParser.DIV, i)

        def getRuleIndex(self):
            return gcalculatorParser.RULE_multiplyingExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplyingExpression" ):
                listener.enterMultiplyingExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplyingExpression" ):
                listener.exitMultiplyingExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplyingExpression" ):
                return visitor.visitMultiplyingExpression(self)
            else:
                return visitor.visitChildren(self)




    def multiplyingExpression(self):

        localctx = gcalculatorParser.MultiplyingExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_multiplyingExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.powExpression()
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==gcalculatorParser.TIMES or _la==gcalculatorParser.DIV:
                self.state = 39
                _la = self._input.LA(1)
                if not(_la==gcalculatorParser.TIMES or _la==gcalculatorParser.DIV):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 40
                self.powExpression()
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PowExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def signedAtom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gcalculatorParser.SignedAtomContext)
            else:
                return self.getTypedRuleContext(gcalculatorParser.SignedAtomContext,i)


        def POW(self, i:int=None):
            if i is None:
                return self.getTokens(gcalculatorParser.POW)
            else:
                return self.getToken(gcalculatorParser.POW, i)

        def getRuleIndex(self):
            return gcalculatorParser.RULE_powExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPowExpression" ):
                listener.enterPowExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPowExpression" ):
                listener.exitPowExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPowExpression" ):
                return visitor.visitPowExpression(self)
            else:
                return visitor.visitChildren(self)




    def powExpression(self):

        localctx = gcalculatorParser.PowExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_powExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.signedAtom()
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==gcalculatorParser.POW:
                self.state = 47
                self.match(gcalculatorParser.POW)
                self.state = 48
                self.signedAtom()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignedAtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(gcalculatorParser.PLUS, 0)

        def signedAtom(self):
            return self.getTypedRuleContext(gcalculatorParser.SignedAtomContext,0)


        def MINUS(self):
            return self.getToken(gcalculatorParser.MINUS, 0)

        def func(self):
            return self.getTypedRuleContext(gcalculatorParser.FuncContext,0)


        def atom(self):
            return self.getTypedRuleContext(gcalculatorParser.AtomContext,0)


        def getRuleIndex(self):
            return gcalculatorParser.RULE_signedAtom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSignedAtom" ):
                listener.enterSignedAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSignedAtom" ):
                listener.exitSignedAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSignedAtom" ):
                return visitor.visitSignedAtom(self)
            else:
                return visitor.visitChildren(self)




    def signedAtom(self):

        localctx = gcalculatorParser.SignedAtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_signedAtom)
        try:
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [gcalculatorParser.PLUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.match(gcalculatorParser.PLUS)
                self.state = 55
                self.signedAtom()
                pass
            elif token in [gcalculatorParser.MINUS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.match(gcalculatorParser.MINUS)
                self.state = 57
                self.signedAtom()
                pass
            elif token in [gcalculatorParser.COS, gcalculatorParser.SIN, gcalculatorParser.TAN, gcalculatorParser.ACOS, gcalculatorParser.ASIN, gcalculatorParser.ATAN, gcalculatorParser.LN, gcalculatorParser.LOG, gcalculatorParser.SQRT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 58
                self.func()
                pass
            elif token in [gcalculatorParser.LPAREN, gcalculatorParser.PI, gcalculatorParser.EULER, gcalculatorParser.I, gcalculatorParser.VARIABLE, gcalculatorParser.SCIENTIFIC_NUMBER]:
                self.enterOuterAlt(localctx, 4)
                self.state = 59
                self.atom()
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


    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scientific(self):
            return self.getTypedRuleContext(gcalculatorParser.ScientificContext,0)


        def variable(self):
            return self.getTypedRuleContext(gcalculatorParser.VariableContext,0)


        def constant(self):
            return self.getTypedRuleContext(gcalculatorParser.ConstantContext,0)


        def LPAREN(self):
            return self.getToken(gcalculatorParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(gcalculatorParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(gcalculatorParser.RPAREN, 0)

        def getRuleIndex(self):
            return gcalculatorParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = gcalculatorParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_atom)
        try:
            self.state = 69
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [gcalculatorParser.SCIENTIFIC_NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.scientific()
                pass
            elif token in [gcalculatorParser.VARIABLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.variable()
                pass
            elif token in [gcalculatorParser.PI, gcalculatorParser.EULER, gcalculatorParser.I]:
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.constant()
                pass
            elif token in [gcalculatorParser.LPAREN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 65
                self.match(gcalculatorParser.LPAREN)
                self.state = 66
                self.expression()
                self.state = 67
                self.match(gcalculatorParser.RPAREN)
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


    class ScientificContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SCIENTIFIC_NUMBER(self):
            return self.getToken(gcalculatorParser.SCIENTIFIC_NUMBER, 0)

        def getRuleIndex(self):
            return gcalculatorParser.RULE_scientific

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScientific" ):
                listener.enterScientific(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScientific" ):
                listener.exitScientific(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScientific" ):
                return visitor.visitScientific(self)
            else:
                return visitor.visitChildren(self)




    def scientific(self):

        localctx = gcalculatorParser.ScientificContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_scientific)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(gcalculatorParser.SCIENTIFIC_NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PI(self):
            return self.getToken(gcalculatorParser.PI, 0)

        def EULER(self):
            return self.getToken(gcalculatorParser.EULER, 0)

        def I(self):
            return self.getToken(gcalculatorParser.I, 0)

        def getRuleIndex(self):
            return gcalculatorParser.RULE_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant" ):
                listener.enterConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant" ):
                listener.exitConstant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstant" ):
                return visitor.visitConstant(self)
            else:
                return visitor.visitChildren(self)




    def constant(self):

        localctx = gcalculatorParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << gcalculatorParser.PI) | (1 << gcalculatorParser.EULER) | (1 << gcalculatorParser.I))) != 0)):
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


    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(gcalculatorParser.VARIABLE, 0)

        def getRuleIndex(self):
            return gcalculatorParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = gcalculatorParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(gcalculatorParser.VARIABLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcname(self):
            return self.getTypedRuleContext(gcalculatorParser.FuncnameContext,0)


        def LPAREN(self):
            return self.getToken(gcalculatorParser.LPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gcalculatorParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(gcalculatorParser.ExpressionContext,i)


        def RPAREN(self):
            return self.getToken(gcalculatorParser.RPAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(gcalculatorParser.COMMA)
            else:
                return self.getToken(gcalculatorParser.COMMA, i)

        def getRuleIndex(self):
            return gcalculatorParser.RULE_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc" ):
                listener.enterFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc" ):
                listener.exitFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc" ):
                return visitor.visitFunc(self)
            else:
                return visitor.visitChildren(self)




    def func(self):

        localctx = gcalculatorParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.funcname()
            self.state = 78
            self.match(gcalculatorParser.LPAREN)
            self.state = 79
            self.expression()
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==gcalculatorParser.COMMA:
                self.state = 80
                self.match(gcalculatorParser.COMMA)
                self.state = 81
                self.expression()
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 87
            self.match(gcalculatorParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncnameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COS(self):
            return self.getToken(gcalculatorParser.COS, 0)

        def TAN(self):
            return self.getToken(gcalculatorParser.TAN, 0)

        def SIN(self):
            return self.getToken(gcalculatorParser.SIN, 0)

        def ACOS(self):
            return self.getToken(gcalculatorParser.ACOS, 0)

        def ATAN(self):
            return self.getToken(gcalculatorParser.ATAN, 0)

        def ASIN(self):
            return self.getToken(gcalculatorParser.ASIN, 0)

        def LOG(self):
            return self.getToken(gcalculatorParser.LOG, 0)

        def LN(self):
            return self.getToken(gcalculatorParser.LN, 0)

        def SQRT(self):
            return self.getToken(gcalculatorParser.SQRT, 0)

        def getRuleIndex(self):
            return gcalculatorParser.RULE_funcname

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncname" ):
                listener.enterFuncname(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncname" ):
                listener.exitFuncname(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncname" ):
                return visitor.visitFuncname(self)
            else:
                return visitor.visitChildren(self)




    def funcname(self):

        localctx = gcalculatorParser.FuncnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_funcname)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << gcalculatorParser.COS) | (1 << gcalculatorParser.SIN) | (1 << gcalculatorParser.TAN) | (1 << gcalculatorParser.ACOS) | (1 << gcalculatorParser.ASIN) | (1 << gcalculatorParser.ATAN) | (1 << gcalculatorParser.LN) | (1 << gcalculatorParser.LOG) | (1 << gcalculatorParser.SQRT))) != 0)):
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


    class RelopContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(gcalculatorParser.EQ, 0)

        def GT(self):
            return self.getToken(gcalculatorParser.GT, 0)

        def LT(self):
            return self.getToken(gcalculatorParser.LT, 0)

        def getRuleIndex(self):
            return gcalculatorParser.RULE_relop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelop" ):
                listener.enterRelop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelop" ):
                listener.exitRelop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelop" ):
                return visitor.visitRelop(self)
            else:
                return visitor.visitChildren(self)




    def relop(self):

        localctx = gcalculatorParser.RelopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_relop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << gcalculatorParser.GT) | (1 << gcalculatorParser.LT) | (1 << gcalculatorParser.EQ))) != 0)):
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





