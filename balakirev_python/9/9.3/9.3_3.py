import sys

# считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))

lst_in = ['8 11 -5', '3 4 10', '-1 -2 3', '-4 5 6']

# lst2D = list(map(lambda s: [int(x) for x in s.split()], lst_in))
lst2D = [list(map(int, s.split())) for s in lst_in]

print(lst2D)
