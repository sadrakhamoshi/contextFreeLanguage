# Generated from D:/git/contextFreeLanguage/var_num/calculator\gcalculator.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .gcalculatorParser import gcalculatorParser
else:
    from gcalculatorParser import gcalculatorParser

# This class defines a complete listener for a parse tree produced by gcalculatorParser.
class gcalculatorListener(ParseTreeListener):

    # Enter a parse tree produced by gcalculatorParser#equation.
    def enterEquation(self, ctx:gcalculatorParser.EquationContext):
        pass

    # Exit a parse tree produced by gcalculatorParser#equation.
    def exitEquation(self, ctx:gcalculatorParser.EquationContext):
        pass


    # Enter a parse tree produced by gcalculatorParser#expression.
    def enterExpression(self, ctx:gcalculatorParser.ExpressionContext):
        pass

    # Exit a parse tree produced by gcalculatorParser#expression.
    def exitExpression(self, ctx:gcalculatorParser.ExpressionContext):
        pass


    # Enter a parse tree produced by gcalculatorParser#multiplyingExpression.
    def enterMultiplyingExpression(self, ctx:gcalculatorParser.MultiplyingExpressionContext):
        pass

    # Exit a parse tree produced by gcalculatorParser#multiplyingExpression.
    def exitMultiplyingExpression(self, ctx:gcalculatorParser.MultiplyingExpressionContext):
        pass


    # Enter a parse tree produced by gcalculatorParser#powExpression.
    def enterPowExpression(self, ctx:gcalculatorParser.PowExpressionContext):
        pass

    # Exit a parse tree produced by gcalculatorParser#powExpression.
    def exitPowExpression(self, ctx:gcalculatorParser.PowExpressionContext):
        pass


    # Enter a parse tree produced by gcalculatorParser#signedAtom.
    def enterSignedAtom(self, ctx:gcalculatorParser.SignedAtomContext):
        pass

    # Exit a parse tree produced by gcalculatorParser#signedAtom.
    def exitSignedAtom(self, ctx:gcalculatorParser.SignedAtomContext):
        pass


    # Enter a parse tree produced by gcalculatorParser#atom.
    def enterAtom(self, ctx:gcalculatorParser.AtomContext):
        pass

    # Exit a parse tree produced by gcalculatorParser#atom.
    def exitAtom(self, ctx:gcalculatorParser.AtomContext):
        pass


    # Enter a parse tree produced by gcalculatorParser#scientific.
    def enterScientific(self, ctx:gcalculatorParser.ScientificContext):
        pass

    # Exit a parse tree produced by gcalculatorParser#scientific.
    def exitScientific(self, ctx:gcalculatorParser.ScientificContext):
        pass


    # Enter a parse tree produced by gcalculatorParser#constant.
    def enterConstant(self, ctx:gcalculatorParser.ConstantContext):
        pass

    # Exit a parse tree produced by gcalculatorParser#constant.
    def exitConstant(self, ctx:gcalculatorParser.ConstantContext):
        pass


    # Enter a parse tree produced by gcalculatorParser#variable.
    def enterVariable(self, ctx:gcalculatorParser.VariableContext):
        pass

    # Exit a parse tree produced by gcalculatorParser#variable.
    def exitVariable(self, ctx:gcalculatorParser.VariableContext):
        pass


    # Enter a parse tree produced by gcalculatorParser#func.
    def enterFunc(self, ctx:gcalculatorParser.FuncContext):
        pass

    # Exit a parse tree produced by gcalculatorParser#func.
    def exitFunc(self, ctx:gcalculatorParser.FuncContext):
        pass


    # Enter a parse tree produced by gcalculatorParser#funcname.
    def enterFuncname(self, ctx:gcalculatorParser.FuncnameContext):
        pass

    # Exit a parse tree produced by gcalculatorParser#funcname.
    def exitFuncname(self, ctx:gcalculatorParser.FuncnameContext):
        pass


    # Enter a parse tree produced by gcalculatorParser#relop.
    def enterRelop(self, ctx:gcalculatorParser.RelopContext):
        pass

    # Exit a parse tree produced by gcalculatorParser#relop.
    def exitRelop(self, ctx:gcalculatorParser.RelopContext):
        pass



del gcalculatorParser