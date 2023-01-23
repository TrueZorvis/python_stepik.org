lst_in = input().lower().split()

d = {key: lst_in.count(key) for key in lst_in}
print(d.get('и', 0))
