def is_isolate(x, y, n, matrix):
    coords = [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]
    coords = [(x, y) for x, y in coords if x >= 0 and y >= 0 and x <= n-1 and y <= n-1]
    for a, b in coords:
        if matrix[a][b] == 1:
            return False
    return True


def verify(matrix):
    N = len(matrix)
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                if not is_isolate(i, j, N, matrix):
                    return False
    return True


matrix = [[1, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 1], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]

print(verify(matrix))
