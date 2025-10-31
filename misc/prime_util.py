# Utilities for prime number related operations

# Check if an input int number is prime
def isPrimeNumber(inputNumInt):
    isPrime = True
    for n in range(2, inputNumInt//2+1):
        if inputNumInt % n == 0:
            isPrime = False
            break
    return isPrime