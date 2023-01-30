lst_in = list(map(lambda x: x if len(x) > 5 else '-', input().split()))
print(*lst_in)
