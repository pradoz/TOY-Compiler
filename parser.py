'''
Parsing, syntax analysis, or syntactic analysis is the process of analysing a
string of symbols, either in natural language, computer languages or data
structures, conforming to the rules of a formal grammar. The term parsing
comes from Latin pars (orationis), meaning part (of speech).
[https://en.wikipedia.org/wiki/Parsing]
'''

from rply import ParserGenerator
from ast import Number, Sum, Sub, Print


class Parser():
    def __init__(self):
        # List of tokens accepted by the parser
        self.pg = ParserGenerator([   
                  'NUMBER',
                  'PRINT',
                  'OPEN_PAREN',
                  'CLOSE_PAREN',
                  'SEMI_COLON',
                  'SUM',
                  'SUB'
                ])
        self.module = module
        self.builder = builder
        self.printf = printf

    def parse(self):
        @self.pg.production('program : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def program(p):
            return Print(self.builder, self.module, self.printf, p[2])

        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        def expression(p):
            left = p[0]
            operator = p[1]
            right = p[2]
            if operator.gettokentype() == 'SUM':
                return Sum(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(self.builder, self.module, left, right)

        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(self.builder, self.module, p[0].value)

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()