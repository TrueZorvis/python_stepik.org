from math import factorial as mf


def factorial(n):
    p = 1
    for i in range(2, n+1):
        p *= i

    print("my factorial")
    return p


print(factorial(5))
print(mf(5))
