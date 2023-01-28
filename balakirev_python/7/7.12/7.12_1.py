def decor_param(start=0):
    def decor_func(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return start + res
        return wrapper
    return decor_func


@decor_param(start=5)
def get_sum(string):
    return sum(map(int, string.split()))


s = input()
print(get_sum(s))
