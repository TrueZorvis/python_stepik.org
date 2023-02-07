def get_list_dig(lst):
    return list(filter(lambda x: type(x) in (int, float), lst))


print(get_list_dig([1, 2, 3, "a", True, [4, 5], "c", (4, 5)]))
print(get_list_dig({5, 6, 7, '8', 5, '4'}))
print(get_list_dig((10, "f", '33', True, 12)))
print(get_list_dig(['1', True, False, (1, 23)]))
