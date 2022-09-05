import pandas as pd
import re

def read_file(p):
    with open(p) as f:
        lines = f.readlines()
    return ''.join(lines)


def parse_file(df, content):
    front_matter = (
        "title: Mocking Functions in Elixir With ExDoubles\n"
        "date: 2019-12-29T09:39:38-05:00\n"
        "featured_image: \"images/mocking_functions_in_elixir_with_exdoubles.jpeg\"\n"
        "images: [\"some/image/path.jpg\"]\n"
        "tags: ['elixir', 'coding', 'testing']\n"
    )
    title = re.match(r"title: (?<title>.*)", front_matter)
    print(title)
    content_row = pd.DataFrame({'title': [title.group("title")]})
    return pd.concat([df, content_row], ignore_index=True)
