#Factorial of a number


def factorialRecursive(n):

    if n>=1:
        return n*factorialRecursive(n-1)


print(factorialRecursive(4))

def factorialIterative(n):
    result=1
    for i in range (2,n+1):
        result *=i

    return result


print(factorialIterative(400))