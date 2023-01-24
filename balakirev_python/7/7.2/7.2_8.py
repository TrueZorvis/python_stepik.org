def func(word):
    return word, len(word)


lst_in = input().split()

d = {city: lenght for city, lenght in [func(item) for item in lst_in]}

a = sorted(d, key=lambda x: d[x])
print(*a)
