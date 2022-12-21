cities = set()
while True:
    str_in = input()
    if str_in == 'q':
        break
    cities.add(str_in)
print(len(cities))
