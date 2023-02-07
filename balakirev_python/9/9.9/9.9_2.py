lst_in = list(map(float, input().split()))
print(any(map(lambda x: x < 0, lst_in)))
