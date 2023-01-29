a, b = map(int, input().split())

g = (abs(x) for x in range(a, b + 1))

for _ in range(5):
    print(next(g))
