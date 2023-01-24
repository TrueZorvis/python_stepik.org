def is_triangle(a, b, c):
    return a < b + c and b < a + c and c < b + a


print(is_triangle(3, 4, 5))
