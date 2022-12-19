numbers = list(map(float, input().split()))

for i, num in enumerate(numbers):
    if num < 0:
        numbers[i] = -1.0
print(*numbers)
