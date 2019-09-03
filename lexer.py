from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
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

        # Number
        self.lexer.add('NUMBER', r'\d+')

        # Ignore whitespace
        self.lexer.ignore('\s+')

    def create(self):
        self._add_tokens()
        return self.lexer.build()