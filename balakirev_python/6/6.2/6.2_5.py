num_lst = list(map(int, input().split()))
d = dict.fromkeys(num_lst)
print(*d.keys())
