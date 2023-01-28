t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


def decor_replace(chars='!?'):
    def decor_func(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)

            for ch in chars:
                if ch in res:
                    res = res.replace(ch, '-')

            while '--' in res:
                res = res.replace('--', '-')

            return res
        return wrapper
    return decor_func


@decor_replace(chars='?!:;,. ')
def translate(string):
    s = ''
    for char in string.lower():
        s += t.get(char, char)
    return s


s_in = input()
print(translate(s_in))
