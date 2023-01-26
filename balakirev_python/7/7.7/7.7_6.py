d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]


def get_line_list(d, a=[]):
    for item in d:
        if type(item) == list:
            get_line_list(item, a)
        else:
            a.append(item)
    return a


res = get_line_list(d)
print(res)
