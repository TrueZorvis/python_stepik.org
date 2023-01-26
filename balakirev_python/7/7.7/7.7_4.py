num = int(input())


def fib_rec(n, f=[1, 1]):
    if len(f) < n:
        f.append(f[-1] + f[-2])
        fib_rec(n, f)
    return f


res = fib_rec(num)
print(*res)
