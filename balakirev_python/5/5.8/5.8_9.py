lst_in = input().split()

cities = lst_in[::2]
population = lst_in[1::2]
lst = [[c, int(p)] for c, p in zip(cities, population)]

print(lst)
