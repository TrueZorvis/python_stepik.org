N = int(input())
matrix = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
for row in matrix:
    print(*row)
