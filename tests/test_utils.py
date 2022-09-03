import unittest
from utils import *


class TestUtils(unittest.TestCase):
    def test_read_file(self):
        file = read_file("tests/fixtures/example_post.md")
        self.assertEqual(file, "some content")


if __name__ == '__main__':
    unittest.main()
