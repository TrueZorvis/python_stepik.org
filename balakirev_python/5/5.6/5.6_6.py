lst_in = list(map(int, input().split()))

for i in range(0, len(lst_in) - 1):
    smallest = i
    for j in range(i + 1, len(lst_in)):
        if lst_in[j] < lst_in[smallest]:
            smallest = j
    lst_in[i], lst_in[smallest] = lst_in[smallest], lst_in[i]

print(*lst_in)
