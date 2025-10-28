import re

def check_if_valid_integer(input_string):
    input_string_strip = input_string.strip()
    if not re.fullmatch(r"[+-]?\d+", input_string_strip):
        return False, None
    return True, int(input_string_strip)

def is_positive_integer(number):
    return number > 0

def get_prime_factors(number):
    prime_factors = []
    for n in range(2, number + 1):
        while number % n == 0:
            prime_factors.append(n)
            number //= n
    return prime_factors

# get the number from the user
print("Enter the number you want to check:")
inputNum = input()

# check input validity
is_valid, inputNumInt = check_if_valid_integer(inputNum)
if not is_valid:
    print(f"{inputNum.strip()} is NOT an integer.")
    exit()
if not is_positive_integer(inputNumInt):
    print(f"{inputNumInt} is NOT a positive integer.")
    exit()
# get prime factors
factors = get_prime_factors(inputNumInt)
if factors == [inputNumInt]:
    print(f"{inputNumInt} is a prime number and has no prime factors other than itself.")
else:
    print(f"Prime factors of {inputNumInt} are: {factors}")