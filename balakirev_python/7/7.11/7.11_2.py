def show_menu(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        for i, item in enumerate(res, start=1):
            print(f"{i}. {item}")

    return wrapper


@show_menu
def get_menu(string):
    return string.split()


str_in = input()
get_menu(str_in)
