cities = tuple(input().split())

res = ()
for i in cities:
    if i != "Ульяновск":
        res += i,
print(*res)
