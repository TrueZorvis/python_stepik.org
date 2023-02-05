import sys

# считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))

lst_in = ['1 2 3 4', '5 6 7 8', '9 8 7 6']

lst = [[int(x) for x in row.split()] for row in lst_in]
table = zip(*lst)
for row in table:
    print(*row)
