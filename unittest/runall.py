import os
import unittest

print 'cur path'
print os.path.abspath(os.path.curdir)
for k, v in os.environ.items():
    if k.startswith('PYTHONPATH'):
        print "%s:%s" %  (k, v)
        break
else:
    print "not found PYTHONPATH"
        

import example

class TestPython(unittest.TestCase):
    def test_a(self):
        self.assertEqual(example.a(), 1)

    def test_b(self):
        self.assertEqual(example.b(), 2)


if __name__ == '__main__':

    unittest.main()
