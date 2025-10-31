import unittest

from prime_util import isPrimeNumber

class PrimeNumberRelateTests(unittest.TestCase):
    # Test methods go here
    def test_isPrimeNumber_returns_correct_value(self):
            resultFalse = isPrimeNumber(10)
            self.assertFalse(resultFalse)
            resultTrue = isPrimeNumber(13)
            self.assertTrue(resultTrue) 
  

