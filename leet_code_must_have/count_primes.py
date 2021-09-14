"""
Count the number of prime numbers less than a non-negative number, n.
"""
from math import ceil, sqrt


class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0

        counter = 0
        for i in range(2, n + 1):
            if self.is_prime(i):
                counter += 1

        return counter

    def is_prime(self, n: int) -> bool:
        # we can check numbers up to ceil(sqrt(n)),
        # as all next values are just squares of previous numbers
        if n == 0 or n == 1:
            return False
        if n == 2:
            return True

        right_bound = ceil(sqrt(n)) + 1
        for i in range(2, right_bound):
            if n % i == 0:
                return False
        return True


class Solution2:
    def countPrimes(self, n: int) -> int:
        # Sieve of Eratosthenes algorithm
        not_primes = [False] * n
        not_primes[0] = True
        not_primes[1] = True

        for i in range(2, ceil(sqrt(n))):
            if not not_primes[i]:
                j = 2
                while i * j < n:
                    not_primes[i * j] = True
                    j += 1

        return sum(not_primes)



if __name__ == '__main__':
    s = Solution()
    print(s.countPrimes(10))

    s2 = Solution2()
    print(s.countPrimes(10))
