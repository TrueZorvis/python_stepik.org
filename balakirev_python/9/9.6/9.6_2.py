s = input()

lst = list(map(int, s.split()))
lst.sort()
tp_lst = tuple(lst)

print(lst)
print(tp_lst)
