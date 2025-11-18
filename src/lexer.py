# MAJU 1.0 — lexer.py
# Desenvolvido por caos

from src.tokens import Token, KEYWORDS, DIGITS, LETTERS

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current = None
        self.advance()

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current = self.text[self.pos]
        else:
            self.current = None

    def make_tokens(self):
        tokens = []

        while self.current:
            if self.current in " \t\r":
                self.advance()
            elif self.current == "#":
                self.skip_comment()
            elif self.current in DIGITS:
                tokens.append(self.make_number())
            elif self.current in LETTERS:
                tokens.append(self.make_identifier())
            elif self.current == '"':
                tokens.append(self.make_string())
            else:
                tokens.append(self.make_symbol())
                self.advance()

        return tokens

    def skip_comment(self):
        while self.current and self.current != "\n":
            self.advance()

    def make_string(self):
        self.advance()
        value = ""

        while self.current and self.current != '"':
            value += self.current
            self.advance()

        self.advance()
        return Token("STRING", value)

    def make_number(self):
        num = ""
        while self.current and self.current in DIGITS:
            num += self.current
            self.advance()
        return Token("NUMBER", int(num))

    def make_identifier(self):
        word = ""
        while self.current and (self.current in LETTERS or self.current in DIGITS):
            word += self.current
            self.advance()

        if word.lower() in KEYWORDS:
            return Token(KEYWORDS[word.lower()])

        return Token("IDENT", word)

    def make_symbol(self):
        symbols = {
            "+": "PLUS",
            "-": "MINUS",
            "*": "MUL",
            "/": "DIV",
            "=": "EQ",
            "(": "LPAREN",
            ")": "RPAREN",
            "{": "LBRACE",
            "}": "RBRACE",
        }
        return Token(symbols.get(self.current, "UNKNOWN"), self.current)
