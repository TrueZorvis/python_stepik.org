lst_in = input().split()

res = sorted(lst_in, key=len, reverse=True)
print(*res)
