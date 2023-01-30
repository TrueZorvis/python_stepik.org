lst_in = list(map(int, input().split()))
lst = list(filter(lambda x: 9 < abs(x) < 100, lst_in))
print(*lst)
