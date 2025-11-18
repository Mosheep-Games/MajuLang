# MAJU 1.0 — tokens.py
# Desenvolvido por caos

class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value

    def __repr__(self):
        if self.value: return f"{self.type}:{self.value}"
        return f"{self.type}"


KEYWORDS = {
    # Variáveis
    "var": "VAR",
    "let": "VAR",
    "variavel": "VAR",

    # Funções
    "func": "FUNC",
    "fun": "FUNC",
    "funcao": "FUNC",

    # Condicionais
    "if": "IF",
    "se": "IF",
    "else": "ELSE",
    "senao": "ELSE",

    # Loops
    "while": "WHILE",
    "enquanto": "WHILE",
    "para": "FOR",

    # Retorno
    "return": "RETURN",
    "retorne": "RETURN",
}

DIGITS = "0123456789"
LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZçÇáÁéÉíÍóÓúÚãÃõÕ_"
