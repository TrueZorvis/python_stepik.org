def get_dict(func):
    def wrapper(*args, **kwargs):
        keys, vals = func(*args, **kwargs)
        zipped = zip(keys, vals)
        return dict(list(zipped))

    return wrapper


@get_dict
def get_2list(str1, str2):
    return str1.split(), str2.split()


str1 = input()
str2 = input()
d = get_2list(str1, str2)
print(*sorted(d.items()))
