import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst_in = ['5=отлично', '4=хорошо', '3=удовлетворительно']

d = {}
for item in lst_in:
    key, value = item.split('=')
    d[int(key)] = value

print(*sorted(d.items()))
