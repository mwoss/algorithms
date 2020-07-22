"""
Let’s count the number of divisors of n. The easiest approach is to iterate through all the
numbers from 1 to n and check whether or not each one is a divisor. The time complexity of
this solution is O(n).
There is a simple way to improve the above solution. Based on one divisor, we can find
the symmetric divisor. More precisely, if number a is a divisor of n, then n
a is also a divisor.
One of these two divisors is less than or equal to √n. (If that were not the case, n would be
a product of two numbers greater than √n, which is impossible.)

Divisor is a number that has more than 2 divisors
"""


def divisors(n):
    # Count the number of divisors, eg 12 has 6 divisors: 1, 2, 3, 4, 6, 12
    divisors_count = 0

    i = 1
    while i * i < n:
        if n % i == 0:
            divisors_count += 2
        i += 1

    if i * i == n:
        divisors_count += 1

    return divisors_count


if __name__ == '__main__':
    print(divisors(12))
