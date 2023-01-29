a, b = map(int, input().split())


def f(x):
    return 0.5 * pow(x, 2) - 2.0


g = (f(x / 100) for x in range(a * 100, b * 100 + 1))

for _ in range(20):
    print(round(next(g), 2), end=' ')
