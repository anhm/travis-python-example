import os
import unittest

for k, v in os.environ.items():
    print "%s:%s" %  (k, v)

import example

class TestPython(unittest.TestCase):
    def test_a(self):
        self.assertEqual(example.a(), 1)

    def test_b(self):
        self.assertEqual(example.b(), 1)


if __name__ == '__main__':

    unittest.main()
