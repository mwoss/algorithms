"""
The primality test of n can be performed in an analogous way to counting the divisors. If we
find a number between 2 and n − 1 that divides n then n is a composite number. Otherwise,
n is a prime number
"""


def primality(n):
    # checks if given number can be considered as prime number
    i = 2
    while i * i < n:
        if n % i == 0:
            return False
        i += 1

    return True


if __name__ == '__main__':
    print(primality(11))
