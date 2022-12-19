lst_in = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [5, 4, 3]]

# A = [[lst_in[i][j] for i in range(len(lst_in))] for j in range(len(lst_in[0]))]
A = [[row[i] for row in lst_in] for i in range(len(lst_in[0]))]

for row in A:
    print(*row)
