N = int(input())


def get_num(n):
    a, b, c = 1, 1, 1

    for i in range(1, n + 1):
        if i < 4:
            pass
        else:
            a, b, c = b, c, a + b + c
        yield c


for i in get_num(N):
    print(i, end=" ")
