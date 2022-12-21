nums = tuple(map(int, input().split()))

for i in range(len(nums)):
    if nums.count(nums[i]) > 1:
        print(i, end=' ')
