# MAJU 1.0 — maju.py
# Desenvolvido por caos

from src.lexer import Lexer
from src.parser import Parser
from src.evaluator import Evaluator

class Maju:
    @staticmethod
    def run(code):
        lexer = Lexer(code)
        tokens = lexer.make_tokens()
        parser = Parser(tokens)
        tree = parser.parse()
        evaluator = Evaluator()
        return evaluator.eval(tree)
