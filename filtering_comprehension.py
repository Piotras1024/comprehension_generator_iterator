from pprint import pprint as pp
from math import sqrt


def is_prime(x: int):
    '''

    Args(x):
        integer
    Returns:
        True if a x number is first number, otherwise False
    '''
    if x < 2:
        return False
    for i in range(2, int(sqrt(x))+  1):
        if x % i == 0:
            return False
    return True

### print all first number from 0 to 100
first_numbers_list = [x for x in range(101) if is_prime(x)]
print(first_numbers_list)
### end of print

### creating a dict that key is a number diveded by 3 numbers,
### and value is that 3 numbers in a tuple

prime_square_divisors = {x*x: (1, x, x*x) for x in range(20) if is_prime(x)}
pp(prime_square_divisors)
