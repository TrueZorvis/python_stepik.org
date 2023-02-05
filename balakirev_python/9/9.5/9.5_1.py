lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
m = map(lambda z: z[0] * z[1], zip(lst1, lst2))

for _ in range(3):
    print(next(m), end=' ')
