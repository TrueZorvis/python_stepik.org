# import sys
#
# # считывание списка из входного потока
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]

lst_in = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 8, 7, 6],
          [5, 4, 3, 2]]

# lst = [x for row in reversed(lst_in) for x in reversed(row)]
lst = [lst_in[row][indx] for row in range(len(lst_in) - 1, -1, -1) for indx in range(len(lst_in[0]) - 1, -1, -1)]

print(*lst)
