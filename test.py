import math

w = math.factorial(13)


def permutation(a, b):
    return (math.factorial(a) / math.factorial(a - b))


def combination(c, d):
    return (math.factorial(c) / math.factorial(c - d) / math.factorial(d))


pp = permutation(5, 5)
cc = combination(32, 16)
