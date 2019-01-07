# Fibonaci sequence Recursion and Dynamic Programming


def fibonaci(n):
    a, b = 0, 1

    for i in range(0, n):
        a, b = b, a + b

    return a


print(fibonaci(10))


# Python fibonaci seq generator with yield
def fibonaciIter():
    a, b = 1, 1

    while True:
        yield a
        a, b = b, a + b


for index, fib_num in zip(range(10), fibonaciIter()):
    print('{f:3}'.format(f=fib_num))


# Recursive way ( with memoization)
def fibonaciRecursive(n, _cache={}):
    if n in _cache:
        return _cache[n]
    elif n>1:
        return _cache.setdefault(n,fibonaciRecursive(n - 1) + fibonaciRecursive(n - 2))
    return n


print(fibonaciRecursive(100))
