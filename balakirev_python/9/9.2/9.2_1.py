n = int(input())


def get_sum(n):
    for x in range(1, n + 1):
        yield sum(range(1, x + 1))


g = get_sum(n)
print(*list(g))
