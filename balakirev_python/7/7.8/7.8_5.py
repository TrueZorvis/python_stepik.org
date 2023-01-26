s = input()

get_sub = lambda x: True if 'ra' in x.lower() else False
print(get_sub(s))
