# greatest common divisor


def gcdIterative(a, b):
    while b != 0:
        a, b = b, (a % b)

    return a


def gcdRecursive(a, b):
    if b == 0:
        return a
    else:
        return gcdRecursive(b, a % b)


a = 12
b = 5

print(gcdIterative(a, b))
print(gcdRecursive(a, b))
