from antlr4 import *

from gcalculatorListener import gcalculatorListener
from gcalculatorParser import gcalculatorParser


class CalculatorListener(gcalculatorListener):

    def exitExpression(self, ctx:gcalculatorParser.ExpressionContext):
        ctx.result = ctx.children[0].result
        ctx.op = None
        for child in ctx.children[1:]:

            if str(child) in ['+', '-']:
                ctx.op = str(child)
            else:
                if ctx.op is '+':
                    ctx.result += child.result
                elif ctx.op is '-':
                    ctx.result -= child.result

    def exitMultiplyingExpression(self, ctx:gcalculatorParser.MultiplyingExpressionContext):
        if len(ctx.children) == 1:
            ctx.result = float(ctx.getText())
            return
        else:
            ctx.result = float(ctx.children[0].getText())
            ctx.op = None
            for child in ctx.children[1:]:
                if str(child) in ['*', '/']:
                    ctx.op = str(child)
                else:
                    if ctx.op == '*':
                        ctx.result *= float(child.getText())
                    elif ctx.op == '/':
                        if float(child.getText()) == 0:
                            exit('Error: divide by zero error.')

                        ctx.result /= float(child.getText())

    def exitEquation(self, ctx:gcalculatorParser.EquationContext):
        print(ctx.expression(0).getText())
        print(ctx.expression(0).result)

    def exitAtom(self, ctx:gcalculatorParser.AtomContext):
        if len(ctx.children) > 1:
            ctx.children.pop(-1)
            ctx.children.pop(0)
