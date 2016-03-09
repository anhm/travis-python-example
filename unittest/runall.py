import unittest

import example

class TestPython(unittest.TestCase):
    def test_a(self):
        self.assertEqual(example.a(), 1)

    def test_b(self):
        self.assertEqual(example.b(), 1)


if __name__ == '__main__':
    unittest.main()
