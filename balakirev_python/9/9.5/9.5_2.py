import sys

# считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))

lst_in = ['1 2 3 4 5 6', '3 4 5 6', '7 8 9', '9 7 5 3 2']
lst = [[int(x) for x in nums.split()] for nums in lst_in]

table = zip(*zip(*lst))
for row in table:
    print(*row)
