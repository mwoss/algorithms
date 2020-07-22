def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


if __name__ == '__main__':
    print(gcd(36, 12))
