def filter_lst(it, key=None):
    if key is None:
        return tuple(it)

    res = ()
    for x in it:
        if key(x):
            res += (x,)

    return res


lst_in = list(map(int, input().split()))
lst = filter_lst(lst_in)
print(*lst)
lst = filter_lst(lst_in, key=lambda x: x < 0)
print(*lst)
lst = filter_lst(lst_in, key=lambda x: x >= 0)
print(*lst)
lst = filter_lst(lst_in, key=lambda x: 3 <= x <= 5)
print(*lst)
