import sys
import random
# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)

# считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = ['1 2 3 4', '5 6 7 8', '9 8 6 7']

lst = [row.split() for row in lst_in]
table = list(zip(*lst))
random.shuffle(table)
lst = list(zip(*table))

for row in lst:
    print(*row)
