def get_add(a, b):
    if type(a) in (int, float) and type(b) in (int, float):
        return a + b

    if type(a) is str and type(b) is str:
        return a + b

    return


print(get_add(1, 2.5))
print(get_add('hello ', 'world'))
print(get_add(True, [1, 2, 3]))
