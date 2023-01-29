a = int(input())

g = (i ** 3 for i in (abs(x) for x in range(-a, a + 1)))

for _ in range(4):
    print(next(g), end=' ')
