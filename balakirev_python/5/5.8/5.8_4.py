lst_in = input().split()

lst = [item for item in lst_in if len(item) > 5]

print(*lst)
