# MAJU 1.0 — evaluator.py
# Desenvolvido por caos

from src.ast_nodes import *
from src.builtins import BUILTINS

class Evaluator:
    def __init__(self):
        self.env = {}

    def eval(self, node):
        if isinstance(node, BlockNode):
            for stmt in node.statements:
                value = self.eval(stmt)
            return value

        if isinstance(node, NumberNode):
            return node.value

        if isinstance(node, StringNode):
            return node.value

        if isinstance(node, VarAssignNode):
            value = self.eval(node.expr)
            self.env[node.name] = value
            return value

        if isinstance(node, VarAccessNode):
            return self.env.get(node.name, None)

        if isinstance(node, BinOpNode):
            left = self.eval(node.left)
            right = self.eval(node.right)
            if node.op.type == "PLUS": return left + right
            if node.op.type == "MINUS": return left - right
            if node.op.type == "MUL": return left * right
            if node.op.type == "DIV": return left / right

        return None
