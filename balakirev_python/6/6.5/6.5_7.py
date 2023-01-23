num = int(input())
setA = set()
setB = {2, 3, 5}
for x in (1, 2, 3, 5, 7):
    if num % x == 0:
        setA.add(x)

print('ДА') if setB <= setA else print('НЕТ')
