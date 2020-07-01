from antlr4 import *

from gcalculatorLexer import gcalculatorLexer
from gcalculatorParser import gcalculatorParser

from CalcListener import CalculatorListener

input = "4+5"
stream = InputStream(input)

lexer = gcalculatorLexer(stream)

token_stream = CommonTokenStream(lexer)

parser = gcalculatorParser(token_stream)

parser_tree = parser.equation()

my_listener = CalculatorListener()
ParseTreeWalker.DEFAULT.walk(t=parser_tree, listener=my_listener)
