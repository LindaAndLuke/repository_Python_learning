import re

# get the number from the user
print("Enter the number you want to check:")
inputNum = input()

# validate the input
inputNumStrip = inputNum.strip()
if not re.fullmatch(r"[+-]?\d+", inputNumStrip):
    print(f"{inputNumStrip} is NOT an integer.")
    exit

# convert to integer and check if positive
inPutNumInt = int(inputNumStrip)
if inPutNumInt <= 0:
    print(f"{inPutNumInt} is NOT a positive integer.")
    exit

# check if prime
notPrime = False
for n in range(2, inPutNumInt//2+1):
    if inPutNumInt % n == 0:
        if notPrime == False:
            print(f"{inPutNumInt} is NOT a prime number.")
            notPrime = True
        print(f"It is divisible by {n}.")
        

if not notPrime:
    # if no divisors found, it is prime
    print(f"{inPutNumInt} is a prime number.")
