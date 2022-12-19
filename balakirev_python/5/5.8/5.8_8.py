lst_in1 = list(map(int, input().split()))
lst_in2 = list(map(int, input().split()))

lst = [i + j for i, j in zip(lst_in1, lst_in2)]

print(*lst)
