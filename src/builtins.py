# MAJU 1.0 — builtins.py
# Desenvolvido por caos

def builtin_print(value):
    print(value)

BUILTINS = {
    "print": builtin_print,
    "escreva": builtin_print,
}
