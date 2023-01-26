lst_in = list(map(int, input().split()))


def get_rec_sum(lst):
    if len(lst) < 1:
        return 0
    else:
        return lst.pop() + get_rec_sum(lst)


s = get_rec_sum(lst_in)
print(s)
