def counter_add(n):
    def func(x):
        return x + n

    return func


k = int(input())
cnt = counter_add(2)
print(cnt(k))
