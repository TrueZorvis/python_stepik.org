nums = tuple(map(int, input().split()))

res = ()
for n in nums:
    if n not in res:
        res += n,
print(*res)
