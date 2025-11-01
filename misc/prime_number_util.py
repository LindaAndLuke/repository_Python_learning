# Utilities for prime number related operations

# Check if an input int number is prime
def isPrimeNumber(inputNumInt):
    isPrime = True
    for n in range(2, inputNumInt//2+1):
        if inputNumInt % n == 0:
            isPrime = False
            break
    return isPrime

# Get all prime factors of an input int number
def get_prime_factors(number):
    prime_factors = []
    for n in range(2, number + 1):
        while number % n == 0:
            prime_factors.append(n)
            number //= n
    return prime_factors

# Check if an input string is a positive int number
def isPositiveIntNumber(inputStr):
    try:
        val = int(inputStr)
        if val > 0:
            return True
        else:
            return False
    except ValueError:
        return False