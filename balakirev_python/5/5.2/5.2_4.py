cities = input().split()
msg = 'ДА'
i = 0
while i < len(cities):
    if len(cities[i]) <= 5:
        msg = "НЕТ"
        break
    i += 1
print(msg)
