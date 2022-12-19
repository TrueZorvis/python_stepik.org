# input: "+71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890"
list_in = [[item[:2], item] for item in input().split()]

d = {}
for item in list_in:
    numbers = d.get(item[0], [])
    numbers.append(item[1])
    d[item[0]] = numbers

print(*sorted(d.items()))
