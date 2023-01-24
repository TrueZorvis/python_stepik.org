def get_mul(a, b):
    return a * b


lst_in = list(map(int, input().split()))
print(get_mul(max(lst_in), min(lst_in)))
