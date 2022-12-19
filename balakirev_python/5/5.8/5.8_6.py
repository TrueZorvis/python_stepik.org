N = int(input())

mtrx = [[i for _ in range(N)] for i in range(N)]

for row in mtrx:
    print(*row)
