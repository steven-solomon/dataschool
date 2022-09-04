import pandas as pd


def read_file(p):
    with open(p) as f:
        lines = f.readlines()
    return ''.join(lines)


def parse_file(df, content):
    content_row = pd.DataFrame({'title': ['Mocking Functions in Elixir With ExDoubles']})
    return pd.concat([df, content_row], ignore_index=True)
