def get_rect_value(a, b, type=0):
    if not type:
        return 2 * (a + b)
    return a * b


print(get_rect_value(2, 3))
