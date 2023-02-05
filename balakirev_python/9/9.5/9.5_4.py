lst_in = input().split()

# lst = [[lst_in[i], lst_in[i+3], lst_in[i+6]] for i in range(len(lst_in) // 3)]
# table = zip(*lst)
# for row in table:
#     print(*row)

a = iter(lst_in)
for i in zip(a, a, a):
    print(*i)
