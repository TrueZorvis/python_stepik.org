data_lst = [item.split('=') for item in input().split()]
data_lst = [[item[0], int(item[1])] for item in data_lst]
d = dict(data_lst)
print(*sorted(d.items()))
