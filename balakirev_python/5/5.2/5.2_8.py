x = int(input())
d = 0
l = 0
while True:
    d += 1
    if d == 1:
        l = 10
    else:
        l *= 1.1
    if l > x:
        break

print(d)
