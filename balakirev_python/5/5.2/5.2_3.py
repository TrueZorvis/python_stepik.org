s = 1
n = 1
while n != 0:
    n = int(input())
    if n <= 0:
        continue
    s *= n
print(s)
