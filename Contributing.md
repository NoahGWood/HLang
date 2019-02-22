# HLang
The Hobo language is a programming language designed by hobos, for hobos.

# How To Create A New Function
## Step 1 — Create A New Token
Create a new token in lexer.py, a token should be defined as:
self.lexer.add('TOKEN_NAME', r'tokenname')

## Step 2 — Define a function in the AST
We currently use codegen to build our code, information on various functions codegen provides out of the box can be found in the codegen module.
You should define a new class named your TokenName using camelcase, for most use cases you will want to pass in BinaryOp, this will enable you to access the previous and following tokens. Because someone will need to look at all of this code and write the docs, you should do your best to follow the below rules for variable naming conventions

i = signed integer
ui = unsigned integer
su = short, unsigned integer
si = short, signed integer 
lu = long, unsigned integer
li = long, signed integer
b = byte
sb = signed byte
f = float (32 bit)
d = double (64 bit)
dec = decimal (128 bits)
boo = boolean values (True/False)
ch = char
E = enumerated type
S = struct
o = object
C = class
I = interface
arr = array
D = delegate

A basic function, already defined in codegen's builder can be defined ala:
class TokenName(BinaryOp):
  def eval(self):
    i = self.builder.TokenFunction(self.left.eval(), self.right.eval())
    return i
    
It's important to note, we are not passing variables into the function as you usually do in python, we get our variables from the previous page e.g. one token to the left) and the next page (one token to the right) that we then pass into codegen.

You should refer to the codegen documentation for the function you are implementing to ensure you are passing the correct variables, in general they *should* be added from left to right, but it never hurts to double check.

## Step 3 — Add function to the Parser
This is a bit more difficult, and you will need to read the rply parser documentation to understand what's going on.

First, we need to import the function:
from ast import TokenName

then, we need to add your token to the list of tokens accepted by the parser.

After that, if you're adding a novel/new function, create a new one in the parse class:

@self.pg.production('expression: TOKEN_NAME OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
def expressions_token_name(p):
  #your code
  return #your output 
  
If your code can be added to an existing expression, do so.

## Step 4 ­— Testing
And now comes the part we've all been waiting for, create a new file and test your new token out, try to use it in as many ways as possible, make sure it works, then submit a pull request
