n = int(input())
a, b, l = 1, 1, 2
print("1 1", end=' ')
while l < n:
    l += 1
    print(f"{a + b}", end=' ')
    a, b = b, (a + b)
