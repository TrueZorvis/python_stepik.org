lst_in = list(map(int, input().split()))
print(all(map(lambda x: not x % 2, lst_in)))
