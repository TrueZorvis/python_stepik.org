d = {}
while True:
    n = int(input())
    if n == 0:
        break

    if n in d:
        print(f"значение из кэша: {d[n]}")
    else:
        d[n] = round(n ** 0.5, 2)
        print(d[n])
