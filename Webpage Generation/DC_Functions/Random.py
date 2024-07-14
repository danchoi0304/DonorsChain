import random

#Making unique code for tracking
def hexa_random():
    # Generate a random integer between 0 and 0xFFFFFF (16777215 in decimal)
    random_number = random.randint(0, 0xFFFFFFFFFF)

    # Convert the random number to a 6-digit hexadecimal string
    hexadecimal_code = format(random_number, '06X')

    return(hexadecimal_code)

