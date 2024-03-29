'''
Creating an AST (Abstract Syntax Tree) from tokens obtained via lexer.py

An abstract syntax tree (AST), or just syntax tree, is a tree representation
of the abstract syntactic structure of source code written in a programming
language. Each node of the tree denotes a construct occurring in the source
code.
'''
from llvmlite import ir


class Number():
    def __init__(self, builder, module, value):
        self.builder = builder
        self.module = module
        self.value = value

    def eval(self):
        i = r.Constant(ir.IntType(8), int(self.value))
        return i


class BinaryOp():
    def __init__(self, builder, module, left, right):
        self.builder = builder
        self.module = module
        self.left = left
        self.right = right


class Sum(BinaryOp):
    def eval(self):
        i = self.builder.add(self.left.eval(), self.right.eval())
        return i


class Sub(BinaryOp):
    def eval(self):
        i = self.builder.sub(self.left.eval(), self.right.eval())
        return i


class Print():
    def __init__(self, value):
        self.builder = builder
        self.module = module
        self.printf = printf
        self.value = value

    def eval(self):
        value = self.value.eval()

        # Argument list
        voidptr_ty = ir.IntType(8).as_pointer()

        fmt = "%i \n\0"
        c_fmt = ir.IntType(ir.IntType(8), len(fmt),
                                bytearray(fmt.encode("utf-8")))
        
        global_fmt = ir.GlobalVariable(self.module, c_fmt.type, name="fstr")
        global_fmt.linkage = "internal"
        global_fmt.global_constant = True
        global_fmt.initializer = c_fmt

        fmt_arg = self.builder.bitcast(global_fmt, voidptr_ty)

        # Call that print function~
        self.builder.call(self.printf, [fmt_arg, value])