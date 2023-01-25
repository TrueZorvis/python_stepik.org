def str_min(str1, str2):
    return str1 if str1 < str2 else str2


def str_min3(str1, str2, str3):
    return str_min(str1, str_min(str2, str3))


def str_min4(str1, str2, str3, str4):
    return str_min(str1, str_min3(str2, str3, str4))


print(str_min('aa', 'ab'))
print(str_min3('aa', 'ab', 'ac'))
print(str_min4('aa', 'ab', 'ac', 'ad'))
