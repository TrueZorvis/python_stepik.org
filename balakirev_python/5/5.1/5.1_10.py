n = int(input())
s = 1000
while n > 0:
    s += (s * 0.05)
    n -= 1
print(round(s, 2))
