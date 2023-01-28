def counter_add():
    def func(x):
        return x + 5

    return func


k = int(input())
cnt = counter_add()
print(cnt(k))
