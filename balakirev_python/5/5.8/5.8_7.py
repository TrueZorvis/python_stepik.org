lst_in = list(map(float, input().split()))

lst = [lst_in[i] for i in range(len(lst_in)) if i % 2 == 0]

print(*lst)
