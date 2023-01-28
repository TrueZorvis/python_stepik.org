def sort_list(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return sorted(res)

    return wrapper


@sort_list
def get_list(string):
    return list(map(int, string.split()))


str_in = input()
lst = get_list(str_in)
print(*lst)
