lst_in = list(input().split())
start = int(lst_in[0])
lst = lst_in[1:]
d = {start + i: value for i, value in enumerate(lst)}
print(d[4])
