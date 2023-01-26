num = int(input())


def fact_rec(n):
    if n <= 0:
        return 1
    else:
        return n * fact_rec(n-1)


res = fact_rec(num)
print(res)
