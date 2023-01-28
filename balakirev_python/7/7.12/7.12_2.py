def decor_tag(tag='h1'):
    def decor_func(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return f"<{tag}>{res}</{tag}>"
        return wrapper
    return decor_func


@decor_tag(tag='div')
def get_lower_string(s):
    return s.lower()


s = input()
print(get_lower_string(s))
