from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Comment
        self.lexer.add('COMMENT', r'#')
#        self.lexer.add('EOL', r'\n+')
        self.lexer.ignore('\n')
        self.lexer.add('IDENT', r'    ')
        self.lexer.add('IDENT', r'\t')
        self.lexer.add('SPACE', r'\s+')
        # Print
        self.lexer.add('PRINT', r'print')
        # Parenthesis
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')
        # Brackets
        self.lexer.add('OPEN_BRACKET', r'\[')
        self.lexer.add('CLOSE_BRACKET', r'\]')
        # Curly Brackets
        self.lexer.add('OPEN_CURLY', r'\{')
        self.lexer.add('CLOSE_CURLY', r'\}')
        # Semi Colon
        self.lexer.add('SEMI_COLON', r'\;')
        # Operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        self.lexer.add('MUL', r'\*')
        self.lexer.add('DIV', r'\/')
        # Number
        self.lexer.add('NUMBER', r'\d+')
        # Quote
        self.lexer.add('DOUBLE_QOUTE', r'"')
        self.lexer.add('SINGLE_QUOTE', r"'")
        # Finished Builtin Functions
        # Python Functions To Transfer
        ## Note: Not all of these are guaranteed to be implemented
        ## each function needs to be evaluated to determine usefulness
        self.lexer.add('ABS', r'abs')
        self.lexer.add('ALL', r'all')
        self.lexer.add('ANY', r'any')
        self.lexer.add('ASCII', r'ascii')
        self.lexer.add('BIN', r'bin')
        self.lexer.add('BOOL', r'bool')
        self.lexer.add('BREAKPOINT', r'breakpoint')
        self.lexer.add('BYTE_ARRAY', r'bytearray')
        self.lexer.add('BYTES', r'bytes')
        self.lexer.add('CALLABLE', r'callable')
        self.lexer.add('CHR', r'chr')
        self.lexer.add('CLASS_METHOD', r'classmethod')
        self.lexer.add('COMPILE', r'compile')
        self.lexer.add('COMPLEX', r'complex')
        self.lexer.add('DEL_ATTR', r'delattr')
        self.lexer.add('DICT', r'dict')
        self.lexer.add('DIR', r'dir')
        self.lexer.add('DIVMOD', r'divmod')
        self.lexer.add('ENUMERATE', r'enumerate')
        self.lexer.add('EVAL', r'eval')
        self.lexer.add('EXEC', r'exec')
        self.lexer.add('FILTER', r'filter')
        self.lexer.add('FLOAT', r'float')
        self.lexer.add('FORMAT', r'format')
        self.lexer.add('FROZENSET', r'frozenset')
        self.lexer.add('GETATTR', r'getattr')
        self.lexer.add('GLOBALS', r'globals')
        self.lexer.add('HASATTR', r'hasattr')
        self.lexer.add('HASH', r'hash')
        self.lexer.add('HELP', r'help')
        self.lexer.add('HEX', r'hex')
        self.lexer.add('ID', r'id')
        self.lexer.add('INPUT', r'input')
        self.lexer.add('INT', r'int')
        self.lexer.add('IS_INSTANCE', r'isinstance')
        self.lexer.add('IS_SUBCLASS', r'issubclass')
        self.lexer.add('ITER', r'iter')
        self.lexer.add('LEN', r'len')
        self.lexer.add('LIST', r'list')
        self.lexer.add('LOCALS', r'locals')
        self.lexer.add('MAP', r'map')
        self.lexer.add('MAX', r'max')
        self.lexer.add('MEMORY_VIEW', r'memoryview')
        self.lexer.add('MIN', r'min')
        self.lexer.add('NEXT', r'next')
        self.lexer.add('OBJECT', r'object')
        self.lexer.add('OCT', r'oct')
        self.lexer.add('OPEN', r'open')
        self.lexer.add('ORD', r'ord')
        self.lexer.add('POW', r'pow')
        self.lexer.add('PROPERTY', r'property')
        self.lexer.add('RANGE', r'range')
        self.lexer.add('REPR', r'repr')
        self.lexer.add('REVERSED', r'reversed')
        self.lexer.add('ROUND', r'round')
        self.lexer.add('SET', r'set')
        self.lexer.add('SETATTR', r'setattr')
        self.lexer.add('SLICE', r'slice')
        self.lexer.add('SORTED', r'sorted')
        self.lexer.add('STATICMETHOD', r'staticmethod')
        self.lexer.add('STR', r'str')
        self.lexer.add('SUM', r'sum')
        self.lexer.add('SUPER', r'super')
        self.lexer.add('TUPLE', r'tuple')
        self.lexer.add('TYPE', r'type')
        self.lexer.add('VARS', r'vars')
        self.lexer.add('ZIP', r'zip')
        self.lexer.add('IMPORT', r'import')
        # Characters
        #self.lexer.add('CHAR', r"[a-z]")
        #self.lexer.add('CHAR', r"[A-Z]")
        self.lexer.add('CHAR', r'\w')
        self.lexer.add('SPECIAL_CHAR', r'\W')
        # Ignore all undefined
        # Ignore spaces
        #self.lexer.ignore('\s+')
    

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
