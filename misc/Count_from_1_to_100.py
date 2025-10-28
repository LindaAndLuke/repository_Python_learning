import random

# Generate a random integer between 1 and 100
counter = 0
already_generated = set()
str_with_comma = ""
output = ""
while counter < 100:
    random_number = random.randint(1, 100)
    if random_number not in already_generated:
        #print(random_number)
        if counter <= 98:
            str_with_comma = str(random_number) + ", "
        else:
            str_with_comma = str(random_number)
        
        output += str_with_comma
        already_generated.add(random_number)
        counter += 1


print(output)
# Print the generated number
print("The END")