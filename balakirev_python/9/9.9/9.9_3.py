def is_string(lst):
    return all(map(lambda x: type(x) is str, lst))


print(is_string(['1', '2', 3]))
print(is_string(['1', '2', '3']))
