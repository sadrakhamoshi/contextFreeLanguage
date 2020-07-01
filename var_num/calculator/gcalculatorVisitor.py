# Generated from D:/git/contextFreeLanguage/var_num/calculator\gcalculator.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .gcalculatorParser import gcalculatorParser
else:
    from gcalculatorParser import gcalculatorParser

# This class defines a complete generic visitor for a parse tree produced by gcalculatorParser.

class gcalculatorVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gcalculatorParser#equation.
    def visitEquation(self, ctx:gcalculatorParser.EquationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcalculatorParser#expression.
    def visitExpression(self, ctx:gcalculatorParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcalculatorParser#multiplyingExpression.
    def visitMultiplyingExpression(self, ctx:gcalculatorParser.MultiplyingExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcalculatorParser#powExpression.
    def visitPowExpression(self, ctx:gcalculatorParser.PowExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcalculatorParser#signedAtom.
    def visitSignedAtom(self, ctx:gcalculatorParser.SignedAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcalculatorParser#atom.
    def visitAtom(self, ctx:gcalculatorParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcalculatorParser#scientific.
    def visitScientific(self, ctx:gcalculatorParser.ScientificContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcalculatorParser#constant.
    def visitConstant(self, ctx:gcalculatorParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcalculatorParser#variable.
    def visitVariable(self, ctx:gcalculatorParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcalculatorParser#func.
    def visitFunc(self, ctx:gcalculatorParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcalculatorParser#funcname.
    def visitFuncname(self, ctx:gcalculatorParser.FuncnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcalculatorParser#relop.
    def visitRelop(self, ctx:gcalculatorParser.RelopContext):
        return self.visitChildren(ctx)



del gcalculatorParser