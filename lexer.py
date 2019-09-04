'''
Lexical analysis, lexing or tokenization is the process of converting
a sequence of characters (such as in a computer program or web page) into
a sequence of tokens (strings with an assigned and thus identified meaning)
[https://en.wikipedia.org/wiki/Parsing]
'''

from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        ''' Definitions for all possible tokens '''

        # Print statement
        self.lexer.add('PRINT', r'print')

        # Left Parenthesis
        self.lexer.add('OPEN_PAREN', r'\(')

        # Close Parenthesis
        self.lexer.add('CLOSE_PAREN', r'\)')

        # Semicolon
        self.lexer.add('SEMI_COLON', r'\;')

        # Binary Operators
        self.lexer.add('SUM', r'\+') # Addition
        self.lexer.add('SUB', r'\-') # Subtraction

        # TODO:
        # Unary Operators

        # TODO:
        # Conditional Statements

        # TODO:
        # Loop Statements

        # Number
        self.lexer.add('NUMBER', r'\d+')

        # Ignore whitespace
        self.lexer.ignore('\s+')

    def create(self):
        self._add_tokens()
        return self.lexer.build()