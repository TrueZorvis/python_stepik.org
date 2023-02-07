def is_free(lst):
    return any(map(lambda row: '#' in row, lst))


lst_in = ['# x o', 'x # x', 'o o #']
print(is_free(lst_in))
