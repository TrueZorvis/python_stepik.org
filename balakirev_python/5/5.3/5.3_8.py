n = int(input())
output = 'ДА'
for x in range(2, n):
    if n % x == 0:
        output = 'НЕТ'
        break
print(output)
