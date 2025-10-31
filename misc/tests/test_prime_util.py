import unittest

import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 
from prime_util import isPrimeNumber
''''''
# from misc.prime_util import isPrimeNumber

class PrimeNumberRelateTests(unittest.TestCase):
    # Test methods go here
    def test_isPrimeNumber(self):
            resultFalse = isPrimeNumber(10)
            self.assertFalse(resultFalse)
            resultTrue = isPrimeNumber(13)
            self.assertTrue(resultTrue)
  
if __name__ == '__main__':
    unittest.main()
