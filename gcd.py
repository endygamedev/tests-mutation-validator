def gcd(a: int, b: int) -> int:
    if (a < b):
        temp = a
        a = b
        b = temp

    while b != 0:
        temp = a
        a = b
        b = temp % a

    return a
