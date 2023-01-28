from functools import wraps


def decor_func(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return sum(res)
    return wrapper


@decor_func
def get_list(string):
    """Функция для формирования списка целых значений"""
    return list(map(int, string.split()))


print(get_list('1 3 4 5'))
print(get_list.__name__)
print(get_list.__doc__)
