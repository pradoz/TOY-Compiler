from lexer import Lexer
from parser import Parser
from code_generator import CodeGen

# text_input = """
# print(6 - 10 +    2);
# """

# Input filename
fname ="input.toy"

# Open input file
with open(fname) as f:
    text_input = f.read()

# Initialize new Lexer object
lexer = Lexer().create()

# Tokenize the text input with the lexer object
tokens = lexer.lex(text_input)

# Test print statement
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


# Initialize new CodeGen object
code_generator = CodeGen()

# Configure the code_generator
module = code_generator.module
builder = code_generator.builder
printf = code_generator.printf

# Initialize Parser object with the configured code_generator
pg = Parser(module, builder, printf)
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()

code_generator.create_ir()
code_generator.save_ir("output.l1")