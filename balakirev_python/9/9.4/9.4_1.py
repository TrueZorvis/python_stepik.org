lst = filter(lambda s: len(s) > 5, input().split())
for _ in range(3):
    print(next(lst), end=' ')
