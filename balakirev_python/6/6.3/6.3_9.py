t = ((1, 0, 0, 0, 0),
     (0, 1, 0, 0, 0),
     (0, 0, 1, 0, 0),
     (0, 0, 0, 1, 0),
     (0, 0, 0, 0, 1))

n = int(input())

t2 = tuple([t[i][:n] for i in range(n)])
# t2 = tuple([row[:n] for row in t[:n]])

for row in t2:
    print(*row)
