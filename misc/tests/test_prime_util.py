import unittest

'''
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

'''

class PrimeNumberRelateTests(unittest.TestCase):
    # Test methods go here
    def test_isPrimeNumber(self):
            from misc.prime_number_util import isPrimeNumber
            resultFalse = isPrimeNumber(10)
            self.assertFalse(resultFalse)
            resultTrue = isPrimeNumber(13)
            self.assertTrue(resultTrue)

    def test_get_prime_factors(self):
        from misc.prime_number_util import get_prime_factors
        factorsOf28 = get_prime_factors(28)
        self.assertEqual(factorsOf28, [2, 2, 7])
        factorsOf13 = get_prime_factors(13)
        self.assertEqual(factorsOf13, [13   ])  # 13 is prime, so its only prime factor is itself
    
    def test_isPositiveIntNumber(self):
        from misc.prime_number_util import isPositiveIntNumber
        resultPositive = isPositiveIntNumber("25")
        self.assertTrue(resultPositive)
        resultNegative = isPositiveIntNumber("-10")
        self.assertFalse(resultNegative)
        resultNonInt = isPositiveIntNumber("abc")
        self.assertFalse(resultNonInt)
        
# end of class PrimeNumberRelateTests  
if __name__ == '__main__':
    unittest.main()
