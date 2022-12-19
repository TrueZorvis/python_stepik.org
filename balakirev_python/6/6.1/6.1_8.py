import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst_in = ['+71234567890 Сергей', '+71234567810 Сергей', '+51234567890 Михаил', '+72134567890 Николай']

d = {}
for item in lst_in:
    number, name = item.split()
    numbers = d.get(name, [])
    numbers.append(number)
    d[name] = numbers

print(*sorted(d.items()))
