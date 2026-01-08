import re

TOKEN_SPECIFICATION = [
    ('KEYWORD', r'\b(class|public|static|void|int|float|if|else|return|new)\b'),
    ('IDENTIFIER', r'\b[a-zA-Z_][a-zA-Z_0-9]*\b'),
    ('NUMBER', r'\b\d+\b'),
    ('OPERATOR', r'[+\-*/=]'),
    ('SEPARATOR', r'[;{}()\[\]]'),
    ('WHITESPACE', r'\s+'),
    ('UNKNOWN', r'.'),
]

token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPECIFICATION)

def tokenize(code):
    tokens = []
    for match in re.finditer(token_regex, code):
        kind = match.lastgroup
        value = match.group()
        if kind != 'WHITESPACE':
            tokens.append((kind, value))
    return tokens
