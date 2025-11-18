# MAJU 1.0 — parser.py
# Desenvolvido por caos

from src.ast_nodes import *
from src.tokens import Token

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = -1
        self.advance()

    def advance(self):
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current = self.tokens[self.pos]
        return self.current

    def parse(self):
        statements = []

        while self.current:
            statements.append(self.statement())
            self.advance()

        return BlockNode(statements)

    def statement(self):
        if self.current.type == "VAR":
            return self.var_assign()

        if self.current.type == "IDENT":
            name = self.current.value
            self.advance()
            if self.current.type == "EQ":
                self.advance()
                expr = self.expr()
                return VarAssignNode(name, expr)

        return self.expr()

    def var_assign(self):
        self.advance()
        name = self.current.value
        self.advance()

        if self.current.type != "EQ":
            raise Exception("Esperado '='")

        self.advance()
        expr = self.expr()
        return VarAssignNode(name, expr)

    def expr(self):
        node = self.term()
        while self.current and self.current.type in ("PLUS", "MINUS"):
            op = self.current
            self.advance()
            node = BinOpNode(node, op, self.term())
        return node

    def term(self):
        node = self.factor()
        while self.current and self.current.type in ("MUL", "DIV"):
            op = self.current
            self.advance()
            node = BinOpNode(node, op, self.factor())
        return node

    def factor(self):
        tok = self.current

        if tok.type == "NUMBER":
            return NumberNode(tok.value)

        if tok.type == "STRING":
            return StringNode(tok.value)

        if tok.type == "IDENT":
            return VarAccessNode(tok.value)

        raise Exception(f"Erro inesperado: {tok}")
