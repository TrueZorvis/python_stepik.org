numbers = list(map(float, input().split()))
min_number = numbers[0]

for i, num in enumerate(numbers):
    if num < min_number:
        min_number = numbers[i]
print(min_number)
