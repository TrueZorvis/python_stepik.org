cities = input().split()
output = 'ДА'
for i in range(len(cities)-1):
    last_char = cities[i][-1]
    if last_char in 'ьыъ':
        last_char = cities[i][-2]
    first_char = cities[i+1].lower()[0]
    if last_char != first_char:
        output = 'НЕТ'
        break
print(output)
