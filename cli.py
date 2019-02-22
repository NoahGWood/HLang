#!/usr/bin/env python3
"""Noah's Language Compiler

Usage:
    cli.py <infile> [<outfile>]
    cli.py <infile> [<outfile>] -a
    cli.py <infile> [<outfile>] -o
    cli.py <infile> [<outfile>] -c
    cli.py -h|--help
    cli.py -v|--version

Options:
    -a --assembly  Only generate assembly language (LLVM)
    -o --object  Generate native object file (from .ll)
    -c --compile  Compile object file (from .o)
    -h --help  Show this screen.
    -v --version  Show version

"""

from lexer import Lexer
from parser import Parser
from codegen import CodeGen
from docopt import docopt
import subprocess

def genASM(infile, outfile="output.ll"):
    print("Input File: {}".format(infile))
    print("Output File: {}".format(outfile))
    with open(infile) as f:
        text_input = f.read()

    lexer = Lexer().get_lexer()
    tokens = lexer.lex(text_input)

    codegen = CodeGen()

    module = codegen.module
    builder = codegen.builder
    printf = codegen.printf

    pg = Parser(module, builder, printf)
    pg.parse()
    parser = pg.get_parser()
    parser.parse(tokens).eval()

    codegen.create_ir()
    codegen.save_ir(outfile)
    return outfile

def genObj(infile, outfile="output.o"):
    print("generating object file")
    subprocess.Popen(['llc', '-filetype=obj', infile]).wait()
    return outfile

def compileObj(infile, outfile="output"):
    print("compiling object file")
    subprocess.Popen(['gcc',infile,'-o',outfile]).wait()
    return outfile

def allInOne(infile,outfile="output"):
    asm = genASM(infile)
    print(asm)
    obj = genObj(asm)
    print(obj)
    compileObj(obj,outfile)

if __name__ =='__main__':
    arguments = docopt(__doc__, version='ALPHA 1.0')
    print(arguments)
    if arguments['<infile>']:
        if arguments['<infile>'] and arguments['<outfile>']:
            if arguments['--assembly']:
                genASM(arguments['<infile>'], arguments['<outfile>'])
            elif arguments['--object']:
                genObj(arguments['<infile>'], arguments['<outfile>'])
            elif arguments['--compile']:
                compileObj(arguments['<infile>'], arguments['<outfile>'])
            else:
                allInOne(arguments['<infile>'], arguments['<outfile>'])
        else:
            if arguments['--assembly']:
                genASM(arguments['<infile>'])
            elif arguments['--object']:
                genObj(arguments['<infile>'])
            elif arguments['--compile']:
                compileObj(arguments['<infile>'])
            else:
                allInOne(arguments['<infile>'])
    else:
        print(arguments)
