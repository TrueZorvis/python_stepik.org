n = int(input())
l = list()
i = 0
while i != n:
    i += 1
    if n >= 100:
        print("слишком большое значение n")
        break
    if i % 3 == 0 and i % 5 == 0:
        l.append(i)
else:
    print(*l)
