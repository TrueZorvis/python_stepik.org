num_list = list(map(int, input().split()))

for i in range(len(num_list) - 1, 0, -1):
    for j in range(0, i):
        if num_list[j + 1] < num_list[j]:
            num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]

print(*num_list)
