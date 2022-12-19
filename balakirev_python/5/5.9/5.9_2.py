lst_in = list(map(int, input().split()))

N = int(len(lst_in) ** 0.5)

lst = [[lst_in[i + j * N] for i in range(N)] for j in range(N)]

print(lst)
