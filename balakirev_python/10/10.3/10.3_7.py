import random
# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)
# начальная инициализация поля (переменные P и N не менять, единицы записывать в список P)
N = int(input())
P = [[0] * N for i in range(N)]
M = 10


def is_free(x, y):
    coords = [(x, y), (x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]
    valid_coords = filter(lambda coord: 0 <= coord[0] <= N-1 and 0 <= coord[1] <= N-1, coords)
    for a, b in valid_coords:
        if P[a][b]:
            return False
    return True


while M > 0:
    x, y = random.randint(0, N - 1), random.randint(0, N - 1)
    if is_free(x, y):
        P[x][y] = 1
        M -= 1

for row in P:
    print(*row)
