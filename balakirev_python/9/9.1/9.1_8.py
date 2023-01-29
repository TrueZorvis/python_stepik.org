cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]

g = (cities[x % len(cities)] for x in range(1000000))

print(*(next(g) for _ in range(20)))
