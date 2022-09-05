from ply import *

tokens = [
    'FRONTMATTER',
    'PROPERTY',
    'SPACE',
    'OPENING_BRACKET',
    'CLOSING_BRACKET',
    'CONTENT',
    'PUNCT',
    'QUOTE',
    'NUMBER',
    'CODE_BLOCK',
    'CODE'
]

t_FRONTMATTER = r"---"
t_PROPERTY = r"[A-Za-z_/]+:"
t_SPACE = r"\s+"
t_OPENING_BRACKET = r"\["
t_CLOSING_BRACKET = r"\]"
t_CONTENT = r"[A-Za-z_/]+"
t_PUNCT = r"[,.!?—]+"
t_QUOTE = r"[\"']+"
t_NUMBER = r"([0-9]+[,.:-]*)+"
t_CODE_BLOCK = r"[`{3}.*`{3}]+"

# Ignored token with an action associated with it
def t_ignore_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')


# Error handler for illegal characters
def t_error(t):
    print(f'Illegal character {t.value[0]!r}')
    t.lexer.skip(1)


lex.lex()

if __name__ == '__main__':
    lex.runmain()

