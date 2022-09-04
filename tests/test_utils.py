import unittest

import pandas as pd

from utils import *


class TestUtils(unittest.TestCase):
    def test_read_file(self):
        file = read_file("tests/fixtures/example_post.md")
        self.assertEqual(file, "some content")

    def test_parse_post(self):
        file = read_file("tests/fixtures/post.md")
        empty_frame = pd.DataFrame()

        result = parse_file(empty_frame, file)

        self.assertEqual(result.loc[0, 'title'], "Mocking Functions in Elixir With ExDoubles")


if __name__ == '__main__':
    unittest.main()
