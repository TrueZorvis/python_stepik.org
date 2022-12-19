p = [0] * 10
i = 0
while i < 5:
    n = int(input())
    if n > len(p):
        continue
    if p[n] != 1:
        p[n] = 1
        i += 1
print(*p)
