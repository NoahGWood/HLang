from lexer import Lexer
from parser import Parser
from codegen import CodeGen


fname = "input.hobo"
with open(fname) as f:
    text_input = f.read()

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)
for token in tokens:
    print(token)
