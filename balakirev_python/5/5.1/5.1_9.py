n = int(input())
cell = 1
while n > 0:
    if n % 3 == 0:
        cell *= 2
    n -= 1
print(cell)
