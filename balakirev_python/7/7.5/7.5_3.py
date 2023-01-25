def get_even(*args):
    return [n for n in args if n % 2 == 0]


print(get_even(1, 2, 3, 4, 5, 6, 7, 8))
