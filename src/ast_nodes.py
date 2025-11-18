# MAJU 1.0 — ast_nodes.py
# Desenvolvido por caos

class NumberNode:
    def __init__(self, value):
        self.value = value

class StringNode:
    def __init__(self, value):
        self.value = value

class VarAssignNode:
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr

class VarAccessNode:
    def __init__(self, name):
        self.name = name

class BinOpNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class BlockNode:
    def __init__(self, statements):
        self.statements = statements
