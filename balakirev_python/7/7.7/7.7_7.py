num = int(input())


def get_path(n):
    if n in [1, 2]:
        return n
    else:
        return get_path(n-1) + get_path(n-2)


res = get_path(num)
print(res)
