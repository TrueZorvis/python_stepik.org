numbers = list(map(int, input().split()))
sum = 0
for x in numbers:
    if x % 2 != 0:
        sum += x
print(sum)
