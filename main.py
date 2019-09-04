from lexer import Lexer

text_input = """
print(6 - 10 +    2);
"""

lexer = Lexer().create()
tokens = lexer.lex(text_input)

for token in tokens:
    print(token)

# Above print statement outputs:
# Token('PRINT', 'print')
# Token('OPEN_PAREN', '(')
# Token('NUMBER', '4')
# Token('SUM', '+')
# Token('NUMBER', '4')
# Token('SUB', '-')
# Token('NUMBER', '2')
# Token('CLOSE_PAREN', ')')