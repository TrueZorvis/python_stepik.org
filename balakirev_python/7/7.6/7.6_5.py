lst_in1 = map(float, input().split())
lst_in2 = input().split()
lst = [*lst_in1, *lst_in2]
print(*lst)
